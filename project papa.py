
import aiogram.types
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils import executor
from keyboards_papa_project import lang_markup1,lang_markup2,lang_markup3,lang_markup4

TOKEN="5701505172:AAEFVT76AqvIMBCUZgJ9cY39BVumvFJNCIM"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state="*")
async def setup_language(message: types.Message, state: FSMContext):
    await message.answer("Выбор действия", reply_markup=lang_markup1)
    await state.set_state("wait_knopka")

@dp.message_handler(state='площадь')
async def age_process(message: types.Message, state: FSMContext):
    a = message.text
    await state.update_data({"a": a})
    if isinstance(a, str) and a.isdigit():
        await state.update_data({'площадь': float(a)})
        await message.answer("Введите толщину(в мм)")
        await state.set_state('толщина')
    else:
        await message.reply("Вы ввели не число. Повторите попытку")

@dp.message_handler(state='толщина')
async def age_process(message: types.Message, state: FSMContext):
    b = message.text
    data = await state.get_data()
    a = float(data["a"])
    if isinstance(b, str) and b.isdigit():
        yre=(a*30)/1000
        await state.update_data({'толщина' : float(b)})
        await message.answer("Количество швов - " + str(int(float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)) + " п.м.")
        await message.answer("Шаг нарезки швов - " + str(int(float(b)*30//1000)) + " п.м.")
    else:
        await message.reply("Вы ввели не число. Повторите попытку")


@dp.message_handler(state="wait_knopka")
async def set_language(message: types.Message, state: FSMContext):
    lang_markup1 = message.text
    if lang_markup1 == "Расчет количества температурно-усадочных швов":
        await message.answer("Эта функция считает количество температурно-усадочных швов\nДля того чтобы получить их количество,введите все данные, которые запрашивает бот и он выведет ответ",reply_markup=ReplyKeyboardRemove())
        await message.answer("Введите площадь(в м²)")
        await state.set_state("площадь")
    elif lang_markup1 == "Расчёт количества арматуры(на квадратный метр)":
        await message.answer("Выбирите скольки слойное армирование хотите сделать",reply_markup=lang_markup2)
        await state.set_state("Скольки слойное армироване")

@dp.message_handler(state="Скольки слойное армироване")
async def set_language(message: types.Message, state: FSMContext):
    lang_markup2 = message.text
    if lang_markup2 == "Однослойное армирование":
        await message.answer(
            "Эта функция считает количество арматуры на квадратный метр\nДля того чтобы получить это количество,введите все данные, которые запрашивает бот и он выведет ответ",
            reply_markup=ReplyKeyboardRemove())
        await message.answer("Выберите диаметр арматуры(в мм)", reply_markup=lang_markup3)
        await state.set_state("однослойное армирование")


@dp.message_handler(state='однослойное армирование')
async def age_process(message: types.Message, state: FSMContext):
    c = message.text
    if isinstance(c, str) and c.isdigit():
        await state.update_data({'однослойное армирование': float(c)})
        if lang_markup3=="8":
            dem20 = 0.395
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Теперь введите шаг арматуры",reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        elif lang_markup3=="10":
            dem20 = 0.617
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Теперь введите шаг арматуры", reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        elif lang_markup3=="12":
            dem20 = 0.888
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Теперь введите шаг арматуры", reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        elif lang_markup3=="14":
            dem20 = 1.210
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Теперь введите шаг арматуры", reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        elif lang_markup3=="16":
            dem20 = 1.580
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Теперь введите шаг арматуры", reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
    else:
        await message.reply("Вы ввели не число. Повторите попытку")



@dp.message_handler(state='шаг арматуры')
async def age_process(message: types.Message, state: FSMContext):
    d = message.text
    if isinstance(d, str) and d.isdigit():
        if lang_markup4 == "100мм":
            shag20 = 100
            await state.update_data({'шаг': float(shag20)})
            await state.set_state("формула 2ой кнопки")
        elif lang_markup4 == "150мм":
            shag20 = 150
            await state.update_data({'шаг': float(shag20)})
            await state.set_state("формула 2ой кнопки")
        elif lang_markup4 == "150мм":
            shag20 = 200
            await state.update_data({'шаг': float(shag20)})
            await state.set_state("формула 2ой кнопки")
        elif lang_markup4 == "150мм":
            shag20 = 250
            await state.update_data({'шаг': float(shag20)})
            await state.set_state("формула 2ой кнопки")
        elif lang_markup4 == "150мм":
            shag20 = 300
            await state.update_data({'шаг': float(shag20)})
            await state.set_state("формула 2ой кнопки")
    else:
        await message.reply("Вы ввели не число. Повторите попытку")



@dp.message_handler(state='формула 2ой кнопки')
async def age_process(message: types.Message, state: FSMContext):
    data = await state.get_data()
    sh = float(data["шаг"])
    data = await state.get_data()
    de = float(data["масса арматуры"])
    await message.answer("Количество арматуры - " + str((((300/float(sh))*2)*float(de))/9))












if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)