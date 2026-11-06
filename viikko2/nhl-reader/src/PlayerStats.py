# pylint: disable=too-few-public-methods
class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        nationality_players = [player for player in self._players
                               if player.nationality == nationality]
        nationality_players.sort(key=lambda x: x.total, reverse=True)
        return nationality_players

    def top_scorers_by_team(self, team):
        team_players = [player for player in self._players
                        if player.team == team]
        team_players.sort(key=lambda x: x.total, reverse=True)
        return team_players

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        maalimäärän mukaan laskevassa järjestyksessä"""
        self._players.sort(key=lambda x: x.goals, reverse=True)
        return self._players[:how_many]
