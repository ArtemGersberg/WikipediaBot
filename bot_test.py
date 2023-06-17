import re

import aiogram.types
import wikipedia
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils import executor
from keyboards import lang_markup

TOKEN="5977899411:AAGcb-0i30DnLoYOm03uRljSMDD_xBYpOfQ"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state="*")
async def setup_language(message: types.Message, state: FSMContext):
    await message.reply("Select a language:", reply_markup=lang_markup)
    await state.set_state("wait_language")
    #await state.set_state("ask_request")


@dp.message_handler(commands=['lang'], state="*")
async def setup_language(message: types.Message, state: FSMContext):
    await message.reply("Select the input language", reply_markup=lang_markup)
    await state.set_state("wait_language")


@dp.message_handler(commands=['help'], state="*")
async def get_help(message: types.Message, state: FSMContext):
    await message.reply("Select a language:", reply_markup=lang_markup)
    #await message.reply(f"Добро пожаловать в Википедию для Telegram.\nЭтот бот может быстро выполнять поиск значений интересующих вас слов.\nВы также можете выбрать язык ввода из 11 доступных.\nНельзя вводить сообщенния на языке не соответствующему выбранному!\nКоманды бота:\n/start - запустить бота\n/help - инструкция и команды бота\n/lang - выбор языка ввода\n/opwiki - открыть сайт Wikipedia")
    await state.set_state("wait_help")

@dp.message_handler(state="wait_help")
async def set_language2(message: types.Message, state: FSMContext):
    lang_markup = message.text
    await state.set_state("")
    if lang_markup == "English🇺🇸":
        await message.reply(f"Welcome to Wikipedia for Telegram.\nThis bot can quickly search for the meanings of the words you are interested in.\nYou can also choose the input language from the 11 available.\nYou cannot enter messages in a language that does not correspond to the selected one!\nBot Commands:\n/start - start the bot\n/help - instructions and commands of the bot\n/lang - select the input language\n/opwiki - open the Wikipedia site",reply_markup=ReplyKeyboardRemove())
    elif lang_markup == "Русский🇷🇺":
        await message.reply("Добро пожаловать в Википедию для Telegram.\nЭтот бот может быстро выполнять поиск значений интересующих вас слов.\nВы также можете выбрать язык ввода из 11 доступных.\nНельзя вводить сообщенния на языке не соответствующему выбранному!\nКоманды бота:\n/start - запустить бота\n/help - инструкция и команды бота\n/lang - выбор языка ввода\n/opwiki - открыть сайт Wikipedia",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Français🇫🇷":
        await message.reply("Bienvenue sur Wikipedia pour Telegram.\nCe bot peut rapidement rechercher les significations des mots qui vous intéressent.\nVous pouvez également choisir la langue d'entrée parmi les 11 disponibles.\nVous ne pouvez pas entrer un message dans une langue qui ne correspond pas à la langue sélectionnée!\nCommandes du bot: \n/start-démarrer le bot\n /help-instructions et commandes du bot\n/lang-sélection de la langue d'entrée\n/opwiki-ouvrir le site Wikipedia",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Deutsch🇩🇪":
        await message.reply("Willkommen bei Wikipedia für Telegram.\nDieser Bot kann schnell nach den Bedeutungen der Wörter suchen, die Sie interessieren.\nSie können auch die Eingabesprache aus den 11 verfügbaren Sprachen auswählen.\nSie können keine Nachrichten in einer Sprache eingeben, die nicht der ausgewählten Sprache entspricht!\nBot-Befehle:\n/start - Bot starten\n/help - Bot-Anweisungen und Befehle\n/lang - Eingabesprache auswählen\n/opwiki - Wikipedia-Webseite öffnen",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Español🇪🇸":
        await message.reply("Bienvenido a Wikipedia para Telegram.\nEste bot puede buscar rápidamente los significados de las palabras que le interesan.\nTambién puede elegir el idioma de entrada de los 11 disponibles.\n¡No se puede escribir un mensaje en un idioma que no sea el idioma seleccionado!\nComandos bot:\n/start-iniciar bot\n/help-instrucciones y comandos bot\n/lang-selección de idioma de entrada \n/opwiki-abrir Wikipedia",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="中文🇨🇳":
        await message.reply("欢迎来到维基百科的电报。\n这个机器人可以快速搜索您感兴趣的单词的含义。\n您也可以从可用的11中选择输入语言。\n您不能以与所选语言不对应的语言输入消息！\n机器人命令：\n/start-启动机器人\n/help-机器人的指令和命令\n/lang-选择输入语言\n/opwiki-打开维基百科网站",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="🇦🇪العربية":
        await message.reply("مرحبا بكم في ويكيبيديا لبرقية.\nيمكن لهذا الروبوت البحث بسرعة عن معاني الكلمات التي تهتم بها.\nيمكنك أيضا اختيار لغة الإدخال من 11 المتاحة.\nا يمكنك إدخال الرسائل بلغة لا تتوافق مع اللغة المحددة!\n أوامر بوت: \n /opwiki-بدء بوت \n /lang-تعليمات وأوامر بوت \n /help-حدد لغة الإدخال\n/start-افتح موقع ويكيبيديا",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Italiano🇮🇹":
        await message.reply("Benvenuto su Wikipedia per Telegram.\nQuesto bot può cercare rapidamente i significati delle parole che ti interessano.\nPuoi anche scegliere la lingua di input tra le 11 Disponibili.\nNon è possibile inserire messaggi in una lingua diversa da quella selezionata!\n Comandi Bot: \n/start-Avvia il bot\n/help-istruzioni e comandi Bot\n/lang-seleziona la lingua di input\n/opwiki-apri il sito Wikipedia",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="िन्दी🇮🇳":
        await message.reply("टेलीग्राम के लिए विकिपीडिया में आपका स्वागत है । \nयह बॉट जल्दी से उन शब्दों के अर्थ खोज सकता है जिनमें आप रुचि रखते हैं । \nआप उपलब्ध 11 में से इनपुट भाषा भी चुन सकते हैं । \nआप ऐसी भाषा में संदेश दर्ज नहीं कर सकते जो चयनित के अनुरूप नहीं है!बॉट कमांड:\n/start - बॉट शुरू करें\n/help - बॉट के निर्देश और कमांड\n/leng - इनपुट भाषा का चयन करें\n/opwiki - विकिपीडिया साइट खोलें",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Svensk🇸🇪":
        await message.reply("Välkommen till Wikipedia för Telegram.\nDenna bot kan snabbt söka efter betydelsen av de ord du är intresserad av.\nDu kan också välja inmatningsspråk från 11 tillgängliga.\nDu kan inte ange meddelanden på ett språk som inte motsvarar det valda!\n Bot-kommandon: \n/start-Starta bot\n/help-instruktioner och kommandon för bot\n/lang-välj inmatningsspråk\n/opwiki-öppna Wikipedia-webbplatsen",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="日本語🇯🇵":
        await message.reply("電報のためのウィキペディアへようこそ。\nこのボットはすぐにあなたが興味を持っている単語の意味を検索することができます。\nまた、利用可能な11から入力言語を選択することができます。\n選択した言語に対応していない言語でメッセージを入力することはできません！\nBotコマンド：\n/start-ボットを開始\n/help-ボットの指示とコマンド\n/lang-入力言語を選択\n/opwiki-Wikipediaサイトを開きます",reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['opwiki'], state="*")
async def get_help(message: types.Message, state: FSMContext):
    await message.reply("Select a language:", reply_markup=lang_markup)
    await state.set_state("wait_opwiki")

@dp.message_handler(state="wait_opwiki")
async def set_language1(message: types.Message, state: FSMContext):
    lang_markup = message.text
    await state.set_state("")
    if lang_markup == "English🇺🇸":
        await message.reply(f"Go to the website\n<a href='https://en.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup == "Русский🇷🇺":
        await message.reply("Перейти на сайт\n<a href='https://ru.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Français🇫🇷":
        await message.reply("Aller sur le site\n<a href='https://fr.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Deutsch🇩🇪":
        await message.reply("Gehe zur Website\n<a href='https://de.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Español🇪🇸":
        await message.reply("Ir al sitio\n<a href='https://es.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="中文🇨🇳":
        await message.reply("进入网站\n<a href='https://zh.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="🇦🇪العربية":
        await message.reply("انتقل إلى الموقع\n<a href='https://ar.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Italiano🇮🇹":
        await message.reply("Vai al sito\n<a href='https://it.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="िन्दी🇮🇳":
        await message.reply("वेबसाइट पर जाएं\n<a href='https://hi.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Svensk🇸🇪":
        await message.reply("Gå till hemsidan\n<a href='https://sv.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="日本語🇯🇵":
        await message.reply("ウェブサイトに行く\n<a href='https://ja.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())



@dp.message_handler(state="wait_language")
async def set_language(message: types.Message, state: FSMContext):
    lang_markup = message.text
    if lang_markup == "English🇺🇸":
        await message.reply("Chosen language: English🇺🇸\nSend me any word and I will find its meaning on Wikipedia",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="en")
    elif lang_markup == "Русский🇷🇺":
        await message.reply("Выбранный язык: Русский🇷🇺\nОтправьте мне любое слово, и я найду его значение на Wikipedia",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="ru")
    elif lang_markup=="Français🇫🇷":
        await message.reply("Langue choisie: Français🇫🇷\nEnvoyez-moi n'importe quel mot et je trouverai sa signification sur Wikipedia",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="fr")
    elif lang_markup=="Deutsch🇩🇪":
        await message.reply("Ausgewählte Sprache: Deutsch🇩🇪\nSende mir ein beliebiges Wort und ich werde seine Bedeutung auf Wikipedia finden",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="de")
    elif lang_markup=="Español🇪🇸":
        await message.reply("Idioma seleccionado: Español🇪🇸\nEnvíame cualquier palabra y encontraré su significado en Wikipedia",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="es")
    elif lang_markup=="中文🇨🇳":
        await message.reply("选定语言：中文🇨🇳\n给我任何单词，我会在维基百科上找到它的含义",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="zh")
    elif lang_markup=="🇦🇪العربية":
        await message.reply("🇦🇪اللغة المختارة: العربية\nأرسل لي أي كلمة وسأجد معناها على ويكيبيديا")
        await state.update_data(language="ar")
    elif lang_markup=="Italiano🇮🇹":
        await message.reply("Lingua selezionata: Italiano🇮🇹\nInviami qualsiasi parola e troverò il suo significato su Wikipedia",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="it")
    elif lang_markup=="िन्दी🇮🇳":
        await message.reply("चयनित भाषा: हिंदी🇮🇳\nमुझे कोई भी शब्द भेजें और मुझे विकिपीडिया पर इसका अर्थ मिलेगा",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="hi")
    elif lang_markup=="Svensk🇸🇪":
        await message.reply("Valt språk: svenska🇸🇪\nSkicka mig något ord och jag kommer att hitta dess betydelse på Wikipedia",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="sv")
    elif lang_markup=="日本語🇯🇵":
        await message.reply("選択された言語：日本語🇯🇵\n私に任意の単語を送信し、私はWikipedia上でその意味を見つけるでしょう",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="ja")


    await state.set_state("ask_request")
@dp.message_handler(state="ask_request")
async def find_on_wiki(message: types.Message, state: FSMContext):
    data = await state.get_data()
    language = data['language']

    txt, url = getwiki(message.text, language)
    if url:
        if language == "ru":
            button = InlineKeyboardButton('Ссылка на статью Wikipedia', url=url)
        elif language == "en":
            button = InlineKeyboardButton('Link to Wikipedia article', url=url)
        elif language == "fr":
            button = InlineKeyboardButton("Lien vers l'article Wikipédia", url=url)
        elif language == "de":
            button = InlineKeyboardButton('Link zum Wikipedia-Artikel', url=url)
        elif language == "es":
            button = InlineKeyboardButton('Enlace al artículo de Wikipedia', url=url)
        elif language == "it":
            button = InlineKeyboardButton("Link All'articolo di Wikipedia", url=url)
        elif language == "ja":
            button = InlineKeyboardButton('ウィキペディアの記事へのリンク', url=url)
        elif language == "sv":
            button = InlineKeyboardButton('Länk till Wikipedia-artikeln', url=url)
        elif language == "العربية":
            button = InlineKeyboardButton('رابط إلى مقالة ويكيبيديا', url=url)
        elif language == "中文":
            button = InlineKeyboardButton('链接到维基百科文章', url=url)
        elif language == "हिन्दी":
            button = InlineKeyboardButton('विकिपीडिया लेख से लिंक करें', url=url)
        kb = InlineKeyboardMarkup().add(button)
        await message.answer(txt[:1000], reply_markup=kb)
    else:
        await message.answer(txt[:1000] + f"\n<a href='https://{language}.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML")

def getwiki(text, language: str):
    try:
        wikipedia.set_lang(language)
        ny = wikipedia.page(text)
        wikitext = ny.content
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

    except wikipedia.exceptions.PageError as er:
        if language == "ru":
            return 'В энциклопедии нет информации об этом, попробуйте сделать запрос более конкретным или поищите на сайте Wikipedia', None
        elif language == "en":
            return 'There is no information about this in the encyclopedia, try to make the request more specific or look on the Wikipedia website', None
        elif language == "fr":
            return "Il n'y a pas d'informations dans l'encyclopédie à ce sujet, essayez de rendre la requête plus spécifique ou recherchez sur le site Wikipedia", None
        elif language == "de":
            return "Es gibt keine Informationen in der Enzyklopädie darüber, versuchen Sie, die Anfrage spezifischer zu machen oder suchen Sie auf der Wikipedia-Website nach", None
        elif language == "es":
            return "No hay información sobre esto en la enciclopedia, intente hacer una solicitud más específica o busque en el sitio web de Wikipedia", None
        elif language == "中文":
            return "百科全书中没有关于此的信息，请尝试使请求更具体或在维基百科网站上查找", None
        elif language == "العربية":
            return "لا توجد معلومات حول هذا في الموسوعة ، حاول أن تجعل الطلب أكثر تحديدا أو ابحث على موقع ويكيبيديا", None
        elif language == "it":
            return "Non ci sono informazioni su questo nell'enciclopedia, prova a rendere la query più specifica o cerca nel sito Wikipedia", None
        elif language == "हिन्दी":
            return "विश्वकोश में इस बारे में कोई जानकारी नहीं है, अनुरोध को अधिक विशिष्ट बनाने या विकिपीडिया वेबसाइट पर देखने का प्रयास करें", None
        elif language == "ja":
            return "百科事典にはこれに関する情報はなく、リクエストをより具体的にするか、Wikipediaのwebサイトを見てみてください", None
        elif language == "sv":
            return "Det finns ingen information om detta i encyklopedin, försök att göra begäran mer specifik eller titta på Wikipedia-webbplatsen", None

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
#artemg