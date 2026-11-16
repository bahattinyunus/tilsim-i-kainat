#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İhlas ve Şahs-ı Manevî Sinerji Modeli (İhlas Synergy Model)
==========================================================

21. Lem'a'nın (İhlas Risalesi) derin ontolojik ve manevî dinamiklerinin
sembolik bir matematiksel modellemesidir:

    "Elbette dört ferdden bin yüz onbir kuvvet-i maneviyeyi temin eden sırr-ı ihlâsı
     kazanmak ile, tesanüd ve ittihad-ı hakikîye muhtacız ve mecburuz.
     Evet, üç elif ittihad etmezse, üç kıymeti var. Sırr-ı adediyet ile ittihad etse,
     yüz on bir (111) kıymet alır.
     Dört kere dört ayrı ayrı olsa, on altı kıymeti var. Eğer sırr-ı uhuvvet ve
     ittihad-ı maksat ile... bir çizgi üstünde omuz omuza verseler, o vakit
     dört bin dört yüz kırk dört (4444) kuvvetinde ve kıymetinde olduğu gibi..."

    "Bahtiyar odur ki, kevser-i Kur'ânîden süzülen tatlı, büyük bir havuzu
     kazanmak için, bir buz parçası nev'indeki şahsiyetini ve enâniyetini
     o havuz içine atıp eritendir."

Model Mantığı:
-------------
- N : Fert (kardeş) sayısı
- I : İhlas derecesi [0, 1] (amelde sırf rıza-yı İlâhî gözetme)
- T : Tesanüd ve Uhuvvet [0, 1] (birbirinin faziletiyle iftihar etme)
- R : Rekabet ve Haset [0, 1] (hubb-u câh, gıybet, enaniyet sürtüşmesi)
- B : Bireysel Enaniyet Buzu [0, 1] (1 = taş gibi buz, 0 = havuzda tamamen erimiş)

Dinamik Diferansiyel Denklem (Euler yöntemi):
    dB/dt = - k_erime * I * T * B + k_donma * R * (1 - B)

Sinerji Çarpanı ve Manevî Kuvvet (K_manevi):
    K_tekil = N
    K_tavan = sum(N * (10 ** i) for i in range(N)) (N=3 için 333/111x3, N=4 için 4444)
    Etkinlik = I * T * (1.0 - B) * (1.0 - R)
    K_manevi = N + (K_tavan - N) * Etkinlik

UYARI: Bu simülasyon manevî bir tefekkür aracıdır; ihlas ve faziletin sırrını
sayısal metaforlarla idrake yaklaştırmak gayesini taşır.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass, field, replace
from typing import Dict, List, Optional

try:  # pragma: no cover
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:  # pragma: no cover
    pass


# ---------------------------------------------------------------------------
# Parametreler
# ---------------------------------------------------------------------------

@dataclass
class IhlasParametreleri:
    """İhlas ve Şahs-ı Manevî parametreleri."""
    fert_sayisi: int = 4            # Kardeş sayısı (N)
    ihlas: float = 0.90             # [0, 1] Sırf rıza-yı İlâhî
    tesanud: float = 0.85           # [0, 1] Birbirinin meziyetiyle iftihar
    rekabet: float = 0.05           # [0, 1] Haset, makam sevgisi, gıybet
    buz_baslangic: float = 0.50     # [0, 1] Başlangıçtaki enaniyet buzu (B0)
    
    # Dinamik katsayılar
    k_erime: float = 0.80           # Kevser havuzundaki erime hızı katsayısı
    k_donma: float = 0.60           # Rekabetle yeniden buzlaşma katsayısı
    
    # Simülasyon zamanı
    sure: float = 10.0
    adim: float = 0.1

    def dogrula(self) -> None:
        if self.fert_sayisi < 1:
            raise ValueError("'fert_sayisi' en az 1 olmalıdır")
        for ad in ("ihlas", "tesanud", "rekabet", "buz_baslangic"):
            v = getattr(self, ad)
            if not 0.0 <= v <= 1.0:
                raise ValueError(f"'{ad}' parametresi [0, 1] aralığında olmalı (verilen: {v})")
        if self.sure <= 0 or self.adim <= 0:
            raise ValueError("'sure' ve 'adim' pozitif olmalıdır")

    @property
    def sirr_i_adediyet_tavani(self) -> float:
        """21. Lem'a'daki sırr-ı adediyet tavanı.
        N=1 -> 1
        N=2 -> 22
        N=3 -> 111 (3x37 veya 3 yan yana elif = 111)
        N=4 -> 4444 (Dört fertten 4444 kuvveti)
        """
        if self.fert_sayisi == 1:
            return 1.0
        elif self.fert_sayisi == 2:
            return 22.0
        elif self.fert_sayisi == 3:
            return 111.0
        elif self.fert_sayisi == 4:
            return 4444.0
        else:
            # Genel formül: N basamaklı N...N
            return sum(self.fert_sayisi * (10 ** i) for i in range(self.fert_sayisi))


# ---------------------------------------------------------------------------
# Simülasyon Sonucu
# ---------------------------------------------------------------------------

@dataclass
class IhlasAdimKaydi:
    t: float
    buz_hacmi: float
    erime_orani: float
    manevi_kuvvet: float
    sinerji_kat: float


@dataclass
class IhlasSonuc:
    adimlar: List[IhlasAdimKaydi] = field(default_factory=list)
    nihai_buz: float = 0.0
    nihai_kuvvet: float = 0.0
    maksimum_sinerji: float = 0.0
    tam_erime_zamani: Optional[float] = None
    ihlas_muhafazasi: bool = True


# ---------------------------------------------------------------------------
# Simülasyon Fonksiyonu
# ---------------------------------------------------------------------------

def ihlas_simule_et(p: IhlasParametreleri) -> IhlasSonuc:
    p.dogrula()
    sonuc = IhlasSonuc()
    
    B = p.buz_baslangic
    t = 0.0
    tavan = p.sirr_i_adediyet_tavani
    N = float(p.fert_sayisi)
    
    n_adim = int(round(p.sure / p.adim))
    
    for i in range(n_adim + 1):
        t_cur = round(t, 4)
        erime_orani = 1.0 - B
        
        # Etkinlik katsayısı
        etkinlik = p.ihlas * p.tesanud * erime_orani * (1.0 - p.rekabet)
        etkinlik = max(0.0, min(1.0, etkinlik))
        
        # Manevî Kuvvet: Bireysel toplam (N) ile sırr-ı adediyet tavanı arasında
        if p.rekabet > 0.7:
            # Şiddetli ihtilaf durumunda adî toplamın da altına düşer
            manevi_kuvvet = max(0.1, N * (1.0 - p.rekabet * 0.9))
        else:
            manevi_kuvvet = N + (tavan - N) * etkinlik
            
        sinerji_katsayisi = manevi_kuvvet / N

        kayit = IhlasAdimKaydi(
            t=t_cur,
            buz_hacmi=round(B, 4),
            erime_orani=round(erime_orani, 4),
            manevi_kuvvet=round(manevi_kuvvet, 1),
            sinerji_kat=round(sinerji_katsayisi, 1),
        )
        sonuc.adimlar.append(kayit)
        
        if B <= 0.02 and sonuc.tam_erime_zamani is None:
            sonuc.tam_erime_zamani = t_cur

        # Euler adımı
        # dB/dt = - k_erime * I * T * B + k_donma * R * (1 - B)
        dB = - (p.k_erime * p.ihlas * p.tesanud * B) + (p.k_donma * p.rekabet * (1.0 - B))
        B = max(0.0, min(1.0, B + p.adim * dB))
        t += p.adim

    sonuc.nihai_buz = sonuc.adimlar[-1].buz_hacmi
    sonuc.nihai_kuvvet = sonuc.adimlar[-1].manevi_kuvvet
    sonuc.maksimum_sinerji = max(d.sinerji_kat for d in sonuc.adimlar)
    sonuc.ihlas_muhafazasi = sonuc.nihai_buz < 0.20 and p.rekabet < 0.30
    
    return sonuc


# ---------------------------------------------------------------------------
# Hazır Senaryolar
# ---------------------------------------------------------------------------

IHLAS_SENARYOLAR: Dict[str, Dict[str, object]] = {
    "dort_elif": {
        "aciklama": "4 fedakâr kardeş: İhlas tam, tesanüd kâmil, rekabet yok. 4444 sırrına inkişaf.",
        "params": dict(fert_sayisi=4, ihlas=0.95, tesanud=0.95, rekabet=0.01, buz_baslangic=0.3),
    },
    "kevser_havuzu": {
        "aciklama": "Büyük enaniyet buzu (B0=0.85); fakat samimi ihlas ve tevazu ile havuzda tamamen erir.",
        "params": dict(fert_sayisi=4, ihlas=0.90, tesanud=0.85, rekabet=0.05, buz_baslangic=0.85),
    },
    "benlik_rekabeti": {
        "aciklama": "Kardeşler arasında hubb-u câh ve rekabet girer; buz erimez, manevî kuvvet çöker.",
        "params": dict(fert_sayisi=4, ihlas=0.20, tesanud=0.15, rekabet=0.80, buz_baslangic=0.70),
    },
    "uc_elif": {
        "aciklama": "Üç elifin sırr-ı adediyet ile 111 kıymetini alması.",
        "params": dict(fert_sayisi=3, ihlas=0.92, tesanud=0.90, rekabet=0.02, buz_baslangic=0.25),
    },
    "sefine_hademeleri": {
        "aciklama": "İnsân-ı kâmil şahs-ı manevîsi: Bir fabrikanın çarkları gibi tam bir ittihad.",
        "params": dict(fert_sayisi=4, ihlas=0.98, tesanud=0.99, rekabet=0.00, buz_baslangic=0.10),
    },
}


def ihlas_senaryo_parametreleri(ad: str, temel: Optional[IhlasParametreleri] = None) -> IhlasParametreleri:
    if ad not in IHLAS_SENARYOLAR:
        raise KeyError(f"Bilinmeyen senaryo: {ad}. Seçenekler: {', '.join(IHLAS_SENARYOLAR)}")
    temel = temel or IhlasParametreleri()
    return replace(temel, **IHLAS_SENARYOLAR[ad]["params"])  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Rapor ve CSV
# ---------------------------------------------------------------------------

def ihlas_raporu(ad: str, p: IhlasParametreleri, r: IhlasSonuc) -> str:
    satirlar = [
        "=" * 72,
        f"  🌊 İHLAS VE ŞAHS-I MANEVÎ RAPORU: {ad.upper()}",
        "=" * 72,
        f"  Fert (Kardeş) Sayısı  : {p.fert_sayisi} fert",
        f"  İhlas Derecesi        : {p.ihlas:.2f} (Sırf rıza-yı Bârî)",
        f"  Tesanüd & Uhuvvet     : {p.tesanud:.2f} (Birbirinin meziyetiyle iftihar)",
        f"  Rekabet & Haset Marazı: {p.rekabet:.2f}",
        f"  Sırr-ı Adediyet Tavanı: {p.sirr_i_adediyet_tavani:,.0f} kat manevî kuvvet",
        "-" * 72,
        f"  Başlangıç Buzu (B0)   : {p.buz_baslangic:.2f}  -->  Nihai Buz (B): {r.nihai_buz:.3f}",
        f"  Adî Toplam Kuvvet     : {p.fert_sayisi} ferd",
        f"  Nihai Manevî Kuvvet   : {r.nihai_kuvvet:,.1f} ({r.maksimum_sinerji:,.1f}x kat sinerji!)",
        "-" * 72,
    ]
    if r.tam_erime_zamani is not None:
        satirlar.append(f"  ✨ Buz parçası t = {r.tam_erime_zamani:.1f} anında kevser havuzunda tamamen eridi.")
    else:
        satirlar.append("  ❄️ Enaniyet buzu henüz tamamen erimedi; havuzdan tam istifade edilemiyor.")

    if r.ihlas_muhafazasi:
        satirlar.append("  🏆 'Dört fedakâr kardeş 4444 kuvvetindedir' sırrı tahakkuk etti!")
    else:
        satirlar.append("  ⚠️ Rekabet veya benlik buzlaşması sebebiyle manevî sinerji inkıtaya uğradı.")
    satirlar.append("=" * 72)
    return "\n".join(satirlar)


def ihlas_csv_yaz(yol: str, r: IhlasSonuc) -> None:
    with open(yol, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["t", "buz_hacmi", "erime_orani", "manevi_kuvvet", "sinerji_kat"])
        for d in r.adimlar:
            w.writerow([d.t, d.buz_hacmi, d.erime_orani, d.manevi_kuvvet, d.sinerji_kat])


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="İhlas ve Şahs-ı Manevî Sinerji Simülasyonu (21. Lem'a).")
    ap.add_argument("--senaryo", "-s", choices=sorted(IHLAS_SENARYOLAR), default="dort_elif",
                    help="Hazır senaryo (varsayılan: dort_elif)")
    ap.add_argument("--listele", action="store_true", help="Senaryoları listele")
    ap.add_argument("--karsilastir", action="store_true", help="Tüm senaryoları karşılaştır")
    ap.add_argument("--csv", metavar="DOSYA.csv", help="CSV çıktısı kaydet")
    ap.add_argument("--fert", type=int, default=None, help="Fert sayısı")
    ap.add_argument("--ihlas", type=float, default=None, help="İhlas [0, 1]")
    ap.add_argument("--tesanud", type=float, default=None, help="Tesanüd [0, 1]")
    ap.add_argument("--rekabet", type=float, default=None, help="Rekabet [0, 1]")
    ap.add_argument("--buz", type=float, default=None, help="Başlangıç buzu [0, 1]")

    args = ap.parse_args(argv)

    if args.listele:
        for k, v in IHLAS_SENARYOLAR.items():
            print(f"  {k:<18} {v['aciklama']}")
        return 0

    elle: Dict[str, object] = {}
    if args.fert is not None:
        elle["fert_sayisi"] = args.fert
    if args.ihlas is not None:
        elle["ihlas"] = args.ihlas
    if args.tesanud is not None:
        elle["tesanud"] = args.tesanud
    if args.rekabet is not None:
        elle["rekabet"] = args.rekabet
    if args.buz is not None:
        elle["buz_baslangic"] = args.buz

    if args.karsilastir:
        print(f"{'Senaryo':<18} {'Fert':>5} {'Buz(0->Son)':>14} {'Nihai Kuvvet':>14} {'Sinerji':>10}  Netice")
        print("-" * 74)
        for ad in IHLAS_SENARYOLAR:
            p = replace(ihlas_senaryo_parametreleri(ad), **elle)  # type: ignore[arg-type]
            r = ihlas_simule_et(p)
            durum = "4444 Sırrı" if r.ihlas_muhafazasi else "Zayi Olma"
            buz_degisim = f"{p.buz_baslangic:.2f} -> {r.nihai_buz:.2f}"
            print(f"{ad:<18} {p.fert_sayisi:>5} {buz_degisim:>14} {r.nihai_kuvvet:>14.1f} {r.maksimum_sinerji:>9.1f}x  {durum}")
        return 0

    try:
        p = replace(ihlas_senaryo_parametreleri(args.senaryo), **elle)  # type: ignore[arg-type]
        r = ihlas_simule_et(p)
    except ValueError as exc:
        print(f"Hata: {exc}", file=sys.stderr)
        return 2

    print(ihlas_raporu(args.senaryo, p, r))
    if args.csv:
        ihlas_csv_yaz(args.csv, r)
        print(f"\nCSV kaydedildi: {args.csv}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
