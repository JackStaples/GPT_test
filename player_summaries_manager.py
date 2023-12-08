class PlayerSummariesManager:
    def __init__(self):
        self.player_summaries = {}  # Dictionary to store player summaries

    def add_player_to_summaries(self, player_id):
        if player_id not in self.player_summaries:
            self.player_summaries[player_id] = []

    def add_play_to_player_summary(self, player_id, play_instance):
        if player_id in self.player_summaries:
            self.player_summaries[player_id].append(play_instance)
            
    def get_player_id(self, index):
        return list(self.player_summaries.keys())[index]
                                      
    def get_player_summaries(self, player_id):
        if player_id in self.player_summaries:
            return self.player_summaries[player_id]
        else:
            return []