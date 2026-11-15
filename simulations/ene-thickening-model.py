#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ene Kalınlaşma Modeli (Ene Thickening Model)
=============================================

30. Söz'ün (Ene ve Zerre Risalesi) birinci maksadında anlatılan sürecin
*sembolik* ve *deneysel* bir dinamik sistem modellemesidir:

    "Ene, zâtında hava gibi şeffaftır; fakat gaflet, inkâr ve isyan ile
     kalınlaşır, büyür, sahibini yutar."

UYARI: Bu bir tefekkür aracıdır, ilmî/teolojik bir hüküm değildir. Manevî
hakikatler sayılarla ölçülemez; buradaki parametreler yalnızca kavramlar
arasındaki ilişkileri (artırıcı / azaltıcı etkiler, eşikler, geri besleme
döngüleri) görselleştirmek için kullanılan metaforlardır.

Model
-----
Durum değişkenleri (hepsi [0, 1] aralığında):

    K : Kalınlık (kesafet)  -> 0 = hava gibi şeffaf, 1 = taş gibi kesif
    S : Şeffafiyet          -> 1 - K (marifet nurunun geçirgenliği)
    H : Harfî nazar oranı   -> eşyaya mana-yı harfî ile bakma meyli

Kalınlaştırıcı (tekâsüf) kuvvetler:
    gaflet, inkar (esbabperestlik / tabiatperestlik), isyan, malikiyet (temellük vehmi)

İnceltici (tasfiye) kuvvetler:
    tefekkur, sukur, dua, ihlas

Diferansiyel denklemler (Euler yöntemiyle çözülür):

    tekasuf = (gaflet + inkar + isyan + malikiyet) / 4
    etkin_tefekkur = tefekkur * (1 - inkar)               # esbabperest tefekkür inceltmez
    tasfiye = (etkin_tefekkur + sukur + dua + ihlas) / 4

    dK/dt = a * tekasuf * (1 - H + e) * (K + e) * (1 - K) # kendini besleyen kalınlaşma
          - b * tasfiye * H * K                           # harfî nazarla incelme

    dH/dt = c * tasfiye * (1 - H) - d * tekasuf * K * H   # nazarın harfîleşmesi / ismîleşmesi

Kalınlık arttıkça ismî nazar güçlenir; ismî nazar güçlendikçe kalınlaşma
hızlanır: bu, "kalınlaşan enenin sahibini yutması" sürecindeki pozitif geri
besleme döngüsünün temsilidir.

Kullanım
--------
    python ene-thickening-model.py                       # varsayılan senaryo
    python ene-thickening-model.py --senaryo firavun
    python ene-thickening-model.py --senaryo tevbe --grafik
    python ene-thickening-model.py --karsilastir         # tüm senaryolar
    python ene-thickening-model.py --gaflet 0.8 --dua 0.1 --csv cikti.csv

Yalnızca Python standart kütüphanesi gerekir. `--grafik` için matplotlib
(opsiyonel) kurulu olmalıdır; yoksa ASCII grafik çizilir.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass, field, asdict, replace
from typing import Dict, List, Optional

# Windows konsollarında Türkçe karakterlerin düzgün görünmesi için
try:  # pragma: no cover - ortam bağımlı
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:  # pragma: no cover
    pass


# ---------------------------------------------------------------------------
# Parametreler
# ---------------------------------------------------------------------------

@dataclass
class Parametreler:
    """Modelin manevî/sembolik parametreleri. Hepsi [0, 1] aralığındadır."""

    # Kalınlaştırıcılar (tekâsüf)
    gaflet: float = 0.5
    inkar: float = 0.3       # esbabperestlik, tabiatperestlik
    isyan: float = 0.3
    malikiyet: float = 0.4   # "bu benimdir" vehmi (temellük)

    # İnceltici (tasfiye) kuvvetler
    tefekkur: float = 0.4
    sukur: float = 0.4
    dua: float = 0.4
    ihlas: float = 0.4

    # Başlangıç durumu
    K0: float = 0.10   # fıtrî hâl: neredeyse şeffaf
    H0: float = 0.70   # fıtrat harfî nazara meyyaldir

    # Dinamik katsayılar
    a: float = 1.6
    b: float = 1.4
    c: float = 0.9
    d: float = 0.9
    e: float = 0.02    # en şeffaf enede bile bulunan "vehmî çizgi"

    # Zaman
    adim: float = 0.05
    sure: float = 40.0

    def dogrula(self) -> None:
        for ad in ("gaflet", "inkar", "isyan", "malikiyet",
                   "tefekkur", "sukur", "dua", "ihlas", "K0", "H0"):
            v = getattr(self, ad)
            if not 0.0 <= v <= 1.0:
                raise ValueError(f"'{ad}' parametresi [0, 1] aralığında olmalı (verilen: {v})")
        if self.adim <= 0 or self.sure <= 0:
            raise ValueError("'adim' ve 'sure' pozitif olmalı")

    @property
    def tekasuf(self) -> float:
        return (self.gaflet + self.inkar + self.isyan + self.malikiyet) / 4.0

    @property
    def etkin_tefekkur(self) -> float:
        """Esbabperest (mana-yı ismî) nazarla yapılan tefekkür eneyi inceltmez.

        Felsefenin akıl yürütmesi ne kadar keskin olursa olsun, eşyaya
        sebepler adına bakıldıkça tefekkürün tasfiye gücü düşer.
        """
        return self.tefekkur * (1.0 - self.inkar)

    @property
    def tasfiye(self) -> float:
        return (self.etkin_tefekkur + self.sukur + self.dua + self.ihlas) / 4.0


# ---------------------------------------------------------------------------
# Hâl (mertebe) sınıflandırması
# ---------------------------------------------------------------------------

MERTEBELER = [
    (0.15, "Hava gibi şeffaf",  "Ene vâhid-i kıyasî vazifesinde; Sâni'i gösteren bir ayna."),
    (0.35, "Bulutlanma",        "Gaflet perdeleri; mana-yı ismî nazarı belirmeye başlıyor."),
    (0.55, "Su gibi akışkan",   "Malikiyet vehmi yerleşiyor; 'benim' iddiası güçleniyor."),
    (0.75, "Toprak gibi kesif", "Nur geçirmeyen duvar; esbabperestlik hâkim."),
    (0.90, "Taş gibi katı",     "Firavuniyet eşiği; ene büyüyor, mâbudunu unutuyor."),
    (1.01, "Yutulma",           "Ene sahibini yutmuş; insan kendi nefsine tapar hâle gelmiş."),
]


def mertebe(K: float) -> tuple[str, str]:
    for esik, ad, aciklama in MERTEBELER:
        if K < esik:
            return ad, aciklama
    return MERTEBELER[-1][1], MERTEBELER[-1][2]


# ---------------------------------------------------------------------------
# Simülasyon
# ---------------------------------------------------------------------------

@dataclass
class Sonuc:
    t: List[float] = field(default_factory=list)
    K: List[float] = field(default_factory=list)
    H: List[float] = field(default_factory=list)
    yutulma_zamani: Optional[float] = None
    firavuniyet_zamani: Optional[float] = None

    @property
    def S(self) -> List[float]:
        return [1.0 - k for k in self.K]

    @property
    def son_K(self) -> float:
        return self.K[-1]

    @property
    def son_H(self) -> float:
        return self.H[-1]


def _sinirla(x: float) -> float:
    return 0.0 if x < 0.0 else 1.0 if x > 1.0 else x


def turevler(K: float, H: float, p: Parametreler) -> tuple[float, float]:
    """dK/dt ve dH/dt değerlerini döndürür."""
    tk, ts = p.tekasuf, p.tasfiye
    # (1 - H + e): en harfî nazarda bile vehmî çizgi tamamen kaybolmaz;
    # ene "farazî bir hat" olarak daima mevcuttur.
    dK = p.a * tk * (1.0 - H + p.e) * (K + p.e) * (1.0 - K) - p.b * ts * H * K
    dH = p.c * ts * (1.0 - H) - p.d * tk * K * H
    return dK, dH


def simule_et(p: Parametreler) -> Sonuc:
    p.dogrula()
    r = Sonuc()
    K, H, t = p.K0, p.H0, 0.0
    n = int(round(p.sure / p.adim))
    onceki = K
    for i in range(n + 1):
        r.t.append(round(t, 6))
        r.K.append(K)
        r.H.append(H)
        # Eşikler yalnızca aşağıdan yukarı geçildiğinde kaydedilir
        if i > 0:
            if r.firavuniyet_zamani is None and onceki < 0.75 <= K:
                r.firavuniyet_zamani = t
            if r.yutulma_zamani is None and onceki < 0.90 <= K:
                r.yutulma_zamani = t
        onceki = K
        dK, dH = turevler(K, H, p)
        K = _sinirla(K + p.adim * dK)
        H = _sinirla(H + p.adim * dH)
        t += p.adim
    return r


# ---------------------------------------------------------------------------
# Senaryolar
# ---------------------------------------------------------------------------

SENARYOLAR: Dict[str, Dict[str, object]] = {
    "fitrat": {
        "aciklama": "Dengeli hâl: ne aşırı gaflet ne yüksek mücahede.",
        "params": {},
    },
    "firavun": {
        "aciklama": "Gaflet, inkâr, isyan ve temellük zirvede; tasfiye neredeyse yok.",
        "params": dict(gaflet=0.95, inkar=0.9, isyan=0.85, malikiyet=0.95,
                       tefekkur=0.05, sukur=0.05, dua=0.0, ihlas=0.0),
    },
    "gafil": {
        "aciklama": "Kasıtlı inkâr yok ama derin gaflet ve dünyaya dalma var.",
        "params": dict(gaflet=0.85, inkar=0.3, isyan=0.4, malikiyet=0.6,
                       tefekkur=0.1, sukur=0.2, dua=0.15, ihlas=0.2),
    },
    "tevbe": {
        "aciklama": "Kalınlaşmış bir ene; fakat tevbe ile tasfiye kuvvetleri devreye giriyor.",
        "params": dict(K0=0.80, H0=0.15, gaflet=0.2, inkar=0.1, isyan=0.1,
                       malikiyet=0.2, tefekkur=0.8, sukur=0.8, dua=0.9, ihlas=0.8),
    },
    "salik": {
        "aciklama": "Tefekkür, şükür, dua ve ihlas ile ene hava gibi şeffaf kalıyor.",
        "params": dict(gaflet=0.1, inkar=0.0, isyan=0.05, malikiyet=0.1,
                       tefekkur=0.9, sukur=0.9, dua=0.9, ihlas=0.9),
    },
    "filozof": {
        "aciklama": "Yüksek tefekkür ama esbabperest nazar: akıl var, harfî bakış yok.",
        "params": dict(gaflet=0.4, inkar=0.85, isyan=0.3, malikiyet=0.8,
                       tefekkur=0.9, sukur=0.15, dua=0.05, ihlas=0.1),
    },
}


def senaryo_parametreleri(ad: str, temel: Optional[Parametreler] = None) -> Parametreler:
    if ad not in SENARYOLAR:
        raise KeyError(f"Bilinmeyen senaryo: {ad}. Seçenekler: {', '.join(SENARYOLAR)}")
    temel = temel or Parametreler()
    return replace(temel, **SENARYOLAR[ad]["params"])  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Çıktı
# ---------------------------------------------------------------------------

def ascii_grafik(r: Sonuc, genislik: int = 60, yukseklik: int = 16) -> str:
    """Kalınlık (█) ve harfî nazar (·) eğrilerini ASCII olarak çizer."""
    n = len(r.t)
    sutunlar = [int(i * (n - 1) / (genislik - 1)) for i in range(genislik)]
    izgara = [[" "] * genislik for _ in range(yukseklik)]
    for x, idx in enumerate(sutunlar):
        hy = yukseklik - 1 - int(round(r.H[idx] * (yukseklik - 1)))
        izgara[hy][x] = "·"
        ky = yukseklik - 1 - int(round(r.K[idx] * (yukseklik - 1)))
        izgara[ky][x] = "█"
    satirlar = []
    for i, satir in enumerate(izgara):
        deger = 1.0 - i / (yukseklik - 1)
        etiket = f"{deger:4.2f} |" if i % 3 == 0 or i == yukseklik - 1 else "     |"
        satirlar.append(etiket + "".join(satir))
    satirlar.append("     +" + "-" * genislik)
    satirlar.append(f"      t=0{' ' * (genislik - 12)}t={r.t[-1]:g}")
    satirlar.append("      █ Kalınlık (K)    · Harfî nazar (H)")
    return "\n".join(satirlar)


def rapor(ad: str, p: Parametreler, r: Sonuc) -> str:
    m_ad, m_acik = mertebe(r.son_K)
    satirlar = [
        "=" * 66,
        f"  Senaryo: {ad}",
        "=" * 66,
        f"  Tekâsüf (kalınlaştırıcı) gücü : {p.tekasuf:.2f}",
        f"  Tasfiye (inceltici) gücü      : {p.tasfiye:.2f}",
        f"  Başlangıç  -> K={p.K0:.2f}  H={p.H0:.2f}",
        f"  Nihai hâl  -> K={r.son_K:.3f}  Şeffafiyet={1 - r.son_K:.3f}  H={r.son_H:.3f}",
        f"  Mertebe    : {m_ad}",
        f"               {m_acik}",
    ]
    if p.K0 >= 0.75:
        satirlar.append(f"  ↺ Başlangıçta kesafet eşiğinin üzerindeydi (K0={p.K0:.2f}).")
    if r.firavuniyet_zamani is not None:
        satirlar.append(f"  ⚠ Kesafet eşiği (K≥0.75) aşıldı : t = {r.firavuniyet_zamani:.2f}")
    if r.yutulma_zamani is not None:
        satirlar.append(f"  ☠ Yutulma eşiği (K≥0.90) aşıldı : t = {r.yutulma_zamani:.2f}")
    if r.son_K < 0.75 and r.firavuniyet_zamani is None:
        satirlar.append("  ✓ Ene, kesafet eşiğinin altında kaldı.")
    return "\n".join(satirlar)


def csv_yaz(yol: str, r: Sonuc) -> None:
    with open(yol, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["t", "kalinlik", "seffafiyet", "harfi_nazar"])
        for t, k, h in zip(r.t, r.K, r.H):
            w.writerow([f"{t:.4f}", f"{k:.6f}", f"{1 - k:.6f}", f"{h:.6f}"])


def matplotlib_grafik(sonuclar: Dict[str, Sonuc], kaydet: Optional[str] = None) -> bool:
    try:
        import matplotlib.pyplot as plt  # type: ignore
    except ImportError:
        return False
    fig, ax = plt.subplots(figsize=(10, 5.5))
    for ad, r in sonuclar.items():
        ax.plot(r.t, r.K, label=f"{ad} – kalınlık", linewidth=2)
        if len(sonuclar) == 1:
            ax.plot(r.t, r.H, "--", label=f"{ad} – harfî nazar")
    ax.axhline(0.75, color="orange", linestyle=":", label="Kesafet eşiği")
    ax.axhline(0.90, color="red", linestyle=":", label="Yutulma eşiği")
    ax.set_ylim(-0.02, 1.02)
    ax.set_xlabel("Zaman (sembolik)")
    ax.set_ylabel("Değer")
    ax.set_title("Ene'nin Kalınlaşma / Şeffaflaşma Dinamiği")
    ax.legend(loc="best", fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    if kaydet:
        fig.savefig(kaydet, dpi=150)
        print(f"Grafik kaydedildi: {kaydet}")
    else:
        plt.show()
    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

PARAM_ADLARI = ("gaflet", "inkar", "isyan", "malikiyet",
                "tefekkur", "sukur", "dua", "ihlas", "K0", "H0", "sure", "adim")


def arguman_ayristirici() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        description="Ene'nin gaflet ve şirk parametreleriyle kalınlaşmasını / "
                    "tefekkür ve dua ile şeffaflaşmasını modelleyen sembolik simülasyon.",
    )
    ap.add_argument("--senaryo", "-s", choices=sorted(SENARYOLAR), default="fitrat",
                    help="Hazır senaryo (varsayılan: fitrat)")
    ap.add_argument("--listele", action="store_true", help="Senaryoları listele ve çık")
    ap.add_argument("--karsilastir", action="store_true", help="Tüm senaryoları karşılaştır")
    ap.add_argument("--grafik", action="store_true", help="matplotlib ile grafik göster")
    ap.add_argument("--kaydet", metavar="DOSYA.png", help="Grafiği dosyaya kaydet")
    ap.add_argument("--csv", metavar="DOSYA.csv", help="Zaman serisini CSV olarak yaz")
    ap.add_argument("--sessiz", action="store_true", help="ASCII grafiği gösterme")
    for ad in PARAM_ADLARI:
        ap.add_argument(f"--{ad}", type=float, default=None,
                        help=f"'{ad}' parametresini elle ayarla")
    return ap


def main(argv: Optional[List[str]] = None) -> int:
    args = arguman_ayristirici().parse_args(argv)

    if args.listele:
        for ad, s in SENARYOLAR.items():
            print(f"  {ad:<10} {s['aciklama']}")
        return 0

    elle = {ad: getattr(args, ad) for ad in PARAM_ADLARI if getattr(args, ad) is not None}

    if args.karsilastir:
        sonuclar: Dict[str, Sonuc] = {}
        print(f"{'Senaryo':<10} {'Tekâsüf':>8} {'Tasfiye':>8} {'Nihai K':>8} {'Yutulma t':>10}  Mertebe")
        print("-" * 72)
        for ad in SENARYOLAR:
            p = replace(senaryo_parametreleri(ad), **elle)
            r = simule_et(p)
            sonuclar[ad] = r
            yt = f"{r.yutulma_zamani:.2f}" if r.yutulma_zamani is not None else "—"
            print(f"{ad:<10} {p.tekasuf:>8.2f} {p.tasfiye:>8.2f} {r.son_K:>8.3f} {yt:>10}  {mertebe(r.son_K)[0]}")
        if args.grafik or args.kaydet:
            if not matplotlib_grafik(sonuclar, args.kaydet):
                print("\n(matplotlib bulunamadı; `pip install matplotlib` ile kurabilirsiniz.)")
        return 0

    try:
        p = replace(senaryo_parametreleri(args.senaryo), **elle)
        r = simule_et(p)
    except ValueError as exc:
        print(f"Hata: {exc}", file=sys.stderr)
        return 2

    print(rapor(args.senaryo, p, r))
    if not args.sessiz:
        print()
        print(ascii_grafik(r))
    if args.csv:
        csv_yaz(args.csv, r)
        print(f"\nCSV yazıldı: {args.csv}")
    if args.grafik or args.kaydet:
        if not matplotlib_grafik({args.senaryo: r}, args.kaydet):
            print("\n(matplotlib bulunamadı; ASCII grafik yukarıdadır.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
