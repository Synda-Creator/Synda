import tweepy
import json
import os
from datetime import datetime
from time import sleep
from textblob import TextBlob
from logger import setup_logger

# Initialize the logger
logger = setup_logger("sentiment_manager")

class SentimentManager:
    def __init__(self, api_keys_file, sentiment_log_file, state_file):
        self.sentiment_log_file = sentiment_log_file
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

    def log_sentiment(self, tweet, sentiment):
        """Log the sentiment analysis details."""
        log_entry = {
            "tweet_id": tweet.id,
            "tweet_text": tweet.text,
            "sentiment": sentiment,
            "timestamp": datetime.now().isoformat()
        }
        with open(self.sentiment_log_file, 'a') as f:
            f.write(json.dumps(log_entry, indent=4) + '\n')
        logger.info(f"Logged sentiment analysis: {log_entry}")

    def fetch_tweets(self):
        """Fetch tweets mentioning the bot."""
        tweets = self.api.mentions_timeline(since_id=self.last_checked)
        logger.info(f"Fetched {len(tweets)} mentions since {self.last_checked}.")
        return tweets

    def analyze_sentiment(self, tweet):
        """Analyze the sentiment of a tweet using TextBlob."""
        analysis = TextBlob(tweet.text)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity
        sentiment = {
            "polarity": polarity,
            "subjectivity": subjectivity
        }
        self.log_sentiment(tweet, sentiment)
        return sentiment

    def respond_to_tweet(self, tweet, sentiment):
        """Generate a response based on the sentiment and reply to the tweet."""
        if sentiment["polarity"] > 0:
            response = f"Thank you for your positive message, @{tweet.user.screen_name}!"
        elif sentiment["polarity"] < 0:
            response = f"I'm sorry to hear that you feel this way, @{tweet.user.screen_name}. How can I help?"
        else:
            response = f"Thank you for your message, @{tweet.user.screen_name}!"
        
        self.api.update_status(
            status=response,
            in_reply_to_status_id=tweet.id,
            auto_populate_reply_metadata=True
        )
        logger.info(f"Responded to tweet ID: {tweet.id}")

    def process_tweets(self):
        """Fetch