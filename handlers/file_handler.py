from aiogram import types
import os
import config
from handlers import ai_assistant
import random

def get_emojis(count=3):
    return "".join(random.sample(config.SIGMA_EMOJIS, min(count, len(config.SIGMA_EMOJIS))))

async def handle_file(message: types.Message):
    """Handle file uploads"""
    document = message.document
    
    if document.file_size > config.MAX_FILE_SIZE:
        await message.reply(f"❌ File too large! {get_emojis(2)}")
        return
    
    status = await message.reply(f"📥 Downloading... {get_emojis(2)}")
    
    try:
        file_info = await message.bot.get_file(document.file_id)
        file_path = os.path.join(config.UPLOAD_DIR, document.file_name)
        
        await message.bot.download_file(file_info.file_path, file_path)
        
        if document.file_name.endswith(('.py', '.js', '.java', '.txt')):
            analysis = await ai_assistant.handle_ai_file_analysis(message, file_path)
            await status.edit_text(f"📊 Analysis:\n{analysis}\n\n{get_emojis(3)}")
        else:
            await status.edit_text(f"✅ File uploaded! {get_emojis(2)}")
        
        os.remove(file_path)
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")