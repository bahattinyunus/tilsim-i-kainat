#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kozmik Entropi vs. Negentropik Kudret İntizamı Modeli (Entropy-Information Model)
================================================================================

30. Söz'ün (Tahavvülât-ı Zerrât), 23. Lem'a'nın (Tabiat Risalesi) ve modern
termodinamik / kuantum enformasyon teorisinin (Wheeler: "It from Bit")
sembolik bir matematiksel modellemesidir:

    "Zerre mebde-i hareketinde 'Bismillâh' der; nihayetsiz kuvvetinden fazla
     yükleri kaldırır... Nizam-ı umumiyeye tevfik-i hareket eder."

Termodinamiğin 2. kanunu kapalı sistemlerde entropinin (düzensizliğin)
artacağını söyler (dS >= 0). Buna karşılık kâinattaki hayat ve intizam,
entropiye meydan okuyarak akıl almaz bir negentropi (düzen ve bilgi) inşa eder.
Bu model, kör maddeden canlılığa geçişteki "Kudret Kalemi" tesirini simüle eder.
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from dataclasses import dataclass, field, replace
from typing import Dict, List, Optional

try:  # pragma: no cover
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:  # pragma: no cover
    pass


@dataclass
class EntropiParametreleri:
    """Entropi ve bilgi modeli parametreleri."""
    kudret_tesiri: float = 0.95       # [0, 1] İrade ve kudretin nizam verici tesiri
    hayat_seviyesi: float = 0.90      # [0, 1] Hayat ve şuur derecesi
    termal_kaos: float = 0.15         # [0, 1] Fiziksel termodinamik bozucu gürültü
    baslangic_intizami: float = 0.10  # [0, 1] Başlangıçtaki intizam derecesi (0 = kaos, 1 = mükemmel kod)
    
    sure: float = 10.0
    adim: float = 0.1

    def dogrula(self) -> None:
        for ad in ("kudret_tesiri", "hayat_seviyesi", "termal_kaos", "baslangic_intizami"):
            v = getattr(self, ad)
            if not 0.0 <= v <= 1.0:
                raise ValueError(f"'{ad}' parametresi [0, 1] aralığında olmalı (verilen: {v})")
        if self.sure <= 0 or self.adim <= 0:
            raise ValueError("'sure' ve 'adim' pozitif olmalı")


@dataclass
class EntropiAdimKaydi:
    t: float
    intizam: float            # Negentropi derecesi [0, 1]
    entropi: float            # Termodinamik düzensizlik [0, 1]
    shannon_bilgi_bit: float  # Tekvînî enformasyon yoğunluğu (Bit)


@dataclass
class EntropiSonuc:
    adimlar: List[EntropiAdimKaydi] = field(default_factory=list)
    nihai_intizam: float = 0.0
    nihai_entropi: float = 0.0
    maksimum_bilgi: float = 0.0
    kaos_cokusu: bool = False


def entropi_simule_et(p: EntropiParametreleri) -> EntropiSonuc:
    p.dogrula()
    sonuc = EntropiSonuc()
    
    intizam = p.baslangic_intizami
    t = 0.0
    n_adim = int(round(p.sure / p.adim))
    
    # Tesadüf/maddeci senaryoda kudret tesiri yoksa sistem çöker
    if p.kudret_tesiri < 0.20 and p.hayat_seviyesi < 0.20:
        sonuc.kaos_cokusu = True

    for _ in range(n_adim + 1):
        t_cur = round(t, 4)
        entropi = max(0.0, min(1.0, 1.0 - intizam + (p.termal_kaos * 0.2)))
        
        # Shannon Bilgi Yoğunluğu (Bit cinsinden tekvînî kelime derinliği)
        # I = -p*log2(p) - (1-p)*log2(1-p) simetrisi
        prob = max(0.001, min(0.999, intizam))
        shannon = - (prob * math.log2(prob) + (1.0 - prob) * math.log2(1.0 - prob))
        # Düzenli bir DNA veya göz kodu için bilgi derinliği katlanır
        bilgi_bit = (1.0 - shannon) * 100.0 * p.hayat_seviyesi + (intizam * 50.0)

        kayit = EntropiAdimKaydi(
            t=t_cur,
            intizam=round(intizam, 4),
            entropi=round(entropi, 4),
            shannon_bilgi_bit=round(bilgi_bit, 2),
        )
        sonuc.adimlar.append(kayit)

        # Diferansiyel denklem:
        # d(intizam)/dt = k_kudret * Kudret * Hayat * (1 - intizam) - k_kaos * Termal * intizam
        d_intizam = (1.5 * p.kudret_tesiri * p.hayat_seviyesi * (1.0 - intizam)) - (1.2 * p.termal_kaos * intizam)
        intizam = max(0.0, min(1.0, intizam + p.adim * d_intizam))
        t += p.adim

    sonuc.nihai_intizam = sonuc.adimlar[-1].intizam
    sonuc.nihai_entropi = sonuc.adimlar[-1].entropi
    sonuc.maksimum_bilgi = max(d.shannon_bilgi_bit for d in sonuc.adimlar)
    return sonuc


ENTROPI_SENARYOLAR: Dict[str, Dict[str, object]] = {
    "canlilik_ve_dna": {
        "aciklama": "Trilyonlarca atomun harika bir genetik kod oluşturması (Azamî negentropi).",
        "params": dict(kudret_tesiri=0.98, hayat_seviyesi=0.95, termal_kaos=0.10, baslangic_intizami=0.15),
    },
    "tevfikin_gozbebegi": {
        "aciklama": "Göz hücresinde damarlara ve kâinata tam intibak eden zerrenin bilgi yoğunluğu.",
        "params": dict(kudret_tesiri=0.99, hayat_seviyesi=0.98, termal_kaos=0.05, baslangic_intizami=0.20),
    },
    "tohumun_inbisi": {
        "aciklama": "Bir tohumun topraktan filizlenirken entropiye galip gelmesi.",
        "params": dict(kudret_tesiri=0.88, hayat_seviyesi=0.85, termal_kaos=0.20, baslangic_intizami=0.10),
    },
    "materyalist_isi_olumu": {
        "aciklama": "Kudret ve Hayat dışarıda tutulduğunda kör maddenin kaçınılmaz entropi çöküşü.",
        "params": dict(kudret_tesiri=0.05, hayat_seviyesi=0.05, termal_kaos=0.85, baslangic_intizami=0.50),
    },
}


def entropi_senaryo_parametreleri(ad: str, temel: Optional[EntropiParametreleri] = None) -> EntropiParametreleri:
    if ad not in ENTROPI_SENARYOLAR:
        raise KeyError(f"Bilinmeyen senaryo: {ad}. Seçenekler: {', '.join(ENTROPI_SENARYOLAR)}")
    temel = temel or EntropiParametreleri()
    return replace(temel, **ENTROPI_SENARYOLAR[ad]["params"])  # type: ignore[arg-type]


def entropi_raporu(ad: str, p: EntropiParametreleri, r: EntropiSonuc) -> str:
    satirlar = [
        "=" * 72,
        f"  ⚛️ KOZMİK ENTROPİ VE KUDRET İNTİZAMI RAPORU: {ad.upper()}",
        "=" * 72,
        f"  Kudret Kalemi Tesiri  : {p.kudret_tesiri:.2f}",
        f"  Hayat ve Şuur Seviyesi: {p.hayat_seviyesi:.2f}",
        f"  Termodinamik Kaos Meyli: {p.termal_kaos:.2f}",
        "-" * 72,
        f"  Başlangıç İntizamı    : {p.baslangic_intizami:.2f}  -->  Nihai İntizam: {r.nihai_intizam:.3f}",
        f"  Nihai Entropi Derecesi: {r.nihai_entropi:.3f} (1.0 = Mutlak Kaos)",
        f"  Tekvînî Bilgi Derinliği: {r.maksimum_bilgi:,.1f} Bit (Wheeler: It from Bit)",
        "-" * 72,
    ]
    if r.kaos_cokusu:
        satirlar.append("  ❌ ENTROPİ ÇÖKÜŞÜ: Kör sebepler düzeni sağlayamadı, sistem dağıldı!")
    else:
        satirlar.append("  ✅ NEGENTROPİ ZAFERİ: Zerre 'Bismillah' ile entropiyi yendi, canlılık parıldadı.")
    satirlar.append("=" * 72)
    return "\n".join(satirlar)


def entropi_csv_yaz(yol: str, r: EntropiSonuc) -> None:
    with open(yol, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["t", "intizam", "entropi", "shannon_bilgi_bit"])
        for d in r.adimlar:
            w.writerow([d.t, d.intizam, d.entropi, d.shannon_bilgi_bit])


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Kozmik Entropi vs. Negentropik Kudret İntizamı Modeli.")
    ap.add_argument("--senaryo", "-s", choices=sorted(ENTROPI_SENARYOLAR), default="canlilik_ve_dna",
                    help="Hazır senaryo (varsayılan: canlilik_ve_dna)")
    ap.add_argument("--listele", action="store_true", help="Senaryoları listele")
    ap.add_argument("--karsilastir", action="store_true", help="Tüm senaryoları karşılaştır")
    ap.add_argument("--csv", metavar="DOSYA.csv", help="CSV çıktısı kaydet")

    args = ap.parse_args(argv)

    if args.listele:
        for k, v in ENTROPI_SENARYOLAR.items():
            print(f"  {k:<24} {v['aciklama']}")
        return 0

    if args.karsilastir:
        print(f"{'Senaryo':<24} {'İntizam':>9} {'Entropi':>9} {'Bilgi (Bit)':>13}  Netice")
        print("-" * 68)
        for ad in ENTROPI_SENARYOLAR:
            p = entropi_senaryo_parametreleri(ad)
            r = entropi_simule_et(p)
            netice = "Kaos/Dağılma" if r.kaos_cokusu else "Kudret İntizamı"
            print(f"{ad:<24} {r.nihai_intizam:>9.3f} {r.nihai_entropi:>9.3f} {r.maksimum_bilgi:>12.1f}  {netice}")
        return 0

    try:
        p = entropi_senaryo_parametreleri(args.senaryo)
        r = entropi_simule_et(p)
    except ValueError as exc:
        print(f"Hata: {exc}", file=sys.stderr)
        return 2

    print(entropi_raporu(args.senaryo, p, r))
    if args.csv:
        entropi_csv_yaz(args.csv, r)
        print(f"\nCSV kaydedildi: {args.csv}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
