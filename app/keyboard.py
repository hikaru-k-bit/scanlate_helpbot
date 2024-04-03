from aiogram import types
from aiogram.types import InlineKeyboardMarkup

from app.credentials import connect


def get_main_keyboard() -> InlineKeyboardMarkup:
    """
    :return: InlineKeyboardMarkup
    """
    buttons = [
        [types.InlineKeyboardButton(text="Заказчики", callback_data="clients"),
         types.InlineKeyboardButton(text="Проекты", callback_data="projects")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


async def get_clients_list() -> InlineKeyboardMarkup:
    """
    :return: InlineKeyboardMarkup
    """
    pool = await connect()
    async with pool.acquire() as connection:
        async with connection.cursor() as cursor:
            await cursor.execute("SELECT client_name FROM clients")
            clients = await cursor.fetchall()
            buttons = []

            for client in clients:
                client_name = client[0]
                callback_data = client_name.replace(" ", "_").lower()
                buttons.append([types.InlineKeyboardButton(text=client_name, callback_data=callback_data)])

            buttons.append([types.InlineKeyboardButton(text="<<<", callback_data="main_menu")])

            keyboard_markup = types.InlineKeyboardMarkup(inline_keyboard=buttons)
            return keyboard_markup


async def add_project_button() -> InlineKeyboardMarkup:
    """
    :return: InlineKeyboardMarkup
    """
    buttons = [
        [types.InlineKeyboardButton(text="Создать новый проект", callback_data="new_project")],
        [types.InlineKeyboardButton(text="<<<", callback_data="main_menu")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
