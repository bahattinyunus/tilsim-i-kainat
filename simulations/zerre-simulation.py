#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tahavvülât-ı Zerrât ve Kudret Kalemi Simülasyonu (Zerre Dynamics Model)
====================================================================

30. Söz'ün (Ene ve Zerre Risalesi) İkinci Maksadında anlatılan zerre
dinamiklerinin sembolik ve algoritmik bir modellemesidir:

    "Tahavvülât-ı zerrât; Nakkāş-ı Ezelî'nin kalem-i kudreti, kitâb-ı kâinâtta
     yazdığı âyât-ı tekvîniyenin hengâmındaki ihtizâzâtı ve cevelânıdır...
     Zerre mebde-i hareketinde 'Bismillâh' der; nihâyetsiz kuvvetinden fazla
     yükleri kaldırır... Hitâmında 'Elhamdülillâh' der; hikmetli bir sanat
     gösterir."

İki Temel Şahit:
1. Acz ve Cümûd ile Sâni'in VÜCUDUNA şehadet: Zerre câmid (şuursuz) olduğu halde
   şuurkârâne devasa yükleri kaldırır.
2. Nizamat-ı Umumiyeye Tevfik ile Sâni'in VAHDETİNE şehadet: Zerre girdiği her
   yere (toprak, bitki, kan, dimağ, gözbebeği) yabancılık çekmeden tam uyum sağlar.
   "Zerre kimin ise, gezdiği bütün yerler de Onundur."

UYARI: Bu simülasyon bir tefekkür modelidir; fiziki-biyolojik bir iddia değil,
Risale-i Nur'un ontolojik kavramlarını canlandıran bir sistem simülasyonudur.
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from dataclasses import dataclass, field, replace
from typing import Dict, List, Optional, Tuple

try:  # pragma: no cover
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:  # pragma: no cover
    pass


# ---------------------------------------------------------------------------
# Veri Yapıları ve Parametreler
# ---------------------------------------------------------------------------

@dataclass
class ZerreParametreleri:
    """Zerre hareketinin tefekkür parametreleri [0, 1] aralığında."""
    bismillah_nisbeti: float = 0.95   # Kudret-i İlâhiyeye istinad derecesi
    vahdet_intibaki: float = 0.90     # Nizamat-ı umumiyeye tevfik ve uyum meyli
    acz_derecesi: float = 1.0         # Zâtî iktidarsızlık (fıtraten 1.0'dır)
    cumud_derecesi: float = 1.0       # Maddî şuursuzluk / donukluk (fıtraten 1.0'dır)
    tesaduf_sapmasi: float = 0.05     # Kör tesadüf / mânâsız çalkantı katsayısı
    adim_sayisi: int = 5              # Durak (mertebe) sayısı

    def dogrula(self) -> None:
        for ad in ("bismillah_nisbeti", "vahdet_intibaki", "acz_derecesi",
                   "cumud_derecesi", "tesaduf_sapmasi"):
            v = getattr(self, ad)
            if not 0.0 <= v <= 1.0:
                raise ValueError(f"'{ad}' parametresi [0, 1] aralığında olmalı (verilen: {v})")
        if self.adim_sayisi <= 0:
            raise ValueError("'adim_sayisi' pozitif olmalıdır")


# Mertebeler (Duraklar)
MERTEBELER = [
    ("Hava & Toprak", "Câmid serbest zerre, mebde-i hareket", 1.0),
    ("Bitki & Rızık", "Fotosentez ve nebatî inşa, buğday/çam çekirdeği yükü", 25.0),
    ("Dolaşım & Hücre", "Canlı bedeninde sevk ve tanzim", 120.0),
    ("Dimağ & Âsâb", "Hafıza, şuur ve hissiyat mekanizması", 500.0),
    ("Tevfik'in Gözbebeği", "Basar nuru, damarlarla tam münasebet, hitâm", 1200.0),
]


@dataclass
class DurakKaydi:
    mertebe_adi: str
    aciklama: str
    kaldirilan_yuk: float
    intizam_orani: float
    vucud_sehadeti: float
    vahdet_sehadeti: float
    hikmet_skoru: float
    zikir: str


@dataclass
class ZerreSonuc:
    duraklar: List[DurakKaydi] = field(default_factory=list)
    nihai_hikmet: float = 0.0
    ortalama_intizam: float = 0.0
    vucud_sehadet_skoru: float = 0.0
    vahdet_sehadet_skoru: float = 0.0
    tesaduf_cikmazi: bool = False


# ---------------------------------------------------------------------------
# Çekirdek Algoritma
# ---------------------------------------------------------------------------

def zerre_simule_et(p: ZerreParametreleri) -> ZerreSonuc:
    p.dogrula()
    sonuc = ZerreSonuc()
    
    # Tesadüf sapması baskınsa sistem kaosa sürüklenir
    if p.tesaduf_sapmasi > 0.6 and p.bismillah_nisbeti < 0.4:
        sonuc.tesaduf_cikmazi = True

    toplam_intizam = 0.0
    toplam_vucud = 0.0
    toplam_vahdet = 0.0
    
    adimlar = min(p.adim_sayisi, len(MERTEBELER))
    
    for i in range(adimlar):
        ad, aciklama, temel_yuk = MERTEBELER[i]
        
        # Bismillah sırrı: Nihayetsiz acziyetine rağmen kudret namına yük kaldırır
        kaldirilan_yuk = temel_yuk * (p.bismillah_nisbeti * 1.5 + 0.1) * (1.0 - p.tesaduf_sapmasi * 0.8)
        
        # İntizam hesabı: Vahdet intibakı yüksekse intizam artar, tesadüf düşürür
        temel_intizam = (i + 1) / adimlar
        intizam = temel_intizam * p.vahdet_intibaki * (1.0 - p.tesaduf_sapmasi)
        intizam = max(0.0, min(1.0, intizam))
        
        # Vücuda şehadet: Acz ve Cümûd ile zıt olarak bu kadar işi görmek
        vucud_sehadet = (p.acz_derecesi * p.cumud_derecesi * (kaldirilan_yuk / temel_yuk)) * p.bismillah_nisbeti
        vucud_sehadet = min(1.0, vucud_sehadet)
        
        # Vahdete şehadet: Bütün cismin ve kâinatın nizamına tevfik
        vahdet_sehadet = p.vahdet_intibaki * (1.0 - p.tesaduf_sapmasi * 0.5) * (0.8 + 0.2 * (i / adimlar))
        vahdet_sehadet = min(1.0, vahdet_sehadet)
        
        # Hikmet skoru
        hikmet = (intizam * 0.4 + vucud_sehadet * 0.3 + vahdet_sehadet * 0.3)
        
        # Zikir: Girişte Bismillah, Çıkışta Elhamdülillah
        if i == 0:
            zikir = "BİSMİLLÂH (Mebde-i Hareket)"
        elif i == adimlar - 1:
            zikir = "ELHAMDÜLİLLÂH (Hitâm-ı Vazife)"
        else:
            zikir = f"SÜBHÂNALLÂH ({ad} intizamı)"

        kayit = DurakKaydi(
            mertebe_adi=ad,
            aciklama=aciklama,
            kaldirilan_yuk=round(kaldirilan_yuk, 2),
            intizam_orani=round(intizam, 3),
            vucud_sehadeti=round(vucud_sehadet, 3),
            vahdet_sehadeti=round(vahdet_sehadet, 3),
            hikmet_skoru=round(hikmet, 3),
            zikir=zikir,
        )
        sonuc.duraklar.append(kayit)
        toplam_intizam += intizam
        toplam_vucud += vucud_sehadet
        toplam_vahdet += vahdet_sehadet

    sonuc.ortalama_intizam = round(toplam_intizam / adimlar, 3)
    sonuc.vucud_sehadet_skoru = round(toplam_vucud / adimlar, 3)
    sonuc.vahdet_sehadet_skoru = round(toplam_vahdet / adimlar, 3)
    sonuc.nihai_hikmet = round((sonuc.ortalama_intizam + sonuc.vucud_sehadet_skoru + sonuc.vahdet_sehadet_skoru) / 3.0, 3)
    
    return sonuc


# ---------------------------------------------------------------------------
# Hazır Senaryolar
# ---------------------------------------------------------------------------

ZERRE_SENARYOLAR: Dict[str, Dict[str, object]] = {
    "tevfikin_gozu": {
        "aciklama": "30. Söz'ün meşhur misali: Zerre Tevfik'in gözbebeğinde damarlara tam mutabık yerleşir.",
        "params": dict(bismillah_nisbeti=0.98, vahdet_intibaki=0.95, tesaduf_sapmasi=0.02),
    },
    "nebat_ruku": {
        "aciklama": "Bir buğday veya çam çekirdeğinde koca ağacı omuzlayan zerrenin mebde ve hitâmı.",
        "params": dict(bismillah_nisbeti=0.90, vahdet_intibaki=0.88, tesaduf_sapmasi=0.05),
    },
    "camid_madde": {
        "aciklama": "Toprak ve taşta henüz canlanmamış zerre; intizam potansiyeli saklı.",
        "params": dict(bismillah_nisbeti=0.70, vahdet_intibaki=0.65, tesaduf_sapmasi=0.15, adim_sayisi=2),
    },
    "tesaduf_cikmazi": {
        "aciklama": "Materyalist varsayım: Zerre kör tesadüfle hareket eder; nizam ve hikmet çöker.",
        "params": dict(bismillah_nisbeti=0.10, vahdet_intibaki=0.10, tesaduf_sapmasi=0.85),
    },
    "dimag_tefekkur": {
        "aciklama": "İnsan beyninde tefekkür ve marifet aynası olan zerrenin azamî nizamı.",
        "params": dict(bismillah_nisbeti=1.00, vahdet_intibaki=0.99, tesaduf_sapmasi=0.01),
    },
}


def zerre_senaryo_parametreleri(ad: str, temel: Optional[ZerreParametreleri] = None) -> ZerreParametreleri:
    if ad not in ZERRE_SENARYOLAR:
        raise KeyError(f"Bilinmeyen senaryo: {ad}. Seçenekler: {', '.join(ZERRE_SENARYOLAR)}")
    temel = temel or ZerreParametreleri()
    return replace(temel, **ZERRE_SENARYOLAR[ad]["params"])  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Çıktı ve Raporlama
# ---------------------------------------------------------------------------

def zerre_raporu(ad: str, p: ZerreParametreleri, r: ZerreSonuc) -> str:
    satirlar = [
        "=" * 72,
        f"  ⚛️ TAHAVVÜLÂT-I ZERRÂT RAPORU: {ad.upper()}",
        "=" * 72,
        f"  İstinad (Bismillâh) Gücü : {p.bismillah_nisbeti:.2f}",
        f"  Nizam-ı Umumî İntibakı   : {p.vahdet_intibaki:.2f}",
        f"  Tesadüf Sapması          : {p.tesaduf_sapmasi:.2f}",
        "-" * 72,
        f"  {'Mertebe':<22} {'Yük (Kat)':>10} {'İntizam':>9} {'Vücud Ş.':>10} {'Vahdet Ş.':>10}  Zikir",
        "-" * 72,
    ]
    for d in r.duraklar:
        satirlar.append(
            f"  {d.mertebe_adi:<22} {d.kaldirilan_yuk:>10.1f} {d.intizam_orani:>9.2f} "
            f"{d.vucud_sehadeti:>10.2f} {d.vahdet_sehadeti:>10.2f}  {d.zikir}"
        )
    satirlar.append("-" * 72)
    satirlar.append(f"  ⭐ Ortalama İntizam    : {r.ortalama_intizam:.3f}")
    satirlar.append(f"  🔍 Vücud Şehadeti      : {r.vucud_sehadet_skoru:.3f} (Acz ve Cümûd ile Kādir-i Zülcelâl'e)")
    satirlar.append(f"  🌐 Vahdet Şehadeti     : {r.vahdet_sehadet_skoru:.3f} (Nizam-ı Umumiye tevfik ile Vâhid-i Ehad'e)")
    satirlar.append(f"  🏆 Nihai Hikmet Skoru  : {r.nihai_hikmet:.3f} / 1.000")
    
    if r.tesaduf_cikmazi:
        satirlar.append("  ❌ TESADÜF ÇIKMAZI: Kör sebepler nizamı kuramadı, zerre kaosta boğuldu!")
    else:
        satirlar.append("  ✅ KUDRET KALEMİ: Zerre 'Zerre kimin ise kâinat da Onundur' hakikatini ispat etti.")
    satirlar.append("=" * 72)
    return "\n".join(satirlar)


def zerre_csv_yaz(yol: str, r: ZerreSonuc) -> None:
    with open(yol, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["mertebe", "kaldirilan_yuk", "intizam", "vucud_sehadeti", "vahdet_sehadeti", "hikmet", "zikir"])
        for d in r.duraklar:
            w.writerow([d.mertebe_adi, d.kaldirilan_yuk, d.intizam_orani, d.vucud_sehadeti, d.vahdet_sehadeti, d.hikmet_skoru, d.zikir])


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Tahavvülât-ı Zerrât ve Kudret Kalemi Simülasyonu.")
    ap.add_argument("--senaryo", "-s", choices=sorted(ZERRE_SENARYOLAR), default="tevfikin_gozu",
                    help="Hazır senaryo (varsayılan: tevfikin_gozu)")
    ap.add_argument("--listele", action="store_true", help="Senaryoları listele")
    ap.add_argument("--karsilastir", action="store_true", help="Tüm senaryoları karşılaştır")
    ap.add_argument("--csv", metavar="DOSYA.csv", help="CSV çıktısı kaydet")
    ap.add_argument("--bismillah", type=float, default=None, help="Bismillah istinad nisbeti [0, 1]")
    ap.add_argument("--vahdet", type=float, default=None, help="Vahdet nizamına intibak [0, 1]")
    ap.add_argument("--tesaduf", type=float, default=None, help="Tesadüf sapması [0, 1]")

    args = ap.parse_args(argv)

    if args.listele:
        for k, v in ZERRE_SENARYOLAR.items():
            print(f"  {k:<18} {v['aciklama']}")
        return 0

    elle: Dict[str, float] = {}
    if args.bismillah is not None:
        elle["bismillah_nisbeti"] = args.bismillah
    if args.vahdet is not None:
        elle["vahdet_intibaki"] = args.vahdet
    if args.tesaduf is not None:
        elle["tesaduf_sapmasi"] = args.tesaduf

    if args.karsilastir:
        print(f"{'Senaryo':<18} {'İntizam':>9} {'Vücud Ş.':>10} {'Vahdet Ş.':>10} {'Hikmet':>9}  Durum")
        print("-" * 68)
        for ad in ZERRE_SENARYOLAR:
            p = replace(zerre_senaryo_parametreleri(ad), **elle)
            r = zerre_simule_et(p)
            durum = "Kaos/Tesadüf" if r.tesaduf_cikmazi else "Kudret İntizamı"
            print(f"{ad:<18} {r.ortalama_intizam:>9.2f} {r.vucud_sehadet_skoru:>10.2f} {r.vahdet_sehadet_skoru:>10.2f} {r.nihai_hikmet:>9.2f}  {durum}")
        return 0

    try:
        p = replace(zerre_senaryo_parametreleri(args.senaryo), **elle)
        r = zerre_simule_et(p)
    except ValueError as exc:
        print(f"Hata: {exc}", file=sys.stderr)
        return 2

    print(zerre_raporu(args.senaryo, p, r))
    if args.csv:
        zerre_csv_yaz(args.csv, r)
        print(f"\nCSV kaydedildi: {args.csv}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
