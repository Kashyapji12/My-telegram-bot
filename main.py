import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from handlers import start, code_execution, file_handler, ai_assistant
import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

async def on_startup(dispatcher):
    logger.info("✅ CodeFlow Bot Started!")
    logger.info("🔥 SIGMA MODE: ACTIVATED! 🔥")

async def on_shutdown(dispatcher):
    logger.info("❌ CodeFlow Bot Stopped!")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)