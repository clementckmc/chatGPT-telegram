import asyncio
import os
import logging
import requests
from telegram import Update, Bot
from telegram.ext import MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, filters
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

def getResponse(prompt):
    response = requests.post(
        'https://api.openai.com/v1/completions',
        headers={'Authorization': 'Bearer ' + openai.api_key},
        json={'model': MODEL, 'prompt': prompt, 'max_tokens': 1024, 'temperature': 0.5 }  )
    print(response.json()['choices'][0]['text'])
    return response.json()['choices'][0]['text']

async def chatBot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    reply = getResponse(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), chatBot))

    application.run_polling()
