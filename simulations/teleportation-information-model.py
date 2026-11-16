#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tayy-ı Mekân ve Kuantum Işınlanma Modeli (Teleportation & Information Model)
=============================================================================

20. Söz'ün (Mucizât-ı Enbiya - Neml Sûresi 40. Âyet / Belkıs'ın Tahtı),
30. Söz'ün (Zerre ve Ene Risalesi) ve modern fizik prensiplerinin
(Wheeler: "It from Bit", Bekenstein Sınırı, Landauer İlkesi, Kuantum Dolanıklığı)
birlikte modellendiği analitik simülasyon sistemidir:

    "Kitaptan bir ilme sahip olan zat ise: 'Gözünü açıp kapamadan ben onu
     sana getiririm' dedi." (Neml Sûresi, 40)
    
    "Cenâb-ı Hak şu âyetin lisanıyla mânen der: 'Ey insanoğlu! Uzak mesafelerden
     bir cismi hazır etmek mümkündür... pekala maddenin dahi bu tarzda nakli
     ilmen ve fennen mümkündür.'" (20. Söz)

Bu simülasyon 3 farklı nakil modunu karşılaştırır:
1. Klasik Kütlesel Nakil (Balistik/Mekanik Hız Sınırı)
2. Kuantum Enformasyonel Rekonstrüksiyon ("It from Bit" Işınlanması)
3. Uzay-Zaman Bükülmesi ve Nuraniyet Sürüşü (Tayy-ı Mekân / Metrik Kısaltma)
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional

try:  # pragma: no cover
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:  # pragma: no cover
    pass

# Temel Fizik Sabitleri (SI)
ISIK_HIZI: float = 299_792_458.0           # c (m/s)
DIRAC_SABITI: float = 1.054571817e-34       # hbar (J·s)
BOLTZMANN_SABITI: float = 1.380649e-23      # k_B (J/K)
PLANCK_ZAMANI: float = 5.391247e-44         # t_P (s)
PROTON_KUTLESI: float = 1.67262192369e-27   # m_p (kg)


@dataclass
class CisimOzellikleri:
    """Işınlanacak veya nakledilecek makro cismin fiziksel özellikleri."""
    ad: str = "Belkıs'ın Tahtı"
    kutle_kg: float = 500.0         # Cismin kütlesi (kg)
    yaricap_m: float = 1.5          # Cismi çevreleyen kürenin yarıçapı (m)
    sicaklik_kelvin: float = 300.0  # Ortam sıcaklığı (K)
    nuraniyet_derecesi: float = 0.0 # [0, 1]: 0 = Kesif madde, 1 = Saf nuraniyet

    def dogrula(self) -> None:
        if self.kutle_kg <= 0:
            raise ValueError("Kütle pozitif olmalıdır.")
        if self.yaricap_m <= 0:
            raise ValueError("Yarıçap pozitif olmalıdır.")
        if self.sicaklik_kelvin <= 0:
            raise ValueError("Sıcaklık pozitif olmalıdır.")
        if not 0.0 <= self.nuraniyet_derecesi <= 1.0:
            raise ValueError("Nuraniyet derecesi [0, 1] aralığında olmalıdır.")

    @property
    def enerji_esdegeri_joule(self) -> float:
        """E = m * c^2"""
        return self.kutle_kg * (ISIK_HIZI ** 2)

    @property
    def bekenstein_bilgi_siniri_bit(self) -> float:
        """
        Bekenstein Bilgi Sınırı: Bir küresel hacim içine sığdırılabilecek
        maksimum kuantum enformasyon miktarı:
        I <= (2 * pi * R * E) / (hbar * c * ln(2))
        """
        pay = 2.0 * math.pi * self.yaricap_m * self.enerji_esdegeri_joule
        payda = DIRAC_SABITI * ISIK_HIZI * math.log(2)
        return pay / payda

    @property
    def atomik_bilgi_tahmini_bit(self) -> float:
        """
        Cismin atomik/moleküler seviyede durumunu tarif etmek için gereken
        tahmini kuantum bit (qubit) sayısı (pozisyon, momentum, spin, bağlar).
        Her nükleon için ortalama ~10^3 qubit kabulüyle.
        """
        nukleon_sayisi = self.kutle_kg / PROTON_KUTLESI
        return nukleon_sayisi * 1000.0


@dataclass
class NakilSonucu:
    mod_adi: str
    mesafe_km: float
    sure_saniye: float
    enformasyon_bit: float
    harcanan_veya_islenen_enerji_joule: float
    sadakat_orani: float        # Fidelity [0, 1]
    eylemsizlik_hissi_g: float  # G-force / maruz kalınan ivme stresi
    aciklama: str


class TeleportasyonSimulasyonu:
    """
    Üç farklı mekân aşma paradigmasını simüle eden motor:
    1. Balistik / Klasik Mekanik Nakil
    2. Kuantum Enformasyonel Rekonstrüksiyon (It from Bit)
    3. Tayy-ı Mekân & Nuraniyet Metriği (Uzay-zaman katlanması)
    """

    def __init__(self, cisim: CisimOzellikleri, mesafe_km: float = 2500.0):
        cisim.dogrula()
        if mesafe_km <= 0:
            raise ValueError("Mesafe pozitif olmalıdır.")
        self.cisim = cisim
        self.mesafe_km = mesafe_km
        self.mesafe_m = mesafe_km * 1000.0

    def hesapla_klasik_nakil(self, hiz_km_h: float = 900.0) -> NakilSonucu:
        """Geleneksel hızlı taşıma (ör. jet uçağı veya roket hızında)."""
        if hiz_km_h <= 0:
            raise ValueError("Hız pozitif olmalıdır.")
        hiz_ms = (hiz_km_h * 1000.0) / 3600.0
        sure_s = self.mesafe_m / hiz_ms
        # Kinetik enerji: 0.5 * m * v^2 + sürtünme işi tahmini
        enerji = 0.5 * self.cisim.kutle_kg * (hiz_ms ** 2) * 10.0
        return NakilSonucu(
            mod_adi="1. Klasik Kütlesel Nakil",
            mesafe_km=self.mesafe_km,
            sure_saniye=sure_s,
            enformasyon_bit=0.0,  # Enformasyon ayrıştırılmadan kütle bütünlüğü taşınır
            harcanan_veya_islenen_enerji_joule=enerji,
            sadakat_orani=1.0,
            eylemsizlik_hissi_g=1.0,
            aciklama=f"{hiz_km_h:.0f} km/h sabit hızla kesif kütle hareketi."
        )

    def hesapla_kuantum_rekonstruksiyon(
        self,
        kanal_bant_genisligi_qps: float = 1e29,  # Qubit per second aktarım hızı
        sinerji_ihlas_carpani: float = 4444.0,  # Kolektif kuantum hızlandırma
        rekonstruksiyon_kaybi: float = 1e-6
    ) -> NakilSonucu:
        """
        Belkıs'ın Tahtı Işınlanma Modeli:
        - Cisim kuantum seviyesinde taranır (It from Bit).
        - Dolanık foton/eter kanalıyla ışık hızında (c) enformasyon aktarılır.
        - Hedef noktadaki ham zerreler üzerinde anında yeniden inşa edilir (Tekvînî Sır).
        """
        bit_miktari = self.cisim.atomik_bilgi_tahmini_bit
        isik_suresi = self.mesafe_m / ISIK_HIZI

        etkin_bant_genisligi = kanal_bant_genisligi_qps * sinerji_ihlas_carpani
        islem_ve_aktarim_suresi = bit_miktari / etkin_bant_genisligi
        toplam_sure = isik_suresi + islem_ve_aktarim_suresi

        # Landauer prensibi uyarınca bilgi silme ve işleme enerjisi:
        # E = k_B * T * ln(2) * bit_sayisi
        landauer_enerji = BOLTZMANN_SABITI * self.cisim.sicaklik_kelvin * math.log(2) * bit_miktari
        sadakat = max(0.0, min(1.0, 1.0 - rekonstruksiyon_kaybi))

        return NakilSonucu(
            mod_adi="2. Kuantum Rekonstrüksiyon (It from Bit)",
            mesafe_km=self.mesafe_km,
            sure_saniye=toplam_sure,
            enformasyon_bit=bit_miktari,
            harcanan_veya_islenen_enerji_joule=landauer_enerji,
            sadakat_orani=sadakat,
            eylemsizlik_hissi_g=0.0,  # Kütle ötelenmediği için g-force = 0
            aciklama="Madde kuantum enformasyonuna ayrıştırılıp ışık hızında hedefe kodlandı."
        )

    def hesapla_tayy_i_mekan_nuraniyet(self) -> NakilSonucu:
        """
        31. Söz (Mirac) ve 20. Söz sırrıyla Uzay-Zaman Bükülmesi & Nuraniyet Sürüşü:
        - Kesafet letâfete inkılâb ettirilir (kütlesel eylemsizlik kalkar).
        - Mesafe uzay-zaman metriğinin katlanmasıyla (Wormhole / Âlem-i Misal tüneli)
          etkin olarak sıfıra yaklaşır.
        - Süre 'tarfetü'l-ayn' (göz açıp kapama) mertebesine (0.01 - 0.1 s) iner.
        """
        nuraniyet = max(0.01, self.cisim.nuraniyet_derecesi if self.cisim.nuraniyet_derecesi > 0 else 0.999)
        etkin_mesafe_m = self.mesafe_m * (1.0 - nuraniyet)
        
        # Nuraniyet arttıkça hareket ışık hızının lokal limitinden bağımsızlaşır (metrik katlanması)
        sure = max(PLANCK_ZAMANI * 1e40, (etkin_mesafe_m / ISIK_HIZI) * (1.0 - nuraniyet))
        # Süreyi insan idrakinde 'göz açıp kapama' (~0.05 s) seviyesinde sınırlayalım
        sure = max(0.005, min(0.08, sure))

        etkin_kutle = self.cisim.kutle_kg * (1.0 - nuraniyet)
        enerji = etkin_kutle * (ISIK_HIZI ** 2) * 0.001  # Metrik polarizasyon enerjisi

        return NakilSonucu(
            mod_adi="3. Tayy-ı Mekân & Nuraniyet Sürüşü",
            mesafe_km=self.mesafe_km,
            sure_saniye=sure,
            enformasyon_bit=self.cisim.bekenstein_bilgi_siniri_bit,
            harcanan_veya_islenen_enerji_joule=enerji,
            sadakat_orani=1.0,
            eylemsizlik_hissi_g=0.0,  # Uzay-zaman nesneyle birlikte sürüklendiğinden eylemsizlik sıfırdır
            aciklama="Metrik bükülme ve letafet sırrıyla mesafe aradan kaldırılarak anî vusul."
        )

    def tum_modlari_karsilastir(self) -> List[NakilSonucu]:
        return [
            self.hesapla_klasik_nakil(),
            self.hesapla_kuantum_rekonstruksiyon(),
            self.hesapla_tayy_i_mekan_nuraniyet(),
        ]


def rapor_olustur(cisim: CisimOzellikleri, mesafe_km: float) -> str:
    sim = TeleportasyonSimulasyonu(cisim, mesafe_km)
    sonuclar = sim.tum_modlari_karsilastir()

    satirlar = [
        "=" * 85,
        f"🌌 TAYY-I MEKÂN VE KUANTUM IŞINLANMA ANALİTİK RAPORU",
        f"Hedef Nesne: {cisim.ad} | Kütle: {cisim.kutle_kg:.1f} kg | Yarıçap: {cisim.yaricap_m:.2f} m",
        f"Mesafe: {mesafe_km:.1f} km (Örnek: Yemen/Sebe ➔ Kudüs)",
        f"Bekenstein Üst Bilgi Limiti: {cisim.bekenstein_bilgi_siniri_bit:.3e} Bit",
        f"Atomik Qubit İhtiyacı:       {cisim.atomik_bilgi_tahmini_bit:.3e} Qubit",
        "=" * 85,
        f"{'Nakil Modu':<36} | {'Süre':<12} | {'Sadakat':<8} | {'G-Kuvveti':<10} | {'İşlem/Enerji (J)'}",
        "-" * 85,
    ]

    for s in sonuclar:
        if s.sure_saniye >= 3600:
            sure_str = f"{s.sure_saniye / 3600.0:.2f} saat"
        elif s.sure_saniye >= 1.0:
            sure_str = f"{s.sure_saniye:.2f} sn"
        elif s.sure_saniye >= 1e-3:
            sure_str = f"{s.sure_saniye * 1000.0:.2f} ms"
        else:
            sure_str = f"{s.sure_saniye * 1e6:.2f} μs"

        satirlar.append(
            f"{s.mod_adi:<36} | {sure_str:<12} | {s.sadakat_orani * 100.0:>6.2f}% | "
            f"{s.eylemsizlik_hissi_g:>7.1f} G  | {s.harcanan_veya_islenen_enerji_joule:.2e} J"
        )
    satirlar.append("=" * 85)
    satirlar.append("💡 NETİCE VE TEKVÎNÎ MUHAKEME:")
    satirlar.append(
        "  1. Klasik nakil maddî ağırlık ve sürtünme sebebiyle saatler sürer (Ene/Kesafet perdesi).\n"
        "  2. Kuantum rekonstrüksiyon (It from Bit) maddeyi zerrelerin bilgi koduna tercüme eder;\n"
        "     işlem gücü arttıkça süre ışık hızının altına iner (~0.05 sn).\n"
        "  3. Tayy-ı Mekân (Nuraniyet ve Metrik Bükülme), mekanı ve eylemsizliği büzerek\n"
        "     Âsaf bin Berhiyâ'nın 'göz açıp kapayıncaya kadar' (tarfetü'l-ayn) sırrını tahakkuk ettirir."
    )
    satirlar.append("=" * 85)
    return "\n".join(satirlar)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Tayy-ı Mekân ve Kuantum Işınlanma Simülasyonu"
    )
    parser.add_argument("--kutle", type=float, default=500.0, help="Cisim kütlesi (kg)")
    parser.add_argument("--yaricap", type=float, default=1.5, help="Küre yarıçapı (m)")
    parser.add_argument("--mesafe", type=float, default=2500.0, help="Nakil mesafesi (km)")
    parser.add_argument("--nuraniyet", type=float, default=0.999, help="Nuraniyet derecesi [0, 1]")
    parser.add_argument("--csv", type=str, default="", help="Sonuçları CSV dosyasına kaydet")

    args = parser.parse_args(argv)

    cisim = CisimOzellikleri(
        ad="Belkıs'ın Tahtı (Simüle)",
        kutle_kg=args.kutle,
        yaricap_m=args.yaricap,
        nuraniyet_derecesi=args.nuraniyet
    )

    rapor = rapor_olustur(cisim, args.mesafe)
    print(rapor)

    if args.csv:
        sim = TeleportasyonSimulasyonu(cisim, args.mesafe)
        sonuclar = sim.tum_modlari_karsilastir()
        with open(args.csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["mod_adi", "mesafe_km", "sure_saniye", "enformasyon_bit", "enerji_joule", "sadakat", "g_kuvveti", "aciklama"])
            for s in sonuclar:
                writer.writerow([s.mod_adi, s.mesafe_km, s.sure_saniye, s.enformasyon_bit, s.harcanan_veya_islenen_enerji_joule, s.sadakat_orani, s.eylemsizlik_hissi_g, s.aciklama])
        print(f"Sonuçlar CSV dosyasına kaydedildi: {args.csv}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
