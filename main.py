import os
import logging
import requests
from telegram import Update
from telegram.ext import MessageHandler, ApplicationBuilder, ContextTypes, filters
from dotenv import load_dotenv
import openai

load_dotenv()

# telegram
BOT_TOKEN = os.environ['BOT_TOKEN']

# openai
openai.organization = "org-xAfG7yH1ydHAjgbRGCeSFfrO"
openai.api_key = os.environ['OPENAI_API_KEY']

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# completion model (text-davinci)
# def getResponse(prompt):
#     response = requests.post(
#         'https://api.openai.com/v1/completions',
#         headers={'Authorization': 'Bearer ' + openai.api_key},
#         json={'model': "text-davinci-002", 'prompt': prompt, 'max_tokens': 512, 'temperature': 0.5 }  )
#     reply = response.json()['choices'][0]['text']
#     print("AI: "+ reply)
#     return reply

# chat completion (chat-3.5-turbo)
def getResponse(prompt):
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={'Authorization': 'Bearer ' + openai.api_key},
        json={'model': "gpt-3.5-turbo", 'messages': [{'role': 'user', 'content': prompt}], 'max_tokens': 512, 'temperature': 0.5 }  )
    reply = response.json()['choices'][0]['message']['content']
    print("AI: "+ reply)
    return reply

async def chatBot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("User: " + update.message.text)
    reply = getResponse(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), chatBot))

    application.run_polling()
