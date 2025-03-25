import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_konstruktori_asettaa_rahat_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_konstruktori_asettaa_myynnit_oikein(self):
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 0)

    def test_syo_edullisesti_kateisella(self):
        testi = self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(testi, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_ei_tarpeeksi_rahaa(self):
        testi = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(testi, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella(self):
        testi = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(testi, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_ei_tarpeeksi_rahaa(self):
        testi = self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(testi, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_syo_edullisesti_kortilla(self):
        testi = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertTrue(testi)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_ei_tarpeeksi_saldoa(self):
        kortti = Maksukortti(200)
        testi = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertFalse(testi)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla(self):
        testi = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        
        self.assertTrue(testi)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_ei_tarpeeksi_saldoa(self):
        kortti = Maksukortti(300)
        testi = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        
        self.assertFalse(testi)
        self.assertEqual(kortti.saldo, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortille_lataaminen_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortille_lataaminen_negatiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_rahaa_euroina_toimii_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)