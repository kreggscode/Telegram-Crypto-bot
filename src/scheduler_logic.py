"""
Scheduler Logic - Determines what type of content to post based on time
Optimized for cryptocurrency content with 3-4 posts per day
"""
from datetime import datetime, timedelta
from .config import TIMEZONE_OFFSET_HOURS
import random


def get_local_hour_24() -> int:
    """Return current local hour (0-23) based on TIMEZONE_OFFSET_HOURS."""
    now_utc = datetime.utcnow()
    local = now_utc + timedelta(hours=TIMEZONE_OFFSET_HOURS)
    return local.hour


def decide_post_type() -> str:
    """
    Decide what to post based on hour.
    Posts 3-4 times per day optimized for crypto content:
    - Morning (8-10 AM): Crypto Prices & Market Data (PRIORITY)
    - Afternoon (2-4 PM): Educational Content & News
    - Evening (8-10 PM): Interactive Content (Polls, Challenges, Images)
    - Late Night (11 PM-12 AM): Trending Coins & Analysis (Optional)

    Returns one of:
    - "crypto_prices" (Real-time price data - MOST IMPORTANT)
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

    # Morning Post (8-10 AM): CRYPTO PRICES & MARKET DATA (Priority!)
    if 8 <= hour < 10:
        # 70% chance of prices, 30% chance of news/trending
        morning_weighted = (
            ["crypto_prices"] * 7 + 
            ["crypto_news"] * 2 + 
            ["trending_coins"] * 1
        )
        return random.choice(morning_weighted)
    
    # Afternoon Post (2-4 PM): EDUCATIONAL CONTENT & NEWS
    elif 14 <= hour < 16:
        afternoon_options = [
            "crypto_education", "trading_tips", "crypto_security",
            "defi_explained", "crypto_project", "nft_knowledge",
            "beginner_guide", "crypto_terminology", "crypto_news"
        ]
        return random.choice(afternoon_options)
    
    # Evening Post (8-10 PM): INTERACTIVE & VISUAL CONTENT
    elif 20 <= hour < 22:
        evening_options = [
            "image_plus_text", "poll", "daily_challenge",
            "thread", "market_analysis"
        ]
        return random.choice(evening_options)
    
    # Late Night Post (11 PM-12 AM): TRENDING & ANALYSIS (Optional 4th post)
    elif 23 <= hour < 24:
        late_night_options = [
            "trending_coins", "market_analysis", "crypto_prices"
        ]
        return random.choice(late_night_options)
    
    # Fallback for manual runs outside scheduled times
    else:
        all_options = [
            "crypto_prices", "crypto_news", "trending_coins",
            "crypto_education", "trading_tips", "crypto_security",
            "defi_explained", "market_analysis", "crypto_project",
            "nft_knowledge", "beginner_guide", "crypto_terminology",
            "daily_challenge", "image_plus_text", "poll", "thread"
        ]
        return random.choice(all_options)
