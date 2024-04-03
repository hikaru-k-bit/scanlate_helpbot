import os

import aiomysql
from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.environ.get("TOKEN"))


async def connect():
    """
    :return: None
    """
    pool = await aiomysql.create_pool(
        host=os.environ.get("HOST"),
        port=3306,
        user=os.environ.get("USER"),
        password=os.environ.get("PASSWORD"),
        db=os.environ.get("DATABASE"),
        autocommit=True  # Ensure autocommit is enabled for aiomysql
    )
    return pool
