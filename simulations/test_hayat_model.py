#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hayat, Şuur ve Bütünleşik Bilgi (IIT Φ) Modeli Birim Testleri
"""

import os
import tempfile
import unittest
import importlib.util

dosya_yolu = os.path.join(os.path.dirname(__file__), "hayat-suur-model.py")
spec = importlib.util.spec_from_file_location("hayat_suur_model", dosya_yolu)
hayat_modulu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hayat_modulu)

HayatParametreleri = hayat_modulu.HayatParametreleri
hesapla_hayat_durumu = hayat_modulu.hesapla_hayat_durumu
calistir_senaryo = hayat_modulu.calistir_senaryo
tum_senaryolari_karsilastir = hayat_modulu.tum_senaryolari_karsilastir
csv_yaz = hayat_modulu.csv_yaz
SENARYOLAR = hayat_modulu.SENARYOLAR


class HayatModelTestleri(unittest.TestCase):

    def test_parametre_dogrulama(self):
        with self.assertRaises(ValueError):
            p = HayatParametreleri(
                zerre_sayisi=0,
                vahdet_rabitasi=0.5,
                alem_i_emir_irtibati=0.5,
                suur_derecesi=0.5,
                ene_miftahi=0.5,
                negentropi_pompasi=0.5
            )
            hesapla_hayat_durumu(p)

        with self.assertRaises(ValueError):
            p = HayatParametreleri(
                zerre_sayisi=100,
                vahdet_rabitasi=1.5,
                alem_i_emir_irtibati=0.5,
                suur_derecesi=0.5,
                ene_miftahi=0.5,
                negentropi_pompasi=0.5
            )
            hesapla_hayat_durumu(p)

    def test_insani_ruh_en_yuksek_phi_ve_ebediyet(self):
        cikti = calistir_senaryo("insani_ruh")
        self.assertGreater(cikti.phi_butunlesik_bilgi, 80.0)
        self.assertEqual(cikti.ebediyet_kabiliyeti, 1.0)
        self.assertGreater(cikti.negentropi_orani, 0.90)
        self.assertGreater(cikti.kulliyet_indisi, 0.90)
        self.assertIn("Ahsen-i Takvîm", cikti.durum_etiketi)

    def test_yapay_zeka_zombi_phi_sifirdir(self):
        # Milyarlarca parametre olsa bile harici vücutlu ruh ve şuursuzlukta Φ sıfıra çöker
        cikti = calistir_senaryo("yapay_zeka_zombi")
        self.assertEqual(cikti.phi_butunlesik_bilgi, 0.0)
        self.assertEqual(cikti.ebediyet_kabiliyeti, 0.0)
        self.assertIn("Felsefî Zombi", cikti.durum_etiketi)

    def test_camid_madde_entropik(self):
        cikti = calistir_senaryo("camid_madde")
        self.assertEqual(cikti.phi_butunlesik_bilgi, 0.0)
        self.assertEqual(cikti.negentropi_orani, 0.0)
        self.assertEqual(cikti.ebediyet_kabiliyeti, 0.0)

    def test_vefat_ve_tecerrud_ruhun_basitligi(self):
        # Beden dağılıp zerre=1 kalsa bile ruh basit olduğu için ebediyeti tamdır
        cikti = calistir_senaryo("vefat_ve_tecerrud")
        self.assertEqual(cikti.ebediyet_kabiliyeti, 1.0)
        self.assertIn("Berzah", cikti.durum_etiketi)

    def test_tum_senaryolar(self):
        sonuclar = tum_senaryolari_karsilastir()
        self.assertEqual(len(sonuclar), 6)
        for ad, res in sonuclar.items():
            self.assertIsNotNone(res.durum_etiketi)
            self.assertIsNotNone(res.izahat)

    def test_csv_yazma(self):
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
            gecici_yol = tmp.name
        try:
            csv_yaz(gecici_yol)
            self.assertTrue(os.path.exists(gecici_yol))
            with open(gecici_yol, "r", encoding="utf-8") as f:
                satirlar = f.readlines()
            self.assertGreater(len(satirlar), 6)
        finally:
            if os.path.exists(gecici_yol):
                os.remove(gecici_yol)


if __name__ == "__main__":
    unittest.main()
