from plays.play import Play

class BlockedShotPlay(Play):
    def __init__(self, play, game_info):
        super().__init__(play, game_info)
        self.shooting_player = game_info.get_player_name(play['details'].get('shootingPlayerId'))
        self.blocking_player = game_info.get_player_name(play['details'].get('blockingPlayerId'))
        self.shooting_player_id = play['details'].get('shootingPlayerId')
        self.blocking_player_id = play['details'].get('blockingPlayerId')

    def __str__(self):
        return (f"Missed Shot - Period: {self.period}, Time: {self.time_in_period}, "
                f"Shooting Player: {self.shooting_player}, Reason: {self.reason}")

    def __repr__(self):
        return (f"MissedShotPlay({super().__repr__()}, shooting_player='{self.shooting_player}')")
    
    def get_involved_player_ids(self):
        return [self.shooting_player_id]