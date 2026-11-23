#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İhlas ve Şahs-ı Manevî Sinerji Modeli Birim Testleri
"""

import os
import sys
import tempfile
import unittest
import importlib.util

dosya_yolu = os.path.join(os.path.dirname(__file__), "ihlas-synergy-model.py")
spec = importlib.util.spec_from_file_location("ihlas_synergy_model", dosya_yolu)
ihlas_modulu = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = ihlas_modulu
spec.loader.exec_module(ihlas_modulu)

IhlasParametreleri = ihlas_modulu.IhlasParametreleri
ihlas_simule_et = ihlas_modulu.ihlas_simule_et
ihlas_senaryo_parametreleri = ihlas_modulu.ihlas_senaryo_parametreleri
IHLAS_SENARYOLAR = ihlas_modulu.IHLAS_SENARYOLAR
ihlas_csv_yaz = ihlas_modulu.ihlas_csv_yaz


class IhlasModelTestleri(unittest.TestCase):

    def test_parametre_dogrulama(self):
        with self.assertRaises(ValueError):
            p = IhlasParametreleri(fert_sayisi=0)
            p.dogrula()

        with self.assertRaises(ValueError):
            p = IhlasParametreleri(ihlas=1.2)
            p.dogrula()

    def test_dort_elif_4444_sinerjisi(self):
        p = ihlas_senaryo_parametreleri("dort_elif")
        r = ihlas_simule_et(p)
        self.assertTrue(r.ihlas_muhafazasi)
        self.assertGreater(r.nihai_kuvvet, 3000.0)
        self.assertIsNotNone(r.tam_erime_zamani)
        self.assertLess(r.nihai_buz, 0.05)

    def test_uc_elif_111_sinerjisi(self):
        p = ihlas_senaryo_parametreleri("uc_elif")
        r = ihlas_simule_et(p)
        self.assertEqual(p.fert_sayisi, 3)
        self.assertEqual(p.sirr_i_adediyet_tavani, 111.0)
        self.assertGreater(r.nihai_kuvvet, 80.0)

    def test_benlik_rekabetinde_kuvvet_coker(self):
        p = ihlas_senaryo_parametreleri("benlik_rekabeti")
        r = ihlas_simule_et(p)
        self.assertFalse(r.ihlas_muhafazasi)
        self.assertLess(r.nihai_kuvvet, 4.0)  # 4 kişinin toplam gücünden bile az kalır
        self.assertGreater(r.nihai_buz, 0.80)  # Buz erimez, donar

    def test_tum_senaryolar_calisiyor(self):
        for ad in IHLAS_SENARYOLAR:
            p = ihlas_senaryo_parametreleri(ad)
            r = ihlas_simule_et(p)
            self.assertGreater(len(r.adimlar), 0)
            self.assertGreaterEqual(r.nihai_kuvvet, 0.0)

    def test_csv_yazma(self):
        p = ihlas_senaryo_parametreleri("kevser_havuzu")
        r = ihlas_simule_et(p)
        with tempfile.TemporaryDirectory() as td:
            csv_yol = os.path.join(td, "ihlas.csv")
            ihlas_csv_yaz(csv_yol, r)
            self.assertTrue(os.path.exists(csv_yol))
            with open(csv_yol, "r", encoding="utf-8") as f:
                satirlar = f.readlines()
                self.assertGreaterEqual(len(satirlar), 10)


if __name__ == "__main__":
    unittest.main()
