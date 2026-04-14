import os
from dotenv import load_dotenv

load_dotenv()

# Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN", "8538583987:AAGTvOowcUaCIjlUDn-6im996ptYcXhWdeg")

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyCE7E9MfkRlVL9_gNjp7PvLivDXrt_GhTs")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Admin ID
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# Directories
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
LOGS_DIR = "logs"

# Supported Languages
SUPPORTED_LANGUAGES = {
    'python': 'python3',
    'javascript': 'node',
    'bash': 'bash',
    'cpp': 'g++',
    'java': 'javac',
}

# File limits
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
TIMEOUT = 30  # seconds

# ========== SIGMA MODE SETTINGS ==========

# Sigma Roasting Lines (SAVAGE MODE)
SIGMA_ROASTS = [
    "Bro, is code ko dekh ke toh Python bhi shame se rota hai 💀🚬",
    "Aise bugs toh Windows XP mein bhi nahi dekhe the 🤡😏",
    "Code likhna aata hai ya sirf copy-paste? 🥲🔥",
    "Sigma rule #47: Pehle logic samajh, fir run mar 🕶️⚡",
    "Result dekh ke AI ko bhi ek dum shock laga 😲👑",
    "Bhai, iske liye degree kaat denge college wale 🎓💥",
    "Variables toh naam rakh, random alphabet nahi! 🧠🤌",
    "Oof, kya tareeka tha code todne ka bhai! 💀🫡",
    "Complexity itni ke O(n³) bhi jealous ho jayega 🤖😈",
    "Beta, Stack Overflow bhi thak gaya tumhara help karte-karte 🚀🔮",
    "Code review dekh kar meri neend ud gai 😴💀",
    "Semicolon ek baat hain, logic doosri 🫥🔥",
    "Sigma grindset: Optimize karo bhai, optimize! 💪😎",
    "Recursion dekh ke mera brain freeze ho gaya 🧊🤡",
    "Comments nahi likhe kya? Hieroglyphics samझ jayun? 📝💀",
    "Performance itni slow ki DSL connection bhi fast lagega 🐢⚡",
    "Database queries dekh kar DBA ne resign de diya 😅👑",
    "Error handling? Toh ek hi message hai: YOLO! 🎲🔥",
    "Memory leak itna bada ke titanic doob gaya hota 🚢💥",
    "Production mein iska code deploy mat karna bhai 🛑⚠️"
]

# Premium Telegram Emojis (Sigma Edition)
SIGMA_EMOJIS = [
    "😎", "🤡", "💀", "😏", "🔥", "🥲", "🚬", "🦾", "👑", "🧠", 
    "🤌", "🕶️", "💥", "👏", "🫡", "🚀", "🛡️", "🔮", "����", "🫠",
    "🥹", "😈", "⚡", "💯", "🎯", "🔧", "⚙️", "🎭", "🎪", "🃏",
    "🎲", "💎", "🏆", "🥇", "🎖️", "🏅", "🎗️", "⭐", "✨", "🌟",
    "💫", "🌠", "🔥", "⚔️", "🗡️", "🛠️", "⚒️", "🔨", "🪛", "🪚"
]

# Response Templates (Sigma Style)
SIGMA_RESPONSES = {
    'code_error': "Bhai, ye code toh sirf errors de raha hai 💀\n\n{error}\n\nYeh Sigma rule #1: Debug karke dekh 🔍🕶️",
    'code_success': "Waah! Code chalega toh chalega 😏✨\n\n{output}\n\nSigma moment! 👑🚀",
    'file_analysis': "Teri file dekhi bhai, kya story hai! 📄💀\n\n{analysis}\n\nNext time better code likha kar! 🧠🔥",
    'ai_response': "Tera sawaal sunke mein ne soch samjha 🤔\n\n{response}\n\nSigma grindset: Seekhta reh! 📚👑",
    'zip_analysis': "Poora project dekha bhai, kya madness hai! 📦💀\n\n{analysis}\n\nRefactoring time! 🔧⚡",
    'timeout': "Bhai code itna slow ki snail bhi race jeet le! 🐢💀",
    'big_file': "File itni badi ki universe expand ho gaya! 🌌💥",
}

# Sigma Mode Default
SIGMA_MODE_DEFAULT = True  # Always on by default

# Create directories if not exist
for directory in [UPLOAD_DIR, OUTPUT_DIR, LOGS_DIR]:
    os.makedirs(directory, exist_ok=True)