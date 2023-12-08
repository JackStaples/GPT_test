class PenaltyPlay:
    def __init__(self, play, game_info):
        self.period = play.get('period')
        self.time_in_period = play.get('timeInPeriod')
        self.penalized_team = game_info.get_team(play['details'].get('eventOwnerTeamId')).get('abbrev', 'Unknown Team')
        self.penalized_player = game_info.get_player_name(play['details'].get('committedByPlayerId'))
        self.penalty_type = play['details'].get('descKey')
        self.penalty_duration = play['details'].get('duration')
        
        self.committedByPlayerId = play['details'].get('committedByPlayerId')
        self.drawnByPlayerId = play['details'].get('drawnByPlayerId')
        if (self.drawnByPlayerId != None):
            self.drawing_player = game_info.get_player_name(play['details'].get('drawnByPlayerId'))

    def format_summary(self):
        if (hasattr(self, 'drawing_player')):
            return (
                f"Penalty - Period: {self.period}, Time: {self.time_in_period}, "
                f"Penalized Team: {self.penalized_team}, Penalized Player: {self.penalized_player}, "
                f"Penalty Type: {self.penalty_type}, Penalty Duration: {self.penalty_duration} minutes, "
                f"Drawing Player: {self.drawing_player}"
            )
        return (
            f"Penalty - Period: {self.period}, Time: {self.time_in_period}, "
            f"Penalized Team: {self.penalized_team}, Penalized Player: {self.penalized_player}, "
            f"Penalty Type: {self.penalty_type}, Penalty Duration: {self.penalty_duration} minutes"
        )
        
    def getPlayerId(self):
        return self.playerid

    def get_involved_player_ids(self):
        player_ids = [self.committedByPlayerId]
        if self.drawnByPlayerId:
            player_ids.append(self.drawnByPlayerId)
        return player_ids