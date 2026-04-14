import random
import config

def get_sigma_roast():
    """Get random sigma roasting line"""
    return random.choice(config.SIGMA_ROASTS)

def get_sigma_emojis(count=3):
    """Get random premium emojis"""
    return "".join(random.sample(config.SIGMA_EMOJIS, min(count, len(config.SIGMA_EMOJIS))))

def sigma_wrap(response: str, roast_type: str = 'default') -> str:
    """Wrap response with sigma roasting style"""
    roast = get_sigma_roast()
    emojis = get_sigma_emojis(4)
    
    if roast_type == 'error':
        return f"💀 {roast}\n\n{response}\n\n{emojis}"
    elif roast_type == 'success':
        return f"👑 {roast}\n\n{response}\n\n{emojis}"
    elif roast_type == 'analysis':
        return f"🕵️ {roast}\n\n{response}\n\n{emojis}"
    else:
        return f"{roast}\n\n{response}\n\n{emojis}"

def sigma_message(text: str) -> str:
    """Add sigma flair to any message"""
    emojis = get_sigma_emojis(2)
    return f"{text} {emojis}"

def get_sigma_reaction():
    """Get random sigma reaction emoji"""
    return random.choice(config.SIGMA_EMOJIS)