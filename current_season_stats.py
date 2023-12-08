class CurrentSeasonStats:
    def __init__(self, player_stats):
        """
        Initializes a CurrentSeasonStats object with statistics of a player for the current season.

        Args:
            player_stats (dict): A dictionary containing player statistics.
        """
        season_stats = player_stats['featuredStats']['regularSeason']['subSeason']
        self.games_played = season_stats['gamesPlayed']
        self.goals = season_stats['goals']
        self.assists = season_stats['assists']
        self.points = season_stats['points']
        self.plus_minus = season_stats['plusMinus']
        self.shots = season_stats['shots']
        self.shooting_pctg = season_stats['shootingPctg']
        self.pim = season_stats['pim']  # Penalties in minutes

    def __str__(self):
        """
        Returns a readable string representation of the player's current season statistics.
        """
        return (f"Current Season Stats: Games Played: {self.games_played}, Goals: {self.goals}, "
                f"Assists: {self.assists}, Points: {self.points}, Plus/Minus: {self.plus_minus}, "
                f"Shots: {self.shots}, Shooting Percentage: {self.shooting_pctg}, PIM: {self.pim}")

    def __repr__(self):
        """
        Returns an unambiguous string representation of the player's current season statistics.
        """
        return (f"CurrentSeasonStats(games_played={self.games_played}, goals={self.goals}, "
                f"assists={self.assists}, points={self.points}, plus_minus={self.plus_minus}, "
                f"shots={self.shots}, shooting_pctg={self.shooting_pctg}, pim={self.pim})")
