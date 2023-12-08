class GiveawayPlay:
    def __init__(self, play, game_info):
        self.period = play.get('period')
        self.time_in_period = play.get('timeInPeriod')
        self.giveaway_player = game_info.get_player_name(play['details'].get('playerId'))
        
        self.giveaway_player_id = play['details'].get('playerId')

    def format_summary(self):
        return (
            f"Giveaway - Period: {self.period}, Time: {self.time_in_period}, "
            f"Player: {self.giveaway_player}"
        )
    
    def get_giveaway_player_id(self):
        return self.giveaway_player_id

    def get_involved_player_ids(self):
        return [self.giveaway_player_id]