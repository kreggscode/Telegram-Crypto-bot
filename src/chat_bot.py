"""
Chat Bot Handler - Handles user commands and interactions
Allows users to query crypto prices, get info, and interact with the bot
"""
import requests
from .config import BOT_TOKEN
from .crypto_data_client import crypto_client
from . import pollinations_client as ai
from .templates import TEXT_TEMPLATES

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def get_updates(offset=None):
    """Get new messages from Telegram"""
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 30, "offset": offset}
    try:
        response = requests.get(url, params=params, timeout=35)
        return response.json()
    except Exception as e:
        print(f"Error getting updates: {e}")
        return None


def send_message(chat_id, text):
    """Send a message to a specific chat"""
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Error sending message: {e}")


def handle_command(message):
    """Process user commands"""
    chat_id = message['chat']['id']
    text = message.get('text', '').strip()
    
    if not text:
        return
    
    # Convert to lowercase for command matching
    text_lower = text.lower()
    
    # /start command
    if text_lower == '/start' or text_lower == '/help':
        help_text = """
🤖 **Welcome to Crypto Bot!** 🚀

I provide real-time cryptocurrency data, news, and education!

**Available Commands:**
📊 `/price` - Get top 15 crypto prices
📰 `/news` - Latest crypto news
🔥 `/trending` - Trending cryptocurrencies
💰 `/btc` or `/bitcoin` - Bitcoin price
💎 `/eth` or `/ethereum` - Ethereum price
🔍 `/price <symbol>` - Get price for any crypto (e.g., `/price sol`)
📚 `/learn` - Random crypto education
💡 `/tip` - Trading tip
🔐 `/security` - Security advice
🎯 `/quiz` - Crypto quiz

**More Info:**
ℹ️ `/about` - About this bot
❓ `/help` - Show this message

*Stay informed, trade smart!* 💎🚀
        """
        send_message(chat_id, help_text)
    
    # /price command - top cryptos
    elif text_lower == '/price' or text_lower == '/prices':
        crypto_list = crypto_client.get_top_cryptos(limit=15)
        message_text = crypto_client.format_price_table(crypto_list)
        send_message(chat_id, message_text)
    
    # /news command
    elif text_lower == '/news':
        news_list = crypto_client.get_crypto_news(limit=5)
        message_text = crypto_client.format_news(news_list)
        send_message(chat_id, message_text)
    
    # /trending command
    elif text_lower == '/trending':
        trending = crypto_client.get_trending_coins()
        message_text = crypto_client.format_trending(trending)
        send_message(chat_id, message_text)
    
    # Bitcoin price
    elif text_lower in ['/btc', '/bitcoin']:
        send_message(chat_id, "🔍 Fetching Bitcoin price...")
        crypto_list = crypto_client.get_top_cryptos(limit=1)
        if crypto_list:
            btc = crypto_list[0]
            price_str = f"${btc['price']:,.2f}"
            change = btc['change_24h']
            change_emoji = "📈" if change > 0 else "📉"
            msg = f"₿ **Bitcoin (BTC)**\n💰 Price: {price_str}\n{change_emoji} 24h: {change:+.2f}%"
            send_message(chat_id, msg)
    
    # Ethereum price
    elif text_lower in ['/eth', '/ethereum']:
        send_message(chat_id, "🔍 Fetching Ethereum price...")
        crypto_list = crypto_client.get_top_cryptos(limit=10)
        eth = next((c for c in crypto_list if c['symbol'] == 'ETH'), None)
        if eth:
            price_str = f"${eth['price']:,.2f}"
            change = eth['change_24h']
            change_emoji = "📈" if change > 0 else "📉"
            msg = f"💎 **Ethereum (ETH)**\n💰 Price: {price_str}\n{change_emoji} 24h: {change:+.2f}%"
            send_message(chat_id, msg)
    
    # Specific crypto price query
    elif text_lower.startswith('/price '):
        symbol = text[7:].strip().upper()
        send_message(chat_id, f"🔍 Fetching {symbol} price...")
        crypto_list = crypto_client.get_top_cryptos(limit=50)
        coin = next((c for c in crypto_list if c['symbol'] == symbol), None)
        if coin:
            price = coin['price']
            if price >= 1:
                price_str = f"${price:,.2f}"
            else:
                price_str = f"${price:.6f}"
            change = coin['change_24h']
            change_emoji = "📈" if change > 0 else "📉"
            msg = f"**{coin['name']} ({symbol})**\n💰 Price: {price_str}\n{change_emoji} 24h: {change:+.2f}%"
            send_message(chat_id, msg)
        else:
            send_message(chat_id, f"❌ Could not find price for {symbol}")
    
    # Educational content
    elif text_lower == '/learn':
        prompt = TEXT_TEMPLATES["crypto_education"]
        text = ai.generate_text(prompt)
        send_message(chat_id, text)
    
    # Trading tip
    elif text_lower == '/tip':
        prompt = TEXT_TEMPLATES["trading_tips"]
        text = ai.generate_text(prompt)
        send_message(chat_id, text)
    
    # Security advice
    elif text_lower == '/security':
        prompt = TEXT_TEMPLATES["crypto_security"]
        text = ai.generate_text(prompt)
        send_message(chat_id, text)
    
    # Quiz
    elif text_lower == '/quiz':
        prompt = TEXT_TEMPLATES["daily_challenge"]
        text = ai.generate_text(prompt)
        send_message(chat_id, text)
    
    # About
    elif text_lower == '/about':
        about_text = """
ℹ️ **About Crypto Bot**

I'm an automated cryptocurrency bot that provides:
✅ Real-time crypto prices (CoinGecko API)
✅ Latest crypto news (CryptoCompare API)
✅ Educational content (AI-powered)
✅ Trading tips & security advice
✅ Interactive quizzes and polls

**Features:**
🔄 Auto-posts 3-4 times daily
📊 Live market data
📰 Breaking crypto news
🎓 Educational content
🤖 AI-generated insights

*Built with ❤️ for the crypto community*
        """
        send_message(chat_id, about_text)
    
    # Unknown command
    elif text.startswith('/'):
        send_message(chat_id, "❓ Unknown command. Type /help to see available commands.")


def run_chat_bot():
    """
    Run the chat bot in polling mode
    This allows users to interact with the bot via commands
    """
    print("🤖 Starting Crypto Chat Bot...")
    print("📡 Listening for commands...")
    
    offset = None
    
    try:
        while True:
            updates = get_updates(offset)
            
            if updates and updates.get('ok'):
                for update in updates.get('result', []):
                    offset = update['update_id'] + 1
                    
                    if 'message' in update:
                        handle_command(update['message'])
    
    except KeyboardInterrupt:
        print("\n👋 Chat bot stopped by user")
    except Exception as e:
        print(f"❌ Chat bot error: {e}")


if __name__ == "__main__":
    run_chat_bot()
