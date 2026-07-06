"""
Crypto Data Client - Fetches real-time cryptocurrency data from various APIs
"""
import requests
from pycoingecko import CoinGeckoAPI
from datetime import datetime
import time


class CryptoDataClient:
    def __init__(self):
        self.cg = CoinGeckoAPI()
        self.cryptocompare_base = "https://min-api.cryptocompare.com/data/v2"
        
    def get_top_cryptos(self, limit=15):
        """
        Get top cryptocurrencies by market cap with current prices
        Returns formatted data ready for display
        """
        try:
            # Get top coins by market cap
            print(f"Calling CoinGecko API for top {limit} cryptos...")
            data = self.cg.get_coins_markets(
                vs_currency='usd',
                order='market_cap_desc',
                per_page=limit,
                page=1,
                sparkline=False,
                price_change_percentage='24h'
            )
            
            print(f"CoinGecko returned {len(data)} coins")
            crypto_list = []
            for coin in data:
                rank = coin.get('market_cap_rank')
                name = coin.get('name')
                symbol = coin.get('symbol')
                price = coin.get('current_price')
                change = coin.get('price_change_percentage_24h')
                mcap = coin.get('market_cap')
                vol = coin.get('total_volume')

                crypto_info = {
                    'rank': rank if rank is not None else 'N/A',
                    'name': name if name is not None else 'Unknown',
                    'symbol': str(symbol if symbol is not None else '').upper(),
                    'price': float(price) if price is not None else 0.0,
                    'change_24h': float(change) if change is not None else 0.0,
                    'market_cap': float(mcap) if mcap is not None else 0.0,
                    'volume_24h': float(vol) if vol is not None else 0.0,
                }
                crypto_list.append(crypto_info)
            
            print(f"Formatted {len(crypto_list)} coins successfully")
            return crypto_list
        except Exception as e:
            print(f"Error fetching crypto prices: {e}")
            return []
    
    def format_price_table(self, crypto_list):
        """
        Format cryptocurrency data into a beautiful Telegram message
        """
        if not crypto_list:
            return "❌ Unable to fetch crypto prices at the moment."
        
        # Get current UTC timestamp
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        
        message = f"💰 TOP CRYPTOCURRENCY PRICES 💰\n"
        message += f"📅 As of: {timestamp}\n\n"
        
        for crypto in crypto_list:
            # Format price
            price = crypto['price']
            if price >= 1:
                price_str = f"${price:,.2f}"
            else:
                price_str = f"${price:.6f}"
            
            # Format 24h change with emoji
            change = crypto['change_24h']
            if change > 0:
                change_emoji = "📈"
                change_str = f"+{change:.2f}%"
            else:
                change_emoji = "📉"
                change_str = f"{change:.2f}%"
            
            # Format market cap
            mcap = crypto['market_cap']
            if mcap >= 1_000_000_000:
                mcap_str = f"${mcap/1_000_000_000:.2f}B"
            elif mcap >= 1_000_000:
                mcap_str = f"${mcap/1_000_000:.2f}M"
            else:
                mcap_str = f"${mcap:,.0f}"
            
            message += f"{crypto['rank']}. {crypto['name']} ({crypto['symbol']})\n"
            message += f"   💵 Price: {price_str}\n"
            message += f"   {change_emoji} 24h: {change_str}\n"
            message += f"   📊 MCap: {mcap_str}\n\n"
        
        message += "━━━━━━━━━━━━━━━━━━━━\n"
        message += "🔄 Data updates every few hours\n"
        message += "💡 Powered by CoinGecko API"
        
        return message
    
    def get_crypto_news(self, limit=5):
        """
        Fetch latest cryptocurrency news from CryptoCompare
        """
        try:
            url = f"{self.cryptocompare_base}/news/?lang=EN"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                news_items = data.get('Data', [])[:limit]
                
                news_list = []
                for item in news_items:
                    title = item.get('title')
                    body = item.get('body')
                    url = item.get('url')
                    source = item.get('source')
                    published = item.get('published_on')
                    
                    news_info = {
                        'title': title if title is not None else 'No title',
                        'body': (body[:200] if body is not None else '') + '...',
                        'url': url if url is not None else '',
                        'source': source if source is not None else 'Unknown',
                        'published': published if published is not None else 0
                    }
                    news_list.append(news_info)
                
                return news_list
            else:
                return []
        except Exception as e:
            print(f"Error fetching crypto news: {e}")
            return []
    
    def format_news(self, news_list):
        """
        Format news into a Telegram message
        """
        if not news_list:
            return "❌ Unable to fetch crypto news at the moment."
        
        message = "📰 **LATEST CRYPTO NEWS** 📰\n\n"
        
        for i, news in enumerate(news_list, 1):
            # Convert timestamp to readable date
            pub_date = datetime.fromtimestamp(news['published']).strftime("%b %d, %Y")
            
            message += f"**{i}. {news['title']}**\n"
            message += f"📅 {pub_date} | 🗞️ {news['source']}\n"
            message += f"{news['body']}\n"
            message += f"🔗 [Read More]({news['url']})\n\n"
        
        message += "━━━━━━━━━━━━━━━━━━━━\n"
        message += "💡 *Stay informed, trade smart!*"
        
        return message
    
    def get_price_by_symbol(self, symbol):
        """
        Get current price for a specific cryptocurrency by symbol
        Used for chat/command features
        """
        try:
            symbol = symbol.lower()
            data = self.cg.get_price(
                ids=symbol,
                vs_currencies='usd',
                include_24hr_change=True
            )
            
            if data:
                coin_id = list(data.keys())[0]
                price = data[coin_id].get('usd')
                change = data[coin_id].get('usd_24h_change')
                
                return {
                    'symbol': symbol.upper(),
                    'price': float(price) if price is not None else 0.0,
                    'change_24h': float(change) if change is not None else 0.0
                }
            return None
        except Exception as e:
            print(f"Error fetching price for {symbol}: {e}")
            return None
    
    def get_trending_coins(self):
        """
        Get trending cryptocurrencies
        """
        try:
            data = self.cg.get_search_trending()
            trending = []
            
            for item in data.get('coins', [])[:7]:
                coin = item.get('item', {})
                name = coin.get('name')
                symbol = coin.get('symbol')
                rank = coin.get('market_cap_rank')
                price_btc = coin.get('price_btc')
                
                trending.append({
                    'name': name if name is not None else 'Unknown',
                    'symbol': str(symbol if symbol is not None else '').upper(),
                    'rank': rank if rank is not None else 'N/A',
                    'price_btc': float(price_btc) if price_btc is not None else 0.0
                })
            
            return trending
        except Exception as e:
            print(f"Error fetching trending coins: {e}")
            return []
    
    def format_trending(self, trending_list):
        """
        Format trending coins into a message
        """
        if not trending_list:
            return "❌ Unable to fetch trending coins."
        
        message = "🔥 **TRENDING CRYPTOCURRENCIES** 🔥\n\n"
        message += "🚀 *Most searched coins right now:*\n\n"
        
        for i, coin in enumerate(trending_list, 1):
            message += f"{i}. **{coin['name']} ({coin['symbol']})**\n"
            message += f"   📊 Rank: #{coin['rank']}\n\n"
        
        message += "━━━━━━━━━━━━━━━━━━━━\n"
        message += "💡 *Trending = High interest, not investment advice!*"
        
        return message


# Singleton instance
crypto_client = CryptoDataClient()
