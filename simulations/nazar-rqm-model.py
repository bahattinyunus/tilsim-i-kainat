#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌌 TILSIM-I KÂİNAT: MÂNÂ-YI HARFÎ, NİYET-NAZAR VE İLİŞKİSEL KUANTUM MODELİ
============================================================================
Kaynak Eserler:
  - Mesnevî-i Nuriye (Mukaddime & Katre — Dört Kelime: Mânâ-yı Harfî, Mânâ-yı İsmî, Niyet, Nazar)
    "Niyet bir ruh-u âherdir. Âdâtı ibadâta, gafleti huzura kalbeder."
    "Eşyaya mânâ-yı ismî ile bakmak, onları kendi hesabına mütâlaa etmek hatadır;
     mânâ-yı harfî ile bakmak, Sâni' hesabına nazar etmek hakikattir."
  - 11. Söz & 17. Söz & 30. Söz (Ene'nin Vâhid-i Kıyasî ve Ayna Vazifesi)

21. Yüzyıl Fiziği & Bilişsel Bilim Paralelleri:
  - Carlo Rovelli — İlişkisel Kuantum Mekaniği (Relational Quantum Mechanics / RQM):
    Hiçbir fiziksel sistemin tek başına (mânâ-yı ismî / mutlak töz) tanımlı bir durumu yoktur;
    özellikler yalnızca başka sistemlerle kurulan ilişkide (mânâ-yı harfî / nisbet) zuhur eder.
  - Donald Hoffman — Arayüz Algı Kuramı (Interface Theory of Perception / ITP):
    Uzay-zaman ve maddî cisimler mutlak hakikat değil, şuurun muhatap olduğu bir "masaüstü arayüzü"dür
    (şehadet perdesi). Sadece biyolojik faydaya (nefsânî istifade) odaklanan algı, arayüzün
    arkasındaki kodu (esmâ-i ilâhiye) gizler; niyet ve nazar ise arayüzün şifresini çözer.
  - Enformasyon Teorisi (Karşılıklı Bilgi / Epistemik Kazanç):
    Harfî nazar, gözlemlenen kâinat kitabından elde edilen marifet bitlerini (anlam yoğunluğunu)
    üstel olarak artırır; ismî nazar ise veriyi "gürültü ve kör tesadüf"e indirger.
"""

from dataclasses import dataclass
import argparse
import csv
import math
import sys
from typing import Dict, Optional


@dataclass
class NazarParametreleri:
    """Mânâ-yı harfî, niyet-nazar ve ilişkisel gözlem parametreleri."""
    nazar_harfi_orani: float      # Eşyaya Sâni' hesabına (harfî) bakış oranı [0.0 - 1.0]
    niyet_halisiyeti: float       # Niyetin sırf rıza-yı İlâhîye yönelme safiyeti [0.0 - 1.0]
    arayuz_farkindaligi: float    # Şehadet perdesinin (Hoffman ITP) arka planını okuma [0.0 - 1.0]
    iliskisel_bag_derinligi: float  # RQM ilişkisel ağ / esmâ nisbetini kavrama derecesi [0.0 - 1.0]


@dataclass
class NazarCiktisi:
    """Mânâ-yı harfî ve ilişkisel kuantum simülasyonu analitik çıktıları."""
    epistemik_berraklik: float     # Hakikati arayüz yanılsamasından ayırma berraklığı [0 - 100]
    ibadet_simyasi_carpani: float  # Niyetin âdâtı ibadete çevirme çarpanı [0.0 - 100.0]
    iliskisel_anlam_biti: float    # RQM / Harfî okuma ile kazanılan marifet enformasyonu (bit)
    arayuz_yanilsamasi: float      # Mânâ-yı ismî / materyalist masaüstü illüzyonu [0 - 100]
    hakikat_mertebesi: str         # Epistemolojik ve manevî makam
    hukum: str                     # Kelâmî ve fiziksel netice


SENARYOLAR: Dict[str, NazarParametreleri] = {
    "mana_yi_harfi_velayet": NazarParametreleri(
        nazar_harfi_orani=0.98,
        niyet_halisiyeti=0.96,
        arayuz_farkindaligi=0.95,
        iliskisel_bag_derinligi=0.97,
    ),
    "tefekkur_ve_niyet": NazarParametreleri(
        nazar_harfi_orani=0.82,
        niyet_halisiyeti=0.85,
        arayuz_farkindaligi=0.75,
        iliskisel_bag_derinligi=0.80,
    ),
    "bilimsel_gozlem_notr": NazarParametreleri(
        nazar_harfi_orani=0.45,
        niyet_halisiyeti=0.40,
        arayuz_farkindaligi=0.55,
        iliskisel_bag_derinligi=0.65,
    ),
    "mana_yi_ismi_gaflet": NazarParametreleri(
        nazar_harfi_orani=0.12,
        niyet_halisiyeti=0.15,
        arayuz_farkindaligi=0.10,
        iliskisel_bag_derinligi=0.15,
    ),
    "materyalist_arayuz_yanilsamasi": NazarParametreleri(
        nazar_harfi_orani=0.02,
        niyet_halisiyeti=0.05,
        arayuz_farkindaligi=0.02,
        iliskisel_bag_derinligi=0.05,
    ),
}


def dogrula_nazar_parametreleri(p: NazarParametreleri) -> None:
    """Parametrelerin [0.0, 1.0] kapalı aralığında olduğunu doğrular."""
    alanlar = {
        "nazar_harfi_orani": p.nazar_harfi_orani,
        "niyet_halisiyeti": p.niyet_halisiyeti,
        "arayuz_farkindaligi": p.arayuz_farkindaligi,
        "iliskisel_bag_derinligi": p.iliskisel_bag_derinligi,
    }
    for ad, deger in alanlar.items():
        if not (0.0 <= deger <= 1.0):
            raise ValueError(f"{ad} parametresi [0.0, 1.0] aralığında olmalıdır (verilen: {deger}).")


def hesapla_nazar_durumu(p: NazarParametreleri) -> NazarCiktisi:
    """
    Mesnevî-i Nuriye (Dört Kelime), Rovelli RQM ve Hoffman ITP ilkeleriyle
    mânâ-yı harfî / ismî epistemolojisini hesaplar.
    """
    dogrula_nazar_parametreleri(p)

    # 1. Epistemik Berraklık (0 - 100):
    # Harfî nazar, arayüz farkındalığı ve ilişkisel bağın harmonik-ağırlıklı sentezi
    berraklik_ham = (
        0.40 * p.nazar_harfi_orani
        + 0.25 * p.arayuz_farkindaligi
        + 0.20 * p.iliskisel_bag_derinligi
        + 0.15 * p.niyet_halisiyeti
    )
    # Harfî nazar sıfıra yakınken arayüz perdelemesi berraklığı bastırır
    epistemik_berraklik = round(min(100.0, 100.0 * berraklik_ham * (0.25 + 0.75 * p.nazar_harfi_orani)), 2)

    # 2. İbadet Simyası Çarpanı (Mesnevî-i Nuriye — Niyetin iksiri):
    # Niyet + Harfî nazar birleşince sıradan âdetler (yeme, içme, bakma) üstel olarak ibadete inkılap eder.
    # f(niyet, harfi) = (10^(2 * niyet * harfi) - 1) / 99 * 100  -> [0, 100]
    sinerji = p.niyet_halisiyeti * p.nazar_harfi_orani
    ibadet_simyasi = round(((10.0 ** (2.0 * sinerji)) - 1.0) / 99.0 * 100.0, 2)

    # 3. İlişkisel Anlam Biti (RQM Karşılıklı Bilgi / Marifet Enformasyonu):
    # Tekil töz (mânâ-yı ismî) bilgisizliğe sürüklerken, harfî nisbet logaritmik-üstel bilgi açar.
    # I_rqm = -log2(1 - 0.999 * b) * (1 + 2 * iliskisel_bag)
    etkin_oran = min(0.999, p.nazar_harfi_orani * (0.5 + 0.5 * p.arayuz_farkindaligi))
    iliskisel_anlam_biti = round(-math.log2(1.0 - etkin_oran) * (0.5 + 1.5 * p.iliskisel_bag_derinligi), 2)

    # 4. Arayüz Yanılsaması (Hoffman ITP — Masaüstünü hakikat sanma hatası):
    # Mânâ-yı ismî arttıkça şehadet perdesi mutlak töz zannedilir.
    arayuz_yanilsamasi = round(
        100.0 * (1.0 - p.nazar_harfi_orani) * (0.6 + 0.4 * (1.0 - p.arayuz_farkindaligi)),
        2,
    )

    # 5. Hakikat Mertebesi ve Hüküm
    if epistemik_berraklik >= 85.0 and ibadet_simyasi >= 70.0:
        mertebe = "Mânâ-yı Harfî & Huzur-u Dâimî"
        hukum = (
            "Kâinat kitabının harfleri Sâni' hesabına okunuyor; niyet iksiriyle âdât ibadete "
            "dönüşmüş, şehadet arayüzünün arkasındaki Esmâ-i İlâhiye müşahede edilmiştir."
        )
    elif epistemik_berraklik >= 55.0:
        mertebe = "Tefekkür-ü İmânî & İlişkisel İdrak"
        hukum = (
            "Eşyadaki nisbet (RQM) ve ayinedarlık okunmaya başlanmıştır; niyet ve nazar "
            "derinleştikçe arayüz perdesi tamamen şeffaflaşacaktır."
        )
    elif epistemik_berraklik >= 25.0:
        mertebe = "Nötr Bilimsel / İki Arada Nazar"
        hukum = (
            "Kâinatın ilişkisel yasaları kısmen görülse de mânâ-yı ismî eğilimi tam kırılmamıştır; "
            "harfî nazar olmadan eşyanın hakiki gayesi kapalı kalır."
        )
    elif arayuz_yanilsamasi >= 75.0:
        mertebe = "Mânâ-yı İsmî & Arayüz Yanılsaması"
        hukum = (
            "Hoffman'ın masaüstü yanılsaması hakimdir: Şehadet perdesi mutlak hakikat sanılmakta, "
            "sebepler ve madde kendi hesabına (mânâ-yı ismî) değerlendirilerek anlam yitirilmektedir."
        )
    else:
        mertebe = "Gaflet ve Yüzeysel Algı"
        hukum = (
            "Niyet ve harfî nazar zayıftır; âdetler sıradan alışkanlıkta kalmakta, kâinatın "
            "mânâ derinliği perdelenmektedir."
        )

    return NazarCiktisi(
        epistemik_berraklik=epistemik_berraklik,
        ibadet_simyasi_carpani=ibadet_simyasi,
        iliskisel_anlam_biti=iliskisel_anlam_biti,
        arayuz_yanilsamasi=arayuz_yanilsamasi,
        hakikat_mertebesi=mertebe,
        hukum=hukum,
    )


def calistir_senaryo(ad: str) -> NazarCiktisi:
    """Ön tanımlı bir senaryoyu çalıştırır."""
    if ad not in SENARYOLAR:
        raise KeyError(f"Bilinmeyen senaryo: '{ad}'. Geçerliler: {list(SENARYOLAR.keys())}")
    return hesapla_nazar_durumu(SENARYOLAR[ad])


def tum_senaryolari_karsilastir() -> Dict[str, NazarCiktisi]:
    """Bütün ön tanımlı senaryoları hesaplar ve sözlük olarak döndürür."""
    return {ad: hesapla_nazar_durumu(p) for ad, p in SENARYOLAR.items()}


def tablo_yazdir(sonuclar: Dict[str, NazarCiktisi]) -> None:
    """Sonuçları düzenli bir terminal tablosu olarak yazdırır."""
    print("=" * 98)
    print("  👁️  MÂNÂ-YI HARFÎ, NİYET-NAZAR VE İLİŞKİSEL KUANTUM (RQM & ITP) KARŞILAŞTIRMASI")
    print("=" * 98)
    print(f"{'Senaryo':<32} | {'Berraklık':>9} | {'İbadet':>8} | {'RQM Bit':>8} | {'Yanılsama':>9} | {'Mertebe'}")
    print("-" * 98)
    for ad, c in sonuclar.items():
        print(
            f"{ad:<32} | {c.epistemik_berraklik:>8.1f}% | {c.ibadet_simyasi_carpani:>7.1f}x | "
            f"{c.iliskisel_anlam_biti:>8.2f} | {c.arayuz_yanilsamasi:>8.1f}% | {c.hakikat_mertebesi}"
        )
    print("=" * 98)


def csv_yaz(dosya_yolu: str) -> None:
    """Tüm senaryo sonuçlarını CSV dosyasına aktarır."""
    sonuclar = tum_senaryolari_karsilastir()
    with open(dosya_yolu, "w", newline="", encoding="utf-8") as f:
        yazici = csv.writer(f)
        yazici.writerow([
            "senaryo",
            "epistemik_berraklik",
            "ibadet_simyasi_carpani",
            "iliskisel_anlam_biti",
            "arayuz_yanilsamasi",
            "hakikat_mertebesi",
            "hukum",
        ])
        for ad, c in sonuclar.items():
            yazici.writerow([
                ad,
                c.epistemik_berraklik,
                c.ibadet_simyasi_carpani,
                c.iliskisel_anlam_biti,
                c.arayuz_yanilsamasi,
                c.hakikat_mertebesi,
                c.hukum,
            ])


def main(argv: Optional[list] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Mânâ-yı Harfî, Niyet-Nazar ve İlişkisel Kuantum (RQM / ITP) Simülasyonu"
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
        print(f"\n👁️  Senaryo: {args.senaryo}")
        print(f"  • Epistemik Berraklık   : %{c.epistemik_berraklik}")
        print(f"  • İbadet Simyası Çarpanı: {c.ibadet_simyasi_carpani}x")
        print(f"  • İlişkisel Anlam Biti  : {c.iliskisel_anlam_biti} bit")
        print(f"  • Arayüz Yanılsaması    : %{c.arayuz_yanilsamasi}")
        print(f"  • Hakikat Mertebesi     : {c.hakikat_mertebesi}")
        print(f"  • Hüküm                 : {c.hukum}\n")
        return 0

    tablo_yazdir(tum_senaryolari_karsilastir())
    return 0


if __name__ == "__main__":
    sys.exit(main())
