# -*- coding: utf-8 -*-
"""Ene kalınlaşma modeli için birim testleri.

Çalıştırma:  python -m unittest discover -s simulations -p "test_*.py"
"""

import importlib.util
import os
import sys
import tempfile
import unittest
from dataclasses import replace

_YOL = os.path.join(os.path.dirname(__file__), "ene-thickening-model.py")
_spec = importlib.util.spec_from_file_location("ene_model", _YOL)
m = importlib.util.module_from_spec(_spec)
sys.modules["ene_model"] = m  # dataclass'ların modülü bulabilmesi için
_spec.loader.exec_module(m)  # type: ignore[union-attr]


class ModelTestleri(unittest.TestCase):
    def test_degerler_sinirli(self):
        for ad in m.SENARYOLAR:
            r = m.simule_et(m.senaryo_parametreleri(ad))
            self.assertTrue(all(0.0 <= k <= 1.0 for k in r.K), ad)
            self.assertTrue(all(0.0 <= h <= 1.0 for h in r.H), ad)

    def test_firavun_yutulur(self):
        r = m.simule_et(m.senaryo_parametreleri("firavun"))
        self.assertIsNotNone(r.yutulma_zamani)
        self.assertGreater(r.son_K, 0.9)

    def test_salik_seffaf_kalir(self):
        r = m.simule_et(m.senaryo_parametreleri("salik"))
        self.assertIsNone(r.firavuniyet_zamani)
        self.assertLess(r.son_K, 0.15)

    def test_tevbe_kalinligi_azaltir(self):
        p = m.senaryo_parametreleri("tevbe")
        r = m.simule_et(p)
        self.assertLess(r.son_K, p.K0)

    def test_esbabperest_tefekkur_inceltmez(self):
        """Aynı tefekkür, esbabperest nazarla yapılınca daha az tasfiye eder."""
        harfi = m.Parametreler(tefekkur=0.9, inkar=0.0)
        ismi = m.Parametreler(tefekkur=0.9, inkar=0.9)
        self.assertGreater(harfi.tasfiye, ismi.tasfiye)
        r = m.simule_et(m.senaryo_parametreleri("filozof"))
        self.assertGreater(r.son_K, 0.75)

    def test_gaflet_monoton(self):
        """Gaflet arttıkça nihai kalınlık azalmamalıdır."""
        onceki = -1.0
        for g in (0.0, 0.25, 0.5, 0.75, 1.0):
            p = replace(m.senaryo_parametreleri("gafil"), gaflet=g)
            k = m.simule_et(p).son_K
            self.assertGreaterEqual(k + 1e-9, onceki)
            onceki = k

    def test_gecersiz_parametre(self):
        with self.assertRaises(ValueError):
            m.simule_et(m.Parametreler(gaflet=1.5))

    def test_mertebe(self):
        self.assertEqual(m.mertebe(0.0)[0], "Hava gibi şeffaf")
        self.assertEqual(m.mertebe(0.95)[0], "Yutulma")

    def test_cli_ve_csv(self):
        with tempfile.TemporaryDirectory() as d:
            yol = os.path.join(d, "out.csv")
            self.assertEqual(m.main(["-s", "gafil", "--sessiz", "--csv", yol]), 0)
            with open(yol, encoding="utf-8") as f:
                satirlar = f.read().strip().splitlines()
            self.assertEqual(satirlar[0], "t,kalinlik,seffafiyet,harfi_nazar")
            self.assertGreater(len(satirlar), 10)
        self.assertEqual(m.main(["--karsilastir"]), 0)
        self.assertEqual(m.main(["--listele"]), 0)


if __name__ == "__main__":
    unittest.main()
