
import aiogram.types
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils import executor
from keyboards_papa_project import lang_markup1,lang_markup2,lang_markup3,lang_markup4,lang_markup5

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
        await state.update_data({'толщина' : float(b)})
        await message.answer("Количество швов - " + str(int(float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)) + " п.м.")
        await message.answer("Шаг нарезки швов - " + str(int(float(b)*30//1000)) + " п.м.")
        if (float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)%200==0:
            await message.answer("Количество необходимых алмазных дисков для нарезки швов -" + str(int((float(a // (float(b) * 30 // 1000) ** 2) * (float(b) * 30 // 1000) * 2)/200)) +"шт" )
            await message.answer(f"Алмазные диски для нарезки швов можно приобрести на сайте:http://samishsib.ru/catalog/70/")
        else:
            await message.answer("Количество необходимых алмазных дисков для нарезки швов - " + str(int((float(a // (float(b) * 30 // 1000) ** 2) * (float(b) * 30 // 1000) * 2)/200)+1) +"шт")
            await message.answer(f"Алмазные диски для нарезки швов можно приобрести на сайте:http://samishsib.ru/catalog/70/")

    else:
        await message.reply("Вы ввели не число. Повторите попытку")


@dp.message_handler(state="wait_knopka")
async def set_language(message: types.Message, state: FSMContext):
    lang_markup1 = message.text
    if lang_markup1 == "Расчет количества температурно-усадочных швов":
        await message.answer("Эта функция считает количество температурно-усадочных швов\nДля того чтобы получить их количество,введите все данные, которые запрашивает бот и он выведет ответ",reply_markup=ReplyKeyboardRemove())
        await message.answer("Введите площадь(в м²)")
        await state.set_state("площадь")
    elif lang_markup1 == "Расчёт количества арматуры":
        await message.answer("На сколько расчитать количество арматуры",reply_markup=lang_markup5)
        await state.set_state("на сколько расчитать")

@dp.message_handler(state="на сколько расчитать")
async def set_language(message: types.Message, state: FSMContext):
    h=message.text
    await state.update_data({"h": h})
    if h=="Расчёт количества арматуры(на квадратный метр)":
        await message.answer("Выбирите скольки слойное армирование хотите сделать",reply_markup=lang_markup2)
        await state.set_state("Скольки слойное армироване")
    elif h=="Расчёт количества арматуры(на всю площадь)":
        await message.answer("Введите площадь объекта:",reply_markup=ReplyKeyboardRemove())
        await state.set_state("Скольки слойное армироване на всю п")

@dp.message_handler(state="Скольки слойное армироване")
async def set_language(message: types.Message, state: FSMContext):
    lang_markup2 = message.text
    await state.update_data({"сколько слоёв арматуры": lang_markup2})
    if lang_markup2 == "Однослойное армирование":
        await message.answer(
            "Эта функция считает количество арматуры на квадратный метр\nДля того чтобы получить это количество,введите все данные, которые запрашивает бот и он выведет ответ",
            reply_markup=ReplyKeyboardRemove())
        await message.answer("Выберите диаметр арматуры(в мм)", reply_markup=lang_markup3)
        await state.set_state("однослойное армирование")
    elif lang_markup2=="Двухслойное армирование":
        await message.answer(
            "Эта функция считает количество арматуры на квадратный метр c двуслойным армированием\nДля того чтобы получить это количество,введите все данные, которые запрашивает бот и он выведет ответ",
            reply_markup=ReplyKeyboardRemove())
        await message.answer("Выберите диаметр первого слоя арматуры(в мм)", reply_markup=lang_markup3)
        await state.set_state("однослойное армирование")
@dp.message_handler(state="Скольки слойное армироване на всю п")
async def set_language(message: types.Message, state: FSMContext):
    f = message.text
    if isinstance(f, str) and f.isdigit():
        await state.update_data({"f": f})
        await message.answer("Выбирите скольки слойное армирование на всю площадь хотите сделать", reply_markup=lang_markup2)
        await state.set_state("однослойное армирование на всю")
    else:
        await message.reply("Вы ввели не число. Повторите попытку")


@dp.message_handler(state='однослойное армирование на всю')
async def age_process(message: types.Message, state: FSMContext):
    lang_markup2 = message.text
    await state.update_data({"сколько слоёв арматуры": lang_markup2})
    if lang_markup2 == "Однослойное армирование":
        await message.answer("Эта функция считает количество арматуры на всю площадь\nДля того чтобы получить это количество,введите все данные, которые запрашивает бот и он выведет ответ",reply_markup=ReplyKeyboardRemove())
        await message.answer("Выберите диаметр арматуры(в мм)", reply_markup=lang_markup3)
        await state.set_state("однослойное армирование")
    elif lang_markup2 =="Двухслойное армирование":
        await message.answer(
            "Эта функция считает количество арматуры на всю площадь с двухслойным армированием\nДля того чтобы получить это количество,введите все данные, которые запрашивает бот и он выведет ответ",
            reply_markup=ReplyKeyboardRemove())
        await message.answer("Выберите диаметр первого слоя арматуры(в мм)", reply_markup=lang_markup3)
        await state.set_state("однослойное армирование")

@dp.message_handler(state='однослойное армирование')
async def age_process(message: types.Message, state: FSMContext):
    c = message.text
    data = await state.get_data()
    ckokclov = str(data["сколько слоёв арматуры"])
    if isinstance(c, str) and c.isdigit():
        if ckokclov=="Однослойное армирование":
            await state.update_data({'однослойное армирование': float(c)})
            if c=="8":
                dem20 = 0.395
                await state.update_data({'масса арматуры': float(dem20)})
                await message.answer("Теперь введите шаг арматуры",reply_markup=lang_markup4)
                await state.set_state("шаг арматуры")
            elif c=="10":
                dem20 = 0.617
                await state.update_data({'масса арматуры': float(dem20)})
                await message.answer("Теперь введите шаг арматуры", reply_markup=lang_markup4)
                await state.set_state("шаг арматуры")
            elif c=="12":
                dem20 = 0.888
                await state.update_data({'масса арматуры': float(dem20)})
                await message.answer("Теперь введите шаг арматуры", reply_markup=lang_markup4)
                await state.set_state("шаг арматуры")
            elif c=="14":
                dem20 = 1.210
                await state.update_data({'масса арматуры': float(dem20)})
                await message.answer("Теперь введите шаг арматуры", reply_markup=lang_markup4)
                await state.set_state("шаг арматуры")
            elif c=="16":
                dem20 = 1.580
                await state.update_data({'масса арматуры': float(dem20)})
                await message.answer("Теперь введите шаг арматуры(в мм)", reply_markup=lang_markup4)
                await state.set_state("шаг арматуры")
        elif ckokclov=="Двухслойное армирование":
            await message.answer("Введите диаметр второго слоя арматуры(в мм)", reply_markup=lang_markup3)
            await state.set_state("второй слой армирования на м2")
    else:
        await message.reply("Вы ввели не число. Повторите попытку")


@dp.message_handler(state='второй слой армирования на м2')
async def age_process(message: types.Message, state: FSMContext):
    p = message.text
    if isinstance(p, str) and p.isdigit():
        await state.update_data({'однослойное армирование': float(p)})
        if p=="8":
            dem201 = 0.395
            await state.update_data({'масса арматуры2слой': float(dem201)})
            await message.answer("Теперь введите шаг первого слоя арматуры(в мм)",reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        elif p=="10":
            dem201 = 0.617
            await state.update_data({'масса арматуры2слой': float(dem201)})
            await message.answer("Теперь введите шаг первого слоя арматуры(в мм)", reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        elif p=="12":
            dem201 = 0.888
            await state.update_data({'масса арматуры2слой': float(dem201)})
            await message.answer("Теперь введите шаг первого слоя арматуры(в мм)", reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        elif p=="14":
            dem201 = 1.210
            await state.update_data({'масса арматуры2слой': float(dem201)})
            await message.answer("Теперь введите шаг первого слоя арматуры(в мм)", reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        elif p=="16":
            dem201 = 1.580
            await state.update_data({'масса арматуры2слой': float(dem201)})
            await message.answer("Теперь введите шаг первого слоя арматуры(в мм)", reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
    else:
        await message.reply("Вы ввели не число. Повторите попытку")

    await state.set_state("шаг арматуры")



@dp.message_handler(state='шаг арматуры')
async def age_process(message: types.Message, state: FSMContext):
    d = message.text
    data = await state.get_data()
    ckokclov = str(data["сколько слоёв арматуры"])
    h = str(data["h"])
    if isinstance(d, str) and d.isdigit():
        if ckokclov=="Однослойное армирование":
            if d == "100":
                shag20 = 100
                await state.update_data({'шаг': float(shag20)})
                data = await state.get_data()
                sh = float(data["шаг"])
                data = await state.get_data()
                de = float(data["масса арматуры"])
                if h=="Расчёт количества арматуры(на квадратный метр)":
                    await message.answer("Количество арматуры на квадратный метр - " + str((((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²",reply_markup=ReplyKeyboardRemove())
                elif h=="Расчёт количества арматуры(на всю площадь)":
                    data = await state.get_data()
                    f = float(data["f"])
                    await message.answer("Количество арматуры на квадратный метр - " + str((((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²",reply_markup=ReplyKeyboardRemove())
                    await message.answer("Количество арматуры на всю площадь - " + str(((((9000 / float(sh)) * 2) * float(de)) / 9)*float(f)) + "кг",reply_markup=ReplyKeyboardRemove())
            elif d == "150":
                shag20 = 150
                await state.update_data({'шаг': float(shag20)})
                data = await state.get_data()
                sh = float(data["шаг"])
                data = await state.get_data()
                de = float(data["масса арматуры"])
                if h == "Расчёт количества арматуры(на квадратный метр)":
                    await message.answer("Количество арматуры на квадратный метр - " + str((((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²",reply_markup=ReplyKeyboardRemove())
                elif h == "Расчёт количества арматуры(на всю площадь)":
                    data = await state.get_data()
                    f = float(data["f"])
                    await message.answer("Количество арматуры на квадратный метр - " + str((((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²",reply_markup=ReplyKeyboardRemove())
                    await message.answer("Количество арматуры на всю площадь - " + str(((((9000 / float(sh)) * 2) * float(de)) / 9) * float(f)) + "кг",reply_markup=ReplyKeyboardRemove())
            elif d == "200":
                shag20 = 200
                await state.update_data({'шаг': float(shag20)})
                data = await state.get_data()
                sh = float(data["шаг"])
                data = await state.get_data()
                de = float(data["масса арматуры"])
                if h == "Расчёт количества арматуры(на квадратный метр)":
                    await message.answer("Количество арматуры на квадратный метр - " + str((((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²",reply_markup=ReplyKeyboardRemove())
                elif h == "Расчёт количества арматуры(на всю площадь)":
                    data = await state.get_data()
                    f = float(data["f"])
                    await message.answer("Количество арматуры на квадратный метр - " + str((((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²",reply_markup=ReplyKeyboardRemove())
                    await message.answer("Количество арматуры на всю площадь - " + str(((((9000 / float(sh)) * 2) * float(de)) / 9) * float(f)) + "кг",reply_markup=ReplyKeyboardRemove())
            elif d == "250":
                shag20 = 250
                await state.update_data({'шаг': float(shag20)})
                data = await state.get_data()
                sh = float(data["шаг"])
                data = await state.get_data()
                de = float(data["масса арматуры"])
                if h == "Расчёт количества арматуры(на квадратный метр)":
                    await message.answer("Количество арматуры на квадратный метр - " + str((((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²",reply_markup=ReplyKeyboardRemove())
                elif h == "Расчёт количества арматуры(на всю площадь)":
                    data = await state.get_data()
                    f = float(data["f"])
                    await message.answer("Количество арматуры на квадратный метр - " + str((((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²",reply_markup=ReplyKeyboardRemove())
                    await message.answer("Количество арматуры на всю площадь - " + str(((((9000 / float(sh)) * 2) * float(de)) / 9) * float(f)) + "кг",reply_markup=ReplyKeyboardRemove())
            elif d == "300":
                shag20 = 300
                await state.update_data({'шаг': float(shag20)})
                data = await state.get_data()
                sh = float(data["шаг"])
                data = await state.get_data()
                de = float(data["масса арматуры"])
                if h == "Расчёт количества арматуры(на квадратный метр)":
                    await message.answer("Количество арматуры на квадратный метр - " + str((((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²",reply_markup=ReplyKeyboardRemove())
                elif h == "Расчёт количества арматуры(на всю площадь)":
                    data = await state.get_data()
                    f = float(data["f"])
                    await message.answer("Количество арматуры на квадратный метр - " + str((((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²",reply_markup=ReplyKeyboardRemove())
                    await message.answer("Количество арматуры на всю площадь - " + str(((((9000 / float(sh)) * 2) * float(de)) / 9) * float(f)) + "кг",reply_markup=ReplyKeyboardRemove())
        elif ckokclov=="Двухслойное армирование":
            await message.answer("Введите шаг второго слоя арматуры(в мм)", reply_markup=lang_markup4)
            await state.set_state("второй слой армирования на м2 шаг")

    else:
        await message.reply("Вы ввели не число. Повторите попытку")

@dp.message_handler(state='второй слой армирования на м2 шаг')
async def age_process(message: types.Message, state: FSMContext):
    o = message.text
    data = await state.get_data()
    h = str(data["h"])
    if isinstance(o, str) and o.isdigit():
        if o == "100":
            shag201 = 100
            await state.update_data({'шаг2слой': float(shag201)})
            data = await state.get_data()
            sh = float(data["шаг"])
            data = await state.get_data()
            de = float(data["масса арматуры"])
            data = await state.get_data()
            sh2 = float(data["шаг2слой"])
            data = await state.get_data()
            de2 = float(data["масса арматуры"])
            if h == "Расчёт количества арматуры(на квадратный метр)":
                await message.answer("Количество арматуры необходимое для первого слоя(в м²) - " + str(
                    (((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры необходимое для второго слоя(в м²) - " + str(
                    (((9000 / float(sh2)) * 2) * float(de2)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
            elif h == "Расчёт количества арматуры(на всю площадь)":
                data = await state.get_data()
                f = float(data["f"])
                await message.answer("Количество арматуры необходимое для первого слоя(в м²) - " + str(
                    (((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры необходимое для второго слоя(в м²) - " + str(
                    (((9000 / float(sh2)) * 2) * float(de2)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры на всю площадь первого слоя(в кг) - " + str(
                    ((((9000 / float(sh)) * 2) * float(de)) / 9) * float(f)) + "кг", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры на всю площадь второго слоя(в кг) - " + str(
                    ((((9000 / float(sh2)) * 2) * float(de2)) / 9) * float(f)) + "кг", reply_markup=ReplyKeyboardRemove())

        elif o == "150":
            shag201 = 150
            await state.update_data({'шаг2слой': float(shag201)})
            data = await state.get_data()
            sh = float(data["шаг"])
            data = await state.get_data()
            de = float(data["масса арматуры"])
            data = await state.get_data()
            sh2 = float(data["шаг2слой"])
            data = await state.get_data()
            de2 = float(data["масса арматуры"])
            if h == "Расчёт количества арматуры(на квадратный метр)":
                await message.answer("Количество арматуры необходимое для первого слоя(в м²) - " + str(
                    (((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры необходимое для второго слоя(в м²) - " + str(
                    (((9000 / float(sh2)) * 2) * float(de2)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
            elif h == "Расчёт количества арматуры(на всю площадь)":
                data = await state.get_data()
                f = float(data["f"])
                await message.answer("Количество арматуры необходимое для первого слоя(в м²) - " + str(
                    (((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры необходимое для второго слоя(в м²) - " + str(
                    (((9000 / float(sh2)) * 2) * float(de2)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры на всю площадь первого слоя(в кг) - " + str(
                    ((((9000 / float(sh)) * 2) * float(de)) / 9) * float(f)) + "кг", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры на всю площадь второго слоя(в кг) - " + str(
                    ((((9000 / float(sh2)) * 2) * float(de2)) / 9) * float(f)) + "кг",
                                     reply_markup=ReplyKeyboardRemove())
        elif o == "200":
            shag201 = 200
            await state.update_data({'шаг2слой': float(shag201)})
            data = await state.get_data()
            sh = float(data["шаг"])
            data = await state.get_data()
            de = float(data["масса арматуры"])
            data = await state.get_data()
            sh2 = float(data["шаг2слой"])
            data = await state.get_data()
            de2 = float(data["масса арматуры2слой"])
            if h == "Расчёт количества арматуры(на квадратный метр)":
                await message.answer("Количество арматуры необходимое для первого слоя(в м²) - " + str(
                    (((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры необходимое для второго слоя(в м²) - " + str(
                    (((9000 / float(sh2)) * 2) * float(de2)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
            elif h == "Расчёт количества арматуры(на всю площадь)":
                data = await state.get_data()
                f = float(data["f"])
                await message.answer("Количество арматуры необходимое для первого слоя(в м²) - " + str(
                    (((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры необходимое для второго слоя(в м²) - " + str(
                    (((9000 / float(sh2)) * 2) * float(de2)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры на всю площадь первого слоя(в кг) - " + str(
                    ((((9000 / float(sh)) * 2) * float(de)) / 9) * float(f)) + "кг", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры на всю площадь второго слоя(в кг) - " + str(
                    ((((9000 / float(sh2)) * 2) * float(de2)) / 9) * float(f)) + "кг",
                                     reply_markup=ReplyKeyboardRemove())
        elif o == "250":
            shag201 = 250
            await state.update_data({'шаг2слой': float(shag201)})
            data = await state.get_data()
            sh = float(data["шаг"])
            data = await state.get_data()
            de = float(data["масса арматуры"])
            data = await state.get_data()
            sh2 = float(data["шаг2слой"])
            data = await state.get_data()
            de2 = float(data["масса арматуры2слой"])
            if h == "Расчёт количества арматуры(на квадратный метр)":
                await message.answer("Количество арматуры необходимое для первого слоя(в м²) - " + str(
                    (((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры необходимое для второго слоя(в м²) - " + str(
                    (((9000 / float(sh2)) * 2) * float(de2)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
            elif h == "Расчёт количества арматуры(на всю площадь)":
                data = await state.get_data()
                f = float(data["f"])
                await message.answer("Количество арматуры необходимое для первого слоя(в м²) - " + str(
                    (((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры необходимое для второго слоя(в м²) - " + str(
                    (((9000 / float(sh2)) * 2) * float(de2)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры на всю площадь первого слоя(в кг) - " + str(
                    ((((9000 / float(sh)) * 2) * float(de)) / 9) * float(f)) + "кг", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры на всю площадь второго слоя(в кг) - " + str(
                    ((((9000 / float(sh2)) * 2) * float(de2)) / 9) * float(f)) + "кг",
                                     reply_markup=ReplyKeyboardRemove())
        elif o == "300":
            shag201 = 300
            await state.update_data({'шаг2слой': float(shag201)})
            data = await state.get_data()
            sh = float(data["шаг"])
            data = await state.get_data()
            de = float(data["масса арматуры"])
            data = await state.get_data()
            sh2 = float(data["шаг2слой"])
            data = await state.get_data()
            de2 = float(data["масса арматуры2слой"])
            if h == "Расчёт количества арматуры(на квадратный метр)":
                await message.answer("Количество арматуры необходимое для первого слоя(в м²) - " + str(
                    (((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры необходимое для второго слоя(в м²) - " + str(
                    (((9000 / float(sh2)) * 2) * float(de2)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
            elif h == "Расчёт количества арматуры(на всю площадь)":
                data = await state.get_data()
                f = float(data["f"])
                await message.answer("Количество арматуры необходимое для первого слоя(в м²) - " + str(
                    (((9000 / float(sh)) * 2) * float(de)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры необходимое для второго слоя(в м²) - " + str(
                    (((9000 / float(sh2)) * 2) * float(de2)) / 9) + "кг/м²", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры на всю площадь первого слоя(в кг) - " + str(
                    ((((9000 / float(sh)) * 2) * float(de)) / 9) * float(f)) + "кг", reply_markup=ReplyKeyboardRemove())
                await message.answer("Количество арматуры на всю площадь второго слоя(в кг) - " + str(
                    ((((9000 / float(sh2)) * 2) * float(de2)) / 9) * float(f)) + "кг",
                                     reply_markup=ReplyKeyboardRemove())






if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)