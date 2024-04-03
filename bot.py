import asyncio
import logging

from aiogram import Dispatcher

import app.states.projecting
from app.credentials import bot
from app.handlers import router

dp = Dispatcher()


async def main() -> None:
    """
    :return: None
    """
    dp.include_routers(router, app.states.projecting.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
