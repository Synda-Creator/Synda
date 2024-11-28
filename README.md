# Synda: AI-Powered Twitter Interaction Bot

## [Visit Twitter Page](https://x.com/SyndaAI_)

## Concept

Synda is an AI-powered Twitter bot designed to engage with users in real-time conversations. It uses natural language processing to understand incoming tweets and generate contextually appropriate responses. The bot aims to provide a seamless and intelligent interaction experience, simulating human-like conversations on Twitter.

## Project Structure

The project consists of a single main Python file (main.py) that handles all the functionality, including Twitter API interaction, AI response generation, and AI management.

## Key Components

1. Twitter API Integration: Uses the Tweepy library to connect to the Twitter API, listen for mentions, and post responses.

2. OpenAI GPT-3 Integration: Leverages the OpenAI API to generate contextually relevant responses to tweets.

3. Logging: Utilizes Python's logging module to keep track of the bot's activities and any errors that occur.

## Features

- Real-time monitoring of Twitter mentions
- AI-powered response generation using OpenAI's GPT-3
- Contextual understanding of incoming tweets
- Automatic liking of mentions
- Letter-by-letter display of tweets and responses for a more engaging console output
- Logging of all interactions
- Graceful error handling and shutdown

## Setup and Installation

1. Clone the repository or create a new Python file named main.py.
2. Install required dependencies:
3. Create a .env file in the same directory as main.py with the following content:
4. Replace "@YourTwitterHandle" in main.py with your actual Twitter handle.
5. Ensure you have set up a Twitter Developer account and have the necessary API keys and tokens.
6. Set up an OpenAI account and obtain an API key.

## Usage

To run the bot, execute the following command in your terminal:

Once running, Synda will:
1. Display a startup animation
2. Connect to the Twitter API
3. Listen for mentions of your specified Twitter handle
4. Like incoming tweets
5. Generate AI responses using OpenAI's GPT-3
6. Reply to the tweets with the generated responses

## Configuration

The bot's behavior can be customized by modifying the following in main.py:
- Modify the `track` parameter in `stream.filter()` to listen for different keywords
- Adjust the OpenAI API parameters in the `generate_response` function to fine-tune response generation

## Disclaimer

This bot is for educational purposes only. Ensure compliance with Twitter's and OpenAI's terms of service when deploying or modifying this bot. Be mindful of rate limits and usage guidelines for both APIs.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions to Synda are welcome! Feel free to submit issues, feature requests, or pull requests to help improve the bot's functionality.

## Support

If you encounter any problems or have questions about setting up or using Synda, please open an issue in the project repository.

Remember to always keep your API keys and tokens secure and never share them publicly. Happy bot building!
