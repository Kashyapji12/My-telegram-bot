from aiogram import types
from utils.sigma_roaster import sigma_message, get_sigma_emojis
import config

async def cmd_start(message: types.Message):
    """Start command - Sigma Welcome"""
    welcome_text = f"""
{get_sigma_emojis(3)} <b>Welcome to CodeFlow - Sigma Edition!</b> {get_sigma_emojis(3)}

Your AI-powered coding companion jo roast bhi karega!

<b>🕶️ Sigma Features:</b>
• <code>/ask</code> - AI se puchho, sigma roasting bhi paao 🔥
��� <code>/run</code> - Code execute kar, result dekh 💀
• Upload files/ZIP for savage analysis 📦

<b>😈 Special Powers:</b>
✅ AI coding help (Gemini - Sigma Mode)
✅ Code execution with brutal feedback
✅ File & ZIP analysis (koi kharabi nahi hogi)
✅ Premium emojis everywhere 💯
✅ Roasting on every response 🚬

<b>⚡ Commands:</b>
1. `/ask` - Coding question pucho
2. `/run` - Code chalao
3. `/sigma_on` - Roasting mode ON (default 😈)
4. `/sigma_off` - Normal mode (boring!)
5. `/help` - Full guide

<b>💡 Pro Tips:</b>
→ Ghalat code upload mat kar, roasting heavy padegi! 💀
→ Comments likha kar, warna refactor timeline extend hoga 📝
→ Variables ka naam samझao, random alphabet nahi! 🧠

<b>🎮 Examples:</b>
/ask "How to optimize Python code?"
/ask "Debug this - (paste code)"

Upload: your_code.py (instant analysis + roasting)

<b>Ready for sigma grindset?</b> Type /help
"""
    await message.reply(welcome_text)

async def cmd_help(message: types.Message):
    """Help command - Sigma Guide"""
    help_text = f"""
{get_sigma_emojis(4)} <b>CodeFlow - SIGMA Mode Guide</b> {get_sigma_emojis(4)}

<b>🎯 Main Commands:</b>

<code>/start</code> - Welcome bhai
<code>/help</code> - This sigma guide
<code>/ask &lt;question&gt;</code> - AI help with roasting
<code>/run</code> - Code execution guide
<code>/sigma_on</code> - Roasting mode ON 🔥
<code>/sigma_off</code> - Normal mode (weak!)

<b>💀 Code Snippets:</b>
Send code in backticks (with roasting included):
```python
print("Hello Sigma!")