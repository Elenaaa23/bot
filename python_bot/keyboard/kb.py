from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

kb_client = ReplyKeyboardMarkup(
    keyboard=[
        
        [KeyboardButton(text='Ознакомиться с услугами')],
        [KeyboardButton(text='Рассчитать стоимость')],
        [KeyboardButton(text='Записаться на обслуживание')],
        [KeyboardButton(text='Заказать обратный звонок')],
        [KeyboardButton(text='Контактные данные автосервиса')],
        [KeyboardButton(text='Связаться с колл-центром')]
        
    ],
    resize_keyboard=True
)

kb_back = ReplyKeyboardMarkup(
    keyboard=[
        
        [KeyboardButton(text='Вернуться в главное меню')]
        
    ],
    resize_keyboard=True
) 
