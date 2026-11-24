#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esmâ-i Hüsnâ Fraktal Öz-Benzerlik ve Ölçek Değişmezliği Modeli (30. Lem'a) Birim Testleri.
"""

import importlib.util
from pathlib import Path
import tempfile
import unittest

MOD_PATH = Path(__file__).resolve().parent / "esma-fractal-resonance-model.py"
spec = importlib.util.spec_from_file_location("esma_fractal_model", MOD_PATH)
mod = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(mod)


class TestEsmaFractalModel(unittest.TestCase):
    def test_ism_i_azam_kainat_yuksek_vahdet(self):
        c = mod.hesapla_fraktal_durumu(mod.SENARYOLAR["ism_i_azam_kainat"])
        self.assertGreaterEqual(c.sikke_i_vahdet_skoru, 95.0)
        self.assertGreater(c.fraktal_boyut_df, 2.8)
        self.assertIn("İsm-i Âzam", c.tevhid_imzasi)

    def test_insan_fihristesi_misal_i_musaggar(self):
        c = mod.hesapla_fraktal_durumu(mod.SENARYOLAR["insan_fihristesi"])
        self.assertGreaterEqual(c.sikke_i_vahdet_skoru, 85.0)
        self.assertGreater(c.fihriste_yogunlugu, 70.0)

    def test_cekirdek_ve_agac_yuksek_tutarlilik(self):
        c = mod.hesapla_fraktal_durumu(mod.SENARYOLAR["cekirdek_ve_agac"])
        self.assertGreaterEqual(c.sikke_i_vahdet_skoru, 80.0)
        self.assertGreater(c.renormalizasyon_kararliligi, 70.0)

    def test_kristal_ve_bulut_orta_mertebe(self):
        c = mod.hesapla_fraktal_durumu(mod.SENARYOLAR["kristal_ve_bulut"])
        self.assertGreater(c.sikke_i_vahdet_skoru, 55.0)
        self.assertLess(c.sikke_i_vahdet_skoru, 85.0)

    def test_tesadufi_gurultu_kopukluk(self):
        c = mod.hesapla_fraktal_durumu(mod.SENARYOLAR["tesadufi_gurultu"])
        self.assertLess(c.sikke_i_vahdet_skoru, 20.0)
        self.assertLess(c.renormalizasyon_kararliligi, 5.0)
        self.assertIn("Kopukluğu", c.tevhid_imzasi)

    def test_monotonik_oz_benzerlik_etkisi(self):
        dusuk = mod.hesapla_fraktal_durumu(
            mod.FraktalParametreleri(20.0, 0.25, 30, 0.7)
        )
        yuksek = mod.hesapla_fraktal_durumu(
            mod.FraktalParametreleri(20.0, 0.90, 30, 0.7)
        )
        self.assertGreater(yuksek.sikke_i_vahdet_skoru, dusuk.sikke_i_vahdet_skoru)
        self.assertGreater(yuksek.fraktal_boyut_df, dusuk.fraktal_boyut_df)
        self.assertGreater(yuksek.renormalizasyon_kararliligi, dusuk.renormalizasyon_kararliligi)

    def test_esma_tenevvuu_fihriste_artisi(self):
        az = mod.hesapla_fraktal_durumu(mod.FraktalParametreleri(12.0, 0.85, 5, 0.85))
        cok = mod.hesapla_fraktal_durumu(mod.FraktalParametreleri(12.0, 0.85, 99, 0.85))
        self.assertGreater(cok.fihriste_yogunlugu, az.fihriste_yogunlugu)
        self.assertGreater(cok.fraktal_boyut_df, az.fraktal_boyut_df)

    def test_fraktal_boyut_sinirlari(self):
        for p in mod.SENARYOLAR.values():
            c = mod.hesapla_fraktal_durumu(p)
            self.assertGreaterEqual(c.fraktal_boyut_df, 1.0)
            self.assertLessEqual(c.fraktal_boyut_df, 3.0)

    def test_gecersiz_olcek_hatasi(self):
        with self.assertRaises(ValueError):
            mod.hesapla_fraktal_durumu(mod.FraktalParametreleri(0.5, 0.8, 10, 0.8))
        with self.assertRaises(ValueError):
            mod.hesapla_fraktal_durumu(mod.FraktalParametreleri(70.0, 0.8, 10, 0.8))

    def test_gecersiz_oz_benzerlik_hatasi(self):
        with self.assertRaises(ValueError):
            mod.hesapla_fraktal_durumu(mod.FraktalParametreleri(10.0, -0.1, 10, 0.8))
        with self.assertRaises(ValueError):
            mod.hesapla_fraktal_durumu(mod.FraktalParametreleri(10.0, 1.2, 10, 0.8))

    def test_gecersiz_esma_hatasi(self):
        with self.assertRaises(ValueError):
            mod.hesapla_fraktal_durumu(mod.FraktalParametreleri(10.0, 0.8, 0, 0.8))
        with self.assertRaises(ValueError):
            mod.hesapla_fraktal_durumu(mod.FraktalParametreleri(10.0, 0.8, 100, 0.8))

    def test_gecersiz_intizam_hatasi(self):
        with self.assertRaises(ValueError):
            mod.hesapla_fraktal_durumu(mod.FraktalParametreleri(10.0, 0.8, 10, -0.05))
        with self.assertRaises(ValueError):
            mod.hesapla_fraktal_durumu(mod.FraktalParametreleri(10.0, 0.8, 10, 1.05))

    def test_cli_tablo_ve_senaryo(self):
        self.assertEqual(mod.main(["--tablo"]), 0)
        self.assertEqual(mod.main(["--senaryo", "insan_fihristesi"]), 0)

    def test_csv_aktarimi(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = Path(tmpdir) / "fraktal.csv"
            self.assertEqual(mod.main(["--csv", str(csv_path)]), 0)
            icerik = csv_path.read_text(encoding="utf-8")
            self.assertIn("ism_i_azam_kainat", icerik)
            self.assertIn("sikke_i_vahdet_skoru", icerik)


if __name__ == "__main__":
    unittest.main()
