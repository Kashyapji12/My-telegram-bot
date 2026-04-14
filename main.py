import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from handlers import start, code_execution, file_handler, ai_assistant
import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot)
    
    # Register handlers
    dp.register_message_handler(start.cmd_start, commands=['start'])
    dp.register_message_handler(start.cmd_help, commands=['help'])
    dp.register_message_handler(start.cmd_sigma_on, commands=['sigma_on'])
    dp.register_message_handler(start.cmd_sigma_off, commands=['sigma_off'])
    dp.register_message_handler(ai_assistant.ask_ai, commands=['ask'])
    dp.register_message_handler(code_execution.run_code, commands=['run'])
    dp.register_message_handler(file_handler.handle_file, content_types=['document'])
    dp.register_message_handler(code_execution.handle_code_snippet, regexp=r'^```')
    
    logger.info("✅ CodeFlow Bot Started!")
    logger.info("🔥 SIGMA MODE: ACTIVATED! 🔥")
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())