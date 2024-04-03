from aiogram import types, Router, F
from aiogram.filters.command import CommandStart

from app.credentials import bot
from app.helpers import is_projects
from app.keyboard import get_main_keyboard, get_clients_list, add_project_button

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await bot.send_message(
        chat_id=message.chat.id,
        text="Приветствую. Все мои возможности представлены в кнопках ниже.",
        reply_markup=get_main_keyboard(),
    )


@router.callback_query(F.data == "clients")
async def show_clients_list(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text("Ниже предоставлены заказчики. Нажмите на кнопку для продолжения")
    await callback.message.edit_reply_markup(inline_message_id=callback.inline_message_id,
                                             reply_markup=await get_clients_list())
    await callback.answer()


@router.callback_query(F.data == "projects")
async def show_projects_list(callback: types.CallbackQuery) -> None:
    if not await is_projects():
        await callback.message.edit_text(
            "На данный момент проекты отсутствуют. Нажмите кнопку ниже для начала работы.")
        await callback.message.edit_reply_markup(inline_message_id=callback.inline_message_id,
                                                 reply_markup=await add_project_button())
    await callback.answer()


@router.callback_query(F.data == "main_menu")
async def go_main_menu(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text("Приветствую. Все мои возможности представлены в кнопках ниже.")
    await callback.message.edit_reply_markup(inline_message_id=callback.inline_message_id,
                                             reply_markup=get_main_keyboard())
