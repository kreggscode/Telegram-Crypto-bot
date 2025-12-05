# 🚀 Quick Reference Guide - Cryptocurrency Bot

## ⚡ Quick Start Commands

### Test the Bot Locally
```bash
# Single automated post (based on current time)
python -m src.main

# Interactive chat bot (responds to user commands)
python -m src.chat_bot

# Manual control dashboard
cd dashboard && python app.py
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## 📝 Environment Variables (.env)

```env
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_channel_chat_id
TIMEZONE_OFFSET_HOURS=5.5
```

## 💬 Chat Bot Commands (User-Facing)

| Command | Description |
|---------|-------------|
| `/start` | Welcome message and help |
| `/price` | Top 15 crypto prices |
| `/news` | Latest crypto news |
| `/trending` | Trending cryptocurrencies |
| `/btc` | Bitcoin price |
| `/eth` | Ethereum price |
| `/price sol` | Solana price (any symbol) |
| `/learn` | Crypto education |
| `/tip` | Trading tip |
| `/security` | Security advice |
| `/quiz` | Crypto quiz |
| `/about` | Bot information |

## 📊 Post Types

### Live Data
- `crypto_prices` - Top 15 cryptocurrencies with prices
- `crypto_news` - Latest news (5 articles)
- `trending_coins` - Trending cryptocurrencies

### Educational
- `crypto_education` - Blockchain/crypto concepts
- `trading_tips` - Trading strategies
- `crypto_security` - Security best practices
- `defi_explained` - DeFi concepts
- `market_analysis` - Market trends
- `crypto_project` - Project spotlights
- `nft_knowledge` - NFT education
- `beginner_guide` - Getting started
- `crypto_terminology` - Crypto slang

### Interactive
- `daily_challenge` - Quiz/trivia
- `image_plus_text` - AI image + caption
- `poll` - Multiple choice quiz
- `thread` - 4-part educational thread

## ⏰ Default Posting Schedule (IST)

- **8:00 AM** - Crypto Prices (70% chance)
- **2:00 PM** - Educational Content
- **8:00 PM** - Interactive Content
- **11:00 PM** - Trending/Analysis (optional)

## 🔧 Common Customizations

### Change Posting Times
Edit `.github/workflows/auto-post.yml`:
```yaml
schedule:
  - cron: '30 2 * * *'   # 8:00 AM IST
  - cron: '30 8 * * *'   # 2:00 PM IST
  - cron: '30 14 * * *'  # 8:00 PM IST
  - cron: '30 17 * * *'  # 11:00 PM IST
```

### Modify AI Prompts
Edit `src/templates.py`:
```python
TEXT_TEMPLATES = {
    "crypto_education": "Your custom prompt here...",
    # ... more templates
}
```

### Change Number of Cryptos
Edit `src/crypto_data_client.py`:
```python
crypto_client.get_top_cryptos(limit=20)  # Change from 15 to 20
```

### Adjust Posting Logic
Edit `src/scheduler_logic.py`:
```python
# Modify time ranges and post type probabilities
if 8 <= hour < 10:
    # Morning logic
```

## 🎨 Dashboard Routes

Access at `http://127.0.0.1:5000`

### Live Data
- `/send/crypto-prices`
- `/send/crypto-news`
- `/send/trending-coins`

### Educational
- `/send/crypto-education`
- `/send/trading-tips`
- `/send/crypto-security`
- `/send/defi-explained`
- `/send/market-analysis`
- `/send/crypto-project`
- `/send/nft-knowledge`
- `/send/beginner-guide`
- `/send/crypto-terminology`

### Interactive
- `/send/daily-challenge`
- `/send/image-post`
- `/send/poll`
- `/send/thread`

## 🔑 API Information

### CoinGecko (Free)
- **Endpoint**: `https://api.coingecko.com/api/v3/`
- **Rate Limit**: 10-50 calls/minute
- **No API Key Required**
- **Used For**: Crypto prices, trending coins

### CryptoCompare (Free)
- **Endpoint**: `https://min-api.cryptocompare.com/data/v2/`
- **Rate Limit**: Generous free tier
- **No API Key Required**
- **Used For**: Crypto news

### Pollinations.ai (Free)
- **Text**: `https://text.pollinations.ai/`
- **Image**: `https://image.pollinations.ai/prompt/`
- **No API Key Required**
- **Used For**: AI content generation

## 🐛 Troubleshooting

### Bot doesn't post
```bash
# Check bot token and chat ID
python get_chat_id.py

# Test manually
python -m src.main
```

### Wrong timezone
```env
# Update .env file
TIMEZONE_OFFSET_HOURS=5.5  # IST
TIMEZONE_OFFSET_HOURS=-5   # EST
TIMEZONE_OFFSET_HOURS=0    # UTC
```

### API errors
```python
# Check rate limits
# CoinGecko: 10-50 calls/minute
# Add delays if needed in crypto_data_client.py
```

### Chat bot not responding
```bash
# Make sure it's running
python -m src.chat_bot

# Send commands to bot directly (not channel)
# Commands must start with /
```

## 📁 File Structure

```
telegram-crypto-bot/
├── src/
│   ├── main.py              # Automated posting
│   ├── chat_bot.py          # Interactive chat
│   ├── crypto_data_client.py # API client
│   ├── templates.py         # AI prompts
│   ├── scheduler_logic.py   # Posting schedule
│   ├── telegram_client.py   # Telegram API
│   └── config.py           # Configuration
├── dashboard/
│   ├── app.py              # Flask app
│   ├── templates/          # HTML
│   └── static/            # CSS
├── .github/workflows/
│   └── auto-post.yml      # GitHub Actions
├── .env                   # Your secrets (DO NOT COMMIT)
├── .env.example          # Template
├── requirements.txt      # Dependencies
├── README.md            # Main documentation
├── SETUP_GUIDE.md       # Setup instructions
└── BOT_SUMMARY.md       # Feature summary
```

## 🚀 Deployment Checklist

- [ ] Create Telegram bot with @BotFather
- [ ] Create Telegram channel
- [ ] Add bot as admin to channel
- [ ] Get chat ID
- [ ] Create `.env` file with credentials
- [ ] Install dependencies (`pip install -r requirements.txt`)
- [ ] Test locally (`python -m src.main`)
- [ ] Push to GitHub
- [ ] Add GitHub Secrets (BOT_TOKEN, CHAT_ID, TIMEZONE_OFFSET_HOURS)
- [ ] Enable GitHub Actions
- [ ] Monitor first few posts
- [ ] Customize content as needed

## 💡 Pro Tips

1. **Test First**: Always test locally before enabling automation
2. **Monitor Engagement**: Track which post types get the most engagement
3. **Adjust Schedule**: Optimize posting times for your audience
4. **Customize Content**: Tailor AI prompts to your audience's interests
5. **Use Chat Bot**: Enable interactive features for better engagement
6. **Stay Updated**: Keep dependencies updated for security
7. **Backup Tokens**: Save your bot token securely
8. **Rate Limits**: Be mindful of API rate limits
9. **Error Handling**: Check logs if posts fail
10. **Iterate**: Continuously improve based on feedback

## 📞 Support Resources

- **Telegram Bot API**: https://core.telegram.org/bots/api
- **CoinGecko API**: https://www.coingecko.com/en/api
- **CryptoCompare API**: https://min-api.cryptocompare.com/
- **Python Requests**: https://requests.readthedocs.io/
- **Flask Docs**: https://flask.palletsprojects.com/

---

**Quick tip**: Bookmark this page for easy reference! 🔖
