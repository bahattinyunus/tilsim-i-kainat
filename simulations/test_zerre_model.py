#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tahavvülât-ı Zerrât Simülasyonu Birim Testleri
"""

import os
import tempfile
import unittest

from importlib.machinery import SourceFileLoader

# Tireli dosya adını yükleme
dosya_yolu = os.path.join(os.path.dirname(__file__), "zerre-simulation.py")
zerre_modulu = SourceFileLoader("zerre_simulation", dosya_yolu).load_module()

ZerreParametreleri = zerre_modulu.ZerreParametreleri
zerre_simule_et = zerre_modulu.zerre_simule_et
zerre_senaryo_parametreleri = zerre_modulu.zerre_senaryo_parametreleri
ZERRE_SENARYOLAR = zerre_modulu.ZERRE_SENARYOLAR
zerre_csv_yaz = zerre_modulu.zerre_csv_yaz


class ZerreModelTestleri(unittest.TestCase):

    def test_parametre_dogrulama(self):
        with self.assertRaises(ValueError):
            p = ZerreParametreleri(bismillah_nisbeti=1.5)
            p.dogrula()

        with self.assertRaises(ValueError):
            p = ZerreParametreleri(adim_sayisi=0)
            p.dogrula()

    def test_tevfikin_gozu_hikmetli(self):
        p = zerre_senaryo_parametreleri("tevfikin_gozu")
        r = zerre_simule_et(p)
        self.assertFalse(r.tesaduf_cikmazi)
        self.assertGreater(r.nihai_hikmet, 0.70)
        self.assertEqual(len(r.duraklar), 5)
        # Son durak Tevfik'in Gözbebeği olmalı ve Elhamdülillah demeli
        self.assertIn("Gözbebeği", r.duraklar[-1].mertebe_adi)
        self.assertIn("ELHAMDÜLİLLÂH", r.duraklar[-1].zikir)

    def test_tesaduf_cikmazinda_kaos(self):
        p = zerre_senaryo_parametreleri("tesaduf_cikmazi")
        r = zerre_simule_et(p)
        self.assertTrue(r.tesaduf_cikmazi)
        self.assertLess(r.nihai_hikmet, 0.20)
        self.assertLess(r.ortalama_intizam, 0.15)

    def test_bismillah_kuvvet_artisi(self):
        # Bismillah nisbeti yüksek olan zerre daha çok yük kaldırır
        p_az = ZerreParametreleri(bismillah_nisbeti=0.2, vahdet_intibaki=0.8, tesaduf_sapmasi=0.0)
        p_cok = ZerreParametreleri(bismillah_nisbeti=0.9, vahdet_intibaki=0.8, tesaduf_sapmasi=0.0)
        r_az = zerre_simule_et(p_az)
        r_cok = zerre_simule_et(p_cok)
        self.assertGreater(r_cok.duraklar[-1].kaldirilan_yuk, r_az.duraklar[-1].kaldirilan_yuk)

    def test_tum_senaryolar_calisiyor(self):
        for ad in ZERRE_SENARYOLAR:
            p = zerre_senaryo_parametreleri(ad)
            r = zerre_simule_et(p)
            self.assertGreater(len(r.duraklar), 0)
            self.assertTrue(0.0 <= r.nihai_hikmet <= 1.0)

    def test_csv_yazma(self):
        p = zerre_senaryo_parametreleri("nebat_ruku")
        r = zerre_simule_et(p)
        with tempfile.TemporaryDirectory() as td:
            csv_yol = os.path.join(td, "zerre.csv")
            zerre_csv_yaz(csv_yol, r)
            self.assertTrue(os.path.exists(csv_yol))
            with open(csv_yol, "r", encoding="utf-8") as f:
                satirlar = f.readlines()
                self.assertGreaterEqual(len(satirlar), 6)  # başlık + 5 durak


if __name__ == "__main__":
    unittest.main()
