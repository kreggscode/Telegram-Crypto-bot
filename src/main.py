"""
Main Bot Logic - Cryptocurrency Education & Data Bot
"""
from . import pollinations_client as ai
from . import telegram_client as tg
from . import scheduler_logic as sched
from .templates import TEXT_TEMPLATES, IMAGE_TEMPLATES
from .crypto_data_client import crypto_client
import random


def post_crypto_prices():
    """Post top cryptocurrency prices with real-time data"""
    print("Fetching crypto prices...")
    crypto_list = crypto_client.get_top_cryptos(limit=15)
    message = crypto_client.format_price_table(crypto_list)
    tg.send_text(message)


def post_crypto_news():
    """Post latest cryptocurrency news"""
    print("Fetching crypto news...")
    news_list = crypto_client.get_crypto_news(limit=5)
    message = crypto_client.format_news(news_list)
    tg.send_text(message)


def post_trending_coins():
    """Post trending cryptocurrencies"""
    print("Fetching trending coins...")
    trending = crypto_client.get_trending_coins()
    message = crypto_client.format_trending(trending)
    tg.send_text(message)


def post_crypto_education():
    """Post educational content about cryptocurrency"""
    prompt = TEXT_TEMPLATES["crypto_education"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_trading_tips():
    """Post cryptocurrency trading tips"""
    prompt = TEXT_TEMPLATES["trading_tips"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_crypto_security():
    """Post about cryptocurrency security best practices"""
    prompt = TEXT_TEMPLATES["crypto_security"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_defi_explained():
    """Post about DeFi concepts"""
    prompt = TEXT_TEMPLATES["defi_explained"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_market_analysis():
    """Post market analysis and trends"""
    prompt = TEXT_TEMPLATES["market_analysis"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_crypto_project():
    """Post about a cryptocurrency project"""
    prompt = TEXT_TEMPLATES["crypto_project"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_nft_knowledge():
    """Post about NFTs"""
    prompt = TEXT_TEMPLATES["nft_knowledge"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_beginner_guide():
    """Post beginner-friendly crypto guide"""
    prompt = TEXT_TEMPLATES["beginner_guide"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_crypto_terminology():
    """Post explanation of crypto terms"""
    prompt = TEXT_TEMPLATES["crypto_terminology"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_daily_challenge():
    """Post a daily crypto challenge or quiz"""
    prompt = TEXT_TEMPLATES["daily_challenge"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_image_plus_text():
    """Post a visually impressive crypto image with educational content"""
    # Randomly select a text template
    text_options = [
        "crypto_education", "trading_tips", "defi_explained", 
        "nft_knowledge", "crypto_project", "market_analysis"
    ]
    selected_text = random.choice(text_options)
    
    # Select a crypto image
    image_keys = list(IMAGE_TEMPLATES.keys())
    selected_image = random.choice(image_keys)
    
    text_prompt = TEXT_TEMPLATES[selected_text]
    img_prompt = IMAGE_TEMPLATES[selected_image]

    caption = ai.generate_text(text_prompt)
    img_url = ai.image_url(img_prompt)

    tg.send_photo(img_url, caption)


def post_poll():
    """Post a cryptocurrency quiz poll"""
    poll_prompt = TEXT_TEMPLATES["poll_question"]
    raw = ai.generate_text(poll_prompt)

    # Expect format: "Question? | A, B, C, D"
    if "|" in raw:
        q_part, opts_part = raw.split("|", 1)
        question = q_part.strip()
        options = [o.strip() for o in opts_part.split(",") if o.strip()]
        if len(options) >= 2:
            tg.send_poll(question, options[:10])
        else:
            tg.send_text("Poll generation failed: not enough options.")
    else:
        tg.send_text("Poll generation failed: invalid format from AI.")


def post_thread():
    """Post an educational thread about crypto topics"""
    thread_prompt = TEXT_TEMPLATES["thread_explainer"]
    raw = ai.generate_text(thread_prompt)
    # Split by double-newline into sections
    parts = [p.strip() for p in raw.split("\n\n") if p.strip()]
    if len(parts) == 0:
        tg.send_text(raw)
    else:
        tg.send_thread(parts)


def main():
    """Main entry point - decides what type of post to make"""
    post_type = sched.decide_post_type()
    print(f"Decided post type: {post_type}")

    # Map post types to functions
    post_functions = {
        "crypto_prices": post_crypto_prices,
        "crypto_news": post_crypto_news,
        "trending_coins": post_trending_coins,
        "crypto_education": post_crypto_education,
        "trading_tips": post_trading_tips,
        "crypto_security": post_crypto_security,
        "defi_explained": post_defi_explained,
        "market_analysis": post_market_analysis,
        "crypto_project": post_crypto_project,
        "nft_knowledge": post_nft_knowledge,
        "beginner_guide": post_beginner_guide,
        "crypto_terminology": post_crypto_terminology,
        "daily_challenge": post_daily_challenge,
        "image_plus_text": post_image_plus_text,
        "poll": post_poll,
        "thread": post_thread,
    }

    # Execute the selected post function
    post_function = post_functions.get(post_type)
    if post_function:
        post_function()
    else:
        tg.send_text(f"No valid post type decided: {post_type}")


if __name__ == "__main__":
    main()
