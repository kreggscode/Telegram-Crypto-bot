import urllib.parse
import requests
import random
from datetime import datetime


def generate_text(prompt: str) -> str:
    """Generate free-form text from Pollinations.ai with dynamic seed for variety."""
    # Add timestamp and random seed to ensure unique responses every time
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    seed = random.randint(1000, 999999)
    
    # Enhance prompt with dynamic elements to prevent repetitive content
    enhanced_prompt = f"{prompt}\n\n[Generation Context: Date={timestamp}, Seed={seed}, Ensure unique and fresh content]"
    
    encoded = urllib.parse.quote(enhanced_prompt)
    url = f"https://text.pollinations.ai/{encoded}"
    resp = requests.get(url, timeout=30)
    if resp.status_code == 200:
        return resp.text.strip()
    return "AI generation failed. Please try again."


def image_url(prompt: str) -> str:
    """Return an image URL from Pollinations based on prompt with random seed."""
    # Add random seed to ensure different images each time
    seed = random.randint(1000, 999999)
    encoded = urllib.parse.quote(prompt)
    return f"https://image.pollinations.ai/prompt/{encoded}?seed={seed}&width=1024&height=1024&nologo=true"

