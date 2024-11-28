import tweepy
import json
import os
from datetime import datetime
from time import sleep
from logger import setup_logger

# Initialize the logger
logger = setup_logger("dm_manager")

class DMManager:
    def __init__(self, api_keys_file, dm_log_file, state_file):
        self.dm_log_file = dm_log_file
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
                self.last_checked_id = state.get('last_checked_id', None)
            logger.info("Loaded state from file.")
        else:
            self.last_checked_id = None
            logger.info("Initialized new state.")

    def save_state(self):
        """Save the current state to the state file."""
        state = {
            'last_checked_id': self.last_checked_id
        }
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=4)
        logger.info("Saved state to file.")

    def log_dm(self, dm):
        """Log the direct message details."""
        with open(self.dm_log_file, 'a') as f:
            f.write(json.dumps(dm, indent=4) + '\n')
        logger.info(f"Logged direct message: {dm}")

    def fetch_dms(self):
        """Fetch direct messages from Twitter."""
        if self.last_checked_id:
            dms = self.api.list_direct_messages(since_id=self.last_checked_id)
        else:
            dms = self.api.list_direct_messages()
        
        dms = dms[:10]  # Limit to latest 10 DMs to avoid API rate limits
        logger.info(f"Fetched {len(dms)} direct messages.")
        return dms

    def reply_to