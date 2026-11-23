#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kozmik Entropi ve Bilgi Modeli Birim Testleri
"""

import os
import sys
import tempfile
import unittest
import importlib.util

dosya_yolu = os.path.join(os.path.dirname(__file__), "entropy-information-model.py")
spec = importlib.util.spec_from_file_location("entropy_information_model", dosya_yolu)
entropi_modulu = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = entropi_modulu
spec.loader.exec_module(entropi_modulu)

EntropiParametreleri = entropi_modulu.EntropiParametreleri
entropi_simule_et = entropi_modulu.entropi_simule_et
entropi_senaryo_parametreleri = entropi_modulu.entropi_senaryo_parametreleri
ENTROPI_SENARYOLAR = entropi_modulu.ENTROPI_SENARYOLAR
entropi_csv_yaz = entropi_modulu.entropi_csv_yaz


class EntropiModelTestleri(unittest.TestCase):

    def test_parametre_dogrulama(self):
        with self.assertRaises(ValueError):
            p = EntropiParametreleri(kudret_tesiri=1.5)
            p.dogrula()

        with self.assertRaises(ValueError):
            p = EntropiParametreleri(sure=-1.0)
            p.dogrula()

    def test_dna_negentropi_yuksek(self):
        p = entropi_senaryo_parametreleri("canlilik_ve_dna")
        r = entropi_simule_et(p)
        self.assertFalse(r.kaos_cokusu)
        self.assertGreater(r.nihai_intizam, 0.85)
        self.assertLess(r.nihai_entropi, 0.15)
        self.assertGreater(r.maksimum_bilgi, 80.0)

    def test_materyalist_isi_olumu_coker(self):
        p = entropi_senaryo_parametreleri("materyalist_isi_olumu")
        r = entropi_simule_et(p)
        self.assertTrue(r.kaos_cokusu)
        self.assertLess(r.nihai_intizam, 0.05)
        self.assertGreaterEqual(r.nihai_entropi, 0.95)

    def test_tum_senaryolar_calisiyor(self):
        for ad in ENTROPI_SENARYOLAR:
            p = entropi_senaryo_parametreleri(ad)
            r = entropi_simule_et(p)
            self.assertGreater(len(r.adimlar), 0)
            self.assertTrue(0.0 <= r.nihai_intizam <= 1.0)

    def test_csv_yazma(self):
        p = entropi_senaryo_parametreleri("tohumun_inbisi")
        r = entropi_simule_et(p)
        with tempfile.TemporaryDirectory() as td:
            csv_yol = os.path.join(td, "entropi.csv")
            entropi_csv_yaz(csv_yol, r)
            self.assertTrue(os.path.exists(csv_yol))
            with open(csv_yol, "r", encoding="utf-8") as f:
                satirlar = f.readlines()
                self.assertGreaterEqual(len(satirlar), 10)


if __name__ == "__main__":
    unittest.main()
