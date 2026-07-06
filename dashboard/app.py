"""
Flask Dashboard for Manual Crypto Bot Control
"""
import os
import random
from flask import Flask, render_template, redirect, url_for, flash, request
from dotenv import load_dotenv

# Allow dashboard to use same bot config
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"), override=False)

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src import telegram_client as tg
from src import pollinations_client as ai
from src.templates import TEXT_TEMPLATES, IMAGE_TEMPLATES, HASHTAGS
from src.crypto_data_client import crypto_client

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")

CURRENT_POST_TYPE = None

# Wrap tg.send_text to automatically append hashtags based on CURRENT_POST_TYPE
_original_send_text = tg.send_text
def custom_send_text(text, parse_mode="Markdown"):
    global CURRENT_POST_TYPE
    if CURRENT_POST_TYPE and CURRENT_POST_TYPE != "thread":
        tags = HASHTAGS.get(CURRENT_POST_TYPE, "")
        text = text + tags
    return _original_send_text(text, parse_mode)
tg.send_text = custom_send_text

# Wrap tg.send_photo to automatically append hashtags based on CURRENT_POST_TYPE
_original_send_photo = tg.send_photo
def custom_send_photo(image_url, caption=""):
    global CURRENT_POST_TYPE
    if CURRENT_POST_TYPE:
        tags = HASHTAGS.get(CURRENT_POST_TYPE, "")
        caption = caption + tags
    return _original_send_photo(image_url, caption)
tg.send_photo = custom_send_photo

@app.before_request
def set_post_type():
    global CURRENT_POST_TYPE
    path = request.path
    if path.startswith("/send/"):
        post_type = path.split("/")[-1].replace("-", "_")
        if post_type == "image_post":
            post_type = "image_plus_text"
        CURRENT_POST_TYPE = post_type


@app.route("/")
def index():
    return render_template("dashboard.html")


# ============ CRYPTO DATA ROUTES ============

@app.route("/send/crypto-prices")
def send_crypto_prices():
    crypto_list = crypto_client.get_top_cryptos(limit=15)
    message = crypto_client.format_price_table(crypto_list)
    tg.send_text(message)
    flash("💰 Crypto prices sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/crypto-news")
def send_crypto_news():
    news_list = crypto_client.get_crypto_news(limit=5)
    message = crypto_client.format_news(news_list)
    tg.send_text(message)
    flash("📰 Crypto news sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/trending-coins")
def send_trending_coins():
    trending = crypto_client.get_trending_coins()
    message = crypto_client.format_trending(trending)
    tg.send_text(message)
    flash("🔥 Trending coins sent!", "success")
    return redirect(url_for("index"))


# ============ EDUCATIONAL CONTENT ROUTES ============

@app.route("/send/crypto-education")
def send_crypto_education():
    text = ai.generate_text(TEXT_TEMPLATES["crypto_education"])
    tg.send_text(text)
    flash("📚 Crypto education sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/trading-tips")
def send_trading_tips():
    text = ai.generate_text(TEXT_TEMPLATES["trading_tips"])
    tg.send_text(text)
    flash("💡 Trading tips sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/crypto-security")
def send_crypto_security():
    text = ai.generate_text(TEXT_TEMPLATES["crypto_security"])
    tg.send_text(text)
    flash("🔐 Security tips sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/defi-explained")
def send_defi_explained():
    text = ai.generate_text(TEXT_TEMPLATES["defi_explained"])
    tg.send_text(text)
    flash("🏦 DeFi explanation sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/market-analysis")
def send_market_analysis():
    text = ai.generate_text(TEXT_TEMPLATES["market_analysis"])
    tg.send_text(text)
    flash("📊 Market analysis sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/crypto-project")
def send_crypto_project():
    text = ai.generate_text(TEXT_TEMPLATES["crypto_project"])
    tg.send_text(text)
    flash("🚀 Crypto project info sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/nft-knowledge")
def send_nft_knowledge():
    text = ai.generate_text(TEXT_TEMPLATES["nft_knowledge"])
    tg.send_text(text)
    flash("🎨 NFT knowledge sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/beginner-guide")
def send_beginner_guide():
    text = ai.generate_text(TEXT_TEMPLATES["beginner_guide"])
    tg.send_text(text)
    flash("👋 Beginner guide sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/crypto-terminology")
def send_crypto_terminology():
    text = ai.generate_text(TEXT_TEMPLATES["crypto_terminology"])
    tg.send_text(text)
    flash("📖 Crypto terminology sent!", "success")
    return redirect(url_for("index"))


# ============ INTERACTIVE CONTENT ROUTES ============

@app.route("/send/daily-challenge")
def send_daily_challenge():
    text = ai.generate_text(TEXT_TEMPLATES["daily_challenge"])
    tg.send_text(text)
    flash("🎯 Daily challenge sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/image-post")
def send_image_post():
    # Random selection for variety
    text_options = [
        "crypto_education", "trading_tips", "defi_explained",
        "nft_knowledge", "crypto_project", "market_analysis"
    ]
    selected_text = random.choice(text_options)
    selected_image = random.choice(list(IMAGE_TEMPLATES.keys()))
    
    caption = ai.generate_text(TEXT_TEMPLATES[selected_text])
    img_url = ai.image_url(IMAGE_TEMPLATES[selected_image])
    tg.send_photo(img_url, caption)
    flash("🎨 Image + caption sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/poll")
def send_poll():
    raw = ai.generate_text(TEXT_TEMPLATES["poll_question"])
    if "|" in raw:
        q_part, opts_part = raw.split("|", 1)
        question = q_part.strip()
        options = [o.strip() for o in opts_part.split(",") if o.strip()]
        if len(options) >= 2:
            tg.send_poll(question, options[:10])
            flash("📊 Poll sent!", "success")
        else:
            flash("Poll generation failed (not enough options).", "error")
    else:
        flash("Poll generation failed (bad format).", "error")
    return redirect(url_for("index"))


@app.route("/send/thread")
def send_thread():
    raw = ai.generate_text(TEXT_TEMPLATES["thread_explainer"])
    parts = [p.strip() for p in raw.split("\n\n") if p.strip()]
    if parts:
        parts[-1] = parts[-1] + HASHTAGS.get("thread", "")
        tg.send_thread(parts)
        flash("🧵 Thread sent!", "success")
    else:
        flash("Thread generation failed.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
