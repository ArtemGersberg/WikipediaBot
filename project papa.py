
import aiogram.types
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils import executor
from keyboards_papa_project import lang_markup12

TOKEN="5701505172:AAEFVT76AqvIMBCUZgJ9cY39BVumvFJNCIM"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state="*")
async def setup_language(message: types.Message, state: FSMContext):
    await message.reply("Выбор действия", reply_markup=lang_markup12)
    await state.set_state("wait_knopka")

@dp.message_handler(state='площадь')
async def age_process(message: types.Message, state: FSMContext):
    text = message.text
    #await message.reply("Введите площадь")
    if text.isdigit():
        await state.update_data({'площадь' : int(text)})
        await message.answer("теперь введите толщину")
        await state.set_state('толщина')
    else:
        await message.reply("Вы ввели не число. Повторите попытку")

@dp.message_handler(state='толщина')
async def age_process(message: types.Message, state: FSMContext):
    text1 = message.text
    if text1.isdigit():
        #await message.reply("Введите толщину")
        await state.update_data({'площадь' : int(text1)})
        await message.reply("всё")

    else:
        await message.reply("Вы ввели не число. Повторите попытку")


@dp.message_handler(state="wait_knopka")
async def set_language(message: types.Message, state: FSMContext):
    lang_markup12 = message.text
    if lang_markup12 == "Расчет количества температурно-усадочных швов":
        await message.reply("Введите площадь")
        await state.set_state("площадь")





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)