import unittest

from player import Player
from playerstats import PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player({
                "name": "Semenko",
                "nationality": "CAN",
                "team": "EDM",
                "goals": 4,
                "assists": 12,
            }),
            Player({
                "name": "Lemieux",
                "nationality": "CAN",
                "team": "PIT",
                "goals": 45,
                "assists": 54,
            }),
            Player({
                "name": "Kurri",
                "nationality": "FIN",
                "team": "EDM",
                "goals": 37,
                "assists": 53,
            }),
            Player({
                "name": "Yzerman",
                "nationality": "CAN",
                "team": "DET",
                "goals": 42,
                "assists": 56,
            }),
            Player({
                "name": "Gretzky",
                "nationality": "CAN",
                "team": "EDM",
                "goals": 35,
                "assists": 89,
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        players = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman", "Semenko"],
        )

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        players = self.stats.top_scorers_by_team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Kurri", "Semenko"],
        )

    def test_top_goal_scorers_returns_requested_number_in_descending_order(self):
        players = self.stats.top_goal_scorers(3)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman", "Kurri"],
        )

    def test_top_goal_scorers_returns_all_players_when_requested_number_is_large(self):
        players = self.stats.top_goal_scorers(10)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman", "Kurri", "Gretzky", "Semenko"],
        )


if __name__ == "__main__":
    unittest.main()
