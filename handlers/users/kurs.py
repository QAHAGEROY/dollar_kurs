from aiogram import types


from loader import dp
import requests


api = '8998d38873dbe676481f6c29'
url = f"https://v6.exchangerate-api.com/v6/{api}/pair/USD/UZS"

text = requests.get(url)
kurs = text.json()
A = kurs['conversion_rate']

@dp.message_handler(commands=("kurs"))
async def bot_help(message: types.Message):
    text = (f"Buguni kurs narxi {A} ga teng")
    
    await message.answer(text)