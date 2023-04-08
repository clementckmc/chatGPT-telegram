import asyncio
import os
import telegram
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ['BOT_TOKEN']

async def main():
    bot = telegram.Bot(BOT_TOKEN)
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())
