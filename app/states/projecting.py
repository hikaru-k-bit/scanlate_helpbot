from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.credentials import bot

router = Router()


class Projecting(StatesGroup):
    project_name = State()
    price_per_chapter = State()
    any_chapters_completed = State()
    isCompletedOnesForTheSamePrice = State()
    ChaptersCompleted = State()


@router.callback_query(F.data == "new_project")
async def project_creation_interface_start(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    :param callback:
    :param state:
    :return: None
    """
    await bot.send_message(chat_id=callback.message.chat.id, text="Как называется проект, над которым вы работаете?")
    await state.set_state(Projecting.project_name)
    await callback.answer()


@router.message(Projecting.project_name)
async def catch_project_name(message: types.Message, state: FSMContext) -> None:
    """
    :param message:
    :param state:
    :return: None
    """
    await state.update_data(project_name=message.text)
    await state.set_state(Projecting.price_per_chapter)
    await bot.send_message(chat_id=message.chat.id, text="Какова ставка за главу? (в рублях)")


@router.message(Projecting.price_per_chapter)
async def catch_price_per_chapter(message: types.Message, state: FSMContext) -> None:
    """
    :param message:
    :param state:
    :return: None
    """
    await state.update_data(price_per_chapter=int(message.text))
    await state.set_state(Projecting.price_per_chapter)
