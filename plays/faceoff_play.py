from plays.play import Play

class FaceoffPlay(Play):
    def __init__(self, play, game_info):
        super().__init__(play, game_info)
        self.winning_player = game_info.get_player_name(play['details'].get('winningPlayerId'))
        self.losing_player = game_info.get_player_name(play['details'].get('losingPlayerId'))
        self.winning_player_id = play['details'].get('winningPlayerId')
        self.losing_player_id = play['details'].get('losingPlayerId')

    def __str__(self):
        return (
            f"Faceoff - Period: {self.period}, Time: {self.time_in_period}, "
            f"Winning Player: {self.winning_player}, Losing Player: {self.losing_player}"
        )
    
    def __repr__(self):
        return (f"FaceoffPlay({super().__repr__()}, winning_player='{self.winning_player}', losing_player='{self.winning_player}')")
    
    def get_involved_player_ids(self):
        return [self.winning_player_id, self.losing_player_id]