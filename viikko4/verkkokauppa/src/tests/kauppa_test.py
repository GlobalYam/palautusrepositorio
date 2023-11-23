import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0


        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "muro", 5)
            if tuote_id == 3:
                return Tuote(3, "haarukka", 50000)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostos(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        nimi = "pekka"
        viitenumero = 42
        tililta = "12345"
        tilille = "33333-44455"
        summa = 5


        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(nimi, viitenumero, tililta, tilille, summa)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostos_kaksi_eri_tuotetta(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        nimi = "pekka"
        viitenumero = 42
        tililta = "12345"
        tilille = "33333-44455"
        summa = 10


        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(nimi, viitenumero, tililta, tilille, summa)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostos_kaksi_samaa_tuotetta(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        nimi = "pekka"
        viitenumero = 42
        tililta = "12345"
        tilille = "33333-44455"
        summa = 10


        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(nimi, viitenumero, tililta, tilille, summa)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_ostos_yksi_puuttuu(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        nimi = "pekka"
        viitenumero = 42
        tililta = "12345"
        tilille = "33333-44455"
        summa = 5


        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(nimi, viitenumero, tililta, tilille, summa)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_ostos_poistetaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("pekka", "12345")

        nimi = "pekka"
        viitenumero = 42
        tililta = "12345"
        tilille = "33333-44455"
        summa = 5


        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(nimi, viitenumero, tililta, tilille, summa)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_aloita_asiointi(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pena", "12345")
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        nimi = "pekka"
        viitenumero = 42
        tililta = "12345"
        tilille = "33333-44455"
        summa = 5


        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(nimi, viitenumero, tililta, tilille, summa)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_pyydetaan_uusi_viite_jokaiseen_maksuun(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pena", "12345")
        # tarkistetaan että tässä vaiheessa viitegeneraattorin metodia uusi on kutsuttu kerran
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pena", "12345")

        # tarkistetaan että tässä vaiheessa viitegeneraattorin metodia uusi on kutsuttu kaksi kertaa
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)