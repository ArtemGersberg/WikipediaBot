from aiogram.types import \
    KeyboardButton, \
    ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, \
    InlineKeyboardMarkup, \
    InlineKeyboardButton

k1 = KeyboardButton("English🇺🇸")
k2 = KeyboardButton("Русский🇷🇺")
k3 = KeyboardButton("Français🇫🇷")
k4 = KeyboardButton("Deutsch🇩🇪")
k5 = KeyboardButton("Español🇪🇸")
k6 = KeyboardButton("中文🇨🇳")
k7 = KeyboardButton("🇦🇪العربية")
k8 = KeyboardButton("Italiano🇮🇹")
k9 = KeyboardButton("िन्दी🇮🇳")
k10 = KeyboardButton("Svensk🇸🇪")
k11 = KeyboardButton("日本語🇯🇵")

lang_markup = ReplyKeyboardMarkup().add(k1).add(k2).add(k3).add(k4).add(k5).add(k6).add(k7).add(k8).add(k9).add(k10).add(k11)

