#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tılsım-ı Kâinat — Statik Web Portalı Üreticisi (Site Builder)
=============================================================
Depodaki tüm Markdown dokümanlarını, 19 Mermaid diyagramını, 145+ kavramlar
sözlüğü maddesini, görselleri ve 12 modelli interaktif simülasyon laboratuvarını
`site/` klasörüne üretim (production) kalitesinde derler.
Harici Python paketi gerektirmez (yalnızca standart kütüphane).
"""

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT / "site"
DATA_DIR = SITE_DIR / "data"
ASSETS_IMG_DIR = SITE_DIR / "assets" / "images"


CATEGORY_MAP = {
    "ene-ontolojisi": "Ene Ontolojisi",
    "zerre-dinamikleri": "Zerre Dinamikleri",
    "tilsim-i-kainat-kullî-cozum.md": "Küllî Sentez",
    "gelecegin-teknolojileri-ve-tilsim-i-kainat.md": "Fizik & Teknoloji",
    "modern-fizik-ve-tilsim-i-kainat.md": "Fizik & Teknoloji",
    "mirac-ve-tayy-i-zaman.md": "Fizik & Teknoloji",
    "holografik-alem-ve-ehadiyet.md": "Fizik & Teknoloji",
    "esma-fraktal-ve-olcek-degismezligi.md": "Fizik & Teknoloji",
    "hayat-ve-ruh-tilsimi.md": "Hayat & Şuur",
    "kader-ve-irade-tilsimi.md": "Kader & Ebediyet",
    "hasir-ve-ebediyet-tilsimi.md": "Kader & Ebediyet",
    "suunat-i-ilahiye-ve-faaliyet-i-daime.md": "Esmâ & Şuûnât",
    "dort-kelime-dort-kelam.md": "Epistemoloji",
    "nubuvvet-ve-felsefe.md": "Epistemoloji",
    "tabiat-ve-esbab-elestirisi.md": "Epistemoloji",
    "kainat-sarayi-ve-uc-sual.md": "Kâinat & İnsan",
    "taallum-ve-tekamul.md": "Kâinat & İnsan",
}


def extract_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            return m.group(1).strip()
    return fallback


def extract_excerpt(md_text: str) -> str:
    lines = []
    for raw in md_text.splitlines():
        s = raw.strip()
        if not s or s.startswith("#") or s.startswith(">") or s.startswith("---") or s.startswith("|") or s.startswith("```"):
            continue
        cleaned = re.sub(r"[*_`]", "", s)
        cleaned = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", cleaned)
        if len(cleaned) > 30:
            lines.append(cleaned)
            if len(" ".join(lines)) > 170:
                break
    excerpt = " ".join(lines)
    return excerpt[:190].rsplit(" ", 1)[0] + "…" if len(excerpt) > 190 else excerpt


def build_docs() -> list[dict]:
    docs_root = ROOT / "docs"
    items = []
    for md_path in sorted(docs_root.rglob("*.md")):
        rel = md_path.relative_to(docs_root).as_posix()
        text = md_path.read_text(encoding="utf-8")
        title = extract_title(text, md_path.stem.replace("-", " ").title())
        words = len(text.split())
        read_min = max(1, round(words / 200))
        parent = md_path.parent.name
        category = CATEGORY_MAP.get(md_path.name) or CATEGORY_MAP.get(parent) or "Araştırma"
        items.append({
            "id": rel.replace("/", "__").replace(".md", ""),
            "path": f"docs/{rel}",
            "title": title,
            "category": category,
            "words": words,
            "readMin": read_min,
            "excerpt": extract_excerpt(text),
            "content": text,
        })
    return items


def build_diagrams() -> list[dict]:
    diag_root = ROOT / "assets" / "diagrams"
    readme_text = (diag_root / "README.md").read_text(encoding="utf-8")
    meta: dict[str, tuple[str, str]] = {}
    for line in readme_text.splitlines():
        m = re.match(r"^\|\s*\[`([^`]+)`\]\([^\)]+\)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$", line.strip())
        if m:
            meta[m.group(1)] = (m.group(2).strip(), m.group(3).strip())

    diagrams = []
    for mmd_path in sorted(diag_root.glob("*.mmd")):
        fname = mmd_path.name
        title, desc = meta.get(fname, (mmd_path.stem.replace("-", " ").title(), "Kavramsal Mermaid Diyagramı"))
        code = mmd_path.read_text(encoding="utf-8").strip()
        diagrams.append({
            "id": mmd_path.stem,
            "file": fname,
            "title": title,
            "description": desc,
            "code": code,
        })
    return diagrams


def build_glossary() -> list[dict]:
    gloss_path = ROOT / "kavramlar-sozlugu" / "glossary.md"
    text = gloss_path.read_text(encoding="utf-8")
    entries = []
    current_letter = "A"
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        hm = re.match(r"^##\s+(.+)$", line)
        if hm:
            current_letter = hm.group(1).strip()
            i += 1
            continue
        tm = re.match(r"^\*\*([^*]+)\*\*\s*[—–-]\s*(.+)$", line)
        if tm:
            term = tm.group(1).strip()
            desc_parts = [tm.group(2).strip()]
            i += 1
            while i < len(lines):
                nxt = lines[i].strip()
                if not nxt or nxt.startswith("## ") or nxt.startswith("---") or re.match(r"^\*\*[^*]+\*\*\s*[—–-]", nxt):
                    break
                desc_parts.append(nxt)
                i += 1
            full_desc = " ".join(desc_parts)
            full_desc = re.sub(r"→\s*\[([^\]]+)\]\([^\)]+\)", r"• Kaynak: \1", full_desc)
            entries.append({
                "letter": current_letter,
                "term": term,
                "definition": full_desc,
            })
            continue
        i += 1
    return entries


def copy_assets() -> None:
    ASSETS_IMG_DIR.mkdir(parents=True, exist_ok=True)
    src_img_dir = ROOT / "assets" / "images"
    if src_img_dir.exists():
        for img in src_img_dir.glob("*"):
            if img.is_file():
                shutil.copy2(img, ASSETS_IMG_DIR / img.name)

    # Copy interactive 12-model simulation lab
    dash_src = ROOT / "dashboard" / "index.html"
    if dash_src.exists():
        shutil.copy2(dash_src, SITE_DIR / "lab.html")


def main() -> int:
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    docs = build_docs()
    diagrams = build_diagrams()
    glossary = build_glossary()
    copy_assets()

    (DATA_DIR / "docs.json").write_text(json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8")
    (DATA_DIR / "diagrams.json").write_text(json.dumps(diagrams, ensure_ascii=False, indent=2), encoding="utf-8")
    (DATA_DIR / "glossary.json").write_text(json.dumps(glossary, ensure_ascii=False, indent=2), encoding="utf-8")

    summary = {
        "models": 12,
        "tests": 87,
        "docs": len(docs),
        "diagrams": len(diagrams),
        "glossary": len(glossary),
    }
    (DATA_DIR / "stats.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(
        f"✅ Site verileri üretildi: {len(docs)} doküman, {len(diagrams)} diyagram, "
        f"{len(glossary)} sözlük maddesi -> {SITE_DIR}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
