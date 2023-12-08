from plays.play import Play

class GiveawayPlay(Play):
    def __init__(self, play, game_info):
        super().__init__(play, game_info)
        self.giveaway_player_id = play['details'].get('playerId')
        self.giveaway_player = game_info.get_player_name(self.giveaway_player_id)

    def __str__(self):
        return (f"Giveaway - Period: {self.period}, Time: {self.time_in_period}, "
                f"Player: {self.giveaway_player}")

    def __repr__(self):
        return (f"GiveawayPlay({super().__repr__()}, giveaway_player='{self.giveaway_player}')")

    def get_involved_player_ids(self):
        return [self.giveaway_player_id]
