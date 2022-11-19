from time import sleep
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from config import admin
from config import API_TOKEN as token
import keyboard as kb
import functions as func
import sqlite3
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)
connection = sqlite3.connect('data.db')
print("⛩️ Connection database...")
sleep(4)
print("✅ Database connected")
q = connection.cursor()

print(f"Bot username:")
botun = input(" ")
if botun == " ":
	sleep(2)
	print("No bot username")
else:
	sleep(3)
	print(f"💡 Bot [{botun}] started")

TEXT = """<b>
👨‍🎓 Internet-talk rules:

🚫 Do not send just <u>'Hello'</u>
🚫 Do not <u>advertise</u>
🚫 Do not <u>insult</u>
🚫 Do not split message
✅ Write your question in <u>one message</u>
</b>
"""

markup = InlineKeyboardMarkup(row_width=2)

markup.add(
	InlineKeyboardButton(text='⭐ Owner', url='https://t.me/kamolgks'),
	
	

class st(StatesGroup):
	item = State()
	item2 = State()
	item3 = State()
	item4 = State()
	item5 = State() 

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	print(f"Bot started by: {message.from_user.id}")
	await message.answer_video(
		video="https://te.legra.ph/file/79daf5a219e88b907375b.mp4", 
		caption='🪄 Welcome to my feedback bot, You may contact with me\n▫️Write your message and my host will answer you!\n▫️Please read /nometa',
		parse_mode= 'HTML',
		reply_markup=get_menu('startmenu'),
	)

@dp.message_handler(commands=['login'])
async def handfler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			await message.answer('💓 Welcome to admin panel', parse_mode= 'Markdown', reply_markup=kb.adm)
		else:
			await message.answer('🚫 You are not admin')

@dp.message_handler(commands=['nometa'])
async def wtf(message: types.Message, state: FSMContext):
	await message.answer(TEXT, parse_mode='HTML')

@dp.message_handler(content_types=['text'], text='↩️ Back')
async def handledr(message: types.Message, state: FSMContext):
	await message.answer('👋🏻*Cancelled!*', parse_mode='Markdown', reply_markup=kb.menu)

@dp.message_handler(content_types=['text'], text='🔅 Black list')
async def handlaer(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			q.execute(f"SELECT * FROM users WHERE block == 1")
			result = q.fetchall()
			sl = []
			for index in result:
				i = index[0]
				sl.append(i)

			ids = '\n'.join(map(str, sl))
			await message.answer(f'<b>🆔 Black List :</b>\n{ids}', parse_mode= 'HTML')


@dp.message_handler(content_types=['text'], text='✅ Add to BL')
async def hanadler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	resultk = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			await message.answer('<b>📝 Enter the ID of the user you want to ban.</b>\n\n↩️<b>To cancel, click the button below..</b>', parse_mode= 'HTML', reply_markup=kb.back)
			await st.item3.set()

@dp.message_handler(content_types=['text'], text='📛 Remove from BL')
async def hfandler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			await message.answer('<b>📝 Enter the ID of the user you want to unban..</b>\n\n↩️<b>To cancel, click the button below.</b>', parse_mode= 'HTML', reply_markup=kb.back)
			await st.item4.set()

@dp.message_handler(content_types=['text'], text='☕ Mailing')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			await message.answer('<b>📝 Введи текст для рассылки.</b>\n\n↩️<b>Для отмены нажми на кнопку ниже.</b>', parse_mode= 'HTML', reply_markup=kb.back)
			await st.item.set()

@dp.message_handler(content_types=['text'])
@dp.throttled(func.antiflood, rate=3)
async def h(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			pass
		else:
			await message.answer('✅ *Message has been sended!*', parse_mode='Markdown')
			await bot.send_message(admin, f"<b>(*^_^*) Sempai! You have new message</b>\n\n<b>From :</b> {message.from_user.mention}\n🆔 <b>ID</b>: <code>{message.chat.id}</code>\n<b>📝 Message:</b> {message.text}", reply_markup=kb.fun(message.chat.id), parse_mode='HTML')
	else:
		await message.answer('You are blocked') 

@dp.callback_query_handler(lambda call: True)
async def cal(call, state: FSMContext):
	if 'ans' in call.data:
		a = call.data.index('-ans')
		ids = call.data[:a]
		await call.message.answer('🖊 *Write answer:*', parse_mode= 'Markdown', reply_markup=kb.back)
		await st.item2.set()
		await state.update_data(uid=ids)
	elif 'ignor' in call.data:
		await call.answer('Удалено!')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await state.finish()

@dp.callback_query_handler()
async def callback_handler(call: CallbackQuery):
    if call.data == 'nometa':
        await call.answer(TEXT, show_alert=True)

@dp.message_handler(state=st.item2)
async def proc(message: types.Message, state: FSMContext):
	if message.text == '↩️ Back':
		await message.answer('↩️ *Cancel! i am going back!*', parse_mode= 'Markdown', reply_markup=kb.menu)
		await state.finish()
	else:
		await message.answer('✅ *The message has been sent*', parse_mode= 'Markdown', reply_markup=kb.menu)
		data = await state.get_data()
		id = data.get("uid")
		await state.finish()
		await bot.send_message(id, '<b>☂️ You have received an answer from the Kamol!</b>\n\n<b>✨ Message:</b> {}'.format(message.text), parse_mode= 'HTML')

@dp.message_handler(state=st.item)
async def process_name(message: types.Message, state: FSMContext):
	q.execute(f'SELECT user_id FROM users')
	row = q.fetchall()
	connection.commit()
	text = message.text
	if message.text == '↩️ Back':
		await message.answer('↩️*Cancel! i am going back!*', parse_mode= 'Markdown', reply_markup=kb.adm)
		await state.finish()
	else:
		info = row
		await message.answer('📣*Mailing started!*', parse_mode= 'Markdown', reply_markup=kb.adm)
		for i in range(len(info)):
			try:
				await bot.send_message(info[i][0], str(text))
			except:
				pass
		await message.answer('*☑️ Mailing finished!*', parse_mode= 'Markdown', reply_markup=kb.adm)
		await state.finish()

@dp.message_handler(state=st.item3)
async def proce(message: types.Message, state: FSMContext):
	if message.text == '↩️ Back':
		await message.answer('↩️*Cancel! i am going back!*', parse_mode= 'Markdown', reply_markup=kb.adm)
		await state.finish()
	else:
		if message.text.isdigit():
			q.execute(f"SELECT block FROM users WHERE user_id = {message.text}")
			result = q.fetchall()
			connection.commit()
			if len(result) == 0:
				await message.answer('⛔️ *Such a user is not found in the database!*', parse_mode= 'Markdown', reply_markup=kb.adm)
				await state.finish()
			else:
				a = result[0]
				id = a[0]
				if id == 0:
					q.execute(f"UPDATE users SET block = 1 WHERE user_id = {message.text}")
					connection.commit()
					await message.answer('☑️ *User has been added to BL!*', parse_mode= 'Markdown', reply_markup=kb.adm)
					await state.finish()
					await bot.send_message(message.text, '‼️*You was banned(*‼️', parse_mode= 'Markdown')
				else:
					await message.answer('*⁉️User was in BL*', parse_mode= 'Markdown', reply_markup=kb.adm)
					await state.finish()
		else:
			await message.answer('❌ *Incorrecy ID!*', parse_mode= 'Markdown')

@dp.message_handler(state=st.item4)
async def procr(message: types.Message, state: FSMContext):
	if message.text == '↩️ Back':
		await message.answer('↩️ *Cancel! i am going back!*', parse_mode= 'Markdown', reply_markup=kb.adm)
		await state.finish()
	else:
		if message.text.isdigit():
			q.execute(f"SELECT block FROM users WHERE user_id = {message.text}")
			result = q.fetchall()
			connection.commit()
			if len(result) == 0:
				await message.answer('❌ *Such a user is not found in the database!*', parse_mode= 'Markdown', reply_markup=kb.adm)
				await state.finish()
			else:
				a = result[0]
				id = a[0]
				if id == 1:
					q.execute(f"UPDATE users SET block = 0 WHERE user_id = {message.text}")
					connection.commit()
					await message.answer('*🌸 The user has been successfully unbanned!*', parse_mode= 'Markdown', reply_markup=kb.adm)
					await state.finish()
					await bot.send_message(message.text, '*🌸 You was unbanned!*', parse_mode= 'Markdown')
				else:
					await message.answer('🌝', reply_markup=kb.adm)
					await state.finish()
		else:
			await message.answer('❌ *Incorrect ID!*', parse_mode= 'Markdown')

async def main():
	await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
