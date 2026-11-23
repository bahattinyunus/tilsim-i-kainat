#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌌 TILSIM-I KÂİNAT: HOLOGRAFİK ÂLEM-İ MİSÂL, EHADİYET VE AYNALAR MODELİ (16. SÖZ)
===================================================================================
Kaynak Eserler:
  - 16. Söz (İkinci Şua — Güneş'in Aynalardaki Temessülü, Vâhidiyet ve Ehadiyet Sırrı)
    "Nasıl ki güneş, nuraniyeti cihetiyle bir iken, bütün şeffaf eşyada ve her bir
     katre suda ve her bir cam parçasında bütün sıfatlarıyla (ziyası, harareti,
     yedi rengiyle) tecezzi etmeden ve bölünmeden bulunur; öyle de..."
  - 16. Söz (Birinci Şua — Kurb ve Bu'd Sırrı: "O bize nihayetsiz yakındır, biz Ona nihayetsiz uzağız.")
  - 28. Mektup & 29. Söz (Âlem-i Misâl — Her hadisenin gaybî/misâlî sınırda kaydı)

21. Yüzyıl Fiziği & Kozmoloji Paralelleri:
  - Holografik İlke (Gerard 't Hooft, Leonard Susskind & Juan Maldacena — AdS/CFT):
    3 boyutlu hacimsel uzayda (Bulk / Âlem-i Şehadet) bulunan bütün fiziksel bilgi,
    aslında onu çevreleyen 2 boyutlu sınır yüzeyinde (Boundary / Âlem-i Misâl & Levh-i Mahfuz)
    Planck alanı başına kodlanmıştır: I_max = A / (4 * l_P^2 * ln 2).
  - Hologramın Bütünlük Özelliği (Ehadiyet Analojisi):
    Bir hologram bin parçaya bölünse dahi, her bir küçük parça (katre) bütün resmin
    eksiksiz projeksiyonunu taşır; kaynak bölünmez (tecezzi etmez).
  - ER = EPR (Maldacena & Susskind):
    Uzay-zaman mesafesi ne kadar büyük olursa olsun, dolanıklık (EPR) ile mekân ötesi
    anlık kurb (yakınlık) vardır; nuraniyet için uzaklık ve sayı engel (mâni) teşkil etmez.
"""

from dataclasses import dataclass
import argparse
import csv
import math
import sys
from typing import Dict, Optional


@dataclass
class HolografiParametreleri:
    """16. Söz Aynalar, Ehadiyet ve Holografik İlke (AdS/CFT) girdi parametreleri."""
    ayna_seffafiyeti: float      # Kalp / zerre aynasının safiyet ve şeffaflığı [0.0 - 1.0]
    ayna_sayisi_log10: float     # Aynaların sayısının log10 değeri (0 = 1 ayna, 20 = 10^20 katre) [0.0 - 30.0]
    holografik_cozunurluk: float # Sınır (Boundary / Âlem-i Misâl) projeksiyon sadakati [0.0 - 1.0]
    mesafe_log10_km: float       # Kaynaktan zâhirî maddî uzaklık (log10 km) [0.0 - 20.0]


@dataclass
class HolografiCiktisi:
    """Holografik Âlem-i Misâl ve Ehadiyet analitik çıktıları."""
    ehadiyet_tecellisi: float      # Tek bir aynada Güneş'in bütün sıfatlarıyla zuhuru [0 - 100]
    kaynak_bolunme_kaybi: float    # Kaynağın sayı ve mesafeyle bölünme kaybı (Nuraniyet için daima 0.0!)
    kurb_etkinligi: float          # ER=EPR / Kurb-i İlâhî mesafeden bağımsız yakınlık skoru [0 - 100]
    holografik_sadakat: float      # Bulk (Şehadet) <-> Boundary (Âlem-i Misâl) bilgi korunumu [0 - 100]
    vahidiyet_kapasitesi_log10: float  # Bütün aynalarda aynı anda tecelli eden küllî iz (log10)
    ontolojik_mertebe: str         # 16. Söz mertebesi
    hukum: str                     # Fiziksel ve kelâmî netice


SENARYOLAR: Dict[str, HolografiParametreleri] = {
    "kalb_i_selim_ehadiyet": HolografiParametreleri(
        ayna_seffafiyeti=0.99,
        ayna_sayisi_log10=24.0,     # 10^24 şeffaf zerre ve kalp
        holografik_cozunurluk=0.98,
        mesafe_log10_km=15.0,       # Kozmik uzaklık — nuraniyet için engel değil
    ),
    "katre_aynasi_holografi": HolografiParametreleri(
        ayna_seffafiyeti=0.95,
        ayna_sayisi_log10=12.0,     # 1 trilyon çiğ tanesi (katre)
        holografik_cozunurluk=0.92,
        mesafe_log10_km=8.17,       # Güneş-Dünya mesafesi (~1.5e8 km)
    ),
    "okyanus_vahidiyet": HolografiParametreleri(
        ayna_seffafiyeti=0.88,
        ayna_sayisi_log10=0.0,      # Tek dev ayna (Bahr / Okyanus)
        holografik_cozunurluk=0.90,
        mesafe_log10_km=8.17,
    ),
    "puslu_ayna_gaflet": HolografiParametreleri(
        ayna_seffafiyeti=0.25,
        ayna_sayisi_log10=6.0,
        holografik_cozunurluk=0.35,
        mesafe_log10_km=8.17,
    ),
    "kirik_maddeci_ayna": HolografiParametreleri(
        ayna_seffafiyeti=0.04,
        ayna_sayisi_log10=3.0,
        holografik_cozunurluk=0.10,
        mesafe_log10_km=12.0,
    ),
}


def dogrula_holografi_parametreleri(p: HolografiParametreleri) -> None:
    """Girdi parametrelerinin geçerliliğini denetler."""
    if not (0.0 <= p.ayna_seffafiyeti <= 1.0):
        raise ValueError("ayna_seffafiyeti [0.0, 1.0] aralığında olmalıdır.")
    if not (0.0 <= p.ayna_sayisi_log10 <= 30.0):
        raise ValueError("ayna_sayisi_log10 [0.0, 30.0] aralığında olmalıdır.")
    if not (0.0 <= p.holografik_cozunurluk <= 1.0):
        raise ValueError("holografik_cozunurluk [0.0, 1.0] aralığında olmalıdır.")
    if not (0.0 <= p.mesafe_log10_km <= 20.0):
        raise ValueError("mesafe_log10_km [0.0, 20.0] aralığında olmalıdır.")


def hesapla_holografi_durumu(p: HolografiParametreleri) -> HolografiCiktisi:
    """
    16. Söz (Temessül & Ehadiyet) ve AdS/CFT Holografik İlke denklemleriyle
    ayna tecellisini ve bilgi bütünlüğünü hesaplar.
    """
    dogrula_holografi_parametreleri(p)

    # 1. Kaynak Bölünme Kaybı (Tecezzi):
    # 16. Söz'ün temel teoremi: Nuraniyet, ayna sayısı 1'den 10^30'a çıksa dahi
    # ve mesafe ne kadar artsa da tecezzi etmez (bölünmez).
    kaynak_bolunme_kaybi = 0.0

    # 2. Ehadiyet Tecellisi (0 - 100):
    # Ayna sayısından ve mesafeden TAMAMEN bağımsızdır! Yalnızca aynanın kabiliyetine
    # (şeffafiyetine) ve holografik sınır sadakatine bağlıdır.
    ehadiyet_tecellisi = round(
        100.0 * (0.70 * p.ayna_seffafiyeti + 0.30 * p.ayna_seffafiyeti * p.holografik_cozunurluk),
        2,
    )

    # 3. Kurb Etkinliği (16. Söz Kurb-Bu'd Sırrı & ER=EPR):
    # Hakikatte kurb mesafeye tabi değildir; engel sadece aynanın kesafetidir (bu'd bizim cihetimizdedir).
    # Şeffaflık yükseldikçe mesafe perdesi tamamen silinir.
    kesafet_perdesi = (1.0 - p.ayna_seffafiyeti) * (0.15 + 0.02 * p.mesafe_log10_km)
    kurb_etkinligi = round(max(0.0, min(100.0, 100.0 * (1.0 - min(1.0, kesafet_perdesi)))), 2)

    # 4. Holografik Sadakat (Bulk <-> Boundary / Âlem-i Şehadet <-> Âlem-i Misâl):
    # AdS/CFT'de sınır bilgisinin hacimde eksiksiz tezahürü
    holografik_sadakat = round(
        100.0 * math.sqrt(p.holografik_cozunurluk * max(0.0001, p.ayna_seffafiyeti)),
        2,
    )

    # 5. Vâhidiyet Kapasitesi (log10):
    # Tüm aynalardaki eşzamanlı ihata: N ayna * (ehadiyet/100)
    if ehadiyet_tecellisi > 0.0:
        vahidiyet_kapasitesi_log10 = round(
            p.ayna_sayisi_log10 + math.log10(max(1e-4, ehadiyet_tecellisi / 100.0)),
            2,
        )
    else:
        vahidiyet_kapasitesi_log10 = 0.0

    # 6. Ontolojik Mertebe ve Hüküm
    if ehadiyet_tecellisi >= 90.0:
        mertebe = "Cilve-i Ehadiyet & Şeffaf Hologram"
        hukum = (
            "16. Söz Sırrı Tahakkuk Etti: Kaynak bölünmeden (tecezzi=0.0) ve mesafe engel olmadan "
            "her bir katrede bütün sıfatlarıyla tecelli etmektedir (AdS/CFT & ER=EPR tam uyumu)."
        )
    elif ehadiyet_tecellisi >= 75.0:
        mertebe = "Vâhidiyet İhatası & Parlak Temessül"
        hukum = (
            "Büyük ayna (okyanus) ile küçük ayna (katre) kaynak karşısında müsavidir; "
            "Âlem-i Misâl kaydı şehadet âleminde yüksek sadakatle projekte olmaktadır."
        )
    elif ehadiyet_tecellisi >= 20.0:
        mertebe = "Puslu Ayna & Kısmi Perdelenme"
        hukum = (
            "Gaflet ve kesafet aynayı puslandırmıştır; kurb hakikatte değişmese de "
            "bu'd (uzaklık) hissiyatı aynanın kendi bulanıklığından kaynaklanmaktadır."
        )
    else:
        mertebe = "Kesif / Kırık Ayna (Zulmet Perdesi)"
        hukum = (
            "Maddeci nazar aynayı kararttığı için güneşin aksi görünmemekte; "
            "holografik bütünlük yerine kopuk, karanlık parçacıklar algılanmaktadır."
        )

    return HolografiCiktisi(
        ehadiyet_tecellisi=ehadiyet_tecellisi,
        kaynak_bolunme_kaybi=kaynak_bolunme_kaybi,
        kurb_etkinligi=kurb_etkinligi,
        holografik_sadakat=holografik_sadakat,
        vahidiyet_kapasitesi_log10=vahidiyet_kapasitesi_log10,
        ontolojik_mertebe=mertebe,
        hukum=hukum,
    )


def calistir_senaryo(ad: str) -> HolografiCiktisi:
    """Ön tanımlı bir senaryoyu çalıştırır."""
    if ad not in SENARYOLAR:
        raise KeyError(f"Bilinmeyen senaryo: '{ad}'. Geçerliler: {list(SENARYOLAR.keys())}")
    return hesapla_holografi_durumu(SENARYOLAR[ad])


def tum_senaryolari_karsilastir() -> Dict[str, HolografiCiktisi]:
    """Bütün senaryoları hesaplar."""
    return {ad: hesapla_holografi_durumu(p) for ad, p in SENARYOLAR.items()}


def tablo_yazdir(sonuclar: Dict[str, HolografiCiktisi]) -> None:
    """Sonuçları terminal tablosu olarak yazdırır."""
    print("=" * 102)
    print("  🪞 HOLOGRAFİK ÂLEM-İ MİSÂL, EHADİYET VE AYNALAR (16. SÖZ & AdS/CFT) KARŞILAŞTIRMASI")
    print("=" * 102)
    print(f"{'Senaryo':<26} | {'Ehadiyet':>8} | {'Tecezzi':>7} | {'Kurb':>7} | {'Holo':>7} | {'Vâhidiyet':>10} | {'Mertebe'}")
    print("-" * 102)
    for ad, c in sonuclar.items():
        print(
            f"{ad:<26} | {c.ehadiyet_tecellisi:>7.1f}% | {c.kaynak_bolunme_kaybi:>6.1f}% | "
            f"{c.kurb_etkinligi:>6.1f}% | {c.holografik_sadakat:>6.1f}% | "
            f"10^{c.vahidiyet_kapasitesi_log10:<6.2f} | {c.ontolojik_mertebe}"
        )
    print("=" * 102)


def csv_yaz(dosya_yolu: str) -> None:
    """Tüm senaryo sonuçlarını CSV dosyasına aktarır."""
    sonuclar = tum_senaryolari_karsilastir()
    with open(dosya_yolu, "w", newline="", encoding="utf-8") as f:
        yazici = csv.writer(f)
        yazici.writerow([
            "senaryo",
            "ehadiyet_tecellisi",
            "kaynak_bolunme_kaybi",
            "kurb_etkinligi",
            "holografik_sadakat",
            "vahidiyet_kapasitesi_log10",
            "ontolojik_mertebe",
            "hukum",
        ])
        for ad, c in sonuclar.items():
            yazici.writerow([
                ad,
                c.ehadiyet_tecellisi,
                c.kaynak_bolunme_kaybi,
                c.kurb_etkinligi,
                c.holografik_sadakat,
                c.vahidiyet_kapasitesi_log10,
                c.ontolojik_mertebe,
                c.hukum,
            ])


def main(argv: Optional[list] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Holografik Âlem-i Misâl, Ehadiyet ve Aynalar (16. Söz & AdS/CFT) Simülasyonu"
    )
    parser.add_argument("--senaryo", choices=list(SENARYOLAR.keys()), help="Tekil senaryo çalıştır")
    parser.add_argument("--tablo", action="store_true", help="Tüm senaryoları tablo olarak karşılaştır")
    parser.add_argument("--csv", type=str, help="Sonuçları CSV dosyasına yaz")
    args = parser.parse_args(argv)

    if args.csv:
        csv_yaz(args.csv)
        print(f"CSV raporu yazıldı: {args.csv}")
        return 0

    if args.senaryo:
        c = calistir_senaryo(args.senaryo)
        print(f"\n🪞 Senaryo: {args.senaryo}")
        print(f"  • Ehadiyet Tecellisi   : %{c.ehadiyet_tecellisi}")
        print(f"  • Kaynak Bölünme Kaybı : %{c.kaynak_bolunme_kaybi} (Nuraniyet tecezzi etmez)")
        print(f"  • Kurb Etkinliği       : %{c.kurb_etkinligi}")
        print(f"  • Holografik Sadakat   : %{c.holografik_sadakat}")
        print(f"  • Vâhidiyet İhatası    : 10^{c.vahidiyet_kapasitesi_log10}")
        print(f"  • Ontolojik Mertebe    : {c.ontolojik_mertebe}")
        print(f"  • Hüküm                : {c.hukum}\n")
        return 0

    tablo_yazdir(tum_senaryolari_karsilastir())
    return 0


if __name__ == "__main__":
    sys.exit(main())
