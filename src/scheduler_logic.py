"""
Scheduler Logic - Determines what type of content to post based on time
Optimized for cryptocurrency content with 5 posts per day —
  crypto prices sent RELIABLY 5 times a day at fixed times.
"""
from datetime import datetime, timedelta, timezone
from .config import TIMEZONE_OFFSET_HOURS
import random


def get_local_hour_24() -> int:
    """Return current local hour (0-23) based on TIMEZONE_OFFSET_HOURS."""
    now_utc = datetime.now(timezone.utc)
    local = now_utc + timedelta(hours=TIMEZONE_OFFSET_HOURS)
    return local.hour


def decide_post_type() -> str:
    """
    Decide what to post based on hour.
    Posts 5 times per day — crypto prices at 5 fixed times, other content fills the rest.

    ALWAYS posts crypto prices at these hours:
      - Slot 1: 6-7 AM   (Morning Open)
      - Slot 2: 10-11 AM (Mid-Morning)
      - Slot 3: 2-3 PM   (Afternoon)
      - Slot 4: 6-7 PM   (Evening)
      - Slot 5: 10-11 PM (Night Close)

    Other hours fall back to varied educational/interactive content.

    Returns one of:
    - "crypto_prices" (Real-time price data - ALWAYS at price slots)
    - "crypto_news" (Latest news)
    - "trending_coins" (Trending cryptocurrencies)
    - "crypto_education" (Educational content)
    - "trading_tips" (Trading advice)
    - "crypto_security" (Security tips)
    - "defi_explained" (DeFi concepts)
    - "market_analysis" (Market trends)
    - "crypto_project" (Project spotlights)
    - "nft_knowledge" (NFT education)
    - "beginner_guide" (Getting started)
    - "crypto_terminology" (Crypto slang)
    - "daily_challenge" (Quiz/Challenge)
    - "image_plus_text" (Visual content)
    - "poll" (Interactive poll)
    - "thread" (Deep-dive thread)
    """
    hour = get_local_hour_24()

    # ── 5 FIXED PRICE SLOTS (always posts crypto_prices with ±1 hour window for GitHub Actions delay) ──
    price_hours = [6, 10, 14, 18, 22]
    if any(abs(hour - slot_hour) <= 1 for slot_hour in price_hours):
        return "crypto_prices"

    # ── EDUCATIONAL / INTERACTIVE SLOTS (fill the remaining runs) ──
    # Morning fill (7-9 AM)
    if 7 <= hour <= 9:
        morning_options = [
            "crypto_news", "trending_coins",
            "crypto_education", "trading_tips",
        ]
        return random.choice(morning_options)

    # Mid-day fill (11 AM - 1 PM)
    elif 11 <= hour <= 13:
        midday_options = [
            "crypto_education", "trading_tips", "crypto_security",
            "defi_explained", "crypto_project", "nft_knowledge",
            "beginner_guide", "crypto_terminology",
        ]
        return random.choice(midday_options)

    # Afternoon fill (3-5 PM)
    elif 15 <= hour <= 17:
        afternoon_options = [
            "crypto_news", "market_analysis",
            "crypto_education", "crypto_project",
        ]
        return random.choice(afternoon_options)

    # Evening fill (7-9 PM)
    elif 19 <= hour <= 21:
        evening_options = [
            "image_plus_text", "poll", "daily_challenge",
            "thread", "market_analysis",
        ]
        return random.choice(evening_options)

    # Late fill (11 PM - 12 AM)
    elif 23 <= hour < 24:
        late_options = [
            "trending_coins", "market_analysis", "crypto_news",
        ]
        return random.choice(late_options)

    # Fallback for manual runs outside scheduled times
    else:
        all_options = [
            "crypto_prices", "crypto_news", "trending_coins",
            "crypto_education", "trading_tips", "crypto_security",
            "defi_explained", "market_analysis", "crypto_project",
            "nft_knowledge", "beginner_guide", "crypto_terminology",
            "daily_challenge", "image_plus_text", "poll", "thread",
        ]
        return random.choice(all_options)
