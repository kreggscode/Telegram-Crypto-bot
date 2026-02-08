"""
Main Bot Logic - Cryptocurrency Education & Data Bot
"""
from . import pollinations_client as ai
from . import telegram_client as tg
from . import scheduler_logic as sched
from .templates import TEXT_TEMPLATES, IMAGE_TEMPLATES
from .crypto_data_client import crypto_client
from .topic_rotator import get_varied_prompt
import random



def post_crypto_prices():
    """Post top cryptocurrency prices with real-time data"""
    print("Fetching crypto prices...")
    crypto_list = crypto_client.get_top_cryptos(limit=15)
    message = crypto_client.format_price_table(crypto_list)
    # Send without Markdown to avoid parsing errors
    tg.send_text(message, parse_mode=None)


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
    base_prompt = TEXT_TEMPLATES["crypto_education"]
    prompt = get_varied_prompt(base_prompt, "crypto_education")
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_trading_tips():
    """Post cryptocurrency trading tips"""
    base_prompt = TEXT_TEMPLATES["trading_tips"]
    prompt = get_varied_prompt(base_prompt, "trading_tips")
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_crypto_security():
    """Post about cryptocurrency security best practices"""
    base_prompt = TEXT_TEMPLATES["crypto_security"]
    prompt = get_varied_prompt(base_prompt, "crypto_security")
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_defi_explained():
    """Post about DeFi concepts"""
    base_prompt = TEXT_TEMPLATES["defi_explained"]
    prompt = get_varied_prompt(base_prompt, "defi_explained")
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_market_analysis():
    """Post market analysis and trends"""
    base_prompt = TEXT_TEMPLATES["market_analysis"]
    prompt = get_varied_prompt(base_prompt, "market_analysis")
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_crypto_project():
    """Post about a cryptocurrency project"""
    base_prompt = TEXT_TEMPLATES["crypto_project"]
    prompt = get_varied_prompt(base_prompt, "crypto_project")
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_nft_knowledge():
    """Post about NFTs"""
    base_prompt = TEXT_TEMPLATES["nft_knowledge"]
    prompt = get_varied_prompt(base_prompt, "nft_knowledge")
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_beginner_guide():
    """Post beginner-friendly crypto guide"""
    base_prompt = TEXT_TEMPLATES["beginner_guide"]
    prompt = get_varied_prompt(base_prompt, "beginner_guide")
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_crypto_terminology():
    """Post explanation of crypto terms"""
    base_prompt = TEXT_TEMPLATES["crypto_terminology"]
    prompt = get_varied_prompt(base_prompt, "crypto_terminology")
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
    
    # Use topic rotation for varied captions
    base_prompt = TEXT_TEMPLATES[selected_text]
    text_prompt = get_varied_prompt(base_prompt, selected_text)
    img_prompt = IMAGE_TEMPLATES[selected_image]

    caption = ai.generate_text(text_prompt)
    img_url = ai.image_url(img_prompt)

    tg.send_photo(img_url, caption)


def post_poll():
    """Post a cryptocurrency quiz poll in Quiz Mode"""
    poll_prompt = TEXT_TEMPLATES["poll_question"]
    raw = ai.generate_text(poll_prompt)

    try:
        lines = [l.strip() for l in raw.split('\n') if l.strip()]
        q_text = ""
        options = []
        correct_letter = ""
        explanation = ""
        
        for line in lines:
            if line.lower().startswith("question:"):
                q_text = line.split(":", 1)[1].strip()
            elif line.upper().startswith("A:"):
                options.append(line.split(":", 1)[1].strip())
            elif line.upper().startswith("B:"):
                options.append(line.split(":", 1)[1].strip())
            elif line.upper().startswith("C:"):
                options.append(line.split(":", 1)[1].strip())
            elif line.upper().startswith("D:"):
                options.append(line.split(":", 1)[1].strip())
            elif line.lower().startswith("correct:"):
                correct_letter = line.split(":", 1)[1].strip().upper()
            elif line.lower().startswith("explanation:"):
                explanation = line.split(":", 1)[1].strip()
        
        letter_to_index = {"A": 0, "B": 1, "C": 2, "D": 3}
        correct_id = letter_to_index.get(correct_letter[0] if correct_letter else "A", 0)
        
        if q_text and len(options) >= 2:
            tg.send_poll(q_text, options[:10], correct_option_id=correct_id, explanation=explanation)
        else:
            print(f"Poll parsing failed. Raw: {raw[:100]}")
            # Fallback to old simple format if AI ignored instructions
            if "|" in raw:
                q_part, opts_part = raw.split("|", 1)
                tg.send_poll(q_part.strip(), [o.strip() for o in opts_part.split(",")])
    except Exception as e:
        print(f"Error in post_poll: {e}")


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
