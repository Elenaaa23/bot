from aiogram.utils import executor
from create_bot import dp
import handlers

async def on_startup(_):
	print('Бот вышел в онлайн')


from handlers import admin




executor.start_polling(dp, skip_updates=True, on_startup=on_startup)