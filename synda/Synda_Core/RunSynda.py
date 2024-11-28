# synda/main.py
import tweepy
import time
import os
import sys
import random
from dotenv import load_dotenv
from threading import Thread

# Adjust path if script is being run directly
if __name__ == "__main__" and __package__ is None:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    __package__ = "synda"

from synda.ai_functions import generate_response, analyze_sentiment
from synda.logger import setup_logger

# Load environment variables
load_dotenv()

logger = setup_logger("Synda")

# Twitter API credentials
CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def print_letter_by_letter(text, delay_range=(0.01, 0.05)):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(*delay_range))
    print()  # New line at the end

def authenticate_to_twitter():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def display_startup_effect():
    print("\n" * 2)
    startup_messages = [
        "Initializing Synda...",
        "Loading AI modules...",
        "Connecting to Twitter API...",
        "Calibrating response algorithms...",
        "Warming up tweet generator...",
        "Activating sentiment analysis..."
    ]
    
    for message in startup_messages:
        print_letter_by_letter(message)
        time.sleep(0.5)
    
    print_letter_by_letter("\nStartup complete!")
    time.sleep(1)
    print("\n" * 2)

class SyndaStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        super().__init__()
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet from @{tweet.user.screen_name}")
        
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        
        Thread(target=self.process_tweet, args=(tweet,)).start()

    def process_tweet(self, tweet):
        try:
            if not tweet.favorited:
                # Mark it as Liked, since we have not done it yet
                tweet.favorite()

            print_letter_by_letter(f"Incoming tweet from @{tweet.user.screen_name}: {tweet.text}")
            
            sentiment = analyze_sentiment(tweet.text)
            print_letter_by_letter(f"Sentiment analysis: {sentiment}")

            response = generate_response(tweet.text, sentiment)
            print_letter_by_letter(f"AI response: {response}")
            
            if response:
                self.api.update_status(
                    status=f"@{tweet.user.screen_name} {response}",
                    in_reply_to_status_id=tweet.id,
                )
                logger.info(f"Replied to @{tweet.user.screen_name}")

            print("\n" + "-"*50 + "\n")

        except tweepy.TweepError as e:
            logger.error(f"Twitter API error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")

    def on_error(self, status):
        if status == 420:
            logger.error("Rate limit exceeded. Waiting for 15 minutes.")
            time.sleep(15 * 60)
            return True
        else:
            logger.error(f"Stream error: {status}")
            return False

def main():
    display_startup_effect()

    # Authenticate to Twitter API
    api = authenticate_to_twitter()
    logger.info("✅ Authenticated to Twitter API")
    print_letter_by_letter("🚀 Synda is now online and ready to interact! 🌐")
    time.sleep(1)
    print()  # Add an extra newline for spacing

    # Create Stream listener
    tweets_listener = SyndaStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)

    try:
        print_letter_by_letter("🎧 Starting to listen for tweets...")
        stream.filter(track=["@YourTwitterHandle"], languages=["en"])
    except KeyboardInterrupt:
        print_letter_by_letter("\nShutting down Synda. Goodbye!")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print_letter_by_letter("An error occurred. Please check the logs.")

if __name__ == "__main__":
    main()
