from aiogram import types
import asyncio
import tempfile
import os
import re
import random
import config

def get_emojis(count=3):
    return "".join(random.sample(config.SIGMA_EMOJIS, min(count, len(config.SIGMA_EMOJIS))))

async def run_code(message: types.Message):
    """Handle /run command"""
    await message.reply(f"Send code in backticks:\n```python\nprint('hello')\n```\n{get_emojis(2)}")

async def handle_code_snippet(message: types.Message):
    """Execute code"""
    pattern = r'```(\w+)?\n(.*?)\n```'
    match = re.search(pattern, message.text, re.DOTALL)
    
    if not match:
        return
    
    language = match.group(1) or 'python'
    code = match.group(2)
    
    status = await message.reply(f"⚙️ Executing... {get_emojis(2)}")
    
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        process = await asyncio.create_subprocess_shell(
            f'python3 {temp_file}',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=10)
        
        os.unlink(temp_file)
        
        output = (stdout or stderr).decode('utf-8')[:500]
        result = f"✅ Output:\n<code>{output}</code>\n{get_emojis(3)}"
        
        await status.edit_text(result)
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")