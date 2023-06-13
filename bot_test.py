import aiogram.types
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
import re
import langdetect
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

#from aiogram.dispatcher.filters import Command
#from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards import keyboard , ininlinekeyboard, keyboard2,lang_markup

TOKEN = "5977899411:AAGcb-0i30DnLoYOm03uRljSMDD_xBYpOfQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Отправьте мне любое слово, и я найду его значение на Wikipedia",reply_markup=aiogram.types.ReplyKeyboardRemove())


@dp.message_handler(commands=['lang'])
async def send_welcome(message: types.Message):
    await message.reply("Выбериете язык ввода",reply_markup=lang_markup)




@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Welcome to Wikipedia for the Telegram.\nThis bot can quickly search for the meanings of the words you are interested in.\nYou can also choose the input language or use the language auto-detection function (it is automotic).\nEnjoy using it)")


@dp.message_handler()
async def any_text_message(message: types.Message):
    txt, url = getwiki(message.text)
    if url:
        button = InlineKeyboardButton('Ссылка на статью Wikipedia', url=url)
        kb = InlineKeyboardMarkup().add(button)
        await message.answer(txt, reply_markup=kb)
    else:
        await message.answer(txt)








def getwiki(text):
    try:
        wikipedia.set_lang("ru")
        ny = wikipedia.page(text)

        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break

        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2, ny.url


    except Exception as e:
        return 'В энциклопедии нет информации об этом', None


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
