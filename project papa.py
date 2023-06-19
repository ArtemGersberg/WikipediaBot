
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
    await message.answer("Выбор действия", reply_markup=lang_markup12)
    await state.set_state("wait_knopka")

@dp.message_handler(state='площадь')
async def age_process(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({"text": text})
    if isinstance(text, str) and text.isdigit():
        await state.update_data({'площадь': float(text)})
        await message.answer("Введите толщину(в мм)")
        await state.set_state('толщина')
    else:
        await message.reply("Вы ввели не число. Повторите попытку")

@dp.message_handler(state='толщина')
async def age_process(message: types.Message, state: FSMContext):
    text1 = message.text
    data = await state.get_data()
    text = float(data["text"])
    if isinstance(text1, str) and text1.isdigit():
        await state.update_data({'толщина' : float(text1)})
        await message.answer("Количество швов:" + str(float((text/(float(text1)*35)**2)*(float(text1)*35)*2)))

    else:
        await message.reply("Вы ввели не число. Повторите попытку")


@dp.message_handler(state="wait_knopka")
async def set_language(message: types.Message, state: FSMContext):
    lang_markup12 = message.text
    if lang_markup12 == "Расчет количества температурно-усадочных швов":
        await message.answer("Эта функция считает количество температурно-усадочных швов\nДля того чтобы получить их количество,введите все данные, которые запрашивает бот и он выведет ответ",reply_markup=ReplyKeyboardRemove())
        await message.answer("Введите площадь(в м²)")
        await state.set_state("площадь")





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)