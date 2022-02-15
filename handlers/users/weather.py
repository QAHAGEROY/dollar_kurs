from email.utils import localtime
import requests
from aiogram import types


from loader import dp

city = "tashkent"
api = 'eac4b8dcd3c24aa89ea23609221601'
sayt = f"https://api.weatherapi.com/v1/current.json?key={api}&q={city}"

text = requests.get(sayt)

x = text.json()
location = x['location']['region']
country = x['location']['country']
time = x['location']['localtime']


temp = x['current']['temp_c']

@dp.message_handler(commands=("weather"))
async def bot_help(message: types.Message):

    shablon = f"Siz qidirayotgan mamlakat nomi {country} va siz qidirgan shaxar {location} va vaqti {time} va obxavosi {temp} gradusda"
    await message.answer(shablon)