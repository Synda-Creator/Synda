# synda/ai_functions.py
import openai
from config import load_config

config = load_config()
openai.api_key = config.OPENAI_API_KEY

def generate_response(tweet_text, sentiment):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Generate a friendly and engaging response to this tweet: '{tweet_text}'\nThe sentiment is {sentiment}.\nResponse:",
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in generating AI response: {e}")
        return None
