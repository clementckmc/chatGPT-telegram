# chatGPT-telegram
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Overview
A Telegram chatbot built with Python, implementing chatGPT by applying [OpenAI API](https://platform.openai.com/docs/introduction).

## Getting Started

### Install python-telegram-bot
Install or upgrade [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library via
```
$ pip3 install python-telegram-bot --upgrade
```

### OpenAI API Setup
Get your own OpenAI API key from [OpenAI API](https://platform.openai.com/overview).

### Telegram Bot Setup
[Create a telegram bot](https://core.telegram.org/bots#how-do-i-create-a-bot) and [get your bot token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token).

### ENV setting
Create `.env` file.
```
$ touch .env
```
Inside `.env`, set the following variables with the api key and bot token from above.
```
BOT_TOKEN=your_own_bot_token
OPENAI_API_KEY=your_own_api_key
```
## Usage
### Run the bot
Start running the bot with the command below.
```
python3 main.py
```
Note: The default model used here is `chat-3.5-turbo` which is the chat completion model. If you wish to switch to text completion model (`text-davinci`), you can uncomment the code under `# completion model (text-davinci)` and comment out the code under `# chat completion (chat-3.5-turbo)`.
