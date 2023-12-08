class ShotOnGoalPlay:
    def __init__(self, play, game_info):
        self.period = play.get('period')
        self.time_in_period = play.get('timeInPeriod')
        self.shooting_player = game_info.get_player_name(play['details'].get('shootingPlayerId'))
        self.goalie_player = game_info.get_player_name(play['details'].get('goalieInNetId'))
        
        self.shooting_player_id = play['details'].get('shootingPlayerId')
        self.goalie_player_id = play['details'].get('goalieInNetId')

    def format_summary(self):
        if (self.goalie_player == None):
            return (
                f"Shot on Goal - Period: {self.period}, Time: {self.time_in_period}, "
                f"Shooting Player: {self.shooting_player}"
            )
        return (
            f"Shot on Goal - Period: {self.period}, Time: {self.time_in_period}, "
            f"Shooting Player: {self.shooting_player}, Goalie: {self.goalie_player}"
        )
    
    def get_shooting_player_id(self):
        return self.shooting_player_id
    
    def get_goalie_player_id(self):
        return self.goalie_player_id

    def get_involved_player_ids(self):
        return [self.shooting_player_id, self.goalie_player_id]