from aiogram.types import \
    KeyboardButton, \
    ReplyKeyboardMarkup


k1 = KeyboardButton("Расчет количества температурно-усадочных швов")
k2 = KeyboardButton("Расчёт количества арматуры")

l1 = KeyboardButton("Расчёт количества арматуры(на квадратный метр)")
l2 = KeyboardButton("Расчёт количества арматуры(на всю площадь)")

lang_markup5 = ReplyKeyboardMarkup().add(l1).add(l2)



lang_markup1 = ReplyKeyboardMarkup().add(k1).add(k2)



a1 = KeyboardButton("Однослойное армирование")
a2 = KeyboardButton("Двухслойное армирование")
lang_markup2 = ReplyKeyboardMarkup().add(a1).add(a2)



dem1 = KeyboardButton("8")
dem2 = KeyboardButton("10")
dem3 = KeyboardButton("12")
dem4 = KeyboardButton("14")
dem5 = KeyboardButton("16")
lang_markup3 = ReplyKeyboardMarkup().add(dem1).add(dem2).add(dem3).add(dem4).add(dem5)


shag1 = KeyboardButton("100")
shag2 = KeyboardButton("150")
shag3 = KeyboardButton("200")
shag4 = KeyboardButton("250")
shag5 = KeyboardButton("300")
lang_markup4 = ReplyKeyboardMarkup().add(shag1).add(shag2).add(shag3).add(shag4).add(shag5)