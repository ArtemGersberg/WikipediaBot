import wikipedia
from aiogram import Bot, Dispatcher, executor, types
import re

from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from env import TOKEN
from keyboards import ininlinekeyboard, keyboard, keyboard2

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Отправьте мне любое слово, и я найду его значение на Wikipedia")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Отправьте мне любое слово, и я найду его значение на Wikipedia")


@dp.message_handler()
async def any_text_message(message: types.Message):
    txt, url = getwiki(message.text)
    if url:
        button = InlineKeyboardButton('Ссылка на wiki', url=url)
        kb = InlineKeyboardMarkup().add(button)
        await message.answer(txt, reply_markup=kb)
    else:
        await message.answer(txt)






def getwiki(text):
    try:
        language = "ru"
        wikipedia.set_lang(language)
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
