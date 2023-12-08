class Player:
    def __init__(self, player_stats):
        """
        Initializes a Player object with all player-related data.

        Args:
            player_stats (dict): A dictionary containing player statistics.
        """
        self.info = PlayerInfo(player_stats)
        self.current_season_stats = CurrentSeasonStats(player_stats)
        self.career_stats = CareerStats(player_stats)

    def __str__(self):
        """
        Returns a readable string representation of the player's complete information and statistics.
        """
        return (f"{self.info}\n{self.current_season_stats}\n{self.career_stats}")

    def __repr__(self):
        """
        Returns an unambiguous string representation of the Player object.
        """
        return (f"Player(info={repr(self.info)}, current_season_stats={repr(self.current_season_stats)}, "
                f"career_stats={repr(self.career_stats)})")
