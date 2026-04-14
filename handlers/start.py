from aiogram import types
import random
import config

def get_emojis(count=3):
    return "".join(random.sample(config.SIGMA_EMOJIS, min(count, len(config.SIGMA_EMOJIS))))

async def cmd_start(message: types.Message):
    """Start command"""
    welcome = f"""
{get_emojis(3)} <b>Welcome to CodeFlow - SIGMA Edition!</b> {get_emojis(3)}

Your AI-powered Telegram bot! 

<b>Commands:</b>
/ask - Ask AI questions
/run - Execute code
/help - Full guide
/sigma_on - Max roasting 🔥
/sigma_off - Normal mode

<b>Features:</b>
✅ AI coding help
✅ Code execution
✅ File analysis
✅ Sigma roasting 💀

Type /help for more!
"""
    await message.reply(welcome)

async def cmd_help(message: types.Message):
    """Help command"""
    help_text = f"""
{get_emojis(3)} <b>CodeFlow - SIGMA Guide</b>

<b>Main Commands:</b>
/start - Welcome
/ask <question> - Ask AI
/run - Execute code
/help - This guide
/sigma_on - Roasting ON 🔥
/sigma_off - Normal mode

<b>Upload Files:</b>
Send .py, .js, .java files
Bot analyzes + roasts! 💀

<b>Code Execution:</b>
Send code in backticks:
```python
print("Hello!")