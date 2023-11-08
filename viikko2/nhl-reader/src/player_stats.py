

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nat: str):
        print(f"Players from {nat}:\n")

        players = self.reader.get_players()
        filtered_players = filter(lambda player: player.nationality == nat, players)
        sorted_players = sorted(filtered_players, key=lambda player: player.goals + player.assists, reverse=True)


        return sorted_players