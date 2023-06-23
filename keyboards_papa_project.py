from aiogram.types import \
    KeyboardButton, \
    ReplyKeyboardMarkup


k1 = KeyboardButton("Расчет количества температурно-усадочных швов")
k2 = KeyboardButton("Расчёт количества арматуры")
lang_markup1 = ReplyKeyboardMarkup().add(k1).add(k2)

l1 = KeyboardButton("Расчёт количества арматуры(на квадратный метр)")
l2 = KeyboardButton("Расчёт количества арматуры(на всю площадь)")
lang_markup5 = ReplyKeyboardMarkup().add(l1).add(l2)

a1 = KeyboardButton("Полимерные полы")
a2 = KeyboardButton("Бетонные полы")
lang_markup6 = ReplyKeyboardMarkup().add(a1).add(a2)

p1 = KeyboardButton("Эпоксидные")
p2 = KeyboardButton("Полиуретановые")
p3 = KeyboardButton("Полиуретан-цементные")
lang_markup7 = ReplyKeyboardMarkup().add(p1).add(p2).add(p3)

b1 = KeyboardButton("Однослойное армирование")
b2 = KeyboardButton("Двухслойное армирование")
lang_markup2 = ReplyKeyboardMarkup().add(b1).add(b2)

dem1 = KeyboardButton("8 мм")
dem2 = KeyboardButton("10 мм")
dem3 = KeyboardButton("12 мм")
dem4 = KeyboardButton("14 мм")
dem5 = KeyboardButton("16 мм")
lang_markup3 = ReplyKeyboardMarkup().add(dem1).add(dem2).add(dem3).add(dem4).add(dem5)

shag1 = KeyboardButton("100 мм")
shag2 = KeyboardButton("150 мм")
shag3 = KeyboardButton("200 мм")
shag4 = KeyboardButton("250 мм")
shag5 = KeyboardButton("300 мм")
lang_markup4 = ReplyKeyboardMarkup().add(shag1).add(shag2).add(shag3).add(shag4).add(shag5)

r1 = KeyboardButton("Гладкое")
r2 = KeyboardButton("Шероховатое")
r3 = KeyboardButton("Декоративное")
lang_markup8 = ReplyKeyboardMarkup().add(r1).add(r2).add(r3)

e1 = KeyboardButton("1 мм")
e2 = KeyboardButton("2 мм")
e3 = KeyboardButton("3 мм")
lang_markup9 = ReplyKeyboardMarkup().add(e1).add(e2).add(e3)

i1 = KeyboardButton("1,5 мм")
i2 = KeyboardButton("2,5 мм")
i3 = KeyboardButton("4 мм")
i4 = KeyboardButton("5 мм")
lang_markup10 = ReplyKeyboardMarkup().add(i1).add(i2).add(i3).add(i4)

u1 = KeyboardButton("1 мм")
u2 = KeyboardButton("2 мм")
lang_markup11 = ReplyKeyboardMarkup().add(u1).add(u2)