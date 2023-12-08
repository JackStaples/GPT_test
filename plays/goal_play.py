class GoalPlay:
    def __init__(self, play, game_info):
        self.period = play.get('period')
        self.time_in_period = play.get('timeInPeriod')
        self.scoring_team = game_info.get_team(play['details'].get('eventOwnerTeamId')).get('abbrev', 'Unknown Team')
        self.scoring_player = game_info.get_player_name(play['details'].get('scoringPlayerId'))
        self.goalie = game_info.get_player_name(play['details'].get('goalieInNetId'))
        self.home_score = play['details'].get('homeScore')
        self.away_score = play['details'].get('awayScore')
        self.shot_type = play['details'].get('shotType')
        self.assist1_player = self.get_assist_player(play['details'].get('assist1PlayerId'), game_info)
        self.assist2_player = self.get_assist_player(play['details'].get('assist2PlayerId'), game_info)
        
        self.playerid = play['details'].get('scoringPlayerId')
        self.assist1_playerid = play['details'].get('assist1PlayerId')
        self.assist2_playerid = play['details'].get('assist2PlayerId')

    def get_assist_player(self, player_id, game_info):
        return game_info.get_player_name(player_id) if player_id else None

    def getPlayerId(self):
        return self.playerid

    def format_summary(self):
        summary_str = (
            "Goal - "
            f"Period: {self.period}, Time: {self.time_in_period}, "
            f"Scoring Team: {self.scoring_team}, Scoring Player: {self.scoring_player}, "
            f"Home Score: {self.home_score}, Away Score: {self.away_score}, "
            f"Shot Type: {self.shot_type}"
        )
        if self.assist1_player:
            summary_str += f", Assist 1 Player: {self.assist1_player}"
        if self.assist2_player:
            summary_str += f", Assist 2 Player: {self.assist2_player}"
        if self.goalie:
            summary_str += f", Goalie: {self.goalie}"
        else:
            summary_str += ", Goalie: Empty Net"
        return summary_str

    def get_involved_player_ids(self):
        player_ids = [self.playerid]
        if self.assist1_playerid:
            player_ids.append(self.assist1_playerid)
        if self.assist2_playerid:
            player_ids.append(self.assist2_playerid)
        return player_ids