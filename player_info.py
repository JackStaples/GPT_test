from datetime import datetime

class PlayerInfo:
    def __init__(self, player_stats):
        """
        Initializes a PlayerInfo object with personal details of a player.

        Args:
            player_stats (dict): A dictionary containing player statistics.
        """
        self.name = player_stats['firstName']['default'] + " " + player_stats['lastName']['default']
        self.team = player_stats['fullTeamName']['default']
        self.position = player_stats['position']
        self.birth_country = player_stats['birthCountry']
        self.birth_city = player_stats['birthCity']['default']
        self.birth_date = datetime.strptime(player_stats['birthDate'], "%Y-%m-%d")
        self.age = (datetime.now() - self.birth_date).days // 365
        self.height = f"{player_stats['heightInInches']} inches"
        self.weight = f"{player_stats['weightInPounds']} lbs"
        self.draft_round = player_stats['draftDetails']['round']
        self.draft_pick = player_stats['draftDetails']['overallPick']

    def __str__(self):
        """
        Returns a readable string representation of the player's information.
        """
        return (f"Name: {self.name}, Team: {self.team}, Position: {self.position}, "
                f"Birth Country: {self.birth_country}, Birth City: {self.birth_city}, Age: {self.age} years, "
                f"Height: {self.height}, Weight: {self.weight}, Draft Round: {self.draft_round}, "
                f"Draft Pick: {self.draft_pick}")

    def __repr__(self):
        """
        Returns an unambiguous string representation of the player's information.
        """
        return (f"PlayerInfo(name='{self.name}', team='{self.team}', position='{self.position}', "
                f"birth_country='{self.birth_country}', birth_city='{self.birth_city}', "
                f"birth_date='{self.birth_date.strftime('%Y-%m-%d')}', age={self.age}, "
                f"height='{self.height}', weight='{self.weight}', draft_round={self.draft_round}, "
                f"draft_pick={self.draft_pick})")
