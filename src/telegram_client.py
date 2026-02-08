import requests
from .config import BOT_TOKEN, CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def ensure_markdown_closed(text: str) -> str:
    """Ensure all markdown tags are properly closed to avoid Telegram parser errors."""
    if text.count('```') % 2 != 0:
        text += '\n```'
    if text.count('**') % 2 != 0:
        text += '**'
    if text.count('*') % 2 != 0:
        text += '*'
    if text.count('_') % 2 != 0:
        text += '_'
    return text


def send_text(text: str, parse_mode: str = "Markdown"):
    """Send text message with integrity checks for Markdown."""
    # Telegram limit is 4096 characters. Truncate safely.
    if len(text) > 4000:
        text = text[:3900]
        last_space = text.rfind(' ')
        if last_space > 3500:
            text = text[:last_space]
        text = ensure_markdown_closed(text)
        text += "\n\n...(truncated)"
    
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
    }
    if parse_mode:
        data["parse_mode"] = parse_mode
    
    try:
        resp = requests.post(url, data=data, timeout=30)
        if resp.status_code != 200:
            print(f"Telegram API Error (Text): {resp.status_code} - {resp.text}")
            # Do NOT fallback to plain text if we have markdown entities that would break
        return resp
    except Exception as e:
        print(f"Telegram Connection Error: {e}")
        return None


def send_photo(image_url: str, caption: str = ""):
    """Send photo with protected caption integrity."""
    # Telegram limit for captions is 1024 characters
    if len(caption) > 1000:
        caption = caption[:950]
        last_space = caption.rfind(' ')
        if last_space > 800:
            caption = caption[:last_space]
        caption = ensure_markdown_closed(caption)
        caption += "..."
    
    url = f"{BASE_URL}/sendPhoto"
    data = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": caption,
        "parse_mode": "Markdown"
    }
    try:
        resp = requests.post(url, data=data, timeout=30)
        if resp.status_code != 200:
            print(f"Telegram API Error (Photo): {resp.status_code} - {resp.text}")
        return resp
    except Exception as e:
        print(f"Telegram Photo Connection Error: {e}")
        return None


def send_poll(question: str, options: list[str], correct_option_id: int = None, explanation: str = None):
    """Send a Telegram poll. If correct_option_id is provided, it becomes a Quiz."""
    import json
    url = f"{BASE_URL}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": json.dumps(options),
        "is_anonymous": False
    }

    if correct_option_id is not None:
        data["type"] = "quiz"
        data["correct_option_id"] = correct_option_id
        if explanation:
            data["explanation"] = explanation
            data["explanation_parse_mode"] = "Markdown"

    try:
        resp = requests.post(url, data=data, timeout=30)
        if resp.status_code != 200:
            print(f"Telegram API Error (Poll): {resp.status_code} - {resp.text}")
        return resp
    except Exception as e:
        print(f"Telegram Poll Connection Error: {e}")
        return None


def send_thread(messages: list[str]):
    for msg in messages:
        send_text(msg)
