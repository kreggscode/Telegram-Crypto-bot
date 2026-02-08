import requests
from .config import BOT_TOKEN, CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def ensure_markdown_closed(text: str) -> str:
    """Hyper-reliable balancing of Telegram Markdown V1 tags."""
    if text.count('```') % 2 != 0: text += '\n```'
    code_parts = text.split('```')
    for i in range(0, len(code_parts), 2):
        if code_parts[i].count('*') % 2 != 0: code_parts[i] += '*'
        if code_parts[i].count('_') % 2 != 0: code_parts[i] += '_'
        if code_parts[i].count('`') % 2 != 0: code_parts[i] += '`'
        if code_parts[i].count('[') > code_parts[i].count(']'): code_parts[i] += ']'
    return '```'.join(code_parts)


def send_text(text: str, parse_mode: str = "Markdown"):
    """Send text with guaranteed formatting for links."""
    if len(text) > 4000: text = text[:3800] + "\n\n...(truncated)"
    text = ensure_markdown_closed(text)
    url = f"{BASE_URL}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": parse_mode, "disable_web_page_preview": True}
    try:
        resp = requests.post(url, json=payload, timeout=30)
        if resp.status_code != 200:
            payload["text"] = text.replace("_", "\\_")
            resp = requests.post(url, json=payload, timeout=30)
            if resp.status_code != 200:
                payload.pop("parse_mode", None)
                payload["text"] = text
                resp = requests.post(url, json=payload, timeout=30)
        return resp
    except Exception as e:
        print(f"Telegram Error: {e}")
        return None


def send_photo(image_url: str, caption: str = ""):
    """Send photo with guaranteed caption integrity."""
    if len(caption) > 1000: caption = caption[:950] + "..."
    caption = ensure_markdown_closed(caption)
    url = f"{BASE_URL}/sendPhoto"
    payload = {"chat_id": CHAT_ID, "photo": image_url, "caption": caption, "parse_mode": "Markdown"}
    try:
        resp = requests.post(url, json=payload, timeout=30)
        if resp.status_code != 200:
            payload["caption"] = caption.replace("_", "\\_")
            resp = requests.post(url, json=payload, timeout=30)
            if resp.status_code != 200:
                payload.pop("parse_mode", None)
                payload["caption"] = caption
                resp = requests.post(url, json=payload, timeout=30)
        return resp
    except Exception as e:
        print(f"Photo Error: {e}")
        return None


def send_poll(question: str, options: list[str], correct_option_id: int = None, explanation: str = None):
    """Send a native Telegram Quiz."""
    import json
    url = f"{BASE_URL}/sendPoll"
    payload = {"chat_id": CHAT_ID, "question": question[:300], "options": json.dumps(options[:10]), "is_anonymous": True}
    if correct_option_id is not None:
        payload["type"] = "quiz"
        payload["correct_option_id"] = int(correct_option_id)
        if explanation:
            payload["explanation"] = explanation[:200]
            payload["explanation_parse_mode"] = "Markdown"
    try:
        resp = requests.post(url, json=payload, timeout=30)
        if resp.status_code != 200:
            print(f"Poll Error: {resp.text}")
        return resp
    except Exception as e:
        print(f"Poll Error: {e}")
        return None


def send_thread(messages: list[str]):
    for msg in messages:
        send_text(msg)
