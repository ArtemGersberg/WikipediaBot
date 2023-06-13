from aiogram.types import \
    KeyboardButton, \
    ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, \
    InlineKeyboardMarkup, \
    InlineKeyboardButton



i1 = InlineKeyboardButton(f'Читать дальше... ',callback_data='i2')
i2 = InlineKeyboardButton(f'Перейти на сайт со статьёй→',callback_data='i2')







b1 = KeyboardButton("Поделиться номером", request_location=True)
b2 = KeyboardButton("Больше не хочу никого искать", request_contact=True)
b3 = KeyboardButton("🙋‍♂️")
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(b1).add(b2).add(b3)

keyboard2 = ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard2.insert(b1).insert(b2).insert(b3)
ininlinekeyboard=InlineKeyboardMarkup().insert(i1).insert(i2)

