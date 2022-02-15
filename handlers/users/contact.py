from aiogram import types


from loader import dp


@dp.message_handler(commands=("contact"))
async def bot_help(message: types.Message):
    contact = "Bot admin murojat : @geroy131990"    
    await message.answer(contact)
