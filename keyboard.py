from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
    types.KeyboardButton('Menu')
)

adm = types.ReplyKeyboardMarkup(resize_keyboard=True)
adm.add(
    types.KeyboardButton('π Black list'),
    types.KeyboardButton('β Add to BL'),
    types.KeyboardButton('π Remove from BL')
)
adm.add(types.KeyboardButton('β Mailing'))

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(
    types.KeyboardButton('β©οΈ Back')
)

def fun(user_id):
    quest = types.InlineKeyboardMarkup(row_width=3)
    quest.add(
        types.InlineKeyboardButton(text='πΈ Answer', callback_data=f'{user_id}-ans'),
        types.InlineKeyboardButton(text='πΆβπ«οΈ Delete', callback_data='ignor')
    )
    return quest
