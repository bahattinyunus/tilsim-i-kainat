#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kader, İrade ve Levh-i Mahfuz Karar Matrisi Modeli
==================================================

26. Söz'ün (Kader Risalesi), Nisa Sûresi 79. Âyetin ve
modern enformasyon/karar teorisinin analitik sentezi:

    "Kader ve cüz'-i ihtiyarî, İslâmiyetin ve imanın nihayet hududunu gösteren,
     hâlî ve vicdanî bir imanın mütemmimâtındandır...
     Nihayette teklif ve mes'uliyetten kurtulmamak için önüne cüz'-i ihtiyarî çıkıyor;
     ona 'Mes'ulsün ve mükellefsin' der.
     Sonra ondan sudûr eden kemâlât ve hasenat ile fahreylememek ve gurura düşmemek
     için kader karşısına çıkıyor; der: 'Fahr etme, haddini bil; yapan sen değilsin.'"
     (26. Söz)

    "مَاۤ اَصَابَكَ مِنْ حَسَنَةٍ فَمِنَ اللّٰهِ وَمَاۤ اَصَابَكَ مِنْ سَيِّئَةٍ فَمِنْ نَفْسِكَ"
    (Sana isabet eden her iyilik Allah'tandır; sana isabet eden her kötülük ise nefsindendir.)
    (Nisa Sûresi, 79)

Bu simülasyon şu 4 temel hakikati modeller:
1. İrade (Kesb / Cüz-i Meyil): Enerjisi sıfıra yakın (1-bitlik) tercih anahtarı.
2. Kudret Halkı: Tercih edilen kanaldan sonsuz Kudret'in fiili yaratması (Hâlık-ı Külli Şey).
3. Ezelî İlim ve Levh-i Mahfuz vs. Levh-i Mahv ve İspat (Dua ve Sadaka ile kaza tebdili).
4. İki Tehlikeli Uçurum (Kibir ve Yeis) karşısında Hakikat Terazisi (İstikamet İndisi).
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional

try:  # pragma: no cover
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:  # pragma: no cover
    pass


@dataclass
class KaderParametreleri:
    """Kader ve İrade Karar Matrisi Parametreleri."""
    ad: str = "istikamet_ehli"
    irade_meyli: float = 0.8         # [-1.0, 1.0]: -1 = mutlak şer/tahrip, +1 = mutlak hayır
    kesb_gayreti: float = 0.85       # [0.0, 1.0]: İnsanın meyil yönündeki cehd ve emeği
    hasenat_kadere_isnad: float = 0.95 # [0.0, 1.0]: İyilikleri Allah'ın lütfu bilme (1.0 = tam şükür)
    seyyiat_nefse_isnad: float = 0.95  # [0.0, 1.0]: Hataları nefsinden bilme (1.0 = tam istiğfar)
    dua_iltica: float = 0.80         # [0.0, 1.0]: Dua ve yalvarış derecesi
    sadaka_ve_ihsan: float = 0.70    # [0.0, 1.0]: Sadaka ve hayır derecesi (Kader-i muallak kalkanı)
    adimi_sayisi: int = 50           # Simülasyon zaman adımı
    dt: float = 0.1                  # Zaman adımı büyüklüğü

    def dogrula(self) -> None:
        if not -1.0 <= self.irade_meyli <= 1.0:
            raise ValueError("irade_meyli [-1.0, 1.0] aralığında olmalıdır.")
        for ad, deger in [
            ("kesb_gayreti", self.kesb_gayreti),
            ("hasenat_kadere_isnad", self.hasenat_kadere_isnad),
            ("seyyiat_nefse_isnad", self.seyyiat_nefse_isnad),
            ("dua_iltica", self.dua_iltica),
            ("sadaka_ve_ihsan", self.sadaka_ve_ihsan),
        ]:
            if not 0.0 <= deger <= 1.0:
                raise ValueError(f"{ad} [0.0, 1.0] aralığında olmalıdır.")
        if self.adimi_sayisi <= 0:
            raise ValueError("adimi_sayisi pozitif olmalıdır.")
        if self.dt <= 0:
            raise ValueError("dt pozitif olmalıdır.")


@dataclass
class KaderZamanAdimi:
    """Tek bir zaman dilimindeki tecelli ve karar durumu."""
    t: float
    hasenat_birikimi: float
    seyyiat_birikimi: float
    kibir_potansiyeli: float      # Ene'nin iyilikleri sahiplenme sapması
    yeis_potansiyeli: float       # Ene'nin seyyiatı kadere atıp ümitsizliğe düşme sapması
    istikamet_indisi: float       # [0.0, 1.0]: Ruhsal denge ve fıtrî mükemmeliyet
    muallak_kaza_tebdili: float   # Dua ve sadaka ile defedilen menfi kaza katsayısı
    kudret_tecelli_kuvveti: float # Kesb vesilesiyle yaratılan ilâhî fiil enerjisi


@dataclass
class KaderSimulasyonSonucu:
    """Simülasyonun küllî analitik neticesi."""
    parametreler: KaderParametreleri
    adimlar: List[KaderZamanAdimi] = field(default_factory=list)
    nihai_istikamet: float = 0.0
    nihai_kibir: float = 0.0
    nihai_yeis: float = 0.0
    toplam_hasenat: float = 0.0
    toplam_seyyiat: float = 0.0
    muallak_kaza_def_orani: float = 0.0
    kudret_verimi: float = 0.0
    ruhi_makam: str = "Bilinmiyor"
    felsefi_hukum: str = ""


# Hazır Senaryolar Kütüphanesi
KADER_SENARYOLARI: Dict[str, KaderParametreleri] = {
    "istikamet_ehli": KaderParametreleri(
        ad="istikamet_ehli",
        irade_meyli=0.85,
        kesb_gayreti=0.80,
        hasenat_kadere_isnad=0.98,  # İyiliği Allah'tan bilir (Şükür)
        seyyiat_nefse_isnad=0.95,   # Kusuru nefsinden bilir (Tevbe)
        dua_iltica=0.85,
        sadaka_ve_ihsan=0.75,
    ),
    "firavun_kibri": KaderParametreleri(
        ad="firavun_kibri",
        irade_meyli=0.40,
        kesb_gayreti=0.70,
        hasenat_kadere_isnad=0.05,  # "Ben kazandım, benim deham" (Karun/Firavun meşrebi)
        seyyiat_nefse_isnad=0.50,
        dua_iltica=0.02,
        sadaka_ve_ihsan=0.05,
    ),
    "cebriye_yeisi": KaderParametreleri(
        ad="cebriye_yeisi",
        irade_meyli=-0.20,
        kesb_gayreti=0.15,
        hasenat_kadere_isnad=0.60,
        seyyiat_nefse_isnad=0.05,   # "Kaderim böyleymiş, ne yapayım?" (Mesuliyetten kaçış)
        dua_iltica=0.10,
        sadaka_ve_ihsan=0.10,
    ),
    "dua_ile_kaza_tehiri": KaderParametreleri(
        ad="dua_ile_kaza_tehiri",
        irade_meyli=0.65,
        kesb_gayreti=0.60,
        hasenat_kadere_isnad=0.90,
        seyyiat_nefse_isnad=0.85,
        dua_iltica=0.95,            # Yüksek iltica (Şartlı kazayı ref' eden dua)
        sadaka_ve_ihsan=0.90,       # Belaları defeden azami sadaka
    ),
    "materyalist_determinizm": KaderParametreleri(
        ad="materyalist_determinizm",
        irade_meyli=0.10,
        kesb_gayreti=0.50,
        hasenat_kadere_isnad=0.00,  # Kaderi inkar, tesadüfe veya tabiata isnad
        seyyiat_nefse_isnad=0.10,   # Biyolojik determinizm mazereti
        dua_iltica=0.00,
        sadaka_ve_ihsan=0.00,
    ),
}


def kader_simule_et(parametreler: KaderParametreleri) -> KaderSimulasyonSonucu:
    """
    Kader, İrade ve Levh-i Mahfuz Karar Matrisi simülasyonunu icra eder.
    """
    parametreler.dogrula()

    adimlar: List[KaderZamanAdimi] = []
    hasenat = 0.0
    seyyiat = 0.0

    # Levh-i Mahv ve İspat'ta dua ve sadakanın kaza-i muallakı def etme kalkanı:
    # Hadis-i Şerif: "Kaza-i muallakı yalnız dua tebdil eder; sadaka belayı def eder."
    kalkan_gucu = 0.6 * parametreler.dua_iltica + 0.4 * parametreler.sadaka_ve_ihsan

    # Cüz-i İrade: Enerjisi sıfıra yakın yönlendirici anahtar
    # Kudret: Meyil yönünde sonsuz kudretin tecelli etmesi
    meyil = parametreler.irade_meyli
    cehd = parametreler.kesb_gayreti

    for i in range(parametreler.adimi_sayisi):
        t = i * parametreler.dt

        # Vücudî / Hayır üretimi: Meyil pozitifse ve cehd varsa Kudret hayrı halk eder.
        # İyilik vücudîdir; fail-i hakiki Allah'tır.
        if meyil > 0:
            anlik_hayir = meyil * cehd * (1.0 + 0.2 * math.sin(t)) * parametreler.dt
            hasenat += anlik_hayir
        else:
            anlik_hayir = 0.0

        # Ademi / Şer üretimi: Meyil negatifse (veya tembellik/terk varsa),
        # tahrip kolay olduğundan az meyil çok tahribat yapar.
        if meyil < 0:
            anlik_ser = abs(meyil) * 1.5 * (1.0 - kalkan_gucu * 0.7) * parametreler.dt
            seyyiat += anlik_ser
        else:
            # İhmal kaynaklı küçük seyyiatlar
            anlik_ser = (1.0 - cehd) * 0.1 * (1.0 - kalkan_gucu * 0.5) * parametreler.dt
            seyyiat += anlik_ser

        # Kibir Potansiyeli: Hasenatı Allah'a değil kendine verme hastalığı (1 - hasenat_kadere_isnad)
        kibir = (1.0 - parametreler.hasenat_kadere_isnad) * (hasenat / (hasenat + 1.0))

        # Yeis Potansiyeli: Seyyiatı nefsine almayıp kadere iftira ederek mesuliyetten kaçma
        yeis = (1.0 - parametreler.seyyiat_nefse_isnad) * (seyyiat / (seyyiat + 1.0))

        # İstikamet İndisi:
        # İdeal Mü'min = (Hasenatı Kadere Verir) * (Seyyiatı Nefse Verir)
        # Kibir ve Yeis uçurumlarından uzaklık
        istikamet = max(
            0.0,
            1.0 - 0.5 * kibir - 0.5 * yeis - 0.2 * abs(kibir - yeis)
        )
        if parametreler.hasenat_kadere_isnad > 0.8 and parametreler.seyyiat_nefse_isnad > 0.8:
            istikamet = min(1.0, istikamet + 0.1)

        # Kudret Tecelli Kuvveti: Cüz-i irade düğmesine basıldığında kudretin yarattığı tecelli
        kudret_enerjisi = (abs(meyil) * cehd + 0.01) * 1000.0  # 1 bitlik tercih -> 1000 birim kudret akışı

        adimlar.append(KaderZamanAdimi(
            t=t,
            hasenat_birikimi=hasenat,
            seyyiat_birikimi=seyyiat,
            kibir_potansiyeli=min(1.0, kibir),
            yeis_potansiyeli=min(1.0, yeis),
            istikamet_indisi=max(0.0, min(1.0, istikamet)),
            muallak_kaza_tebdili=min(1.0, kalkan_gucu),
            kudret_tecelli_kuvveti=kudret_enerjisi,
        ))

    son_adim = adimlar[-1]
    nihai_ist = son_adim.istikamet_indisi
    nihai_kib = son_adim.kibir_potansiyeli
    nihai_yei = son_adim.yeis_potansiyeli

    # Manevi ve Felsefi Makam Tayini
    if nihai_ist >= 0.85:
        ruhi_makam = "İstikamet & Rıza (26. Söz Mizânı)"
        hukum = (
            "Ene hakiki haddini bilmiştir: Hasenatı Kadere verip şükreder, "
            "seyyiatı nefsine alıp istiğfar eder. Ne kibir uçurumuna düşer ne yeise kapılır."
        )
    elif nihai_kib > 0.40 and nihai_kib > nihai_yei:
        ruhi_makam = "Kibir ve Gurur Uçurumu (Firavuniyet/Karuniyet)"
        hukum = (
            "Ene muvaffakiyetleri kendi dehasına mal ederek firavunlaşmıştır. "
            "Kader kalkanını unuttuğu için gurur ve şirk tehlikesine yuvarlanmıştır."
        )
    elif nihai_yei > 0.40:
        ruhi_makam = "Mesuliyetsizlik ve Yeis Uçurumu (Cebriye Sapkınlığı)"
        hukum = (
            "Ene günah ve tembelliğini 'kaderim böyleymiş' diyerek kadere yüklemiştir. "
            "Cüz-i ihtiyariyi inkar edip mesuliyetten kaçtığı için yeise ve atalete mahkumdur."
        )
    else:
        ruhi_makam = "Tereddüt ve Zaaf Dairesi"
        hukum = "Kader ve irade dengesi tam kurulamamış; nefis daima iki uçurum arasında çalkalanmaktadır."

    return KaderSimulasyonSonucu(
        parametreler=parametreler,
        adimlar=adimlar,
        nihai_istikamet=nihai_ist,
        nihai_kibir=nihai_kib,
        nihai_yeis=nihai_yei,
        toplam_hasenat=hasenat,
        toplam_seyyiat=seyyiat,
        muallak_kaza_def_orani=kalkan_gucu,
        kudret_verimi=son_adim.kudret_tecelli_kuvveti,
        ruhi_makam=ruhi_makam,
        felsefi_hukum=hukum,
    )


def kader_csv_yaz(dosya_yolu: str, sonuc: KaderSimulasyonSonucu) -> None:
    """Simülasyon adımlarını CSV dosyasına kaydeder."""
    with open(dosya_yolu, mode="w", newline="", encoding="utf-8") as f:
        yazici = csv.writer(f)
        yazici.writerow([
            "zaman_sn",
            "hasenat",
            "seyyiat",
            "kibir",
            "yeis",
            "istikamet",
            "muallak_def",
            "kudret_enerjisi"
        ])
        for adim in sonuc.adimlar:
            yazici.writerow([
                f"{adim.t:.2f}",
                f"{adim.hasenat_birikimi:.4f}",
                f"{adim.seyyiat_birikimi:.4f}",
                f"{adim.kibir_potansiyeli:.4f}",
                f"{adim.yeis_potansiyeli:.4f}",
                f"{adim.istikamet_indisi:.4f}",
                f"{adim.muallak_kaza_tebdili:.4f}",
                f"{adim.kudret_tecelli_kuvveti:.2f}",
            ])


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Kader, İrade ve Levh-i Mahfuz Karar Matrisi Modeli (26. Söz)"
    )
    parser.add_argument(
        "--senaryo",
        choices=list(KADER_SENARYOLARI.keys()),
        default="istikamet_ehli",
        help="Çalıştırılacak hazır senaryo (varsayılan: istikamet_ehli)",
    )
    parser.add_argument(
        "--karsilastir",
        action="store_true",
        help="Tüm hazır senaryoları karşılaştırmalı tablo olarak yazdırır",
    )
    parser.add_argument(
        "--meyil",
        type=float,
        default=None,
        help="İrade meyli [-1.0, 1.0]",
    )
    parser.add_argument(
        "--hasenat-kader",
        type=float,
        default=None,
        help="Hasenatı kadere isnad oranı [0.0, 1.0]",
    )
    parser.add_argument(
        "--seyyiat-nefis",
        type=float,
        default=None,
        help="Seyyiatı nefse isnad oranı [0.0, 1.0]",
    )
    parser.add_argument(
        "--dua",
        type=float,
        default=None,
        help="Dua ve iltica derecesi [0.0, 1.0]",
    )
    parser.add_argument(
        "--sadaka",
        type=float,
        default=None,
        help="Sadaka derecesi [0.0, 1.0]",
    )
    parser.add_argument(
        "--csv",
        type=str,
        default=None,
        help="Çıktıyı yazmak için CSV dosyası",
    )

    args = parser.parse_args(argv)

    if args.karsilastir:
        print(f"{'Senaryo':<25} {'İstikamet':>10} {'Kibir':>8} {'Yeis':>8} {'Hasenat':>9} {'Seyyiat':>9}  {'Makam'}")
        print("-" * 88)
        for ad, p_senaryo in KADER_SENARYOLARI.items():
            r = kader_simule_et(p_senaryo)
            print(
                f"{ad:<25} {r.nihai_istikamet:>10.3f} {r.nihai_kibir:>8.3f} {r.nihai_yeis:>8.3f} "
                f"{r.toplam_hasenat:>9.2f} {r.toplam_seyyiat:>9.2f}  {r.ruhi_makam}"
            )
        return 0

    p = KADER_SENARYOLARI[args.senaryo]

    # Kullanıcı parametre geçişleri
    if args.meyil is not None:
        p.irade_meyli = args.meyil
    if args.hasenat_kader is not None:
        p.hasenat_kadere_isnad = args.hasenat_kader
    if args.seyyiat_nefis is not None:
        p.seyyiat_nefse_isnad = args.seyyiat_nefis
    if args.dua is not None:
        p.dua_iltica = args.dua
    if args.sadaka is not None:
        p.sadaka_ve_ihsan = args.sadaka

    sonuc = kader_simule_et(p)

    print("=" * 80)
    print("⚖️  KADER, İRADE VE LEVH-İ MAHFUZ KARAR MATRİSİ ANALİTİK RAPORU")
    print(f"Senaryo: {p.ad} | Cüz-i Meyil: {p.irade_meyli:+.2f} | Cehd: {p.kesb_gayreti:.2f}")
    print(f"Hasenat->Kader: %{p.hasenat_kadere_isnad*100:.1f} | Seyyiat->Nefis: %{p.seyyiat_nefse_isnad*100:.1f}")
    print(f"Dua İltica: %{p.dua_iltica*100:.1f} | Sadaka İhsan: %{p.sadaka_ve_ihsan*100:.1f}")
    print("=" * 80)
    print(f"Nihai İstikamet İndisi : {sonuc.nihai_istikamet:.3f} / 1.000")
    print(f"Kibir Potansiyeli      : {sonuc.nihai_kibir:.3f} (Uçurum 1: Firavuniyet)")
    print(f"Yeis Potansiyeli       : {sonuc.nihai_yeis:.3f} (Uçurum 2: Cebriyecilik)")
    print(f"Hasenat / Seyyiat      : {sonuc.toplam_hasenat:.2f} / {sonuc.toplam_seyyiat:.2f}")
    print(f"Muallak Kaza Kalkanı   : %{sonuc.muallak_kaza_def_orani * 100:.1f} (Dua & Sadaka)")
    print(f"Kudret Tecelli Enerjisi: {sonuc.kudret_verimi:.1f} J/Birim (1-bitlik tercih neticesi)")
    print(f"Makam ve Mertebe       : {sonuc.ruhi_makam}")
    print("-" * 80)
    print(f"💡 HÜKÜM: {sonuc.felsefi_hukum}")
    print("=" * 80)

    if args.csv:
        kader_csv_yaz(args.csv, sonuc)
        print(f"Sonuçlar CSV dosyasına kaydedildi: {args.csv}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
