#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Haşir, Bahar İhyası ve Kozmik Bilgi Korunumu Modeli (10. Söz)
==============================================================

10. Söz (Haşir Risalesi) ve modern fizikteki Kuantum Bilgi Korunumu
(Unitarity / Hawking Bilgi Paradoksu) ilkelerinin analitik sentezi:

    "Bir taburu teşkil eden neferat, bir boru sesiyle nasıl kışlaya toplanırsa;
     kudret-i mutlaka dahi tek bir emirle dağılmış zerratı yeniden bir araya
     getirip cesetleri iade edecektir." (10. Söz)

    "Eğer haşrin gelmesi kaza ve kader-i İlâhî gibi muhakkak olmazsa;
     kâinatın bütün hakaiki, zîneti, intizamı, adaleti, merhameti zîr ü zeber olur."
     (10. Söz, On İkinci Hakikat)

Bu model şu 4 temel dinamiği simüle eder:
1. Enformasyonel Korunum (Levh-i Mahfuz / Unitarity): Zerreler dağılsa da ruh ve amel bilgisi kaybolmaz.
2. İbda (İlk Yaratılış) vs. İade (Haşir / Tekrar Toplama) Maliyet Oranı.
3. Bahar İhyası (Kışta dağılan 300.000+ türün baharda ihyası).
4. Haşirsiz vs. Haşirli Kâinatın Adalet, Hikmet ve Rahmet Tutarlılık İndisi.
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
class HasirParametreleri:
    """Haşir ve Kozmik Bilgi Korunumu Parametreleri."""
    ad: str = "bahar_ihyasi"
    ahiret_inanci: float = 1.0      # [0.0, 1.0]: 1 = Haşir var, 0 = Haşirsiz (Maddeci) faraziye
    bilgi_korunumu: float = 1.0     # [0.0, 1.0]: Levh-i Mahfuz / Unitarity derecesi
    kudret_emri_sur: float = 1.0    # [0.0, 1.0]: Tek bir emirle (Sur) iade gücü
    zulm_ve_mazlum_farki: float = 0.85 # [0.0, 1.0]: Dünyadaki adaletsizliklerin (zâlim/mazlum) yoğunluğu
    adim_sayisi: int = 40
    dt: float = 0.25

    def dogrula(self) -> None:
        for ad, deger in [
            ("ahiret_inanci", self.ahiret_inanci),
            ("bilgi_korunumu", self.bilgi_korunumu),
            ("kudret_emri_sur", self.kudret_emri_sur),
            ("zulm_ve_mazlum_farki", self.zulm_ve_mazlum_farki),
        ]:
            if not 0.0 <= deger <= 1.0:
                raise ValueError(f"{ad} [0.0, 1.0] aralığında olmalıdır.")
        if self.adim_sayisi <= 0:
            raise ValueError("adim_sayisi pozitif olmalıdır.")
        if self.dt <= 0:
            raise ValueError("dt pozitif olmalıdır.")


@dataclass
class HasirZamanAdimi:
    t: float
    zerre_dagilimi: float       # Ölüm/Kış ile maddi dağılma [0, 1]
    bilgi_butunlugu: float      # Korunan enformasyon / ruh [0, 1]
    adalet_indisi: float        # Kâinatın ahlakî/hukukî tutarlılığı [0, 1]
    hikmet_indisi: float        # Abesiyetten kurtuluş ve anlamlılık [0, 1]
    ihya_orani: float           # Bahar / Haşir diriliş yüzdesi [0, 1]


@dataclass
class HasirSimulasyonSonucu:
    parametreler: HasirParametreleri
    adimlar: List[HasirZamanAdimi] = field(default_factory=list)
    nihai_adalet: float = 0.0
    nihai_hikmet: float = 0.0
    nihai_ihya: float = 0.0
    iade_kolaylik_carpani: float = 1.0  # İbda'ya göre İade'nin kolaylığı
    netice_hukmu: str = ""
    felsefi_izah: str = ""


HASIR_SENARYOLARI: Dict[str, HasirParametreleri] = {
    "bahar_ihyasi": HasirParametreleri(
        ad="bahar_ihyasi",
        ahiret_inanci=1.0,
        bilgi_korunumu=1.0,
        kudret_emri_sur=1.0,
        zulm_ve_mazlum_farki=0.80,
    ),
    "hasir_i_ecsad": HasirParametreleri(
        ad="hasir_i_ecsad",
        ahiret_inanci=1.0,
        bilgi_korunumu=1.0,
        kudret_emri_sur=1.0,
        zulm_ve_mazlum_farki=0.95,
    ),
    "hasirsiz_faraziye": HasirParametreleri(
        ad="hasirsiz_faraziye",
        ahiret_inanci=0.0,         # Haşir yok farz edilirse
        bilgi_korunumu=0.0,         # Zerre ve ameller yokluğa gider
        kudret_emri_sur=0.0,
        zulm_ve_mazlum_farki=0.90,
    ),
    "suphe_ve_tereddut": HasirParametreleri(
        ad="suphe_ve_tereddut",
        ahiret_inanci=0.45,
        bilgi_korunumu=0.60,
        kudret_emri_sur=0.50,
        zulm_ve_mazlum_farki=0.85,
    ),
}


def hasir_simule_et(p: HasirParametreleri) -> HasirSimulasyonSonucu:
    """Haşir, Bahar İhyası ve Bilgi Korunumu dinamiklerini simüle eder."""
    p.dogrula()
    adimlar: List[HasirZamanAdimi] = []

    # Kış/Ölüm fazı (ilk yarı) -> Bahar/Haşir fazı (ikinci yarı)
    yari = p.adim_sayisi // 2

    for i in range(p.adim_sayisi):
        t = i * p.dt
        if i < yari:
            # Ölüm / Kış / Dağılma süreci
            ilerleme = (i + 1) / max(1, yari)
            zerre_dagilim = ilerleme
            # Bilgi korunumu varsa (Levh-i Mahfuz), madde dağılsa da bilgi sıfırlanmaz
            bilgi = 1.0 - (1.0 - p.bilgi_korunumu) * ilerleme
            ihya = 0.0
        else:
            # Sur / Bahar / İade süreci
            ilerleme = (i - yari + 1) / max(1, p.adim_sayisi - yari)
            if p.ahiret_inanci > 0.1:
                ihya = min(1.0, p.ahiret_inanci * p.kudret_emri_sur * (1.0 - math.exp(-4.0 * ilerleme)))
                zerre_dagilim = max(0.0, 1.0 - ihya)
                bilgi = p.bilgi_korunumu
            else:
                ihya = 0.0
                zerre_dagilim = 1.0
                bilgi = 0.0

        # Adalet İndisi:
        # Dünyada zâlim izzetle, mazlum zilletle giderken; ahiret yoksa adalet sıfırlanır (Zulme döner)
        if i < yari:
            adalet = 1.0 - p.zulm_ve_mazlum_farki * 0.6
        else:
            adalet = (1.0 - p.zulm_ve_mazlum_farki) + p.zulm_ve_mazlum_farki * ihya

        # Hikmet İndisi:
        # Abesiyetten kurtuluş: Ebedî bir meydan olmazsa bütün sanat israf olur
        hikmet = 0.3 * bilgi + 0.7 * (ihya if i >= yari else p.ahiret_inanci)

        adimlar.append(HasirZamanAdimi(
            t=t,
            zerre_dagilimi=zerre_dagilim,
            bilgi_butunlugu=bilgi,
            adalet_indisi=max(0.0, min(1.0, adalet)),
            hikmet_indisi=max(0.0, min(1.0, hikmet)),
            ihya_orani=ihya,
        ))

    son = adimlar[-1]
    # İbda'ya (yoktan yaratmaya) kıyasla İade (yeniden toplama) kolaylık çarpanı
    kolaylik = 100.0 * p.kudret_emri_sur * p.bilgi_korunumu + 1.0

    if son.ihya_orani >= 0.85 and son.adalet_indisi >= 0.85:
        hukum = "Dâr-ı Bekā ve Adalet-i Mahza"
        izah = (
            "Zerreler dağılsa da bilgi (Levh-i Mahfuz ve ruh) bütünüyle korunmuştur. "
            "Tek bir 'Kün / Sur' emriyle tabur kışlasına toplanır gibi bütün mevcudat "
            "ihya edilmiş; adalet, hikmet ve merhamet kemale ermiştir."
        )
    elif p.ahiret_inanci < 0.2:
        hukum = "Abesiyet ve Zulüm Çıkmazı (Muammâ-yı Lâyünhall)"
        izah = (
            "Haşir ve âhiret yok farz edildiğinde zâlim cezasız, mazlum hakkını almadan "
            "gitmiş; bütün kâinat sarayı ve sanatları mânâsız bir israfa dönüşmüştür."
        )
    else:
        hukum = "Tereddüt ve Eksik Huzur"
        izah = "Ebediyet ufku tam yakalanamadığı için adalet ve hikmet dengesi kemale erememiştir."

    return HasirSimulasyonSonucu(
        parametreler=p,
        adimlar=adimlar,
        nihai_adalet=son.adalet_indisi,
        nihai_hikmet=son.hikmet_indisi,
        nihai_ihya=son.ihya_orani,
        iade_kolaylik_carpani=kolaylik,
        netice_hukmu=hukum,
        felsefi_izah=izah,
    )


def hasir_csv_yaz(dosya_yolu: str, sonuc: HasirSimulasyonSonucu) -> None:
    with open(dosya_yolu, mode="w", newline="", encoding="utf-8") as f:
        yazici = csv.writer(f)
        yazici.writerow(["t", "zerre_dagilimi", "bilgi_butunlugu", "adalet", "hikmet", "ihya_orani"])
        for a in sonuc.adimlar:
            yazici.writerow([
                f"{a.t:.2f}",
                f"{a.zerre_dagilimi:.4f}",
                f"{a.bilgi_butunlugu:.4f}",
                f"{a.adalet_indisi:.4f}",
                f"{a.hikmet_indisi:.4f}",
                f"{a.ihya_orani:.4f}",
            ])


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Haşir, Bahar İhyası ve Kozmik Bilgi Korunumu Modeli (10. Söz)"
    )
    parser.add_argument(
        "--senaryo",
        choices=list(HASIR_SENARYOLARI.keys()),
        default="hasir_i_ecsad",
        help="Çalıştırılacak senaryo",
    )
    parser.add_argument(
        "--karsilastir",
        action="store_true",
        help="Tüm senaryoları tablo olarak yazdır",
    )
    parser.add_argument("--csv", type=str, default=None, help="CSV çıktı yolu")

    args = parser.parse_args(argv)

    if args.karsilastir:
        print(f"{'Senaryo':<22} {'İhya':>8} {'Adalet':>8} {'Hikmet':>8} {'Kolaylık':>10}  {'Netice'}")
        print("-" * 86)
        for ad, p_sen in HASIR_SENARYOLARI.items():
            r = hasir_simule_et(p_sen)
            print(
                f"{ad:<22} {r.nihai_ihya:>8.3f} {r.nihai_adalet:>8.3f} {r.nihai_hikmet:>8.3f} "
                f"{r.iade_kolaylik_carpani:>9.1f}x  {r.netice_hukmu}"
            )
        return 0

    p = HASIR_SENARYOLARI[args.senaryo]
    r = hasir_simule_et(p)

    print("=" * 80)
    print("⏳ HAŞİR, BAHAR İHYASI VE BİLGİ KORUNUMU RAPORU (10. SÖZ)")
    print(f"Senaryo: {p.ad} | Ahiret İnancı: %{p.ahiret_inanci*100:.0f} | Bilgi Korunumu: %{p.bilgi_korunumu*100:.0f}")
    print("=" * 80)
    print(f"Nihai İhya (Diriliş) Oranı : %{r.nihai_ihya*100:.1f}")
    print(f"Kâinat Adalet İndisi       : {r.nihai_adalet:.3f} / 1.000")
    print(f"Hikmet ve Anlam İndisi     : {r.nihai_hikmet:.3f} / 1.000")
    print(f"İade / İbda Kolaylık Oranı : {r.iade_kolaylik_carpani:.1f}x")
    print(f"Netice Hükmü               : {r.netice_hukmu}")
    print("-" * 80)
    print(f"💡 İZAH: {r.felsefi_izah}")
    print("=" * 80)

    if args.csv:
        hasir_csv_yaz(args.csv, r)
    return 0


if __name__ == "__main__":
    sys.exit(main())
