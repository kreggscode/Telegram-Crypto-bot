# � Cryptocurrency Bot - Real-Time Crypto Data & Education

An automated Telegram bot that posts real-time cryptocurrency prices, news, educational content, and trading insights to keep your audience informed and engaged in the crypto space.

## 🎯 Features

### 📊 **Real-Time Data**
- **Live Crypto Prices**: Top 15-20 cryptocurrencies with real-time prices from CoinGecko API
- **Crypto News**: Latest cryptocurrency news from CryptoCompare API
- **Trending Coins**: Most searched and trending cryptocurrencies
- **Market Analysis**: AI-generated market sentiment and trend analysis

### 📚 **Educational Content**
- **Crypto Education**: Blockchain, Bitcoin, Ethereum, DeFi, NFTs explained
- **Trading Tips**: Practical trading strategies and risk management
- **Security Best Practices**: Wallet security, scam awareness, private key protection
- **Beginner Guides**: Getting started with cryptocurrency
- **Crypto Terminology**: HODL, FOMO, FUD, whale, gas fees, and more

### 🎨 **Visual & Interactive**
- **AI-Generated Images**: Stunning crypto-themed visuals (Bitcoin, Ethereum, DeFi, NFTs)
- **Interactive Polls**: Cryptocurrency quizzes for engagement
- **Educational Threads**: Deep-dive explanations of crypto concepts
- **Daily Challenges**: Fun crypto puzzles and trivia

### 💬 **Chat Features** (NEW!)
Users can interact with the bot using commands:
- `/price` - Get top 15 crypto prices
- `/news` - Latest crypto news
- `/trending` - Trending cryptocurrencies
- `/btc` or `/bitcoin` - Bitcoin price
- `/eth` or `/ethereum` - Ethereum price
- `/price <symbol>` - Get price for any crypto (e.g., `/price sol`)
- `/learn` - Random crypto education
- `/tip` - Trading tip
- `/security` - Security advice
- `/quiz` - Crypto quiz

## 📅 Posting Schedule

The bot posts **3-4 times per day** at optimal times:

- **Morning (8-10 AM)**: 📊 Crypto Prices & Market Data (PRIORITY - 70% chance)
- **Afternoon (2-4 PM)**: 📚 Educational Content & News
- **Evening (8-10 PM)**: 🎯 Interactive Content (Polls, Challenges, Images)
- **Late Night (11 PM-12 AM)**: 🔥 Trending Coins & Analysis (Optional 4th post)

## 🚀 Setup

### 1. Create Telegram Bot & Channel

1. Talk to **@BotFather** on Telegram:
   - `/newbot` → get your `BOT_TOKEN`
2. Create a **public or private channel**
3. Add the bot as **Admin** to your channel (with "Post Messages" permission)
4. Get your `CHAT_ID`:
   - Post something to your channel
   - Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Look for `"chat":{"id": -100...}` from your channel

### 2. Local Setup

```bash
git clone <this-repo>
cd telegram-crypto-bot

# Copy and edit environment variables
cp .env.example .env
# Edit .env with your BOT_TOKEN, CHAT_ID, and TIMEZONE_OFFSET_HOURS

# Install dependencies
pip install -r requirements.txt

# Test the bot (automated posting)
python -m src.main

# OR run the chat bot (interactive mode)
python -m src.chat_bot
```

### 3. GitHub Actions Automation

1. Push this repo to GitHub
2. Go to: **Settings → Secrets and variables → Actions**
3. Add these repository secrets:
   - `BOT_TOKEN` - Your Telegram bot token
   - `CHAT_ID` - Your channel chat ID
   - `TIMEZONE_OFFSET_HOURS` - Your timezone offset (e.g., 5.5 for IST)

The bot will automatically post 3-4 times daily via GitHub Actions!

### 4. Dashboard (Manual Control)

Run the Flask dashboard for manual posting:

```bash
cd dashboard
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

From the dashboard you can manually trigger:
- 💰 **Live Data**: Crypto Prices, News, Trending Coins
- 📚 **Education**: Crypto Education, Trading Tips, Security, DeFi, NFTs, etc.
- 🎯 **Interactive**: Challenges, Images, Polls, Threads

## 📁 Project Structure

```
telegram-crypto-bot/
├── .github/workflows/     # GitHub Actions automation (3-4x daily posts)
├── dashboard/             # Flask web UI for manual posting
│   ├── app.py            # Flask routes
│   ├── templates/        # HTML templates
│   └── static/           # CSS styles
├── src/                   # Core bot logic
│   ├── config.py         # Configuration management
│   ├── telegram_client.py # Telegram API wrapper
│   ├── crypto_data_client.py # CoinGecko & CryptoCompare API client
│   ├── pollinations_client.py # AI generation (free!)
│   ├── templates.py      # AI prompt templates
│   ├── scheduler_logic.py # Time-based posting logic
│   ├── chat_bot.py       # Interactive chat bot handler
│   └── main.py           # Main orchestrator
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # This file
```

## 🎨 Customization

- **Edit prompts**: Modify `src/templates.py` to change AI generation prompts
- **Change schedule**: Edit `.github/workflows/auto-post.yml` cron times
- **Adjust posting logic**: Modify `src/scheduler_logic.py` to change what posts when
- **Add new post types**: Add templates and functions following the existing pattern
- **Customize data sources**: Modify `src/crypto_data_client.py` for different APIs

## 🔑 API Information

### **CoinGecko API** (Free, No Key Required)
- Real-time cryptocurrency prices
- Market cap, volume, 24h changes
- Top cryptocurrencies by market cap
- **Rate Limit**: 10-50 calls/minute (free tier)

### **CryptoCompare API** (Free Tier)
- Latest cryptocurrency news
- Additional market data
- **Rate Limit**: Generous free tier

### **Pollinations.ai** (Free)
- AI-generated text content
- AI-generated crypto-themed images
- No API key required

## 💡 Why This Bot?

✅ **Real-Time Data**: Always up-to-date crypto prices and news  
✅ **Educational**: Helps users learn about cryptocurrency and blockchain  
✅ **Interactive**: Chat commands allow users to query data on-demand  
✅ **Automated**: Posts 3-4 times daily without manual intervention  
✅ **Free APIs**: Uses free tier APIs (CoinGecko, CryptoCompare, Pollinations.ai)  
✅ **Customizable**: Easy to modify content, schedule, and features  
✅ **Visual Appeal**: AI-generated images make posts engaging  

## 🤖 Chat Bot Usage

To enable interactive chat features, run the chat bot:

```bash
python -m src.chat_bot
```

Users can then send commands to your bot:
- Get real-time prices
- Check trending coins
- Read latest news
- Learn about crypto concepts
- Get trading tips and security advice

## � Chart Generation (Future Feature)

The bot is designed to support chart generation using matplotlib. To enable:
1. Uncomment chart generation code in `crypto_data_client.py`
2. Generate price charts for visual analysis
3. Send charts as images to your channel

*Note: Chart generation is optional and can be added based on your needs.*

## 📝 License

MIT

---

**Powered by CoinGecko API, CryptoCompare & Pollinations.ai**

*Stay informed, trade smart! 🚀�*
