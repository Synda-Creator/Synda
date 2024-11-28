# synda/config.py
import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        
        self.TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
        self.TWITTER_CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
        self.TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
        self.TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        self.TWITTER_HANDLE = os.getenv("TWITTER_HANDLE")
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def load_config():
    return Config()
