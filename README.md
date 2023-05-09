# chatGPT-telegram

## Overview
A Telegram chatbot built with Python, implementing chatGPT by applying [OpenAI API](https://platform.openai.com/docs/introduction).

## Getting Started

### OpenAI API Setup
Get your own OpenAI API key from [OpenAI API](https://platform.openai.com/overview).

### Telegram Bot Setup
[Create a telegram bot](https://core.telegram.org/bots#how-do-i-create-a-bot) and [get your bot token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token).

### ENV setting
Create `.env` file.
```
touch .env
```
Inside `.env`, set the following variables with the api key and bot token from above.
```
BOT_TOKEN=your_own_bot_token
OPENAI_API_KEY=your_own_api_key
```

### Run the bot
Start running the bot with the command below.
```
python3 main.py
```
