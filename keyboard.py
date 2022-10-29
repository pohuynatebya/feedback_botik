from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
    types.KeyboardButton('Menu')
)

adm = types.ReplyKeyboardMarkup(resize_keyboard=True)
adm.add(
    types.KeyboardButton('🔅 Black list'),
    types.KeyboardButton('✅ Add to BL'),
    types.KeyboardButton('📛 Remove from BL')
)
adm.add(types.KeyboardButton('☕ Mailing'))

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(
    types.KeyboardButton('↩️ Back')
)

def fun(user_id):
    quest = types.InlineKeyboardMarkup(row_width=3)
    quest.add(
        types.InlineKeyboardButton(text='😸 Answer', callback_data=f'{user_id}-ans'),
        types.InlineKeyboardButton(text='😶‍🌫️ Delete', callback_data='ignor')
    )
    return quest
