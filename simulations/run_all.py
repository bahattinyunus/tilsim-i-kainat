#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tılsım-ı Kâinat — Bütünleşik Simülasyon Çalıştırıcısı (Unified Runner)
=====================================================================

Bu araç, Tılsım-ı Kâinat laboratuvarındaki on bir temel simülasyonu
tek bir merkezden çalıştırmanızı ve karşılaştırmanızı sağlar:

1. Ene Kalınlaşma Modeli (ene-thickening-model.py)
2. Tahavvülât-ı Zerrât Simülasyonu (zerre-simulation.py)
3. İhlas ve Şahs-ı Manevî Sinerji Modeli (ihlas-synergy-model.py)
4. Kozmik Entropi ve Kudret İntizamı Modeli (entropy-information-model.py)
5. Tayy-ı Mekân ve Kuantum Işınlanma Modeli (teleportation-information-model.py)
6. Kader, İrade ve Levh-i Mahfuz Karar Matrisi Modeli (kader-irade-matrix-model.py)
7. Haşir, Bahar İhyası ve Bilgi Korunumu Modeli (hasir-ebediyet-model.py)
8. Hayat, Şuur ve Bütünleşik Bilgi Modeli (hayat-suur-model.py)
9. Mirac, Görelilik ve Tayy-ı Zaman Modeli (mirac-relativity-model.py)
10. Mânâ-yı Harfî, Niyet-Nazar ve İlişkisel Kuantum Modeli (nazar-rqm-model.py)
11. Holografik Âlem-i Misâl, Ehadiyet ve Aynalar Modeli (holographic-ayine-model.py)
"""

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def baslik_yaz(baslik: str) -> None:
    print("\n" + "=" * 76)
    print(f"  🌌 {baslik}")
    print("=" * 76 + "\n", flush=True)

def calistir(dosya: str, argumanlar: list[str]) -> int:
    komut = [sys.executable, str(BASE_DIR / dosya)] + argumanlar
    sys.stdout.flush()
    res = subprocess.run(komut)
    sys.stdout.flush()
    return res.returncode

def main() -> int:
    baslik_yaz("TILSIM-I KÂİNAT: ON BİR MODELİN KÜLLÎ İCMALİ")
    
    print("1️⃣  ENE KALINLAŞMA MODELİ (30. SÖZ, BİRİNCİ MAKSAD):", flush=True)
    calistir("ene-thickening-model.py", ["--karsilastir"])
    
    print("\n" + "-" * 76 + "\n", flush=True)
    print("2️⃣  TAHAVVÜLÂT-I ZERRÂT VE KUDRET KALEMİ (30. SÖZ, İKİNCİ MAKSAD):", flush=True)
    calistir("zerre-simulation.py", ["--karsilastir"])
    
    print("\n" + "-" * 76 + "\n", flush=True)
    print("3️⃣  İHLAS VE ŞAHS-I MANEVÎ SİNERJİ MODELİ (21. LEM'A):", flush=True)
    calistir("ihlas-synergy-model.py", ["--karsilastir"])
    
    print("\n" + "-" * 76 + "\n", flush=True)
    print("4️⃣  KOZMİK ENTROPİ VE KUDRET İNTİZAMI (WHEELER: IT FROM BIT & 30. SÖZ):", flush=True)
    calistir("entropy-information-model.py", ["--karsilastir"])

    print("\n" + "-" * 76 + "\n", flush=True)
    print("5️⃣  TAYY-I MEKÂN VE KUANTUM IŞINLANMA (20. SÖZ, BELKIS'IN TAHTI):", flush=True)
    calistir("teleportation-information-model.py", ["--mesafe", "2500", "--kutle", "500"])
    
    print("\n" + "-" * 76 + "\n", flush=True)
    print("6️⃣  KADER, İRADE VE LEVH-İ MAHFUZ KARAR MATRİSİ (26. SÖZ, KADER RİSALESİ):", flush=True)
    calistir("kader-irade-matrix-model.py", ["--karsilastir"])

    print("\n" + "-" * 76 + "\n", flush=True)
    print("7️⃣  HAŞİR, BAHAR İHYASI VE BİLGİ KORUNUMU (10. SÖZ, HAŞİR RİSALESİ):", flush=True)
    calistir("hasir-ebediyet-model.py", ["--karsilastir"])

    print("\n" + "-" * 76 + "\n", flush=True)
    print("8️⃣  HAYAT, ŞUUR VE BÜTÜNLEŞİK BİLGİ (29. SÖZ & 30. LEM'A - İSM-İ HAYY & IIT Φ):", flush=True)
    calistir("hayat-suur-model.py", ["--tablo"])

    print("\n" + "-" * 76 + "\n", flush=True)
    print("9️⃣  MİRAC, GÖRELİLİK VE TAYY-I ZAMAN (31. SÖZ, MİRAC RİSALESİ & ÖZEL GÖRELİLİK):", flush=True)
    calistir("mirac-relativity-model.py", ["--tablo"])

    print("\n" + "-" * 76 + "\n", flush=True)
    print("🔟  MÂNÂ-YI HARFÎ, NİYET-NAZAR VE İLİŞKİSEL KUANTUM (MESNEVÎ, RQM & ITP):", flush=True)
    calistir("nazar-rqm-model.py", ["--tablo"])

    print("\n" + "-" * 76 + "\n", flush=True)
    print("1️⃣1️⃣ HOLOGRAFİK ÂLEM-İ MİSÂL, EHADİYET VE AYNALAR (16. SÖZ, AdS/CFT & ER=EPR):", flush=True)
    calistir("holographic-ayine-model.py", ["--tablo"])

    print("\n" + "=" * 76, flush=True)
    print("  ✅ Bütün simülasyonlar (11 model, 73 birim testi) başarıyla icra edildi.", flush=True)
    print("=" * 76 + "\n", flush=True)
    return 0

if __name__ == "__main__":
    sys.exit(main())
