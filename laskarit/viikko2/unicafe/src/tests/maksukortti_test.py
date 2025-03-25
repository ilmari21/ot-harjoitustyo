import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein_alussa(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(250)

        self.assertEqual(self.maksukortti.saldo_euroina(), 12.5)

    def test_ottaminen_toimii(self):
        testi = self.maksukortti.ota_rahaa(250)

        self.assertTrue(testi)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.5)

    def test_rahan_ottaminen_ei_toimi_jos_saldoa_ei_tarpeeksi(self):
        testi = self.maksukortti.ota_rahaa(1500)

        self.assertFalse(testi)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_saldo_euroissa_toimii_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")