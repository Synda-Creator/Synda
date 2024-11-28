# synda/ai_functions.py
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(tweet_text):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Generate a friendly and engaging response to this tweet: '{tweet_text}'\nResponse:",
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in generating AI response: {e}")
        return None
