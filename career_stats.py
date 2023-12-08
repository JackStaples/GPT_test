class CareerStats:
    def __init__(self, player_stats):
        """
        Initializes a CareerStats object with the career statistics of a player.

        Args:
            player_stats (dict): A dictionary containing player statistics.
        """
        career_stats = player_stats['featuredStats']['regularSeason']['career']
        self.games_played = career_stats['gamesPlayed']
        self.goals = career_stats['goals']
        self.assists = career_stats['assists']
        self.points = career_stats['points']
        self.plus_minus = career_stats['plusMinus']
        self.shots = career_stats['shots']
        self.shooting_pctg = career_stats['shootingPctg']
        self.pim = career_stats['pim']  # Penalties in minutes

    def __str__(self):
        """
        Returns a readable string representation of the player's career statistics.
        """
        return (f"Career Stats: Games Played: {self.games_played}, Goals: {self.goals}, "
                f"Assists: {self.assists}, Points: {self.points}, Plus/Minus: {self.plus_minus}, "
                f"Shots: {self.shots}, Shooting Percentage: {self.shooting_pctg}, PIM: {self.pim}")

    def __repr__(self):
        """
        Returns an unambiguous string representation of the player's career statistics.
        """
        return (f"CareerStats(games_played={self.games_played}, goals={self.goals}, "
                f"assists={self.assists}, points={self.points}, plus_minus={self.plus_minus}, "
                f"shots={self.shots}, shooting_pctg={self.shooting_pctg}, pim={self.pim})")
