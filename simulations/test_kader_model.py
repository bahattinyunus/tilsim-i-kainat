#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kader, İrade ve Levh-i Mahfuz Karar Matrisi Modeli Birim Testleri
"""

import os
import sys
import tempfile
import unittest
import importlib.util

dosya_yolu = os.path.join(os.path.dirname(__file__), "kader-irade-matrix-model.py")
spec = importlib.util.spec_from_file_location("kader_irade_matrix_model", dosya_yolu)
kader_modulu = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = kader_modulu
spec.loader.exec_module(kader_modulu)

KaderParametreleri = kader_modulu.KaderParametreleri
kader_simule_et = kader_modulu.kader_simule_et
KADER_SENARYOLARI = kader_modulu.KADER_SENARYOLARI
kader_csv_yaz = kader_modulu.kader_csv_yaz


class KaderModelTestleri(unittest.TestCase):

    def test_parametre_dogrulama(self):
        with self.assertRaises(ValueError):
            p = KaderParametreleri(irade_meyli=1.5)
            p.dogrula()

        with self.assertRaises(ValueError):
            p = KaderParametreleri(irade_meyli=-1.5)
            p.dogrula()

        with self.assertRaises(ValueError):
            p = KaderParametreleri(hasenat_kadere_isnad=1.2)
            p.dogrula()

        with self.assertRaises(ValueError):
            p = KaderParametreleri(adimi_sayisi=-5)
            p.dogrula()

    def test_istikamet_ehli_dengesi(self):
        p = KADER_SENARYOLARI["istikamet_ehli"]
        r = kader_simule_et(p)
        self.assertGreater(r.nihai_istikamet, 0.85)
        self.assertLess(r.nihai_kibir, 0.15)
        self.assertLess(r.nihai_yeis, 0.15)
        self.assertIn("İstikamet", r.ruhi_makam)
        self.assertGreater(r.toplam_hasenat, r.toplam_seyyiat)

    def test_firavun_kibri_ucurumu(self):
        p = KADER_SENARYOLARI["firavun_kibri"]
        r = kader_simule_et(p)
        self.assertGreater(r.nihai_kibir, 0.40)
        self.assertLess(r.nihai_istikamet, 0.70)
        self.assertIn("Kibir", r.ruhi_makam)

    def test_cebriye_yeisi_ucurumu(self):
        p = KADER_SENARYOLARI["cebriye_yeisi"]
        r = kader_simule_et(p)
        self.assertGreater(r.nihai_yeis, 0.35)
        self.assertIn("Yeis", r.ruhi_makam)

    def test_dua_ve_sadaka_kalkani(self):
        p = KADER_SENARYOLARI["dua_ile_kaza_tehiri"]
        r = kader_simule_et(p)
        self.assertGreaterEqual(r.muallak_kaza_def_orani, 0.85)
        self.assertGreater(r.nihai_istikamet, 0.80)

    def test_tum_senaryolar_basarili(self):
        for ad, p in KADER_SENARYOLARI.items():
            r = kader_simule_et(p)
            self.assertGreater(len(r.adimlar), 0)
            self.assertTrue(0.0 <= r.nihai_istikamet <= 1.0)
            self.assertTrue(0.0 <= r.nihai_kibir <= 1.0)
            self.assertTrue(0.0 <= r.nihai_yeis <= 1.0)

    def test_csv_yazma(self):
        p = KADER_SENARYOLARI["istikamet_ehli"]
        r = kader_simule_et(p)
        with tempfile.TemporaryDirectory() as td:
            csv_yol = os.path.join(td, "kader.csv")
            kader_csv_yaz(csv_yol, r)
            self.assertTrue(os.path.exists(csv_yol))
            self.assertGreater(os.path.getsize(csv_yol), 100)


if __name__ == "__main__":
    unittest.main()
