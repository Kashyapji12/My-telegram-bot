
---

**File 3: handlers/ai_assistant.py**

```python name=handlers/ai_assistant.py
from aiogram import types
import google.generativeai as genai
import config
import logging
from utils.sigma_roaster import sigma_wrap, get_sigma_roast, get_sigma_emojis

logger = logging.getLogger(__name__)

# Configure Gemini API
genai.configure(api_key=config.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

async def ask_ai(message: types.Message):
    """Handle /ask command - Sigma Roasting Edition"""
    
    if not message.text or len(message.text) <= 5:
        roast = get_sigma_roast()
        emojis = get_sigma_emojis(3)
        await message.reply(
            f"{roast}\n\n"
            f"<code>/ask How to reverse a string in Python?</code>\n\n"
            f"{emojis}"
        )
        return
    
    question = message.text[5:].strip()
    
    status_msg = await message.reply(f"🤔 Sigma thinking... {get_sigma_emojis(2)}")
    
    try:
        enhanced_prompt = f"""You are a sigma male coding expert who:
1. Gives expert coding advice
2. Adds motivational roasting (light, funny, not offensive)
3. Uses phrases like "Sigma rule #X", "Bro", "Grindset"
4. Is honest but encouraging

Question: {question}

Answer with sigma attitude! Make it memorable and witty."""
        
        response = model.generate_content(enhanced_prompt)
        answer = response.text
        
        roast = get_sigma_roast()
        emojis = get_sigma_emojis(4)
        
        final_response = f"""
{roast}

<b>💡 Sigma's Answer:</b>

{answer}

{emojis}
"""
        
        if len(final_response) > 4096:
            for chunk in [final_response[i:i+4096] for i in range(0, len(final_response), 4096)]:
                await message.reply(chunk)
        else:
            await status_msg.edit_text(final_response)
    
    except Exception as e:
        logger.error(f"Gemini API Error: {e}")
        roast = get_sigma_roast()
        await status_msg.edit_text(f"💀 {roast}\n\n❌ Error: {str(e)}\n\n{get_sigma_emojis(3)}")

async def handle_ai_file_analysis(message: types.Message, file_path: str):
    """Analyze file with AI - Sigma Roasting Edition"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        prompt = f"""You are a sigma code reviewer who roasts bad code but motivates:

Analyze this code and provide (SIGMA STYLE):
1. What this code does (be honest, even if it's bad)
2. Top 3 bugs/issues (if any)
3. Performance problems (brutal honesty)
4. 3 improvements (motivational way)
5. One sigma rule related to this code

Code: