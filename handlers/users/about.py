from aiogram import types


from loader import dp


@dp.message_handler(commands=("about"))
async def bot_help(message: types.Message):
    text = ("Bu bot obxavo va $ kursi haqida")
    
    await message.answer(text)
