import asyncio
import os
import logging
import requests
from telegram import Update, Bot
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import openai

load_dotenv()

# telegram
BOT_TOKEN = os.environ['BOT_TOKEN']

# openai
openai.organization = "org-xAfG7yH1ydHAjgbRGCeSFfrO"
openai.api_key = os.environ['OPENAI_API_KEY']
MODEL = "text-davinci-003"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="This is chatGPT. You can ask me anything!")

def getResponse(prompt):
    response = requests.post(
        'https://api.openai.com/v1/completions',
        headers={'Authorization': "Bearer {openai.api_key}"},
        json={'model': MODEL, 'prompt': prompt, 'max_tokens': 128, 'temperature': 0.5 }  )

    return response.json()

def sendMessage(chat_id, message_id, message):
    data = {
        'chat_id': chat_id,
        'text': message,
        'reply_to_message_id': message_id
    }



if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)

    application.run_polling()
