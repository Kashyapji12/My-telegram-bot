from aiogram import types
import zipfile
import os
import logging
import config
from handlers import ai_assistant
from utils.sigma_roaster import get_sigma_roast, get_sigma_emojis

logger = logging.getLogger(__name__)

async def handle_file(message: types.Message):
    """Handle file uploads - Sigma Edition"""
    
    document = message.document
    file_name = document.file_name
    file_size = document.file_size
    
    if file_size > config.MAX_FILE_SIZE:
        roast = get_sigma_roast()
        await message.reply(
            f"💀 {roast}\n\n"
            f"File itni badi ki NASA ke paas bhi storage nahi hai! 🌌\n\n"
            f"Max: {config.MAX_FILE_SIZE / 1024 / 1024}MB\n\n"
            f"{get_sigma_emojis(3)}"
        )
        return
    
    roast = get_sigma_roast()
    status_msg = await message.reply(f"📥 {roast}\n\nDownloading... {get_sigma_emojis(2)}")
    
    try:
        file_info = await message.bot.get_file(document.file_id)
        file_path = os.path.join(config.UPLOAD_DIR, file_name)
        
        await message.bot.download_file(file_info.file_path, file_path)
        
        if file_name.endswith('.zip'):
            await handle_zip(message, status_msg, file_path)
        elif file_name.endswith(('.py', '.js', '.java', '.cpp', '.txt')):
            await handle_code_file(message, status_msg, file_path)
        else:
            emojis = get_sigma_emojis(3)
            await status_msg.edit_text(f"❌ Unsupported file type bhai! {emojis}")
    
    except Exception as e:
        logger.error(f"File error: {e}")
        roast = get_sigma_roast()
        emojis = get_sigma_emojis(3)
        await status_msg.edit_text(f"💀 {roast}\n\n❌ Error: {str(e)}\n\n{emojis}")

async def handle_zip(message: types.Message, status_msg: types.Message, zip_path: str):
    """Extract and analyze ZIP - Sigma Edition"""
    
    extract_dir = os.path.join(config.UPLOAD_DIR, 'extracted')
    os.makedirs(extract_dir, exist_ok=True)
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        
        code_files = []
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                if file.endswith(('.py', '.js', '.md')):
                    code_files.append(os.path.join(root, file))
        
        if not code_files:
            roast = get_sigma_roast()
            await status_msg.edit_text(
                f"💀 {roast}\n\n"
                f"ZIP mein koi code nahi mil! 📦\n\n"
                f"{get_sigma_emojis(3)}"
            )
            return
        
        roast = get_sigma_roast()
        analysis = f"📦 <b>ZIP Project (Sigma) Analysis</b>\n\n{roast}\n\n"
        analysis += f"📁 Files found: {len(code_files)}\n\n"
        
        summary = await ai_assistant.handle_ai_file_analysis(message, code_files[0])
        
        analysis += f"{summary}"
        
        emojis = get_sigma_emojis(4)
        final_msg = f"{analysis}\n\n{emojis}"
        
        if len(final_msg) > 4096:
            for chunk in [final_msg[i:i+4096] for i in range(0, len(final_msg), 4096)]:
                await message.reply(chunk)
        else:
            await status_msg.edit_text(final_msg)
        
        import shutil
        shutil.rmtree(extract_dir)
    
    except Exception as e:
        logger.error(f"ZIP error: {e}")
        roast = get_sigma_roast()
        emojis = get_sigma_emojis(3)
        await status_msg.edit_text(f"💀 {roast}\n\n❌ Error: {str(e)}\n\n{emojis}")

async def handle_code_file(message: types.Message, status_msg: types.Message, file_path: str):
    """Analyze code file - Sigma Edition"""
    
    try:
        analysis = await ai_assistant.handle_ai_file_analysis(message, file_path)
        
        emojis = get_sigma_emojis(4)
        output = f"{analysis}\n\n{emojis}"
        
        if len(output) > 4096:
            for chunk in [output[i:i+4096] for i in range(0, len(output), 4096)]:
                await message.reply(chunk)
        else:
            await status_msg.edit_text(output)
    
    except Exception as e:
        logger.error(f"Code file error: {e}")
        roast = get_sigma_roast()
        emojis = get_sigma_emojis(3)
        await status_msg.edit_text(f"💀 {roast}\n\n❌ Error: {str(e)}\n\n{emojis}")