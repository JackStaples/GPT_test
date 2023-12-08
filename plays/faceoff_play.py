class FaceoffPlay:
    def __init__(self, play, game_info):
        self.period = play.get('period')
        self.time_in_period = play.get('timeInPeriod')
        self.winning_player = game_info.get_player_name(play['details'].get('winningPlayerId'))
        self.losing_player = game_info.get_player_name(play['details'].get('losingPlayerId'))
        
        self.winning_player_id = play['details'].get('winningPlayerId')
        self.losing_player_id = play['details'].get('losingPlayerId')

    def format_summary(self):
        return (
            f"Faceoff - Period: {self.period}, Time: {self.time_in_period}, "
            f"Winning Player: {self.winning_player}, Losing Player: {self.losing_player}"
        )
    
    def get_winning_player_id(self):
        return self.winning_player_id
    
    def get_losing_player_id(self):
        return self.losing_player_id
    
    def get_involved_player_ids(self):
        return [self.winning_player_id, self.losing_player_id]