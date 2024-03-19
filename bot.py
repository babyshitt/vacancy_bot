import logging
import asyncio
from aiogram import Bot, Dispatcher

from vacancy_bot.my_bot.config import config
from vacancy_bot.my_bot.handlers import main_handlers


logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=config.bot_token.get_secret_value())


async def main():
    dp = Dispatcher()
    dp.include_routers(main_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
