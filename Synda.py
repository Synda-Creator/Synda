import tweepy
import json
import os
from datetime import datetime
from time import sleep
from logger import setup_logger

# Initialize the logger
logger = setup_logger("agent_ayla")


class AgentAyla:
    def __init__(self, api_keys_file, interactions_log_file, state_file):
        self.interactions_log_file = interactions_log_file
        self.state_file = state_file
        self.api = self.authenticate(api_keys_file)
        self.load_state()

    def authenticate(self, api_keys_file):
        """Authenticate to Twitter API using provided keys."""
        with open(api_keys_file, 'r') as f:
            keys = json.load(f)

        auth = tweepy.OAuth1UserHandler(
            keys["API_KEY"], keys["API_SECRET_KEY"],
            keys["ACCESS_TOKEN"], keys["ACCESS_TOKEN_SECRET"]
        )
        api = tweepy.API(auth)
        logger.info("Authenticated with Twitter API.")
        return api

    def load_state(self):
        """Load the state from the state file or initialize state variables."""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                state = json.load(f)
                self.last_checked = state.get('last_checked', datetime.now().isoformat())
            logger.info("Loaded state from file.")
        else:
            self.last_checked = datetime.now().isoformat()
            logger.info("Initialized new state.")

        self.last_checked = datetime.fromisoformat(self.last_checked)

    def save_state(self):
        """Save the current state to the state file."""
        state = {
            'last_checked': self.last_checked.isoformat()
        }
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=4)
        logger.info("Saved state to file.")

    def log_interaction(self, interaction):
        """Log the interaction details."""
        with open(self.interactions_log_file, 'a') as f:
            f.write(json.dumps(interaction, indent=4) + '\n')
        logger.info(f"Logged interaction: {interaction}")

    def fetch_mentions(self):
        """Fetch mentions from Twitter."""
        tweets = self.api.mentions_timeline(since_id=self.last_checked)
        logger.info(f"Fetched {len(tweets)} mentions since {self.last_checked}.")
        return tweets

    def respond_to_tweet(self, tweet, response):
        """Respond to a tweet."""
        self.api.update_status(
            status=response,
            in_reply_to_status_id=tweet.id,
            auto_populate_reply_metadata=True
        )
        interaction = {
            "tweet_id": tweet.id,
            "tweet_text": tweet.text,
            "response": response,
            "timestamp": datetime.now().isoformat()
        }
        self.log_interaction(interaction)
        logger.info(f"Responded to tweet ID: {tweet.id}")

    def process_mentions(self):
        """Fetches mentions and responds to them."""
        mentions = self.fetch_mentions()
        for tweet in mentions:
            response = self.generate_response(tweet)  # Implement this method to tailor interactions
            self.respond_to_tweet(tweet, response)
        if mentions:
            self.last_checked = max(mention.created_at for mention in mentions)
            self.save_state()

    def generate_response(self, tweet):
        """Generate a response to a tweet. Customize this to make more human-like interactions."""
        # Placeholder implementation
        return f"Thank you for your tweet, @{tweet.user.screen_name}!"

    def start(self):
        """Start the Agent Ayla interaction loop."""
        while True:
            self.process_mentions()
            sleep(60)  # Poll every minute


if __name__ == "__main__":
    agent = AgentAyla("api_keys.json", "interactions_log.json", "state.json")
    agent.start()
