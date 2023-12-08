class HitPlay:
    def __init__(self, play, game_info):
        self.period = play.get('period')
        self.time_in_period = play.get('timeInPeriod')
        self.hitting_player = game_info.get_player_name(play['details'].get('hittingPlayerId'))
        self.hittee_player = game_info.get_player_name(play['details'].get('hitteePlayerId'))
        
        self.hitting_player_id = play['details'].get('hittingPlayerId')
        self.hittee_player_id = play['details'].get('hitteePlayerId')

    def format_summary(self):
        return (
            f"Hit - Period: {self.period}, Time: {self.time_in_period}, "
            f"Hitting Player: {self.hitting_player}, Hit Player: {self.hittee_player}"
        )
    
    def get_hitting_player_id(self):
        return self.hitting_player_id
    
    def get_hittee_player_id(self):
        return self.hittee_player_id

    def get_involved_player_ids(self):
        return [self.hitting_player_id, self.hittee_player_id]