class Play:
    def __init__(self, play, game_info):
        self.period = play.get('period')
        self.time_in_period = play.get('timeInPeriod')

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def get_involved_player_ids(self):
        raise NotImplementedError
