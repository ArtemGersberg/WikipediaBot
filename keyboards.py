from aiogram.types import \
    KeyboardButton, \
    ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, \
    InlineKeyboardMarkup, \
    InlineKeyboardButton



i1 = InlineKeyboardButton(f'Читать дальше... ',callback_data='i2')
i2 = InlineKeyboardButton(f'Перейти на сайт со статьёй→',callback_data='i2')




b1 = KeyboardButton("Английский", request_location=True)
b2 = KeyboardButton("Французский", request_contact=True)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(b1).add(b2)

keyboard2 = ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard2.insert(b1).insert(b2)
ininlinekeyboard=InlineKeyboardMarkup().insert(i1).insert(i2)

