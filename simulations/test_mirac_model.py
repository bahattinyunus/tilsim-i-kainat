#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mirac, Görelilik ve Tayy-ı Zaman Modeli Birim Testleri (31. Söz)
"""

import os
import tempfile
import unittest
import importlib.util

dosya_yolu = os.path.join(os.path.dirname(__file__), "mirac-relativity-model.py")
spec = importlib.util.spec_from_file_location("mirac_relativity_model", dosya_yolu)
mirac_modulu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mirac_modulu)

MiracParametreleri = mirac_modulu.MiracParametreleri
hesapla_mirac_durumu = mirac_modulu.hesapla_mirac_durumu
calistir_senaryo = mirac_modulu.calistir_senaryo
tum_senaryolari_karsilastir = mirac_modulu.tum_senaryolari_karsilastir
csv_yaz = mirac_modulu.csv_yaz
SENARYOLAR = mirac_modulu.SENARYOLAR


class MiracModelTestleri(unittest.TestCase):

    def test_parametre_dogrulama(self):
        with self.assertRaises(ValueError):
            # Beta >= 1.0 geçersizdir
            p = MiracParametreleri(
                hiz_orani_beta=1.0,
                letafet_derecesi=0.5,
                seyir_mertebesi=2,
                dunya_suresi_saniye=10.0
            )
            hesapla_mirac_durumu(p)

        with self.assertRaises(ValueError):
            # Letafet negatif olamaz
            p = MiracParametreleri(
                hiz_orani_beta=0.5,
                letafet_derecesi=-0.1,
                seyir_mertebesi=2,
                dunya_suresi_saniye=10.0
            )
            hesapla_mirac_durumu(p)

        with self.assertRaises(ValueError):
            # Seyir mertebesi 5 olamaz
            p = MiracParametreleri(
                hiz_orani_beta=0.5,
                letafet_derecesi=0.5,
                seyir_mertebesi=5,
                dunya_suresi_saniye=10.0
            )
            hesapla_mirac_durumu(p)

    def test_mirac_i_ahmedi_an_i_daim_ve_sifir_g(self):
        cikti = calistir_senaryo("mirac_i_ahmedi")
        self.assertEqual(cikti.tilsim_fethi_skoru, 100.0)
        self.assertEqual(cikti.hissedilen_g_kuvveti, 0.0)
        self.assertEqual(cikti.etkin_kutle_orani, 0.0)
        self.assertLess(cikti.yolcu_oz_zaman_saniye, 1e-10)
        self.assertIn("Kab-ı Kavseyn", cikti.ontolojik_mertebe)

    def test_klasik_roket_zaman_akisi_ayni(self):
        cikti = calistir_senaryo("klasik_roket_astronot")
        self.assertAlmostEqual(cikti.lorentz_gama, 1.0, places=3)
        self.assertLess(cikti.tilsim_fethi_skoru, 1.0)
        self.assertIn("Maddî Kesafet", cikti.ontolojik_mertebe)

    def test_foton_referans_cercevesi(self):
        cikti = calistir_senaryo("foton_referans_cercevesi")
        self.assertGreater(cikti.lorentz_gama, 20000.0)
        self.assertEqual(cikti.etkin_kutle_orani, 1.0)  # Letafet 0 olduğundan kütle direnci var

    def test_tum_senaryolar(self):
        sonuclar = tum_senaryolari_karsilastir()
        self.assertEqual(len(sonuclar), 5)
        for ad, res in sonuclar.items():
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
            self.assertGreater(len(satirlar), 5)
        finally:
            if os.path.exists(gecici_yol):
                os.remove(gecici_yol)


if __name__ == "__main__":
    unittest.main()
