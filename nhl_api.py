import requests
import logging

class NHLGameLiveFeed:
    """
    A class to encapsulate the functionality for retrieving live game data from the NHL API.
    """

    def __init__(self):
        # Initialize logging or any other configurations if needed
        logging.basicConfig(level=logging.INFO)

    def get_game_live_feed(self, game_id):
        """
        Retrieve live game data from the NHL API.

        Args:
            game_id (str): The game ID for which the live feed is requested.

        Returns:
            dict/str: JSON response with game data if successful, otherwise error message.
        """
        url = f"https://api-web.nhle.com/v1/gamecenter/{game_id}/play-by-play"
        logging.info(f"Requesting NHL API for game ID: {game_id}")

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            return f"HTTP error: {http_err}"
        except Exception as err:
            logging.error(f"Other error occurred: {err}")
            return f"Error: {err}"

    def get_player_statistics(self, player_id):
        """
        Retrieves detailed player statistics from the NHL API.

        This method makes a request to the NHL API for a specific player's statistics,
        providing a comprehensive overview of the player's performance and data.

        Args:
            player_id (str): The unique identifier for the player.

        Returns:
            dict: A dictionary containing the player's statistics if the request is successful.
            None: If the request fails or an error occurs.

        Exceptions:
            HTTPError: If an HTTP error occurs during the API request.
            Exception: For any other exceptions that might occur.
        """
        url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"
        print(url)
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()  # Parsing the response as JSON
        except requests.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            return None
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return None