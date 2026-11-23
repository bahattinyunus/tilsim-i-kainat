#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mânâ-yı Harfî, Niyet-Nazar ve İlişkisel Kuantum (RQM & ITP) Modeli Birim Testleri
"""

import os
import tempfile
import unittest
import importlib.util

dosya_yolu = os.path.join(os.path.dirname(__file__), "nazar-rqm-model.py")
spec = importlib.util.spec_from_file_location("nazar_rqm_model", dosya_yolu)
nazar_modulu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nazar_modulu)

NazarParametreleri = nazar_modulu.NazarParametreleri
hesapla_nazar_durumu = nazar_modulu.hesapla_nazar_durumu
calistir_senaryo = nazar_modulu.calistir_senaryo
tum_senaryolari_karsilastir = nazar_modulu.tum_senaryolari_karsilastir
csv_yaz = nazar_modulu.csv_yaz


class NazarModelTestleri(unittest.TestCase):

    def test_parametre_dogrulama(self):
        with self.assertRaises(ValueError):
            hesapla_nazar_durumu(NazarParametreleri(1.2, 0.5, 0.5, 0.5))
        with self.assertRaises(ValueError):
            hesapla_nazar_durumu(NazarParametreleri(0.5, -0.1, 0.5, 0.5))
        with self.assertRaises(ValueError):
            hesapla_nazar_durumu(NazarParametreleri(0.5, 0.5, 1.5, 0.5))
        with self.assertRaises(ValueError):
            hesapla_nazar_durumu(NazarParametreleri(0.5, 0.5, 0.5, -0.05))

    def test_mana_yi_harfi_velayet_en_yuksek_berraklik(self):
        c = calistir_senaryo("mana_yi_harfi_velayet")
        self.assertGreater(c.epistemik_berraklik, 90.0)
        self.assertGreater(c.ibadet_simyasi_carpani, 75.0)
        self.assertGreater(c.iliskisel_anlam_biti, 8.0)
        self.assertLess(c.arayuz_yanilsamasi, 5.0)
        self.assertIn("Mânâ-yı Harfî", c.hakikat_mertebesi)

    def test_materyalist_arayuz_yanilsamasi_yuksek(self):
        c = calistir_senaryo("materyalist_arayuz_yanilsamasi")
        self.assertLess(c.epistemik_berraklik, 5.0)
        self.assertLess(c.ibadet_simyasi_carpani, 1.0)
        self.assertGreater(c.arayuz_yanilsamasi, 90.0)
        self.assertIn("Yanılsama", c.hakikat_mertebesi)

    def test_niyet_simyasi_monoton_artar(self):
        dusuk_niyet = hesapla_nazar_durumu(NazarParametreleri(0.9, 0.1, 0.8, 0.8))
        yuksek_niyet = hesapla_nazar_durumu(NazarParametreleri(0.9, 0.95, 0.8, 0.8))
        self.assertGreater(yuksek_niyet.ibadet_simyasi_carpani, dusuk_niyet.ibadet_simyasi_carpani * 5)

    def test_harfi_nazar_rqm_bilgisini_artirir(self):
        ismi = calistir_senaryo("mana_yi_ismi_gaflet")
        harfi = calistir_senaryo("tefekkur_ve_niyet")
        self.assertGreater(harfi.iliskisel_anlam_biti, ismi.iliskisel_anlam_biti * 5)
        self.assertGreater(harfi.epistemik_berraklik, ismi.epistemik_berraklik)

    def test_tum_senaryolar(self):
        sonuclar = tum_senaryolari_karsilastir()
        self.assertEqual(len(sonuclar), 5)
        for _, res in sonuclar.items():
            self.assertIsNotNone(res.hakikat_mertebesi)
            self.assertIsNotNone(res.hukum)

    def test_csv_yazma(self):
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
            gecici_yol = tmp.name
        try:
            csv_yaz(gecici_yol)
            self.assertTrue(os.path.exists(gecici_yol))
            with open(gecici_yol, "r", encoding="utf-8") as f:
                satirlar = f.readlines()
            self.assertEqual(len(satirlar), 6)
        finally:
            if os.path.exists(gecici_yol):
                os.remove(gecici_yol)


if __name__ == "__main__":
    unittest.main()
