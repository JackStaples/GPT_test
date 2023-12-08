from plays.play import Play

class HitPlay(Play):
    def __init__(self, play, game_info):
        super().__init__(play, game_info)
        self.hitting_player = game_info.get_player_name(play['details'].get('hittingPlayerId'))
        self.hittee_player = game_info.get_player_name(play['details'].get('hitteePlayerId'))
        
        self.hitting_player_id = play['details'].get('hittingPlayerId')
        self.hittee_player_id = play['details'].get('hitteePlayerId')

    def __str__(self):
        return (
            f"Hit - Period: {self.period}, Time: {self.time_in_period}, "
            f"Hitting Player: {self.hitting_player}, Hit Player: {self.hittee_player}"
        )
    
    def __repr__(self):
        return (f"HitPlay({super().__repr__()}, hitting_player='{self.hitting_player}', hittee_player='{self.hittee_player})")

    def get_involved_player_ids(self):
        return [self.hitting_player_id, self.hittee_player_id]