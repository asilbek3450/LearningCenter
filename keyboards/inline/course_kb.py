from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

courses = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text='Starter kursi', callback_data='starter'),
    ],
    [
        InlineKeyboardButton(text='Frontend', callback_data='frontend'),
        InlineKeyboardButton(text='Backend', callback_data='backend'),
    ],
    [
        InlineKeyboardButton(text='Grafik Dizayn', callback_data='grafik'),
        InlineKeyboardButton(text='3D Dizayn', callback_data='3d'),
    ],
    [
        InlineKeyboardButton(text='🔙 Orqaga', callback_data='back_to_main'),
    ]
])


registration = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text='📝 Kursga yozilish', callback_data='registration'),
    ],
    [
        InlineKeyboardButton(text='🔙 Orqaga', callback_data='back_to_course'),
    ]
])
