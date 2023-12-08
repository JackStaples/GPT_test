from plays.goal_play import GoalPlay
from plays.penalty_play import PenaltyPlay
from plays.faceoff_play import FaceoffPlay
from plays.hit_play import HitPlay
from plays.shot_on_goal_play import ShotOnGoalPlay
from plays.missed_shot_play import MissedShotPlay
from plays.blocked_shot_play import BlockedShotPlay
from plays.giveaway_play import GiveawayPlay

class PlayFactory:
    def __init__(self):
        self.play_class_map = {
            "goal": GoalPlay,
            "penalty": PenaltyPlay,
            "faceoff": FaceoffPlay,
            "hit": HitPlay,
            "shot-on-goal": ShotOnGoalPlay,
            "missed-shot": MissedShotPlay,
            "blocked-shot": BlockedShotPlay,
            "giveaway": GiveawayPlay
        }

    def get_play_instance(self, play_data, game_info):
        play_type = play_data.get('typeDescKey')
        play_class = self.play_class_map.get(play_type)
        if play_class:
            return play_class(play_data, game_info)
        else:
            raise ValueError(f"No class defined for play type: {play_type}")