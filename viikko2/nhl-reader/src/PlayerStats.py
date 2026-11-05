# pylint: disable=too-few-public-methods
class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        nationality_players = [player for player in self._players
                               if player.nationality == nationality]
        nationality_players.sort(key=lambda x: x.total, reverse=True)
        return nationality_players
