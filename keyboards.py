from aiogram.types import \
    KeyboardButton, \
    ReplyKeyboardMarkup, \
    InlineKeyboardMarkup, \
    InlineKeyboardButton

i1 = InlineKeyboardButton(f'Читать дальше... ', callback_data='i2')
i2 = InlineKeyboardButton(f'Перейти на сайт со статьёй→', callback_data='i2')

i4 = InlineKeyboardButton("English", callback_data="en")
i3 = InlineKeyboardButton("Русский", callback_data="ru")

k1 = KeyboardButton("English🇺🇸")
k2 = KeyboardButton("Русский🇷🇺")
k3 = KeyboardButton("Français🇫🇷")
k4 = KeyboardButton("Deutsch🇩🇪")
k5 = KeyboardButton("Español🇪🇸")
k6 = KeyboardButton("Polski🇵🇱")
k7 = KeyboardButton("Italiano🇮🇹")
k8 = KeyboardButton("Svensk🇸🇪")
k9 =KeyboardButton("Српски🇷🇸")
k10 = KeyboardButton("Український🇺🇦")
k11 = KeyboardButton("Norsk🇳🇴")
k12 = KeyboardButton("Türk🇹🇷")



lang_markup = ReplyKeyboardMarkup().add(k1).add(k2).add(k3).add(k4).add(k5).add(k6).add(k8).add(k10).add(k12).add(k7).add(k9).add(k11)

ininlinekeyboard = InlineKeyboardMarkup().insert(i1).insert(i2)
