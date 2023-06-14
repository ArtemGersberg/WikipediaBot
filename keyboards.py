from aiogram.types import \
    KeyboardButton, \
    ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, \
    InlineKeyboardMarkup, \
    InlineKeyboardButton

i1 = InlineKeyboardButton(f'Читать дальше... ', callback_data='i2')
i2 = InlineKeyboardButton(f'Перейти на сайт со статьёй→', callback_data='i2')

i4 = InlineKeyboardButton("English", callback_data="en")
i3 = InlineKeyboardButton("Русский", callback_data="ru")

k1 = KeyboardButton("English")
k2 = KeyboardButton("Русский")
k3 = KeyboardButton("Français")
k4 = KeyboardButton("Deutsch")
k5 = KeyboardButton("Español")
k6 = KeyboardButton("中文")
k7 = KeyboardButton("العربية")
k8 = KeyboardButton("Italiano")
k9 = KeyboardButton("िन्दी")
# lang_markup = InlineKeyboardMarkup(row_width=2)
# lang_markup.add(i3).add(i4)

lang_markup = ReplyKeyboardMarkup().add(k1).add(k2).add(k3).add(k4).add(k5).add(k6).add(k7).add(8).add(k9)

ininlinekeyboard = InlineKeyboardMarkup().insert(i1).insert(i2)
