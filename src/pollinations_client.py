import urllib.parse
import requests
import random
from datetime import datetime


from .config import POLLINATIONS_API_KEY

def generate_text(prompt: str) -> str:
    """Generate text using Pollinations.ai paid API."""
    if not POLLINATIONS_API_KEY:
        # Fallback to free endpoint if key is missing (optional, but user wants paid)
        print("Warning: POLLINATIONS_API_KEY is not set. Falling back to free endpoint.")
        encoded = urllib.parse.quote(prompt)
        url = f"https://text.pollinations.ai/{encoded}"
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200:
            return resp.text.strip()
        return "AI generation failed. Please try again."

    # Use the paid endpoint
    url = "https://gen.pollinations.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {POLLINATIONS_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Add variety elements
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    seed = random.randint(1000, 999999)
    
    data = {
        "model": "openai",
        "messages": [
            {"role": "system", "content": "You are a professional cryptocurrency analyst. Provide ONLY the requested content without metadata, dates, or introductory/concluding text."},
            {"role": "user", "content": f"{prompt}\n\nSTRICT: Code blocks must be properly closed. No intro/outro. (Ref: {seed})"}
        ],
        "seed": seed
    }
    
    try:
        resp = requests.post(url, headers=headers, json=data, timeout=60)
        if resp.status_code == 200:
            result = resp.json()
            return result["choices"][0]["message"]["content"].strip()
        else:
            print(f"Pollinations API Error: {resp.status_code} - {resp.text}")
            return "AI generation failed. Please try again."
    except Exception as e:
        print(f"Pollinations Connection Error: {e}")
        return "AI generation failed. Please try again."


def image_url(prompt: str) -> str:
    """Return an image URL from Pollinations paid API."""
    seed = random.randint(1000, 999999)
    encoded = urllib.parse.quote(prompt)
    
    # documentation suggests: https://gen.pollinations.ai/image/{prompt}?model=flux
    # and we can add the key as a query param or bearer token.
    # Since it's a URL for Telegram to fetch, query param might be easier if Telegram doesn't support headers for photos.
    # But usually we send the URL to Telegram. If the URL requires a key, we must include it if it's private.
    
    base_url = "https://gen.pollinations.ai/image"
    params = {
        "model": "flux",
        "seed": seed,
        "width": 1024,
        "height": 1024,
        "nologo": "true"
    }
    
    if POLLINATIONS_API_KEY:
        params["key"] = POLLINATIONS_API_KEY
        
    query_string = urllib.parse.urlencode(params)
    return f"{base_url}/{encoded}?{query_string}"

