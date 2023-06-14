import aiogram.types
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
import re
import langdetect
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
# from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from keyboards import ininlinekeyboard, lang_markup

TOKEN = "5977899411:AAGcb-0i30DnLoYOm03uRljSMDD_xBYpOfQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await state.update_data(language="ru")
    await message.reply("Отправьте мне любое слово, и я найду его значение на Wikipedia",
                        reply_markup=aiogram.types.ReplyKeyboardRemove())
    await state.set_state("ask_request")


@dp.message_handler(commands=['lang'], state="*")
async def setup_language(message: types.Message, state: FSMContext):
    await message.reply("Выберите язык ввода", reply_markup=lang_markup)
    await state.set_state("wait_language")


@dp.message_handler(commands=['help'], state="*")
async def get_help(message: types.Message):
    await message.reply(
        f"Welcome to Wikipedia for the Telegram.\nThis bot can quickly search for the meanings of the words you are interested in.\nYou can also choose the input language or use the language auto-detection function (it is automotic).\nEnjoy using it\n/start)")


@dp.message_handler(state="wait_language")
async def set_language(message: types.Message, state: FSMContext):
    lang_markup = message.text

    if lang_markup == "English":
        await message.reply("Chosen language: English")
        await state.update_data(language="en")
    elif lang_markup == "Русский":
        await message.reply("Выбранный язык: Русский")
        await state.update_data(language="ru")
    elif lang_markup=="Français":
        await message.reply("Langue choisie: Français")
        await state.update_data(language="fr")
    elif lang_markup=="Deutsch":
        await message.reply("Ausgewählte Sprache: Deutsch")
        await state.update_data(language="de")

    await state.set_state("ask_request")


@dp.message_handler(state="ask_request")
async def find_on_wiki(message: types.Message, state: FSMContext):
    data = await state.get_data()
    language = data['language']

    txt, url = getwiki(message.text, language)
    if url:
        button = InlineKeyboardButton('Ссылка на статью Wikipedia', url=url)
        kb = InlineKeyboardMarkup().add(button)
        await message.answer(txt, reply_markup=kb)
    else:
        await message.answer(txt)


def getwiki(text, language: str):
    try:
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
