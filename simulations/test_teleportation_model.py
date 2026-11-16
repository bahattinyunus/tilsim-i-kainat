#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tayy-ı Mekân ve Kuantum Işınlanma Modeli Birim Testleri
"""

import os
import tempfile
import unittest
from importlib.machinery import SourceFileLoader

dosya_yolu = os.path.join(os.path.dirname(__file__), "teleportation-information-model.py")
teleport_modulu = SourceFileLoader("teleportation_information_model", dosya_yolu).load_module()

CisimOzellikleri = teleport_modulu.CisimOzellikleri
TeleportasyonSimulasyonu = teleport_modulu.TeleportasyonSimulasyonu
rapor_olustur = teleport_modulu.rapor_olustur
main = teleport_modulu.main


class TeleportasyonModelTestleri(unittest.TestCase):

    def test_parametre_dogrulama(self):
        with self.assertRaises(ValueError):
            c = CisimOzellikleri(kutle_kg=-10.0)
            c.dogrula()

        with self.assertRaises(ValueError):
            c = CisimOzellikleri(yaricap_m=0.0)
            c.dogrula()

        with self.assertRaises(ValueError):
            c = CisimOzellikleri(nuraniyet_derecesi=1.5)
            c.dogrula()

        with self.assertRaises(ValueError):
            sim = TeleportasyonSimulasyonu(CisimOzellikleri(), mesafe_km=-100.0)

    def test_bekenstein_ve_enerji_esdegerligi(self):
        c = CisimOzellikleri(kutle_kg=100.0, yaricap_m=1.0)
        self.assertGreater(c.enerji_esdegeri_joule, 0)
        self.assertGreater(c.bekenstein_bilgi_siniri_bit, 1e40)
        self.assertGreater(c.atomik_bilgi_tahmini_bit, 1e28)

    def test_klasik_nakil_saatler_alır(self):
        c = CisimOzellikleri(kutle_kg=500.0)
        sim = TeleportasyonSimulasyonu(c, mesafe_km=2500.0)
        sonuc = sim.hesapla_klasik_nakil(hiz_km_h=900.0)
        # 2500 km / 900 km/h ~ 2.77 saat ~ 10,000 saniye
        self.assertGreater(sonuc.sure_saniye, 9000.0)
        self.assertEqual(sonuc.sadakat_orani, 1.0)
        self.assertEqual(sonuc.eylemsizlik_hissi_g, 1.0)

    def test_kuantum_rekonstruksiyon_isik_hizinda(self):
        c = CisimOzellikleri(kutle_kg=500.0)
        sim = TeleportasyonSimulasyonu(c, mesafe_km=2500.0)
        sonuc = sim.hesapla_kuantum_rekonstruksiyon()
        # Işık süresi: 2500 km / 300,000 km/s ~ 0.0083 sn. İşlem süresiyle birlikte < 2 sn olmalı
        self.assertLess(sonuc.sure_saniye, 2.0)
        self.assertGreater(sonuc.sure_saniye, 0.005)
        self.assertGreaterEqual(sonuc.sadakat_orani, 0.99)
        self.assertEqual(sonuc.eylemsizlik_hissi_g, 0.0)

    def test_tayy_i_mekan_anlik_tarfetu_l_ayn(self):
        c = CisimOzellikleri(kutle_kg=500.0, nuraniyet_derecesi=0.999)
        sim = TeleportasyonSimulasyonu(c, mesafe_km=2500.0)
        sonuc = sim.hesapla_tayy_i_mekan_nuraniyet()
        # Göz açıp kapama süresi (< 0.1 saniye)
        self.assertLessEqual(sonuc.sure_saniye, 0.1)
        self.assertEqual(sonuc.eylemsizlik_hissi_g, 0.0)
        self.assertEqual(sonuc.sadakat_orani, 1.0)

    def test_tum_modlari_karsilastir_listesi(self):
        c = CisimOzellikleri()
        sim = TeleportasyonSimulasyonu(c, mesafe_km=1000.0)
        sonuclar = sim.tum_modlari_karsilastir()
        self.assertEqual(len(sonuclar), 3)

    def test_rapor_olusturma_ve_cli(self):
        c = CisimOzellikleri(ad="Test Cisim", kutle_kg=50.0)
        rapor = rapor_olustur(c, 500.0)
        self.assertIn("TAYY-I MEKÂN VE KUANTUM IŞINLANMA", rapor)
        self.assertIn("Test Cisim", rapor)

        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tf:
            gecici_csv = tf.name

        try:
            kod = main(["--kutle", "100", "--mesafe", "1200", "--csv", gecici_csv])
            self.assertEqual(kod, 0)
            self.assertTrue(os.path.exists(gecici_csv))
            self.assertGreater(os.path.getsize(gecici_csv), 50)
        finally:
            if os.path.exists(gecici_csv):
                os.remove(gecici_csv)


if __name__ == "__main__":
    unittest.main()
