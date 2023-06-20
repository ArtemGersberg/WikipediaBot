from aiogram.types import \
    KeyboardButton, \
    ReplyKeyboardMarkup


k1 = KeyboardButton("Расчет количества температурно-усадочных швов")
k2 = KeyboardButton("Расчёт количества арматуры(на квадратный метр)")


lang_markup1 = ReplyKeyboardMarkup().add(k1).add(k2)



a1 = KeyboardButton("Однослойное армирование")
a2 = KeyboardButton("Двхслойное армирование")
lang_markup2 = ReplyKeyboardMarkup().add(a1).add(a2)



dem1 = KeyboardButton("8")
dem2 = KeyboardButton("10")
dem3 = KeyboardButton("12")
dem4 = KeyboardButton("14")
dem5 = KeyboardButton("16")
lang_markup3 = ReplyKeyboardMarkup().add(dem1).add(dem2).add(dem3).add(dem4).add(dem5)


shag1 = KeyboardButton("100мм")
shag2 = KeyboardButton("150мм")
shag3 = KeyboardButton("200мм")
shag4 = KeyboardButton("250мм")
shag5 = KeyboardButton("300мм")
lang_markup4 = ReplyKeyboardMarkup().add(shag1).add(shag2).add(shag3).add(shag4).add(shag5)