from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("contact", "Admin bilan bog'lanish"),
            types.BotCommand("about", "obxavo malumoti va $ kurs"),
            types.BotCommand("kurs", "(usd/uzs)"),
            types.BotCommand("weather", "(Tashkent uchun)"),
        ]
    )
