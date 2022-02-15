import config   # You need use your Telegram Token and Weather Token
import requests
from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=config.TOKEN_TELEGRAM_BOT)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.reply('Hello! Write the city where you want to know the weather: ')


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q="
            f"{message.text}&appid={config.API_TOKEN_WEATHER}&units=metric"
        )
        data = r.json()

        city = data['name']
        temp = data['main']['temp']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        wind = data['wind']['speed']
        weather_info = data['weather'][0]['main']
        if weather_info in config.code_to_smile:
            wd = config.code_to_smile[weather_info]
        else:
            wd = "Look out the window:)"

        await message.reply(f"{datetime.now().strftime('%d/%m/%Y %H:%M')}\nCity: {city}\n"
                            f"Temperature: {temp}° {wd}\n"
                            f"Maximum temperature: {temp_max}°\nMinimal temperature: {temp_min}°\n"
                            f"Wind speed: {wind}\n")
    except:
        await message.reply("Write correct city name")


if __name__ == "__main__":
    executor.start_polling(dp)
