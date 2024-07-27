import asyncio
import json
import requests
from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.chat_action import ChatActionSender
from config import currencies, CBU_URL

message_router = Router()


@message_router.message(F.text.isalnum())
async def exchange_handler(message: Message):
    async with ChatActionSender.typing(
            bot=message.bot,
            chat_id=message.from_user.id):
        x = int(message.text)
        response = requests.get(CBU_URL)
        print(type(response.json()))
        dollar = response.json()[0]['Rate']
        euro = response.json()[1]['Rate']
        rubl = response.json()[2]['Rate']
        s = f"{x} so'm:\n"
        s += f"\t- {x / float(dollar):.2f} US dollar\n"
        s += f"\t- {x / float(euro):.2f} Yevro\n"
        s += f"\t- {x / float(rubl):.2f} Rossiya rubli\n\n"
        s += (f"Barcha Ma'lumotlar <a href='https://cbu.uz/uz/arkhiv-kursov-valyut/'>"
              f"O'zbekiston Respublikasi Markaziy Banki</a>dan olindi ")
        await message.reply(
            text=s,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text='Author',
                            url='t.me/javohir_abduhakimoff'
                        ),
                        InlineKeyboardButton(
                            text='CBU',
                            url='https://cbu.uz/oz/'
                        )
                    ]
                ]
            )
        )
