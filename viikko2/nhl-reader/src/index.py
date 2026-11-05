from rich.table import Table
from rich import print as rprint
from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
    create_table(players)

def create_table(players):
    table = Table(title="Top Scorers by Nationality")
    table.add_column("Released", justify="right", style="cyan", no_wrap=True)
    table.add_column("teams", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")
    for player in players:
        table.add_row(player.name, player.team, str(player.goals),
                      str(player.assists), str(player.total))

    rprint(table)

if __name__ == "__main__":
    main()
