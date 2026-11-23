#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Haşir, Bahar İhyası ve Bilgi Korunumu Modeli Birim Testleri
"""

import os
import sys
import tempfile
import unittest
import importlib.util

dosya_yolu = os.path.join(os.path.dirname(__file__), "hasir-ebediyet-model.py")
spec = importlib.util.spec_from_file_location("hasir_ebediyet_model", dosya_yolu)
hasir_modulu = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = hasir_modulu
spec.loader.exec_module(hasir_modulu)

HasirParametreleri = hasir_modulu.HasirParametreleri
hasir_simule_et = hasir_modulu.hasir_simule_et
HASIR_SENARYOLARI = hasir_modulu.HASIR_SENARYOLARI
hasir_csv_yaz = hasir_modulu.hasir_csv_yaz


class HasirModelTestleri(unittest.TestCase):

    def test_parametre_dogrulama(self):
        with self.assertRaises(ValueError):
            p = HasirParametreleri(ahiret_inanci=1.5)
            p.dogrula()

        with self.assertRaises(ValueError):
            p = HasirParametreleri(bilgi_korunumu=-0.1)
            p.dogrula()

        with self.assertRaises(ValueError):
            p = HasirParametreleri(adim_sayisi=0)
            p.dogrula()

    def test_hasir_i_ecsad_basarili(self):
        p = HASIR_SENARYOLARI["hasir_i_ecsad"]
        r = hasir_simule_et(p)
        self.assertGreater(r.nihai_ihya, 0.90)
        self.assertGreater(r.nihai_adalet, 0.90)
        self.assertGreater(r.nihai_hikmet, 0.90)
        self.assertIn("Adalet-i Mahza", r.netice_hukmu)

    def test_hasirsiz_faraziye_zulme_doner(self):
        p = HASIR_SENARYOLARI["hasirsiz_faraziye"]
        r = hasir_simule_et(p)
        self.assertEqual(r.nihai_ihya, 0.0)
        self.assertLess(r.nihai_adalet, 0.15)
        self.assertLess(r.nihai_hikmet, 0.15)
        self.assertIn("Abesiyet", r.netice_hukmu)

    def test_iade_kolayligi_ibdadan_yuksek(self):
        p = HASIR_SENARYOLARI["bahar_ihyasi"]
        r = hasir_simule_et(p)
        self.assertGreater(r.iade_kolaylik_carpani, 50.0)

    def test_tum_senaryolar(self):
        for ad, p in HASIR_SENARYOLARI.items():
            r = hasir_simule_et(p)
            self.assertGreater(len(r.adimlar), 0)
            self.assertTrue(0.0 <= r.nihai_adalet <= 1.0)
            self.assertTrue(0.0 <= r.nihai_hikmet <= 1.0)

    def test_csv_yazma(self):
        p = HASIR_SENARYOLARI["bahar_ihyasi"]
        r = hasir_simule_et(p)
        with tempfile.TemporaryDirectory() as td:
            yol = os.path.join(td, "hasir.csv")
            hasir_csv_yaz(yol, r)
            self.assertTrue(os.path.exists(yol))
            self.assertGreater(os.path.getsize(yol), 100)


if __name__ == "__main__":
    unittest.main()
