import asyncio
import os
import telegram
from dotenv import load_dotenv
import openai

load_dotenv()

# telegram
BOT_TOKEN = os.environ['BOT_TOKEN']

# openai
openai.organization = "org-xAfG7yH1ydHAjgbRGCeSFfrO"
openai.api_key = os.environ['OPENAI_API_KEY']
MODEL = "text-davinci-003"

async def main():
    bot = telegram.Bot(BOT_TOKEN)
    async with bot:
        await bot.send_message(text="Hi me!", chat_id=766116213)


if __name__ == '__main__':
    asyncio.run(main())
