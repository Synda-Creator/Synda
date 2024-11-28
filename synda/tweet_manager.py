import json
import os
from datetime import datetime
from logger import setup_logger

# Initialize the logger
logger = setup_logger("tweet_manager")


class TweetManager:
    def __init__(self, tweet_queue_file, tweet_log_file, state_file):
        self.tweet_queue_file = tweet_queue_file
        self.tweet_log_file = tweet_log_file
        self.state_file = state_file
        self.load_state()

    def load_state(self):
        """Load the state from the state file or initialize state variables."""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                state = json.load(f)
                self.tweet_queue = state.get('tweet_queue', [])
                self.posted_tweets = state.get('posted_tweets', [])
            logger.info("Loaded state from file.")
        else:
            self.tweet_queue = []
            self.posted_tweets = []
            logger.info("Initialized new state.")

    def save_state(self):
        """Save the current state to the state file."""
        state = {
            'tweet_queue': self.tweet_queue,
            'posted_tweets': self.posted_tweets
        }
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=4)
        logger.info("Saved state to file.")

    def add_tweet(self, tweet):
        """Add a new tweet to the queue."""
        self.tweet_queue.append(tweet)
        self.save_to_file(self.tweet_queue_file, self.tweet_queue)
        logger.info(f"Added new tweet to queue: {tweet}")

    def post_tweet(self):
        """Simulate posting a tweet by removing it from the queue and logging it."""
        if not self.tweet_queue:
            logger.warning("No tweets to post.")
            return None

        tweet = self.tweet_queue.pop(0)
        timestamp = datetime.now().isoformat()
        log_entry = {"tweet": tweet, "timestamp": timestamp}
        self.posted_tweets.append(log_entry)
        self.save_to_file(self.tweet_log_file, self.posted_tweets)
        self.save_state()
        logger.info(f"Posted tweet: {tweet}")
        return tweet

    def save_to_file(self, file_path, data):
        """Write data to a JSON file."""
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Saved data to {file_path}")

    def load_tweets_from_file(self):
        """Load tweets from queue file."""
        if os.path.exists(self.tweet_queue_file):
            with open(self.tweet_queue_file, 'r') as f:
                self.tweet_queue = json.load(f)
            logger.info("Loaded tweets from queue file.")
        else:
            logger.warning(f"{self.tweet_queue_file} does not exist.")

    def load_posted_tweets_from_file(self):
        """Load posted tweets from log file."""
        if os.path.exists(self.tweet_log_file):
            with open(self.tweet_log_file, 'r') as f:
                self.posted_tweets = json.load(f)
            logger.info("Loaded posted tweets from log file.")
        else:
            logger.warning(f"{self.tweet_log_file} does not exist.")
