class BlockedShotPlay:
    def __init__(self, play, game_info):
        self.period = play.get('period')
        self.time_in_period = play.get('timeInPeriod')
        self.shooting_player = game_info.get_player_name(play['details'].get('shootingPlayerId'))
        self.blocking_player = game_info.get_player_name(play['details'].get('blockingPlayerId'))
        
        self.shooting_player_id = play['details'].get('shootingPlayerId')
        self.blocking_player_id = play['details'].get('blockingPlayerId')

    def format_summary(self):
        return (
            f"Blocked Shot - Period: {self.period}, Time: {self.time_in_period}, "
            f"Shooting Player: {self.shooting_player}, Blocking Player: {self.blocking_player}"
        )
    
    def get_shooting_player_id(self):
        return self.shooting_player_id
    
    def get_blocking_player_id(self):
        return self.blocking_player_id
    
    def get_involved_player_ids(self):
        return [self.shooting_player_id, self.blocking_player_id]
