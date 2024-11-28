# synda/tweet_simulation.py
import time


def simulate_tweets():
    # Simulate incoming tweets with a delay to mimic real-world timing
    tweets = [
        {"id": 1, "user": {"screen_name": "user1"}, "text": "What a beautiful day!"},
        {"id": 2, "user": {"screen_name": "user2"}, "text": "I love programming."},
        {"id": 3, "user": {"screen_name": "user3"}, "text": "AI is the future!"},
        {"id": 4, "user": {"screen_name": "user4"}, "text": "Python is so versatile."},
        {"id": 5, "user": {"screen_name": "user5"}, "text": "Just finished a great book!"},
        {"id": 6, "user": {"screen_name": "user6"}, "text": "I am having a tough day, everything is going wrong!"}
    ]

    for tweet in tweets:
        yield tweet
        time.sleep(2)
