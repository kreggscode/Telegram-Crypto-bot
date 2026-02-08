import requests
from .config import BOT_TOKEN, CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_text(text: str, parse_mode: str = "Markdown"):
    # Telegram limit is 4096 characters. Truncate if extreme.
    if len(text) > 4000:
        text = text[:3997] + "..."
    
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
            # If Markdown fails, try sending as plain text
            if parse_mode == "Markdown":
                print(f"Telegram Markdown failed, retrying without formatting...")
                data.pop("parse_mode", None)
                resp = requests.post(url, data=data, timeout=30)
            
            if resp.status_code != 200:
                print(f"Telegram API Error (Text): {resp.status_code} - {resp.text}")
        return resp
    except Exception as e:
        print(f"Telegram Connection Error: {e}")
        return None


def send_photo(image_url: str, caption: str = ""):
    # Telegram limit for captions is 1024 characters
    if len(caption) > 1000:
        caption = caption[:997] + "..."
    
    url = f"{BASE_URL}/sendPhoto"
    data = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": caption
    }
    try:
        resp = requests.post(url, data=data, timeout=30)
        if resp.status_code != 200:
            print(f"Telegram API Error (Photo): {resp.status_code} - {resp.text}")
        return resp
    except Exception as e:
        print(f"Telegram Photo Connection Error: {e}")
        return None


def send_poll(question: str, options: list[str]):
    import json
    url = f"{BASE_URL}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": json.dumps(options),
        "is_anonymous": False
    }
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
