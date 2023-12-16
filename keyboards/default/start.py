from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📚 Kurslarimiz')],
    [KeyboardButton('📌 Manzillarimiz')],
    [KeyboardButton('✍️ Admin'), KeyboardButton('⚙️ Sozlamalar')]
])

contact = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📞 Telefon raqam yuborish', request_contact=True)]
])

manzil = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📌 Manzil jo\'natish', request_location=True)],
    [KeyboardButton('⬅️ Orqaga')]
])
