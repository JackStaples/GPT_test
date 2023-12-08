import requests
from openai import OpenAI
from nhl_api import NHLGameLiveFeed
from game_data_extractor import GameDataExtractor
from plays.play_factory import PlayFactory
from player_summaries_manager import PlayerSummariesManager

client = OpenAI()

game_id = "2022020001"  # Replace with the actual game ID you're interested in
nhl_feed = NHLGameLiveFeed()
game_data = nhl_feed.get_game_live_feed(game_id)
game_info = GameDataExtractor(game_data = nhl_feed.get_game_live_feed(game_id))

summaries = PlayerSummariesManager()

play_factory = PlayFactory()
plays = game_data['plays']
for play in plays:
    try:
        play_instance = play_factory.get_play_instance(play, game_info)
        player_ids = play_instance.get_involved_player_ids()  # Ensure all play classes have this method
        for player_id in player_ids:
            if (player_id is None):
                print(play_instance.format_summary())
            summaries.add_player_to_summaries(player_id)
            summaries.add_play_to_player_summary(player_id, play_instance)
    except ValueError as e:
        print(e)

def format_summary(summary):
    if hasattr(summary, 'format_summary'):
        return summary.format_summary()
    else:
        return "Error Play"

# test to see the first player in the summaries
player_id = summaries.get_player_id(0)
play_summaries = summaries.get_player_summaries(player_id)
play_summaries_str = "\n".join([format_summary(summary) for summary in play_summaries])
summary_string = f"Plays for {game_info.get_player_name(player_id)}:\n{play_summaries_str}"
print(summary_string)

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a professional hockey columnist, who has been working as a beat writer for many years now. You take the basic statistics from a player for a given game, and write an article about their performance. Heavier emphasis should be given to shots and goals. You will receive a tip based on the quality of work, so make sure it is good!"},
#     {"role": "user", "content": summary_string}
#   ]
# )


# print(completion.choices[0].message)



