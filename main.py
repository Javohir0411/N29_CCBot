import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from handlers.command_handlers import command_router
from handlers.message_handlers import message_router
from config import BOT_TOKEN


async def main():
    bot = Bot(
        token=BOT_TOKEN,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )
    await bot.set_my_commands(
        commands=[
            BotCommand(command='start', description='Start/ Botni qayta ishga tushirish'),
            BotCommand(command='help', description="Botdan foydalanish uchun qo'llanma"),
            BotCommand(command='courses', description='Hozirgi vaqtdagi kurslar'),
            BotCommand(command='usd', description='Dollar kursi'),
            BotCommand(command='eur', description='Yevro kursi'),
            BotCommand(command='rub', description='Rubl kursi')
        ]
    )
    dp = Dispatcher()
    dp.include_routers(command_router, message_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot Stopped')
