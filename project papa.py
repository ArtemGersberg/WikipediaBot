from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import  ReplyKeyboardRemove
from aiogram.utils import executor
from keyboards_papa_project import lang_markup1,lang_markup2,lang_markup3,lang_markup4,lang_markup5,lang_markup6,lang_markup7,lang_markup8 ,\
lang_markup9,lang_markup10,lang_markup11,lang_markup,lang_markup102,lang_markup123
from env import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state="*")
async def setup_language(message: types.Message, state: FSMContext):
    await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup)
    await state.set_state("Выборпристарте")

@dp.message_handler(state='Выборпристарте')
async def age_process(message: types.Message, state: FSMContext):
    abc = message.text
    if abc=="Расчёт материала для полов":
        await message.answer("Выберите тип полов", reply_markup=lang_markup6)
        await state.set_state("Выбор вида полов")
    elif abc=="Инструкция/связь с администрацией":
        await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
        await state.set_state("командахелп")
    else:
        if abc=="/calculations":
                await message.answer("Выберите тип полов", reply_markup=lang_markup6)
                await state.set_state("Выбор вида полов")
        elif abc=="/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif abc=="/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")


@dp.message_handler(commands=['help'], state="*")
async def setup_language(message: types.Message, state: FSMContext):
    await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
    await state.set_state("командахелп")

@dp.message_handler(state='командахелп')
async def age_process(message: types.Message, state: FSMContext):
    aba = message.text
    if aba=="Инструкция по пользованию":
        await message.answer("Этот бот предназначен для расчёта материала необходимого при производстве промышленных бетонных и полимерных полов.\nЕсли у вас возникли вопросы с использованием бота, то можите прочитать это и попробовать найти ответ на свой вопрос.\nПри нажати кнопки /start, вам предложат выбрать тип полов, для которых вы сможите расчитать количество материала.\nНажав на кнопку 'Полимерные полы', вам предложат выбрать тип покрытия полимерных полов, а затем фактуру полов. После выбора фактуры полов вы сможите нажать на  нужную кнопку для расчёта того или иного материала в зависимости от вашего выбора.\nЕсли у вас остались вопросы, можите написать администратору бота @igorg80.\nКоманды:\n/start - запустить бота.\n/help - инструкция по пользованию/связь с администрацией.\n/calculation - сразу перейти к расчётам.\nПриятного использования)",reply_markup=ReplyKeyboardRemove())

    elif aba=="Связь с администратором бота":
        await message.answer("Если у вас есть предложения или остались вопросы по функционалу бота, то можите написать администратору @igorg80\nСпасибо, что пользуетесь ботом)",reply_markup=ReplyKeyboardRemove())
    else:
        if aba=="/calculations":
                await message.answer("Выберите тип полов", reply_markup=lang_markup6)
                await state.set_state("Выбор вида полов")
        elif aba=="/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif aba=="/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")

@dp.message_handler(commands=['calculations'], state="*")
async def setup_language(message: types.Message, state: FSMContext):
    await message.answer("Выберите тип полов", reply_markup=lang_markup6)
    await state.set_state("Выбор вида полов")

@dp.message_handler(state='Выбор вида полов')
async def age_process(message: types.Message, state: FSMContext):
    ab = message.text
    if ab=="Полимерные полы":
        await message.answer("Выберите тип материала",reply_markup=lang_markup7)
        await state.set_state("Выбор типа полов")
    elif ab=="Бетонные полы":
        await message.answer("Выбор действия", reply_markup=lang_markup1)
        await state.set_state("wait_knopka")
    else:
        if ab == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif ab == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif ab == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")

@dp.message_handler(commands=['requirements'], state="*")
async def setup_language(message: types.Message, state: FSMContext):
    await message.answer("Выберите тип полов", reply_markup=lang_markup6)
    await state.set_state("Выбор вида полов2")

@dp.message_handler(state='Выбор вида полов2')
async def age_process(message: types.Message, state: FSMContext):
    ab2 = message.text
    if ab2=="Полимерные полы":
        await message.answer("Выберите кнопку",reply_markup=lang_markup123)
        await state.set_state("Выбор кнопки")
    elif ab2=="Бетонные полы":
        await message.answer("Выбор действия", reply_markup=lang_markup1)
        await state.set_state("Выбор кнопки2")
    else:
        if ab2=="/calculations":
                await message.answer("Выберите тип полов", reply_markup=lang_markup6)
                await state.set_state("Выбор вида полов")
        elif ab2=="/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif ab2=="/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")

@dp.message_handler(state='Выбор кнопки2')
async def age_process(message: types.Message, state: FSMContext):
    af=message.text
    if af=="Требования к нанесению":
        await message.answer("Идёт разроботка...")
    elif af=="Требования к готовым покрытиям":
        await message.answer("Идёт разроботка...")
    else:
        if af=="/calculations":
                await message.answer("Выберите тип полов", reply_markup=lang_markup6)
                await state.set_state("Выбор вида полов")
        elif af=="/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif af=="/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")


@dp.message_handler(state='Выбор кнопки')
async def age_process(message: types.Message, state: FSMContext):
    ac2 = message.text
    if ac2=="Требования к нанесению":
        await message.answer("Устройство полов допускается при температуре укладываемых элементов и материалов пола, а также воздуха в помещении и на уровне пола, °С, не ниже:10 — при устройстве покрытий из полимерных материалов; эту температуру следует поддерживать не менее суток после окончания работ.",reply_markup=ReplyKeyboardRemove())
        await message.answer("Перед устройством полов, в конструкции которых заложены изделия и материалы на основе древесины или ее отходов, синтетических смол и волокон, ксилолитовых покрытий, в помещении должны быть выполнены штукатурные и иные работы, связанные с возможностью увлажнения покрытий, в том числе должны быть полностью смонтированы, опрессованы и опробованы системы отопления, водопровода и водоотведения. При устройстве этих полов и в последующий период до сдачи объекта в эксплуатацию относительная влажность воздуха в помещении не должна превышать 60 %. Сквозняки в помещении не допускаются.")
        await message.answer("Конструкционная целостность-основание должно быть плотным и прочным. Не допускается наличие трещин, отслоений и пыления. Метод контроля - Сплошной визуальный осмотр.")
        await message.answer("Прочность основания на сжатие:для уличных условий применения для внутренних помещений при наличии движения транспорта для внутренних помещений при пешеходном движении-Не менее 30 МПаНе менее 25 МПаНе менее 20 МПа. Метод контроля-ГОСТ 22690, не менее шести замеров на каждые 100 м2(методами ударного импульса и отрыва со скалыванием).")
        await message.answer("Прочность основания на растяжение приотрыве: для уличных условий применения- для внутренних помещений при наличии движения транспорта- для внутренних помещений при пешеходном движении-Не менее 2,0МпаНе менее 1,5МПаНе менее 1,0Мпа (когезионный характер отрыва).Метод контроля-ГОСТ 22690, не менее шести замеров на каждые 100 м2.")
        await message.answer("Влажность основания-Не более 4% по массе, если иное не указано в технической документации производителя материалов покрытия.Метод контроля-ГОСТ 21718, не менее шести замеров на каждые 100 м2.")
        await message.answer("Отклонение от плоскости-Не более 2мм на двухметровой рейке.Метод контроля-Инструментальный, не менее шести замеров накаждые 100м2.")
        await message.answer("Возраст бетонного основания-Не менее 28сут, если иное не указано в технической документации производителя материалов покрытия.Метод контроля-Согласно исполнительной документации строительного объекта.")
    elif ac2=="Требования к готовым покрытиям":
        await message.answer("Идёт разроботка...")
    else:
        if ac2=="/calculations":
                await message.answer("Выберите тип полов", reply_markup=lang_markup6)
                await state.set_state("Выбор вида полов")
        elif ac2=="/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif ac2=="/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")



@dp.message_handler(state='Выбор типа полов')
async def age_process(message: types.Message, state: FSMContext):
    ac = message.text
    await state.update_data({"aс": ac})
    if ac=="Эпоксидные":
        await message.answer("Выберите фактуру",reply_markup=lang_markup8)
        await state.set_state("Выбор фактуры полов(Эпоксидные)")
    elif ac=="Полиуретановые":
        await message.answer("Идёт разработка...",reply_markup=ReplyKeyboardRemove())

    elif ac=="Полиуретан-цементные":
        await message.answer("Идёт разработка...",reply_markup=ReplyKeyboardRemove())
    else:
        if ac=="/calculations":
                await message.answer("Выберите тип полов", reply_markup=lang_markup6)
                await state.set_state("Выбор вида полов")
        elif ac=="/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif ac=="/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")

@dp.message_handler(state='Выбор фактуры полов(Эпоксидные)')
async def age_process(message: types.Message, state: FSMContext):
    ad = message.text
    await state.update_data({"ad": ad})
    if ad=="Гладкое":
        await message.answer("Выберите толщину покрытия гладкой фактуры",reply_markup=lang_markup9)
        await state.set_state("Выбор толщины(Гладкое)")
    elif ad=="Шероховатое":
        await message.answer("Выберите толщину покрытия шероховатой фактуры", reply_markup=lang_markup10)
        await state.set_state("Выбор толщины(Шероховатое)")
    elif ad=="Декоративное":
        await message.answer("Выберите толщину покрытия декоративной фактуры", reply_markup=lang_markup11)
        await state.set_state("Выбор толщины(Декоративное)")
    else:
        if ad == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif ad == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif ad == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")

@dp.message_handler(state='Выбор толщины(Декоративное)')
async def age_process(message: types.Message, state: FSMContext):
    au = message.text
    if au=="1 мм":
        await state.update_data({"Толщина(Декоративное)": 1})
        await message.answer("Введите площадь(в м²)",reply_markup=ReplyKeyboardRemove())
        await state.set_state("Вывод формулы")
    elif au=="2 мм":
        await state.update_data({"Толщина(Декоративное)": 2})
        await message.answer("Введите площадь(в м²)",reply_markup=ReplyKeyboardRemove())
        await state.set_state("Вывод формулы")
    else:
        if au == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif au == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif au == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")



@dp.message_handler(state='Выбор толщины(Шероховатое)')
async def age_process(message: types.Message, state: FSMContext):
    ai = message.text
    if ai == "1,5 мм":
        await state.update_data({"Толщина(Шероховатое)": 1.5})
        await message.answer("Введите площадь(в м²)",reply_markup=ReplyKeyboardRemove())
        await state.set_state("Вывод формулы")
    elif ai == "2,5 мм":
        await state.update_data({"Толщина(Шероховатое)": 2.5})
        await message.answer("Введите площадь(в м²)",reply_markup=ReplyKeyboardRemove())
        await state.set_state("Вывод формулы")
    elif ai == "4 мм":
        await state.update_data({"Толщина(Шероховатое)": 4})
        await message.answer("Введите площадь(в м²)",reply_markup=ReplyKeyboardRemove())
        await state.set_state("Вывод формулы")
    elif ai == "5 мм":
        await state.update_data({"Толщина(Шероховатое)": 5})
        await message.answer("Введите площадь(в м²)",reply_markup=ReplyKeyboardRemove())
        await state.set_state("Вывод формулы")
    else:
        if ai == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif ai == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif ai == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")

@dp.message_handler(state='Выбор толщины(Гладкое)')
async def age_process(message: types.Message, state: FSMContext):
    ae=message.text
    if ae=="1 мм":
        await state.update_data({"Толщина(Гладкое)": 1})
        await message.answer("Введите площадь(в м²)",reply_markup=ReplyKeyboardRemove())
        await state.set_state("Вывод формулы")
    elif ae=="2 мм":
        await state.update_data({"Толщина(Гладкое)": 2})
        await message.answer("Введите площадь(в м²)",reply_markup=ReplyKeyboardRemove())
        await state.set_state("Вывод формулы")
    elif ae=="3 мм":
        await state.update_data({"Толщина(Гладкое)": 3})
        await message.answer("Введите площадь(в м²)",reply_markup=ReplyKeyboardRemove())
        await state.set_state("Вывод формулы")
    else:
        if ae == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif ae == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif ae == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")

@dp.message_handler(state='Вывод формулы')
async def age_process(message: types.Message, state: FSMContext):
    pl=message.text
    if isinstance(pl, str) and pl.isdigit():
        data = await state.get_data()
        ad = str(data["ad"])
        if ad == "Гладкое":
            data = await state.get_data()
            tol2 = float(data["Толщина(Гладкое)"])
            await message.answer("Грунтовка Ризопокс 3500 - " + str(float(pl) * 0.35) + " кг")
            await message.answer("Присыпка-песок - " + str(0.5 * float(pl)) + " кг")
            await message.answer("Запечатка Ризопокс 4400 - " + str(0.8 * float(pl)) + " кг")
            await message.answer("Финишный слой Ризопокс 4101 - " + str(tol2 * 2 * float(pl)) + " кг")
            await message.answer("Рекомендуемые материалы можно приобрести по номеру +79600553058")
        elif ad == "Шероховатое":
            data = await state.get_data()
            tol1 = float(data["Толщина(Шероховатое)"])
            await message.answer("Грунтовка Ризопокс 3500 - " + str(float(pl) * 0.35) + " кг")
            await message.answer("Присыпка-песок - " + str(0.5 * float(pl)) + " кг")
            await message.answer("Запечатка Ризопокс 4400 - " + str(0.8 * float(pl)) + " кг")
            await message.answer("Финишный слой Ризопокс 4101 - " + str(tol1 * 2 * float(pl)) + " кг")
            await message.answer("Рекомендуемые материалы можно приобрести по номеру +79600553058")
        elif ad == "Декоративное":
            data = await state.get_data()
            tol3 = float(data["Толщина(Декоративное)"])
            await message.answer("Грунтовка Ризопокс 3500 - " + str(float(pl) * 0.35) + " кг")
            await message.answer("Присыпка-песок - " + str(0.5 * float(pl)) + " кг")
            await message.answer("Запечатка Ризопокс 4400 - " + str(0.8 * float(pl)) + " кг")
            await message.answer("Финишный слой Ризопокс 4101 - " + str(tol3 * 2 * float(pl)) + " кг")
            await message.answer("Рекомендуемые материалы можно приобрести по номеру +79600553058")
        else:
            if ad == "/calculations":
                await message.answer("Выберите тип полов", reply_markup=lang_markup6)
                await state.set_state("Выбор вида полов")
            elif ad == "/requirements":
                await message.answer("Выберите тип полов", reply_markup=lang_markup6)
                await state.set_state("Выбор вида полов2")
            elif ad == "/help":
                await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
                await state.set_state("командахелп")
            else:
                await message.reply("Вводите из предложенных вариантов")
@dp.message_handler(state='площадь')
async def age_process(message: types.Message, state: FSMContext):
    a = message.text
    await state.update_data({"a": a})
    if isinstance(a, str) and a.isdigit():
        await state.update_data({'площадь': float(a)})
        await message.answer("Введите толщину(в мм)")
        await state.set_state('толщина')
    else:
        if a == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif a == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif a == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
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
            await message.answer("Количество необходимых алмазных дисков для нарезки швов -" + str(int((float(a // (float(b) * 30 // 1000) ** 2) * (float(b) * 30 // 1000) * 2)/200)) +" шт" )
            await message.answer(f"Рекомендуемые алмазные диски для нарезки швов можно приобрести на сайте:http://samishsib.ru/catalog/70/")
            if ((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)*1.1)%1==0:
                await message.answer("Количество необходимого вилатерм шнура - "+ str(int((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)*1.1))+" п.м.")
                if (float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)%10==0:
                    await message.answer("Количесто необходимого полиуретанового герметика в банках по 600мл - "+ str(int((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)/10)) + " шт")
                else:
                    await message.answer("Количесто необходимого полиуретанового герметика в банках по 600мл - "+ str(int(((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)/10)+1)) +" шт")
            else:
                await message.answer("Количество необходимого вилатерм шнура - "+ str(int((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)*1.1))+" п.м.")
                if (float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)%10==0:
                    await message.answer("Количесто необходимого полиуретанового герметика в банках по 600мл - "+ str(int((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)/10)) + " шт")
                else:
                    await message.answer("Количесто необходимого полиуретанового герметика в банках по 600мл - "+ str(int(((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)/10)+1)) +" шт")
        else:
            await message.answer("Количество необходимых алмазных дисков для нарезки швов - " + str(int((float(a // (float(b) * 30 // 1000) ** 2) * (float(b) * 30 // 1000) * 2)/200)+1) +" шт")
            await message.answer(f"Рекомендуемые алмазные диски для нарезки швов можно приобрести на сайте:http://samishsib.ru/catalog/70/")
            if ((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)*1.1)%1==0:
                await message.answer("Количество необходимого вилатерм шнура - "+ str(int((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)*1.1))+" п.м.")
                if (float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)%10==0:
                    await message.answer("Количесто необходимого полиуретанового герметика в банках по 600мл - "+ str(int((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)/10)) + " шт")
                else:
                    await message.answer("Количесто необходимого полиуретанового герметика в банках по 600мл - "+ str(int(((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)/10)+1)) +" шт")
            else:
                await message.answer("Количество необходимого вилатерм шнура - "+ str(int((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)*1.1))+" п.м.")
                if (float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)%10==0:
                    await message.answer("Количесто необходимого полиуретанового герметика в банках по 600мл - "+ str(int((float(a//(float(b)*30//1000)**2)*(float(b)*30//1000)*2)/10)) + " шт")
                else:
                    await message.answer("Количесто необходимого полиуретанового герметика в банках по 600мл - " + str(
                        int(((float(a // (float(b) * 30 // 1000) ** 2) * (
                                    float(b) * 30 // 1000) * 2) / 10) + 1)) + " шт")
    else:
        if b == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif b == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif b == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
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
    else:
        if lang_markup1 == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif lang_markup1 == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif lang_markup1 == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")

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
    else:
        if h == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif h == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif h == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")

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
    else:
        if lang_markup2 == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif lang_markup2 == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif lang_markup2 == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")
@dp.message_handler(state="Скольки слойное армироване на всю п")
async def set_language(message: types.Message, state: FSMContext):
    f = message.text
    if isinstance(f, str) and f.isdigit():
        await state.update_data({"f": f})
        await message.answer("Выбирите скольки слойное армирование на всю площадь хотите сделать", reply_markup=lang_markup2)
        await state.set_state("однослойное армирование на всю")
    else:
        if f == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif f == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif f == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
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
    else:
        if lang_markup2 == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif lang_markup2 == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif lang_markup2 == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")

@dp.message_handler(state='однослойное армирование')
async def age_process(message: types.Message, state: FSMContext):
    c = message.text
    await state.update_data({'c': c})
    data = await state.get_data()
    ckokclov = str(data["сколько слоёв арматуры"])
    if ckokclov=="Однослойное армирование":
        if c=="8 мм":
            dem20 = 0.395
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Теперь введите шаг арматуры",reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        elif c=="10 мм":
            dem20 = 0.617
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Теперь введите шаг арматуры", reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        elif c=="12 мм":
            dem20 = 0.888
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Теперь введите шаг арматуры", reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        elif c=="14 мм":
            dem20 = 1.210
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Теперь введите шаг арматуры", reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        elif c=="16 мм":
            dem20 = 1.580
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Теперь введите шаг арматуры(в мм)", reply_markup=lang_markup4)
            await state.set_state("шаг арматуры")
        else:
            if c == "/calculations":
                await message.answer("Выберите тип полов", reply_markup=lang_markup6)
                await state.set_state("Выбор вида полов")
            elif c == "/requirements":
                await message.answer("Выберите тип полов", reply_markup=lang_markup6)
                await state.set_state("Выбор вида полов2")
            elif c == "/help":
                await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
                await state.set_state("командахелп")
            else:
                await message.reply("Вводите из предложенных вариантов")
    elif ckokclov=="Двухслойное армирование":
        if c=="8 мм":
            dem20 = 0.395
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Введите диаметр второго слоя арматуры(в мм)", reply_markup=lang_markup3)
            await state.set_state("второй слой армирования на м2")
        elif c=="10 мм":
            dem20 = 0.617
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Введите диаметр второго слоя арматуры(в мм)", reply_markup=lang_markup3)
            await state.set_state("второй слой армирования на м2")
        elif c=="12 мм":
            dem20 = 0.888
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Введите диаметр второго слоя арматуры(в мм)", reply_markup=lang_markup3)
            await state.set_state("второй слой армирования на м2")
        elif c=="14 мм":
            dem20 = 1.210
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Введите диаметр второго слоя арматуры(в мм)", reply_markup=lang_markup3)
            await state.set_state("второй слой армирования на м2")
        elif c=="16 мм":
            dem20 = 1.580
            await state.update_data({'масса арматуры': float(dem20)})
            await message.answer("Введите диаметр второго слоя арматуры(в мм)", reply_markup=lang_markup3)
            await state.set_state("второй слой армирования на м2")
        else:
            if c == "/calculations":
                await message.answer("Выберите тип полов", reply_markup=lang_markup6)
                await state.set_state("Выбор вида полов")
            elif c == "/requirements":
                await message.answer("Выберите тип полов", reply_markup=lang_markup6)
                await state.set_state("Выбор вида полов2")
            elif c == "/help":
                await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
                await state.set_state("командахелп")
            else:
                await message.reply("Вводите из предложенных вариантов")


@dp.message_handler(state='второй слой армирования на м2')
async def age_process(message: types.Message, state: FSMContext):
    p = message.text
    if p=="8 мм":
        dem201 = 0.395
        await state.update_data({'масса арматуры2слой': float(dem201)})
        await message.answer("Теперь введите шаг первого слоя арматуры(в мм)",reply_markup=lang_markup4)
        await state.set_state("шаг арматуры")
    elif p=="10 мм":
        dem201 = 0.617
        await state.update_data({'масса арматуры2слой': float(dem201)})
        await message.answer("Теперь введите шаг первого слоя арматуры(в мм)", reply_markup=lang_markup4)
        await state.set_state("шаг арматуры")
    elif p=="12 мм":
        dem201 = 0.888
        await state.update_data({'масса арматуры2слой': float(dem201)})
        await message.answer("Теперь введите шаг первого слоя арматуры(в мм)", reply_markup=lang_markup4)
        await state.set_state("шаг арматуры")
    elif p=="14 мм":
        dem201 = 1.210
        await state.update_data({'масса арматуры2слой': float(dem201)})
        await message.answer("Теперь введите шаг первого слоя арматуры(в мм)", reply_markup=lang_markup4)
        await state.set_state("шаг арматуры")
    elif p=="16 мм":
        dem201 = 1.580
        await state.update_data({'масса арматуры2слой': float(dem201)})
        await message.answer("Теперь введите шаг первого слоя арматуры(в мм)", reply_markup=lang_markup4)
        await state.set_state("шаг арматуры")
    else:
        if p == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif p == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif p == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")




@dp.message_handler(state='шаг арматуры')
async def age_process(message: types.Message, state: FSMContext):
    d = message.text
    data = await state.get_data()
    ckokclov = str(data["сколько слоёв арматуры"])
    h = str(data["h"])
    if ckokclov=="Однослойное армирование":
        if d == "100 мм":
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
        elif d == "150 мм":
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
        elif d == "200 мм":
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
        elif d == "250 мм":
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
        elif d == "300 мм":
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
        if d == "100 мм":
            shag20 = 100
            await state.update_data({'шаг': float(shag20)})
        elif d == "150 мм":
            shag20 = 150
            await state.update_data({'шаг': float(shag20)})
        elif d == "200 мм":
            shag20 = 200
            await state.update_data({'шаг': float(shag20)})
        elif d == "250 мм":
            shag20 = 250
            await state.update_data({'шаг': float(shag20)})
        elif d == "300 мм":
            shag20 = 300
            await state.update_data({'шаг': float(shag20)})
        await message.answer("Введите шаг второго слоя арматуры(в мм)", reply_markup=lang_markup4)
        await state.set_state("второй слой армирования на м2 шаг")
    else:
        if d == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif d == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif d == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")


@dp.message_handler(state='второй слой армирования на м2 шаг')
async def age_process(message: types.Message, state: FSMContext):
    o = message.text
    data = await state.get_data()
    h = str(data["h"])
    if o == "100 мм":
        shag201 = 100
        await state.update_data({'шаг2слой': float(shag201)})
        data = await state.get_data()
        sh = float(data["шаг"])
        data = await state.get_data()
        de = float(data['масса арматуры'])
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
                ((((9000 / float(sh2)) * 2) * float(de2)) / 9) * float(f)) + "кг", reply_markup=ReplyKeyboardRemove())
    elif o == "150 мм":
        shag201 = 150
        await state.update_data({'шаг2слой': float(shag201)})
        data = await state.get_data()
        sh = float(data["шаг"])
        data = await state.get_data()
        de = float(data['масса арматуры'])
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
    elif o == "200 мм":
        shag201 = 200
        await state.update_data({'шаг2слой': float(shag201)})
        data = await state.get_data()
        sh = float(data["шаг"])
        data = await state.get_data()
        de = float(data['масса арматуры'])
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
    elif o == "250 мм":
        shag201 = 250
        await state.update_data({'шаг2слой': float(shag201)})
        data = await state.get_data()
        sh = float(data["шаг"])
        data = await state.get_data()
        de = float(data['масса арматуры'])
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
    elif o == "300 мм":
        shag201 = 300
        await state.update_data({'шаг2слой': float(shag201)})
        data = await state.get_data()
        sh = float(data["шаг"])
        data = await state.get_data()
        de = float(data['масса арматуры'])
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
    else:
        if o == "/calculations":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов")
        elif o == "/requirements":
            await message.answer("Выберите тип полов", reply_markup=lang_markup6)
            await state.set_state("Выбор вида полов2")
        elif o == "/help":
            await message.answer("Выберите нужную вам кнопку", reply_markup=lang_markup102)
            await state.set_state("командахелп")
        else:
            await message.reply("Вводите из предложенных вариантов")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)