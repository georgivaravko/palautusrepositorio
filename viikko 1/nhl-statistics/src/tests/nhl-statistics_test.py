import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_statistics_service_luodaan_oikei(self):
        pelaaja = self.stats.search("Lemieux")

        self.assertEqual(pelaaja.name, "Lemieux")

    def test_vaara_nimi(self):
        pelaaja = self.stats.search("vaara")
        
        self.assertEqual(pelaaja, None)

    def test_oikea_pelaaja_ja_oikea_joukkue(self):
        players = self.stats.team("PIT")

        self.assertEqual(players[0].name, "Lemieux")

    def test_jarjestaa_pisteiden_mukaan(self):
        sorted_by_points = self.stats.top(1)
        print(sorted_by_points)

        self.assertEqual(sorted_by_points[0].name, "Gretzky")

# main funktio on jätetty testaamatta, koska se vaatisi nettiyhteyden