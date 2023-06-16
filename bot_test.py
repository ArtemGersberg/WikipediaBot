import re

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


@dp.message_handler(commands=['lang'], state="*")
async def setup_language(message: types.Message, state: FSMContext):
    await message.reply("Select the input language", reply_markup=lang_markup)
    await state.set_state("wait_language")


@dp.message_handler(commands=['help'], state="*")
async def get_help(message: types.Message, state: FSMContext):
    await message.reply("Select a language:", reply_markup=lang_markup)
    await state.set_state("wait_help")

@dp.message_handler(state="wait_help")
async def set_language2(message: types.Message, state: FSMContext):
    lang_markup = message.text
    await state.set_state("")
    if lang_markup == "English🇺🇸":
        await message.reply(f"Welcome to Wikipedia for Telegram.\nThis bot can quickly search for the meanings of the words you are interested in.\nYou can also choose the input language from the 12 available.\nYou cannot enter messages in a language that does not correspond to the selected one!\nBot Commands:\n/start - start the bot\n/help - instructions and commands of the bot\n/lang - select the input language\n/opwiki - open the Wikipedia site",reply_markup=ReplyKeyboardRemove())
    elif lang_markup == "Русский🇷🇺":
        await message.reply("Добро пожаловать в Википедию для Telegram.\nЭтот бот может быстро выполнять поиск значений интересующих вас слов.\nВы также можете выбрать язык ввода из 12 доступных.\nНельзя вводить сообщенния на языке не соответствующему выбранному!\nКоманды бота:\n/start - запустить бота\n/help - инструкция и команды бота\n/lang - выбор языка ввода\n/opwiki - открыть сайт Wikipedia",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Français🇫🇷":
        await message.reply("Bienvenue sur Wikipedia pour Telegram.\nCe bot peut rapidement rechercher les significations des mots qui vous intéressent.\nVous pouvez également choisir la langue d'entrée parmi les 12 disponibles.\nVous ne pouvez pas entrer un message dans une langue qui ne correspond pas à la langue sélectionnée!\nCommandes du bot: \n/start-démarrer le bot\n /help-instructions et commandes du bot\n/lang-sélection de la langue d'entrée\n/opwiki-ouvrir le site Wikipedia",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Deutsch🇩🇪":
        await message.reply("Willkommen bei Wikipedia für Telegram.\nDieser Bot kann schnell nach den Bedeutungen der Wörter suchen, die Sie interessieren.\nSie können auch die Eingabesprache aus den 12 verfügbaren Sprachen auswählen.\nSie können keine Nachrichten in einer Sprache eingeben, die nicht der ausgewählten Sprache entspricht!\nBot-Befehle:\n/start - Bot starten\n/help - Bot-Anweisungen und Befehle\n/lang - Eingabesprache auswählen\n/opwiki - Wikipedia-Webseite öffnen",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Español🇪🇸":
        await message.reply("Bienvenido a Wikipedia para Telegram.\nEste bot puede buscar rápidamente los significados de las palabras que le interesan.\nTambién puede elegir el idioma de entrada de los 12 disponibles.\n¡No se puede escribir un mensaje en un idioma que no sea el idioma seleccionado!\nComandos bot:\n/start-iniciar bot\n/help-instrucciones y comandos bot\n/lang-selección de idioma de entrada \n/opwiki-abrir Wikipedia",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Italiano🇮🇹":
        await message.reply("Benvenuto su Wikipedia per Telegram.\nQuesto bot può cercare rapidamente i significati delle parole che ti interessano.\nPuoi anche scegliere la lingua di input tra le 12 Disponibili.\nNon è possibile inserire messaggi in una lingua diversa da quella selezionata!\n Comandi Bot: \n/start-Avvia il bot\n/help-istruzioni e comandi Bot\n/lang-seleziona la lingua di input\n/opwiki-apri il sito Wikipedia",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Svensk🇸🇪":
        await message.reply("Välkommen till Wikipedia för Telegram.\nDenna bot kan snabbt söka efter betydelsen av de ord du är intresserad av.\nDu kan också välja inmatningsspråk från 12 tillgängliga.\nDu kan inte ange meddelanden på ett språk som inte motsvarar det valda!\n Bot-kommandon: \n/start-Starta bot\n/help-instruktioner och kommandon för bot\n/lang-välj inmatningsspråk\n/opwiki-öppna Wikipedia-webbplatsen",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Српски🇷🇸":
        await message.reply("Добродошли на Википедију за Телеграм.\nОвај бот може брзо да претражује значења речи које вас занимају.\nТакође можете одабрати језик уноса од 12 доступних.\nНе можете уносити поруке на језику који не одговара изабраном!\n Команде бота:\n/start-Покрени бота\n/help-упутства и команде бота\n/lang - избор језика уноса\n/opwiki-отворите веб локацију Википедиа",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Polski🇵🇱":
        await message.reply("Witamy w Wikipedii Dla telegramu.\nTen bot może szybko wyszukiwać znaczenia słów, które Cię interesują.\nMożesz także wybrać język wprowadzania spośród 12 dostępnych.\nNie można wpisywać komunikatu w języku nie odpowiadającym wybranemu!\nPolecenia bota: \n/start-Uruchom bota\n/help-instrukcje i polecenia bota\n/lang-wybór języka wejściowego\n/opwiki-otwórz witrynę Wikipedii",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Український🇺🇦":
        await message.reply("Ласкаво просимо до Вікіпедії для Telegram.\nЦей бот може швидко шукати значення слів, які Вас цікавлять.\nВи також можете вибрати мову введення з 12 доступних.\nНе можна вводити повідомлення на мові не відповідає обраному!\nКоманди бота: \n/start-запустити бота \n/help-інструкція та команди бота\n/lang-вибір мови введення \n/opwiki-відкрити сайт Wikipedia",reply_markup=ReplyKeyboardRemove())
    elif lang_markup == "Norsk🇳🇴":
        await message.reply("Velkommen Til Wikipedia For Telegram.\nDenne bot kan raskt søke etter betydningen av ordene du er interessert i.\nDu kan også velge inndataspråk fra de 12 tilgjengelige.\nDu kan ikke skrive inn meldinger på et språk som ikke samsvarer med den valgte!\nBot-Kommandoer:\n/start-start bot\n/hjelp-instruksjoner og kommandoer for bot\n/lang-velg inndataspråk\n/opwiki-åpne Wikipedia-siden",reply_markup=ReplyKeyboardRemove())
    elif lang_markup == "Türk🇹🇷":
        await message.reply("Telegram için Wikipedia'ya hoş geldiniz.\nBu bot, ilgilendiğiniz kelimelerin anlamlarını hızlı bir şekilde arayabilir.\nAyrıca mevcut 12 dilden giriş dilini de seçebilirsiniz.\nSeçilen dille eşleşmeyen dilde iletişim giremezsiniz!\nBot komutları:\n/start - botu başlat \n/help - bot talimatları ve komutları \n/lang - giriş dilini seç\n/opwiki - wikipedia sitesini aç",reply_markup=ReplyKeyboardRemove())
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
    elif lang_markup=="Italiano🇮🇹":
        await message.reply("Vai al sito\n<a href='https://it.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup=="Svensk🇸🇪":
        await message.reply("Gå till hemsidan\n<a href='https://sv.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup == "Српски🇷🇸":
        await message.reply("Линк до чланка Википедиа\n<a href='https://sr.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup == "Polski🇵🇱":
        await message.reply("Przejdź do strony\n<a href='https://pl.wikipedia.org/wiki/'>Wikipedia</a>",parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup == "Український🇺🇦":
        await message.reply("Перейти на сайт\n<a href='https://uk.wikipedia.org/wiki/'>Wikipedia</a>",parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup == "Norsk🇳🇴":
        await message.reply("Gå til nettstedet\n<a href='https://no.wikipedia.org/wiki/'>Wikipedia</a>",parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    elif lang_markup == "Türk🇹🇷":
        await message.reply("Siteye git\n<a href='https://tr.wikipedia.org/wiki/'>Wikipedia</a>", parse_mode="HTML",reply_markup=ReplyKeyboardRemove())

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
    elif lang_markup=="Italiano🇮🇹":
        await message.reply("Lingua selezionata: Italiano🇮🇹\nInviami qualsiasi parola e troverò il suo significato su Wikipedia",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="it")
    elif lang_markup=="Svensk🇸🇪":
        await message.reply("Valt språk: svenska🇸🇪\nSkicka mig något ord och jag kommer att hitta dess betydelse på Wikipedia",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="sv")
    elif lang_markup == "Српски🇷🇸":
        await message.reply("Изабрани језик: српски пошаљите ми било коју реч и наћи ћу њено значење на Википедији",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="sr")
    elif lang_markup == "Polski🇵🇱":
        await message.reply("Wybrany język: serbski \nwyślij mi dowolne słowo,a znajdę jego znaczenie na Wikipedii",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="pl")
    elif lang_markup == "Український🇺🇦":
        await message.reply("Вибрана мова: Українська \nнадішліть мені будь-яке слово,і я знайду його значення на Wikipedia",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="uk")
    elif lang_markup == "Norsk🇳🇴":
        await message.reply("Valgt språk: russisk istedetfor\nsend meg noen ord, og jeg vil finne sin mening på wikipedia",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="no")
    elif lang_markup == "Türk🇹🇷":
        await message.reply("Seçilen dil: Türkçe\nbana herhangi bir kelime gönderin, ben de Wikipedia'da anlamını bulacağım",reply_markup=ReplyKeyboardRemove())
        await state.update_data(language="tr")

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
        elif language == "sv":
            button = InlineKeyboardButton('Länk till Wikipedia-artikeln', url=url)
        elif language == "sr":
            button = InlineKeyboardButton('वЛинк до чланка Википедиа', url=url)
        elif language == "pl":
            button = InlineKeyboardButton('Link do artykułu Wikipedia', url=url)
        elif language == "uk":
            button = InlineKeyboardButton('Посилання на статтю Wikipedia', url=url)
        elif language == "no":
            button = InlineKeyboardButton('Link Til Wikipedia-artikkel', url=url)
        elif language == "tr":
            button = InlineKeyboardButton('Wikipedia makalesine bağlantı', url=url)

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
        elif language == "it":
            return "Non ci sono informazioni su questo nell'enciclopedia, prova a rendere la query più specifica o cerca nel sito Wikipedia", None
        elif language == "sv":
            return "Det finns ingen information om detta i encyklopedin, försök att göra begäran mer specifik eller titta på Wikipedia-webbplatsen", None
        elif language == "sr":
            return "Енциклопедија нема информације о томе, покушајте да упит учините конкретнијим или потражите на веб локацији Википедиа", None
        elif language == "pl":
            return "W encyklopedii nie ma informacji na ten temat, spróbuj sprecyzować zapytanie lub przeszukaj Wikipedię", None
        elif language == "uk":
            return "В енциклопедії немає інформації про це, спробуйте зробити запит більш конкретним або пошукайте на сайті Wikipedia", None
        elif language == "no":
            return 'Det er ingen informasjon om dette i leksikonet, prøv å gjøre forespørselen mer spesifikk eller se På Wikipedia-nettstedet', None
        elif language == "tr":
            return 'Ansiklopedide bu konuda bilgi yoktur, sorguyu daha spesifik hale getirmeye çalışın veya Wikipedia sitesine bakın', None


    except wikipedia.exceptions.DisambiguationError as e:
        e.options
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
