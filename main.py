import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
import config as cf
from handlers import router

bot = Bot(token=cf.TOKEN)

dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())