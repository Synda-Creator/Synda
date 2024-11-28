# synda/ai_brain.py
import random
import re

def generate_tweet():
    tweets = [
        "Just finished a 5K run. Feeling accomplished! 🏃‍♂️💪 #fitness #motivation",
        "Can't believe it's already Friday! This week flew by. Any fun weekend plans? 🎉",
        "New coffee shop opened downtown. Their latte art is Instagram-worthy! ☕📸 #coffeelover",
        "Binge-watching Stranger Things. No spoilers please! 🤐📺 #StrangerThings",
        "Work from home life: Forgot I was on mute for half the meeting. 🤦‍♂️ #WFHfail",
        "Just adopted the cutest puppy! Say hello to Max! 🐶❤️ #newpuppy",
        "Climate change is real. We need to act now. 🌍 #ClimateAction",
        "Who else is excited for the new Spider-Man movie? 🕷️🎬 #SpiderMan",
        "Trying to learn Spanish. Duolingo owl is judging me hard. 🦉😅 #languagelearning",
        "First attempt at homemade sushi. It's... abstract. 🍣😂 #cookingfail"
    ]
    return random.choice(tweets)

def generate_response(tweet):
    # Extract hashtags
    hashtags = re.findall(r'#\w+', tweet)
    
    responses = {
        "fitness": [
            "That's awesome! 💪 How do you stay motivated?",
            "5K is no joke! What's your next fitness goal?",
            "Nothing beats that post-run feeling, right? 🏃‍♂️"
        ],
        "coffeelover": [
            "Ooh, I'm always on the hunt for good coffee spots! What's your go-to order?",
            "Coffee art is seriously impressive. Ever tried making it yourself?",
            "A good latte can turn any day around! ☕"
        ],
        "StrangerThings": [
            "No spoilers here! 🤐 Which season are you on?",
            "I'm so hooked on that show! Who's your favorite character?",
            "The suspense is killing me! Let me know what you think when you're done!"
        ],
        "WFHfail": [
            "Haha, classic WFH moment! 😂 At least it wasn't something more embarrassing!",
            "We've all been there! What's your favorite thing about working from home?",
            "Mute button: best friend and worst enemy of remote workers everywhere 😅"
        ],
        "newpuppy": [
            "Aww, congrats on the new family member! 🐶 We need puppy pics ASAP!",
            "Max is such a cute name! How's the house training going?",
            "Puppies are the best! Prepare for lots of chewed shoes though 😂"
        ],
        "ClimateAction": [
            "Couldn't agree more. Have you tried any lifestyle changes to reduce your carbon footprint?",
            "It's great to see people speaking up about this! What do you think is the most urgent action needed?",
            "Absolutely. Every small action counts. What's your go-to eco-friendly habit?"
        ],
        "SpiderMan": [
            "Can't wait! 🕷️ Who's your favorite Spider-Man actor so far?",
            "The trailers look amazing! Are you Team Tobey, Andrew, or Tom?",
            "Spider-Man never disappoints! Are you going to a midnight showing?"
        ],
        "languagelearning": [
            "Haha, that Duolingo owl is relentless! 🦉 What made you choose Spanish?",
            "Learning a new language is tough but so rewarding! Any tips to share?",
            "Buena suerte! (Did I use that right? 😅) What's been the hardest part so far?"
        ],
        "cookingfail": [
            "Hey, abstract sushi could be the next big thing! 😂 What went wrong?",
            "Cooking fails make the best stories! At least it's edible... right? 😅",
            "Practice makes perfect! What's your favorite successful dish to make?"
        ]
    }

    # Check for hashtags and generate appropriate response
    for tag in hashtags:
        tag = tag[1:].lower()  # Remove '#' and convert to lowercase
        if tag in responses:
            return random.choice(responses[tag])

    # If no matching hashtags, use these general responses
    general_responses = [
        "That's interesting! Tell me more about it.",
        "Wow, sounds like you've had quite a day!",
        "I can totally relate to that. How are you feeling about it?",
        "That's cool! What inspired you to share that?",
        "I'm curious, what's the story behind this?",
        "Haha, that made me smile. Thanks for sharing!",
        "Oh really? I'd love to hear more details!",
        "That's quite something! How often does this happen?",
        "Interesting perspective! What made you think of this?",
        "I see where you're coming from. Any particular reason for bringing this up now?"
    ]
    return random.choice(general_responses)
