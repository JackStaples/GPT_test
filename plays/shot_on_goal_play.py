from plays.play import Play

class ShotOnGoalPlay(Play):
    def __init__(self, play, game_info):
        super().__init__(play, game_info)
        self.shooting_player = game_info.get_player_name(play['details'].get('shootingPlayerId'))
        self.goalie_player = game_info.get_player_name(play['details'].get('goalieInNetId'))
        
        self.shooting_player_id = play['details'].get('shootingPlayerId')
        self.goalie_player_id = play['details'].get('goalieInNetId')

    def __str__(self):
        if (self.goalie_player == None):
            return (
                f"Shot on Goal - Period: {self.period}, Time: {self.time_in_period}, "
                f"Shooting Player: {self.shooting_player}"
            )
        return (
            f"Shot on Goal - Period: {self.period}, Time: {self.time_in_period}, "
            f"Shooting Player: {self.shooting_player}, Goalie: {self.goalie_player}"
        )
    
    def get_involved_player_ids(self):
        return [self.shooting_player_id, self.goalie_player_id]