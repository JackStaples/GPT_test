class GameDataExtractor:
    def __init__(self, game_data):
        self.game_data = game_data
        self.teams = {}
        self.players = {}
        
        self.extract_teams()
        self.extract_players()

    def extract_teams(self):
        if 'awayTeam' in self.game_data and 'homeTeam' in self.game_data:
            away_team_id = self.game_data['awayTeam']['id']
            home_team_id = self.game_data['homeTeam']['id']
            self.teams[away_team_id] = self.game_data['awayTeam']
            self.teams[home_team_id] = self.game_data['homeTeam']
        else:
            raise ValueError("Team data not found in game_data.")

    def extract_players(self):
        if 'rosterSpots' in self.game_data:
            for player_spot in self.game_data['rosterSpots']:
                player_id = player_spot['playerId']
                self.players[player_id] = player_spot
        else:
            raise ValueError("Player roster data not found in game_data.")

    def get_player_name(self, player_id):
        player = self.players.get(player_id)
        if player:
            first_name = player.get('firstName', {}).get('default', 'Unknown')
            last_name = player.get('lastName', {}).get('default', 'Unknown')
            return f"{first_name} {last_name}"
        else:
            return None

    def get_team(self, team_id):
        return self.teams.get(team_id, {'name': 'Unknown Team'})
