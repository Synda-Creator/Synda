import tweepy
import json
import os
from datetime import datetime
from time import sleep
from logger import setup_logger

# Initialize the logger
logger = setup_logger("engagement_manager")


class EngagementManager:
    def __init__(self, api_keys_file, engagement_log_file, state_file):
        self.engagement_log_file = engagement_log_file
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

    def log_engagement(self, engagement):
        """Log the engagement details."""
        with open(self.engagement_log_file, 'a') as f:
            f.write(json.dumps(engagement, indent=4) + '\n')
        logger.info(f"Logged engagement: {engagement}")

    def fetch_tweets(self, query, max_tweets=10):
        """Fetch tweets based on a search query."""
        tweets = tweepy.Cursor(self.api.search_tweets, q=query, since=self.last_checked).items(max_tweets)
        tweets = list(tweets)
        logger.info(f"Fetched {len(tweets)} tweets with query: {query}.")
        return tweets

    def like_tweet(self, tweet):
        """Like a tweet."""
        self.api.create_favorite(tweet.id)
        engagement = {
            "tweet_id": tweet.id,
            "tweet_text": tweet.text,
            "action": "liked",
            "timestamp": datetime.now().isoformat()
        }
        self.log_engagement(engagement)
        logger.info(f"Liked tweet ID: {tweet.id}")

    def retweet_tweet(self, tweet):
        """Retweet a tweet."""
        self.api.retweet(tweet.id)
        engagement = {
            "tweet_id": tweet.id,
            "tweet_text": tweet.text,
            "action": "retweeted",
            "timestamp": datetime.now().isoformat()
        }
        self.log_engagement(engagement)
        logger.info(f"Retweeted tweet ID: {tweet.id}")

    def engage_with_tweets(self, query):
        """Fetch and engage (like and retweet) with tweets based on a query."""
        tweets = self.fetch_tweets(query)
        for tweet in tweets:
            self.like_tweet(tweet)
            self.retweet_tweet(tweet)
        if tweets:
            self.last_checked = max(tweet.created_at for tweet in tweets)
            self.save_state()

    def start(self, query, interval=60):
        """Start the engagement loop based on the query."""
        while True:
            self.engage_with_tweets(query)
            sleep(interval)


if __name__ == "__main__":
    agent = EngagementManager("api_keys.json", "engagement_log.json", "state.json")
    agent.start(query="AI twitter bot", interval=600)  # Adjust the query and interval as needed
