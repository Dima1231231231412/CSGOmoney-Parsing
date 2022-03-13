import time

from aiogram import Bot, Dispatcher, executor, types
import json
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold,hlink

from main import collection_data

bot = Bot(token=("5195565449:AAFGRTovt55tdpXkE21dHYqAyGLG2w1kj6w"),parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['🔪 Ножи', 'AK-47', '︻デ═一 Винтовки']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Выберите категорию', reply_markup=keyboard)

@dp.message_handler(Text(equals='🔪 Ножи'))
async def get_discount_knives(message: types.Message):
    await message.answer('Пожалуйства подождите...')

    collection_data(type=2)
    with open('result.json',encoding="utf-8") as file:
        data = json.load(file)

    for index,item in enumerate(data):
        card = f'{hlink(item.get("fullname"), item.get("3d"))}\n'\
        f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
        f'{hbold("Цена: ")}${item.get("price")}%🔥'

        if index%20 == 0:
            time.sleep(3)
        await message.answer(card)

@dp.message_handler(Text(equals='︻デ═一 Винтовки'))
async def get_discount_guns(message: types.Message):
    await message.answer('Пожалуйства подождите...')

    collection_data(type=4)
    with open('result.json',encoding="utf-8") as file:
        data = json.load(file)

    for index,item in enumerate(data):
        card = f'{hlink(item.get("fullname"), item.get("3d"))}\n'\
        f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
        f'{hbold("Цена: ")}${item.get("price")}%🔥'

        if index%20 == 0:
            time.sleep(3)
        await message.answer(card)

@dp.message_handler(Text(equals='AK-47'))
async def get_discount_guns(message: types.Message):
    await message.answer('Пожалуйства подождите...')

    collection_data(type=3)
    with open('result.json',encoding="utf-8") as file:
        data = json.load(file)

    for index,item in enumerate(data):
        card = f'{hlink(item.get("fullname"), item.get("3d"))}\n'\
        f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
        f'{hbold("Цена: ")}${item.get("price")}%🔥'

        if index%20 == 0:
            time.sleep(3)
        await message.answer(card)
def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()