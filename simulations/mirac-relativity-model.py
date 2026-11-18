"""
🌌 TILSIM-I KÂİNAT: MİRAC, GÖRELİLİK VE TAYY-I ZAMAN MODELİ (31. SÖZ)
=====================================================================
Kaynak Eser:
  - 31. Söz (Mirac Risalesi)
    "Tılsım-ı kâinatın ve muammâ-yı hilkatin keşşafı ve fatihi olan
     zât-ı Ahmediye Aleyhissalâtü Vesselâmın mi'racı..."
  - 24. Mektup (Birinci Kısım - Zamanın İzafiyeti ve Ân-ı Dâim)
  - 20. Söz (İkinci Makam - Tayy-ı Zaman & Tayy-ı Mekân)

Modern Fizik & Kozmoloji Paralelleri:
  - Albert Einstein: Özel Görelilik (Special Relativity, 1905)
    Lorentz Faktörü: γ = 1 / √(1 - v²/c²)
    Öz-Zaman (Proper Time): Δτ = Δt / γ  (v → c iken Δτ → 0)
  - Fotonun Referans Çerçevesi: Işık hızında giden foton için zaman durur;
    bütün evrenin geçmişi ve geleceği tek bir "an"da yaşanır.
  - Higgs Mekanizması & Nuraniyet: Kütle (m₀), parçacıkların Higgs alanıyla
    sürtünmesidir. Cisim nuraniyet ve letâfet kesbettikçe Higgs direnci
    sıfırlanır (m_eff → 0); böylece maddî beden ezilmeden ve ivme hissetmeden
    ışık hızının ötesine ve zamanın dışına (Ân-ı Dâim) intikal eder.

Temel Teorem (31. Söz, Birinci Esas):
  "Bir zât bir dakikada yüz bin senelik mesafeyi kat'edebilir...
   Zaman bir şerit gibi cereyan ediyor; o şeridin sür'ati muhtelif mahlukata
   göre değişir. Nur ve ruh sür'atinde olan seyyahlar için zaman dürülür."
"""

from dataclasses import dataclass
import math
from typing import Dict, List, Optional


@dataclass
class MiracParametreleri:
    """Mirac ve izafiyet simülasyonu girdi parametreleri."""
    hiz_orani_beta: float    # Hızın ışık hızına oranı v/c [0.0 - 0.999999999999]
    letafet_derecesi: float  # Maddî bedenin nuraniyet ve letafet seviyesi [0.0 - 1.0]
    seyir_mertebesi: int     # 1: Arz-Kamer, 2: Samanyolu, 3: Sidretü'l-Münteha, 4: Kab-ı Kavseyn
    dunya_suresi_saniye: float  # Dünya gözlemcisine göre geçen süre (sn) (örn. 5.0 sn)


@dataclass
class MiracCiktisi:
    """Mirac ve görelilik analitik çıktıları."""
    lorentz_gama: float           # Rölativistik Lorentz faktörü γ
    yolcu_oz_zaman_saniye: float  # Seyyahın hissettiği öz-zaman Δτ (sn)
    etkin_kutle_orani: float      # Nuraniyetle hafifleyen efektif kütle (m_eff / m0)
    hissedilen_g_kuvveti: float   # Letafet sayesinde sıfırlanan ivme direnci (G)
    tilsim_fethi_skoru: float     # Kâinat tılsımının ve esmâsının keşif oranı [0 - 100]
    ontolojik_mertebe: str        # Seyir menzili
    hukum: str                    # Fiziksel ve kelâmî netice


SENARYOLAR: Dict[str, MiracParametreleri] = {
    "mirac_i_ahmedi": MiracParametreleri(
        hiz_orani_beta=0.999999999999,
        letafet_derecesi=1.0,
        seyir_mertebesi=4,       # Kab-ı Kavseyn / İmkân-Vücub Berzahı
        dunya_suresi_saniye=5.0  # Yatağı soğumadan, su dökülmeden (Tarfetü'l-ayn)
    ),
    "ruhani_seyr_evliya": MiracParametreleri(
        hiz_orani_beta=0.9999,
        letafet_derecesi=0.90,
        seyir_mertebesi=2,       # Âlem-i Misal ve Melekût
        dunya_suresi_saniye=60.0
    ),
    "foton_referans_cercevesi": MiracParametreleri(
        hiz_orani_beta=0.999999999,
        letafet_derecesi=0.0,    # Saf elektromanyetik enerji, maddî beden yok
        seyir_mertebesi=3,       # Kozmik uzay-zaman sınırı
        dunya_suresi_saniye=3600.0
    ),
    "klasik_roket_astronot": MiracParametreleri(
        hiz_orani_beta=0.00004,  # ~11.2 km/sn (Kurtulma hızı)
        letafet_derecesi=0.0,    # Ağır kesif madde
        seyir_mertebesi=1,       # Arz-Ay civarı
        dunya_suresi_saniye=259200.0  # 3 gün
    ),
    "kara_delik_olay_ufku": MiracParametreleri(
        hiz_orani_beta=0.995,
        letafet_derecesi=0.0,    # Kesif kütle çekimsel tekillik
        seyir_mertebesi=3,
        dunya_suresi_saniye=86400.0
    )
}


def dogrula_mirac_parametreleri(p: MiracParametreleri) -> None:
    """Girdi değerlerinin rölativistik sınırlarını denetler."""
    if not (0.0 <= p.hiz_orani_beta < 1.0):
        raise ValueError("v/c hız oranı [0.0, 1.0) aralığında olmalıdır.")
    if not (0.0 <= p.letafet_derecesi <= 1.0):
        raise ValueError("Letafet derecesi [0.0, 1.0] aralığında olmalıdır.")
    if p.seyir_mertebesi not in (1, 2, 3, 4):
        raise ValueError("Seyir mertebesi 1, 2, 3 veya 4 olmalıdır.")
    if p.dunya_suresi_saniye <= 0.0:
        raise ValueError("Dünya süresi pozitif olmalıdır.")


def hesapla_mirac_durumu(p: MiracParametreleri) -> MiracCiktisi:
    """
    Özel görelilik ve 31. Söz nuraniyet ilkeleriyle seyrin fiziğini hesaplar.
    """
    dogrula_mirac_parametreleri(p)

    beta = p.hiz_orani_beta
    # Lorentz faktörü: 1 / sqrt(1 - beta^2)
    bir_eksi_beta_kare = max(1e-15, 1.0 - beta * beta)
    gama = 1.0 / math.sqrt(bir_eksi_beta_kare)

    # 1. Öz-Zaman (Proper Time Δτ):
    # Klasik fizikte Δτ = Δt / γ.
    # Letafet = 1.0 olduğunda maddî zaman tamamen dürülür (Ân-ı Dâim / Tarfetü'l-ayn)
    # Δτ = (Δt / γ) * (1 - letafet * 0.999999)
    letafet_carpanı = max(1e-9, 1.0 - p.letafet_derecesi * 0.999999999)
    oz_zaman = (p.dunya_suresi_saniye / gama) * letafet_carpanı

    # 2. Etkin Kütle ve Higgs Direnci (m_eff / m0):
    # Madde nura ve ruha yaklaştıkça Higgs ile olan sürtünmesi sıfırlanır
    etkin_kutle = max(0.0, 1.0 - p.letafet_derecesi)

    # 3. Hissedilen G-Kuvveti (Eylemsizlik):
    # Letafet tam ise (Mirac-ı Nebevî), ivme ne kadar devasa olursa olsun
    # cismin her hücresi nuranîleştiğinden iç direnç hissetmez (0.0 G).
    if p.letafet_derecesi >= 0.99:
        hissedilen_g = 0.0
    else:
        # Klasik maddede yüksek hızlanma ölümcül G kuvveti üretir
        hissedilen_g = round((gama - 1.0) * (1.0 - p.letafet_derecesi) * 9.81, 2)

    # 4. Tılsım Fethi Skoru:
    # 31. Söz'de Mirac, kâinatın 70 bin perdesini ve bütün esmâyı teftiş edip
    # Sultan-ı Ezelî'nin huzuruna çıkmaktır.
    mertebe_carpani = {1: 25.0, 2: 55.0, 3: 85.0, 4: 100.0}[p.seyir_mertebesi]
    tilsim_skoru = mertebe_carpani * (0.5 * (beta ** 0.5) + 0.5 * p.letafet_derecesi)
    tilsim_skoru = round(min(100.0, max(0.0, tilsim_skoru)), 1)

    # 5. Mertebe Tasnifi ve Hüküm
    if p.seyir_mertebesi == 4 and p.letafet_derecesi >= 0.95:
        mertebe = "Kab-ı Kavseyn & Rü'yet-i Cemâlullah (Ân-ı Dâim)"
        hukum = "Kâinat tılsımı tamamen fethedildi; zaman dürülmüş, cisim letafetle nura inkılap ederek ezel-ebed berzahına vasıl olmuştur."
    elif p.seyir_mertebesi == 3:
        mertebe = "Sidretü'l-Münteha (Kozmik Yaratılışın Sınırı)"
        hukum = "Maddî uzay-zamanın nihayeti; esbap perdeleri geride kalmış, melekût nizamı müşahede edilmiştir."
    elif p.letafet_derecesi >= 0.80:
        mertebe = "Tabakat-ı Melekût (Ruhanî Seyr-i Sülûk)"
        hukum = "Ruhun cesede galip gelmesiyle tayy-ı zaman ve mekân tecellisi; kesafet perdesi incelmiştir."
    elif p.letafet_derecesi == 0.0 and beta >= 0.90:
        mertebe = "Fiziksel Foton & Rölativistik Limit"
        hukum = "Kütlesiz ışık fotonu için zaman akmaz; fakat şuur ve irade taşımayan kör fiziksel kanundur."
    else:
        mertebe = "Maddî Kesafet & Eylemsizlik Hapsi"
        hukum = "Higgs direnci ve sürtünme hakimdir; zamanın akışına mahkûmdur, kâinat tılsımını seyredemez."

    return MiracCiktisi(
        lorentz_gama=round(gama, 3),
        yolcu_oz_zaman_saniye=oz_zaman,
        etkin_kutle_orani=round(etkin_kutle, 4),
        hissedilen_g_kuvveti=hissedilen_g,
        tilsim_fethi_skoru=tilsim_skoru,
        ontolojik_mertebe=mertebe,
        hukum=hukum
    )


def calistir_senaryo(senaryo_adi: str) -> MiracCiktisi:
    """Belirtilen senaryoyu koşturur."""
    if senaryo_adi not in SENARYOLAR:
        raise KeyError(f"Bilinmeyen senaryo: '{senaryo_adi}'. Geçerli: {list(SENARYOLAR.keys())}")
    return hesapla_mirac_durumu(SENARYOLAR[senaryo_adi])


def tum_senaryolari_karsilastir() -> Dict[str, MiracCiktisi]:
    """Bütün hazır senaryoları çalıştırır."""
    return {ad: hesapla_mirac_durumu(p) for ad, p in SENARYOLAR.items()}


def csv_yaz(dosya_yolu: str) -> None:
    """Sonuçları CSV formatında diske yazar."""
    import csv
    sonuclar = tum_senaryolari_karsilastir()
    with open(dosya_yolu, mode="w", newline="", encoding="utf-8") as f:
        yazici = csv.writer(f)
        yazici.writerow([
            "Senaryo", "Beta_v_c", "Letafet", "MertebeNo", "DunyaSuresi_sn",
            "Lorentz_Gama", "OzZaman_sn", "EtkinKutle", "Hissedilen_G",
            "TilsimFethiSkoru", "Mertebe", "Hukum"
        ])
        for ad, c in sonuclar.items():
            p = SENARYOLAR[ad]
            yazici.writerow([
                ad, p.hiz_orani_beta, p.letafet_derecesi, p.seyir_mertebesi,
                p.dunya_suresi_saniye, c.lorentz_gama, c.yolcu_oz_zaman_saniye,
                c.etkin_kutle_orani, c.hissedilen_g_kuvveti, c.tilsim_fethi_skoru,
                c.ontolojik_mertebe, c.hukum
            ])


def tablolastir() -> None:
    """Konsola özet analitik rapor basar."""
    print("=" * 96)
    print("  🌌 MİRAC, GÖRELİLİK VE TAYY-I ZAMAN MODELİ (31. SÖZ: MİRAC RİSALESİ)")
    print("=" * 96)
    print(f"{'Senaryo':<24} {'Lorentz γ':>12} {'Öz-Zaman (s)':>14} {'G-Kuvveti':>11} {'Tılsım %':>9}  Ontolojik Mertebe")
    print("-" * 96)
    sonuclar = tum_senaryolari_karsilastir()
    for ad, c in sonuclar.items():
        zaman_str = f"{c.yolcu_oz_zaman_saniye:.2e}" if c.yolcu_oz_zaman_saniye < 0.01 else f"{c.yolcu_oz_zaman_saniye:.3f}"
        print(f"{ad:<24} {c.lorentz_gama:>12.1f} {zaman_str:>14} {c.hissedilen_g_kuvveti:>11.1f} {c.tilsim_fethi_skoru:>9.1f}  {c.ontolojik_mertebe}")
    print("=" * 96)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Mirac ve Görelilik Simülasyonu (31. Söz)")
    parser.add_argument("--senaryo", type=str, choices=list(SENARYOLAR.keys()), help="Tek bir senaryo çalıştır")
    parser.add_argument("--csv", type=str, help="Sonuçları CSV dosyasına yaz")
    parser.add_argument("--tablo", action="store_true", default=True, help="Özet tabloyu ekrana bas")
    args = parser.parse_args()

    if args.senaryo:
        res = calistir_senaryo(args.senaryo)
        print(f"\nSenaryo: {args.senaryo}")
        print(f"Lorentz Faktörü (γ):     {res.lorentz_gama}")
        print(f"Yolcunun Öz-Zamanı (Δτ): {res.yolcu_oz_zaman_saniye} sn")
        print(f"Efektif Kütle Oranı:     {res.etkin_kutle_orani}")
        print(f"Hissedilen G-Kuvveti:    {res.hissedilen_g_kuvveti} G")
        print(f"Tılsım Fethi Skoru:      %{res.tilsim_fethi_skoru}")
        print(f"Ontolojik Mertebe:       {res.ontolojik_mertebe}")
        print(f"Hüküm:                   {res.hukum}\n")
    else:
        tablolastir()

    if args.csv:
        csv_yaz(args.csv)
        print(f"Sonuçlar CSV dosyasına kaydedildi: {args.csv}")
