from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboard import kb_client, kb_back

# from aiogram import types
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):

    await message.answer(f'Привет, {message.from_user.first_name} !')
    await message.answer("Выберите нужный пункт меню, для этого нажмите на кнопку или укажите соответствующую кнопку:\n1 - Ознакомиться с услугами\n2 - Рассчитать стоимость\n3 - Записаться на обслуживание\n4 - Заказать обратный звонок\n5 - Контактные данные автосервиса\n6 - Связаться с колл-центром",reply_markup=kb_client)
    
@dp.message_handler(lambda message: message.text == "Ознакомиться с услугами" or message.text == "1" )
async def without_puree(message: types.Message):
    await message.answer("✓ Автомойка\n✓ Антикор\n✓ Глушитель(снятие/установка)\n✓ Двигатель(ремонт/снятие/установка/сборка/диагностика)\n✓ Замена дисков и колодок\n✓ Подвеска(замена/снятие/установка)\n✓ Проверка, диагностика\n✓ Работы по кондиционированию\n✓ Работы по кузову\n✓ Работы по установке доп оборудования\n✓ Развал/схождение\n✓ Рулевое управление(снятие/установка)\n✓ Слесарные работы\n✓ Техническое обслуживание (бенз,масло,свечи,фильтр и проч)\n✓ Топливная система(снятие/установка)\n✓ Трансмиссия(снятие,установка)\n✓ Электрооборудование(снятие/установка)", reply_markup=kb_back)

@dp.message_handler(lambda message: message.text == "Вернуться в главное меню")
async def without_puree(message: types.Message):
    await message.answer("Выберите нужный пункт меню, для этого нажмите на кнопку или укажите соответствующую кнопку:\n1 - Ознакомиться с услугами\n2 - Рассчитать стоимость\n3 - Записаться на обслуживание\n4 - Заказать обратный звонок\n5 - Контактные данные автосервиса\n6 - Связаться с колл-центром",reply_markup=kb_client)

