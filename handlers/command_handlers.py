import asyncio
import json
import requests
from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart, Command
from aiogram.utils.chat_action import ChatActionSender
from config import currencies, CBU_URL

command_router = Router()


@command_router.message(CommandStart())
async def start_handler(message: Message):
    s = f"Assalomu aleykum <b>{message.from_user.first_name}</b>!  bizning <b>konverter botimizga</b> xush kelibsiz\n"
    s += "Yanada ko'proq ma'lmot uchun /help tugmasini bosing !"
    await message.answer(text=s, reply_markup=ReplyKeyboardRemove())


@command_router.message(Command('help', prefix='!/#'))
async def help_handle(message: Message):
    s = 'Botdan foydalanish uchun quyidagi buyruqlar(commands)dan foydalanishingiz mumkin\n\n'
    s += "/courses Valyuta kurslari haqida barcha ma'lumot olish uchun\n"
    s += "/usd - USD(dollar) valyutasi kursi haqida ma'lumot olish uchun\n"
    s += "/eur - EUR(yevro) valyutasi kursi haqida ma'lumot olish uchun\n"
    s += "/rub - RUBLE(rubl) valyutasi kursi haqida ma'lumot olish uchun\n\n"
    s += "Agar siz o'zingiz xoxlagan valyutaga konvertatsiya qilmoqchi bo'lsangiz kerakli summani(faqat raqamlarda) yuboring !"

    await message.reply(text=s)


@command_router.message(Command('courses', prefix='!/#'))
async def courses_handler(message: Message):
    async with ChatActionSender.typing(
            bot=message.bot,
            chat_id=message.from_user.id):
        response = requests.get(CBU_URL)
        s = 'Bugunning valyutalar qiymati\n\n'

        for course in response.json():
            if course['Ccy'] in currencies.keys():
                currencies[course['Ccy']]['rate'] = course['Rate']
                s += f"\t- 1 <b>{course['CcyNm_UZ']}</b> - {course['Rate']} ga teng\n\n"
        s += '\n\n'
        await message.answer(text=s)


@command_router.message(Command('usd', prefix='!/#'))
async def usd_handler(message: Message):
    async with ChatActionSender.typing(
            bot=message.bot,
            chat_id=message.from_user.id):
        response = requests.get(f"{CBU_URL}USD/")
        res = response.json()[0]
        s = f"1 <b>{res['CcyNm_EN']}</b> - {res['Rate']} so'm"
        await message.reply(s)


@command_router.message(Command('eur', prefix='!/#'))
async def eur_handler(message: Message):
    async with ChatActionSender.typing(
            bot=message.bot,
            chat_id=message.from_user.id):
        response = requests.get(f"{CBU_URL}EUR/")
        res = response.json()[0]
        s = f"1 <b>{res['CcyNm_EN']}</b> - {res['Rate']} so'm"
        await message.reply(s)


@command_router.message(Command('rub', prefix='!/#'))
async def rubl_handler(message: Message):
    async with ChatActionSender.typing(
            bot=message.bot,
            chat_id=message.from_user.id):
        response = requests.get(f"{CBU_URL}RUB/")
        res = response.json()[0]
        s = f"1 <b>{res['CcyNm_EN']}</b> - {res['Rate']} so'm"
        await message.reply(s)
