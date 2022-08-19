import asyncio
from aiogram import Bot

BOT_TOKEN = "5495057823:AAEbWCZmMwYZeGsBzans-lKevrSyulp63t8"


async def main():
    bot = Bot(token=BOT_TOKEN)
    try:
        me = await bot.get_me()
        print(f"🤖 Hello, I'm {me.first_name}.\nHave a nice Day!")
    finally:
        await bot.close()


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())


