
---

## 📝 **File 9: handlers/ai_assistant.py** (SIMPLIFIED)

```python name=handlers/ai_assistant.py
from aiogram import types
import google.generativeai as genai
import config
import random

genai.configure(api_key=config.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_roast():
    return random.choice(config.SIGMA_ROASTS)

def get_emojis(count=3):
    return "".join(random.sample(config.SIGMA_EMOJIS, min(count, len(config.SIGMA_EMOJIS))))

async def ask_ai(message: types.Message):
    """Handle /ask command"""
    if not message.text or len(message.text) <= 5:
        await message.reply("❌ Ask something!\n/ask <your question>")
        return
    
    question = message.text[5:].strip()
    status = await message.reply("🤔 Thinking...")
    
    try:
        response = model.generate_content(f"Answer this coding question:\n{question}")
        roast = get_roast()
        emojis = get_emojis(3)
        
        answer = f"{roast}\n\n<b>Answer:</b>\n{response.text}\n\n{emojis}"
        
        if len(answer) > 4096:
            await message.reply(response.text)
        else:
            await status.edit_text(answer)
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")

async def handle_ai_file_analysis(message: types.Message, file_path: str):
    """Analyze file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()[:1000]  # First 1000 chars
        
        response = model.generate_content(f"Review this code:\n{code}")
        return response.text
    except:
        return "Could not analyze file"