from aiogram import types
import asyncio
import tempfile
import os
import logging
import re
import config
from utils.sigma_roaster import get_sigma_roast, get_sigma_emojis, sigma_wrap

logger = logging.getLogger(__name__)

async def run_code(message: types.Message):
    """Handle /run command - Sigma Edition"""
    emojis = get_sigma_emojis(3)
    await message.reply(
        f"⚡ {get_sigma_roast()}\n\n"
        f"Send code in backticks (Sigma will execute):\n\n"
        f"<code>```python\nprint('Hello Sigma!')\n```</code>\n\n"
        f"{emojis}"
    )

async def handle_code_snippet(message: types.Message):
    """Execute code from message - Sigma Roasting"""
    
    pattern = r'```(\w+)?\n(.*?)\n```'
    match = re.search(pattern, message.text, re.DOTALL)
    
    if not match:
        return
    
    language = match.group(1) or 'python'
    code = match.group(2)
    
    roast = get_sigma_roast()
    status_msg = await message.reply(f"⚙️ {roast}\n\nExecuting sigma code... {get_sigma_emojis(2)}")
    
    try:
        with tempfile.NamedTemporaryFile(
            mode='w',
            suffix=f'.{get_extension(language)}',
            delete=False
        ) as f:
            f.write(code)
            temp_file = f.name
        
        result = await execute_code(language, temp_file, config.TIMEOUT)
        os.unlink(temp_file)
        
        if result:
            output = f"✅ Sigma's Execution Results:\n\n<code>{result}</code>"
        else:
            output = "✅ Code executed (no output generated) 🤷"
        
        success_roast = get_sigma_roast()
        emojis = get_sigma_emojis(4)
        final_msg = f"{success_roast}\n\n{output}\n\n{emojis}"
        
        if len(final_msg) > 4096:
            with open(f"{config.OUTPUT_DIR}/output.txt", 'w') as f:
                f.write(result)
            await message.reply_document(
                open(f"{config.OUTPUT_DIR}/output.txt", 'rb'),
                caption=f"📄 Output (too thicc)\n\n{get_sigma_emojis(3)}"
            )
        else:
            await status_msg.edit_text(final_msg)
    
    except asyncio.TimeoutError:
        timeout_roast = get_sigma_roast()
        await status_msg.edit_text(
            f"⏱️ {timeout_roast}\n\n"
            f"Code itna slow likha hai ki infinity loop bhi shame khaye! 🐢💀\n\n"
            f"{get_sigma_emojis(4)}"
        )
    
    except Exception as e:
        error_roast = get_sigma_roast()
        await status_msg.edit_text(
            f"💥 {error_roast}\n\n"
            f"❌ Error:\n<code>{str(e)}</code>\n\n"
            f"{get_sigma_emojis(3)}"
        )

async def execute_code(language: str, file_path: str, timeout: int) -> str:
    """Execute code in sandbox"""
    commands = {
        'python': f'python3 {file_path}',
        'javascript': f'node {file_path}',
        'bash': f'bash {file_path}',
    }
    
    cmd = commands.get(language, f'python3 {file_path}')
    
    try:
        process = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await asyncio.wait_for(
            process.communicate(),
            timeout=timeout
        )
        
        output = stdout.decode('utf-8') or stderr.decode('utf-8')
        return output[:2000]
    
    except asyncio.TimeoutError:
        raise TimeoutError("Code execution timeout!")

def get_extension(language: str) -> str:
    """Get file extension"""
    extensions = {
        'python': 'py',
        'javascript': 'js',
        'bash': 'sh',
        'cpp': 'cpp',
        'java': 'java',
    }
    return extensions.get(language, 'txt')