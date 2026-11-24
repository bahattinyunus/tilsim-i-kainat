#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌌 TILSIM-I KÂİNAT: ESMÂ-İ HÜSNÂ FRAKTAL ÖZ-BENZERLİK VE ÖLÇEK DEĞİŞMEZLİĞİ MODELİ
=====================================================================================
Kaynak Eserler:
  - 30. Lem'a (İsm-i Âzam Risalesi: Ferd, Hayy, Kayyûm, Hakem, Adl, Kuddûs)
    "Nasıl ki bir çekirdek, bütün ağacın fihristesini taşır; öyle de zerre,
     güneş sisteminin; insan ise bütün kâinatın misâl-i musaggarı ve fihristesidir."
  - 32. Söz (İkinci Mevkıf — Zerrede, Güneşte ve İnsanda Aynı Vahdet Mührü)
  - 17. Lem'a & Mesnevî-i Nuriye ("Kâinat büyük bir insan, insan küçük bir kâinattır.")

21. Yüzyıl Fiziği & Matematik Paralelleri:
  - Fraktal Geometri ve Öz-Benzerlik (Benoit Mandelbrot):
    Doğadaki yapılar (damar ağları, nehir deltaları, galaksi ağları, ağaç dalları)
    ölçekten bağımsız öz-benzer (self-similar) fraktal boyut (D_f) sergiler.
  - Renormalizasyon Grubu ve Ölçek Değişmezliği (Kenneth Wilson):
    Kritik noktalarda fiziksel sistemler mikroskobik (10^-15 m) ölçekten kozmik
    (10^26 m) ölçeğe kadar aynı matematiksel simetri ve yasaları (Sikke-i Vahdet) korur.
  - Esmâ Rezonansı (İsm-i Âzam Mührü):
    Mikro (zerre), mezo (insan/hücre) ve makro (galaksi) ölçekler arasındaki yapısal
    uyum (rezonans), tek bir Sâni-i Hakîm'in kaleminden çıktığının geometrik ispatıdır.
"""

from dataclasses import dataclass
import argparse
import csv
import math
import sys
from typing import Dict, Optional


@dataclass
class FraktalParametreleri:
    """Esmâ-i Hüsnâ Fraktal Öz-Benzerlik ve Ölçek Değişmezliği girdi parametreleri."""
    olcek_araligi_log10: float   # İncelenen ölçek açıklığı (log10 metre; örn. 41 = Planck/Zerre -> Kozmos) [1.0 - 61.0]
    oz_benzerlik_orani: float    # Ölçekler arası yapısal öz-benzerlik / Sikke-i Vahdet uyumu [0.0 - 1.0]
    esma_tenevvuu: int           # Aynı anda tecelli eden aktif Esmâ boyutu sayısı [1 - 99]
    intizam_direnci: float       # Ölçek büyüdükçe entropiye/dağılmaya karşı korunan nizam [0.0 - 1.0]


@dataclass
class FraktalCiktisi:
    """Fraktal Öz-Benzerlik ve İsm-i Âzam Mührü analitik çıktıları."""
    fraktal_boyut_df: float      # Hesaplanan efektif fraktal boyut (D_f: 1.00 - 3.00)
    sikke_i_vahdet_skoru: float  # Ölçekler arası vahdet mührü tutarlılığı [0 - 100]
    renormalizasyon_kararliligi: float  # Ölçek değişmezliği / sabit nokta kararlılığı [0 - 100]
    fihriste_yogunlugu: float    # Küçük parçada büyük âlemin temsiliyet yoğunluğu [0 - 100]
    tevhid_imzasi: str           # Ölçekler arası vahdet derecesi
    hukum: str                   # Fiziksel ve kelâmî netice


SENARYOLAR: Dict[str, FraktalParametreleri] = {
    "ism_i_azam_kainat": FraktalParametreleri(
        olcek_araligi_log10=41.0,   # 10^-15 m (proton/zerre) -> 10^26 m (gözlemlenebilir evren)
        oz_benzerlik_orani=0.98,
        esma_tenevvuu=99,
        intizam_direnci=0.97,
    ),
    "insan_fihristesi": FraktalParametreleri(
        olcek_araligi_log10=12.0,   # Molekül -> Hücre -> Organ -> İnsan bedeni ve şuur
        oz_benzerlik_orani=0.95,
        esma_tenevvuu=70,
        intizam_direnci=0.94,
    ),
    "cekirdek_ve_agac": FraktalParametreleri(
        olcek_araligi_log10=6.0,    # DNA / Çekirdek -> Dev Çınar Ağacı
        oz_benzerlik_orani=0.91,
        esma_tenevvuu=40,
        intizam_direnci=0.88,
    ),
    "kristal_ve_bulut": FraktalParametreleri(
        olcek_araligi_log10=4.0,    # Kar tanesi / Bulut fraktali (yarı-canlı nizam)
        oz_benzerlik_orani=0.72,
        esma_tenevvuu=18,
        intizam_direnci=0.65,
    ),
    "tesadufi_gurultu": FraktalParametreleri(
        olcek_araligi_log10=10.0,   # Ölçekler arası koptu / kaotik gürültü varsayımı
        oz_benzerlik_orani=0.08,
        esma_tenevvuu=1,
        intizam_direnci=0.10,
    ),
}


def dogrula_fraktal_parametreleri(p: FraktalParametreleri) -> None:
    """Girdi parametrelerinin sınırlarını doğrular."""
    if not (1.0 <= p.olcek_araligi_log10 <= 61.0):
        raise ValueError("olcek_araligi_log10 [1.0, 61.0] aralığında olmalıdır.")
    if not (0.0 <= p.oz_benzerlik_orani <= 1.0):
        raise ValueError("oz_benzerlik_orani [0.0, 1.0] aralığında olmalıdır.")
    if not (1 <= p.esma_tenevvuu <= 99):
        raise ValueError("esma_tenevvuu [1, 99] aralığında olmalıdır.")
    if not (0.0 <= p.intizam_direnci <= 1.0):
        raise ValueError("intizam_direnci [0.0, 1.0] aralığında olmalıdır.")


def hesapla_fraktal_durumu(p: FraktalParametreleri) -> FraktalCiktisi:
    """
    30. Lem'a (İsm-i Âzam), 32. Söz (Sikke-i Vahdet) ve Mandelbrot Fraktal /
    Renormalizasyon Grubu denklemleriyle ölçekler arası vahdet mührünü hesaplar.
    """
    dogrula_fraktal_parametreleri(p)

    # 1. Efektif Fraktal Boyut (D_f):
    # Saf doğrusal/dağınık gürültü ~1.0'a yaklaşır; zengin Esmâ tenevvüü ve yüksek
    # öz-benzerlik ile hacmi dolduran canlı/kozmik fraktal boyut (2.5 - 2.95) oluşur.
    esma_faktoru = math.log10(p.esma_tenevvuu + 1.0) / math.log10(100.0)  # [0.15 - 1.0]
    fraktal_boyut_df = round(
        1.0 + 1.95 * (0.55 * p.oz_benzerlik_orani + 0.25 * p.intizam_direnci + 0.20 * esma_faktoru),
        3,
    )

    # 2. Renormalizasyon Kararlılığı (Ölçek Değişmezliği):
    # Ölçek aralığı büyüdükçe nizamı korumak tesadüfen imkânsızlaşır; yüksek intizam
    # direnci ve öz-benzerlik ile sabit nokta (fixed point) kararlılığı %100'e yaklaşır.
    olcek_zorlugu = math.log10(p.olcek_araligi_log10 + 1.0) / math.log10(62.0)  # [0.17 - 1.0]
    renormalizasyon_kararliligi = round(
        100.0 * (p.oz_benzerlik_orani ** (1.0 + 0.6 * olcek_zorlugu)) * (0.35 + 0.65 * p.intizam_direnci),
        2,
    )

    # 3. Sikke-i Vahdet Skoru:
    # Mikro ve makro âlemlerin tek bir Sâni'nin kaleminden çıktığını gösteren bileşik skor.
    sikke_i_vahdet_skoru = round(
        100.0 * (0.45 * p.oz_benzerlik_orani + 0.35 * p.intizam_direnci + 0.20 * esma_faktoru),
        2,
    )

    # 4. Fihriste Yoğunluğu:
    # Bir çekirdeğin ağacı, insanın kâinatı özetleme kapasitesi (Misâl-i Musaggar).
    fihriste_yogunlugu = round(
        min(100.0, 100.0 * (0.50 * esma_faktoru + 0.30 * p.oz_benzerlik_orani + 0.20 * olcek_zorlugu) * p.intizam_direnci),
        2,
    )

    # 5. Tevhid İmzası & Kelâmî Hüküm:
    if sikke_i_vahdet_skoru >= 85.0:
        tevhid_imzasi = "İsm-i Âzam Mührü (Külli Ölçek Değişmezliği)"
        hukum = (
            "Zerrede, insanda ve galakside aynı Sikke-i Vahdet okunur. "
            "41 mertebe ölçek boyunca korunan öz-benzerlik, tek bir Sâni-i Hakîm'in kesin bürhanıdır."
        )
    elif sikke_i_vahdet_skoru >= 65.0:
        tevhid_imzasi = "Misâl-i Musaggar (Fihriste-i Âlem)"
        hukum = (
            "Küçük parça büyük âlemin çekirdek programını taşır; "
            "çekirdekten ağaca, hücreden insana aynı İlim ve Kudret kalemi işler."
        )
    elif sikke_i_vahdet_skoru >= 40.0:
        tevhid_imzasi = "Cüz'î Fraktal Nizam (Kısmi Tecelli)"
        hukum = (
            "Yerel ölçekte geometrik düzen görülür; ancak yüksek Esmâ tenevvüü ve "
            "külli ölçek kararlılığı henüz tam inkişaf etmemiştir."
        )
    else:
        tevhid_imzasi = "Ölçek Kopukluğu (Tesadüf / Gürültü Varsayımı)"
        hukum = (
            "Tesadüf ve esbabperestlik ölçekler arası öz-benzerliği açıklayamaz; "
            "intizam direnci çöker ve yapı kaotik gürültüye dağılır."
        )

    return FraktalCiktisi(
        fraktal_boyut_df=fraktal_boyut_df,
        sikke_i_vahdet_skoru=sikke_i_vahdet_skoru,
        renormalizasyon_kararliligi=renormalizasyon_kararliligi,
        fihriste_yogunlugu=fihriste_yogunlugu,
        tevhid_imzasi=tevhid_imzasi,
        hukum=hukum,
    )


def tablo_yazdir() -> None:
    """Tüm ön tanımlı fraktal ve ölçek değişmezliği senaryolarını tablolaştırır."""
    print("=" * 108)
    print("🌌 ESMÂ-İ HÜSNÂ FRAKTAL ÖZ-BENZERLİK & ÖLÇEK DEĞİŞMEZLİĞİ (30. LEM'A & MANDELBROT)")
    print("=" * 108)
    header = (
        f"{'Senaryo':<22} | {'Ölçek':>6} | {'Esmâ':>4} | {'D_f':>5} | "
        f"{'Vahdet%':>7} | {'RG Karar%':>9} | {'Fihriste%':>9} | {'Tevhid İmzası'}"
    )
    print(header)
    print("-" * 108)
    for ad, param in SENARYOLAR.items():
        c = hesapla_fraktal_durumu(param)
        print(
            f"{ad:<22} | 10^{param.olcek_araligi_log10:>2.0f} | {param.esma_tenevvuu:>4d} | "
            f"{c.fraktal_boyut_df:>5.3f} | {c.sikke_i_vahdet_skoru:>6.2f}% | "
            f"{c.renormalizasyon_kararliligi:>8.2f}% | {c.fihriste_yogunlugu:>8.2f}% | {c.tevhid_imzasi}"
        )
    print("=" * 108)


def csv_yazdir(dosya_yolu: str) -> None:
    """Senaryo çıktılarını CSV dosyasına aktarır."""
    with open(dosya_yolu, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "senaryo",
            "olcek_araligi_log10",
            "oz_benzerlik_orani",
            "esma_tenevvuu",
            "intizam_direnci",
            "fraktal_boyut_df",
            "sikke_i_vahdet_skoru",
            "renormalizasyon_kararliligi",
            "fihriste_yogunlugu",
            "tevhid_imzasi",
        ])
        for ad, p in SENARYOLAR.items():
            c = hesapla_fraktal_durumu(p)
            writer.writerow([
                ad,
                p.olcek_araligi_log10,
                p.oz_benzerlik_orani,
                p.esma_tenevvuu,
                p.intizam_direnci,
                c.fraktal_boyut_df,
                c.sikke_i_vahdet_skoru,
                c.renormalizasyon_kararliligi,
                c.fihriste_yogunlugu,
                c.tevhid_imzasi,
            ])
    print(f"CSV yazıldı: {dosya_yolu}")


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Esmâ-i Hüsnâ Fraktal Öz-Benzerlik ve Ölçek Değişmezliği Modeli (30. Lem'a)"
    )
    parser.add_argument("--senaryo", choices=list(SENARYOLAR.keys()), help="Ön tanımlı bir senaryoyu çalıştır")
    parser.add_argument("--tablo", action="store_true", help="Tüm senaryoları karşılaştırma tablosu olarak yazdır")
    parser.add_argument("--olcek", type=float, default=41.0, help="Ölçek aralığı log10 metre (1.0 - 61.0)")
    parser.add_argument("--benzerlik", type=float, default=0.95, help="Öz-benzerlik oranı (0.0 - 1.0)")
    parser.add_argument("--esma", type=int, default=70, help="Aktif Esmâ boyutu sayısı (1 - 99)")
    parser.add_argument("--intizam", type=float, default=0.94, help="İntizam direnci (0.0 - 1.0)")
    parser.add_argument("--csv", type=str, help="Sonuçları CSV dosyasına kaydet")

    args = parser.parse_args(argv)

    if args.csv:
        csv_yazdir(args.csv)
        return 0

    if args.tablo:
        tablo_yazdir()
        return 0

    if args.senaryo:
        p = SENARYOLAR[args.senaryo]
        ad = args.senaryo
    else:
        p = FraktalParametreleri(
            olcek_araligi_log10=args.olcek,
            oz_benzerlik_orani=args.benzerlik,
            esma_tenevvuu=args.esma,
            intizam_direnci=args.intizam,
        )
        ad = "ozel_parametre"

    c = hesapla_fraktal_durumu(p)
    print(f"\n🌌 Senaryo: {ad}")
    print(f"  Ölçek Aralığı               : 10^{p.olcek_araligi_log10:.1f} m")
    print(f"  Efektif Fraktal Boyut (D_f) : {c.fraktal_boyut_df:.3f}")
    print(f"  Sikke-i Vahdet Skoru        : %{c.sikke_i_vahdet_skoru:.2f}")
    print(f"  Renormalizasyon Kararlılığı : %{c.renormalizasyon_kararliligi:.2f}")
    print(f"  Fihriste Yoğunluğu          : %{c.fihriste_yogunlugu:.2f}")
    print(f"  Tevhid İmzası               : {c.tevhid_imzasi}")
    print(f"  Hüküm                       : {c.hukum}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
