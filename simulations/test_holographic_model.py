#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Holografik Âlem-i Misâl, Ehadiyet ve Aynalar Modeli (16. Söz & AdS/CFT) Birim Testleri
"""

import os
import tempfile
import unittest
import importlib.util

dosya_yolu = os.path.join(os.path.dirname(__file__), "holographic-ayine-model.py")
spec = importlib.util.spec_from_file_location("holographic_ayine_model", dosya_yolu)
holo_modulu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(holo_modulu)

HolografiParametreleri = holo_modulu.HolografiParametreleri
hesapla_holografi_durumu = holo_modulu.hesapla_holografi_durumu
calistir_senaryo = holo_modulu.calistir_senaryo
tum_senaryolari_karsilastir = holo_modulu.tum_senaryolari_karsilastir
csv_yaz = holo_modulu.csv_yaz


class HolografiModelTestleri(unittest.TestCase):

    def test_parametre_dogrulama(self):
        with self.assertRaises(ValueError):
            hesapla_holografi_durumu(HolografiParametreleri(1.5, 5.0, 0.5, 5.0))
        with self.assertRaises(ValueError):
            hesapla_holografi_durumu(HolografiParametreleri(0.5, 35.0, 0.5, 5.0))
        with self.assertRaises(ValueError):
            hesapla_holografi_durumu(HolografiParametreleri(0.5, 5.0, -0.2, 5.0))
        with self.assertRaises(ValueError):
            hesapla_holografi_durumu(HolografiParametreleri(0.5, 5.0, 0.5, 25.0))

    def test_ehadiyet_ayna_sayisindan_ve_mesafeden_bagimsizdir(self):
        tek_ayna = hesapla_holografi_durumu(HolografiParametreleri(0.95, 0.0, 0.95, 1.0))
        trilyon_ayna_uzak = hesapla_holografi_durumu(HolografiParametreleri(0.95, 24.0, 0.95, 18.0))
        self.assertEqual(tek_ayna.ehadiyet_tecellisi, trilyon_ayna_uzak.ehadiyet_tecellisi)
        self.assertEqual(tek_ayna.kaynak_bolunme_kaybi, 0.0)
        self.assertEqual(trilyon_ayna_uzak.kaynak_bolunme_kaybi, 0.0)

    def test_kalb_i_selim_en_yuksek_tecelli(self):
        c = calistir_senaryo("kalb_i_selim_ehadiyet")
        self.assertGreater(c.ehadiyet_tecellisi, 95.0)
        self.assertGreater(c.kurb_etkinligi, 95.0)
        self.assertGreater(c.holografik_sadakat, 95.0)
        self.assertIn("Ehadiyet", c.ontolojik_mertebe)

    def test_kirik_maddeci_ayna_karanlik(self):
        c = calistir_senaryo("kirik_maddeci_ayna")
        self.assertLess(c.ehadiyet_tecellisi, 10.0)
        self.assertLess(c.holografik_sadakat, 15.0)
        self.assertIn("Kırık Ayna", c.ontolojik_mertebe)

    def test_vahidiyet_kapasitesi_ayna_sayisiyla_artar(self):
        okyanus = calistir_senaryo("okyanus_vahidiyet")
        katreler = calistir_senaryo("katre_aynasi_holografi")
        self.assertGreater(katreler.vahidiyet_kapasitesi_log10, okyanus.vahidiyet_kapasitesi_log10 + 10.0)

    def test_tum_senaryolar(self):
        sonuclar = tum_senaryolari_karsilastir()
        self.assertEqual(len(sonuclar), 5)
        for _, res in sonuclar.items():
            self.assertIsNotNone(res.ontolojik_mertebe)
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
