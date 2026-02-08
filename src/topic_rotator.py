"""
Topic Rotation System - Ensures variety in content generation
Provides specific topics for each content type to prevent repetition
"""
import random

# Extensive topic lists for variety
CRYPTO_EDUCATION_TOPICS = [
    "Bitcoin halving and its impact on price",
    "How blockchain consensus mechanisms work",
    "Understanding gas fees on Ethereum",
    "What are Layer 2 scaling solutions",
    "Proof of Work vs Proof of Stake explained",
    "How cryptocurrency wallets store your coins",
    "What is a blockchain fork",
    "Understanding cryptocurrency market cap",
    "How smart contracts execute automatically",
    "What are wrapped tokens (like WBTC)",
    "Understanding cryptocurrency mining difficulty",
    "What is a mempool in blockchain",
    "How decentralized exchanges work",
    "Understanding tokenomics and token supply",
    "What are validator nodes in PoS",
    "How cross-chain bridges function",
    "Understanding ERC-20 token standard",
    "What is slashing in proof of stake",
    "How atomic swaps enable trustless trading",
    "Understanding cryptocurrency airdrops",
]

TRADING_TIPS_TOPICS = [
    "Dollar-cost averaging (DCA) strategy",
    "Setting stop-loss orders effectively",
    "Understanding support and resistance levels",
    "How to read candlestick patterns",
    "Portfolio diversification in crypto",
    "Risk management: the 1-2% rule",
    "Identifying bullish and bearish trends",
    "Using RSI (Relative Strength Index)",
    "Understanding MACD indicator",
    "How to spot pump and dump schemes",
    "Taking profits: ladder selling strategy",
    "Avoiding FOMO in volatile markets",
    "Reading trading volume for insights",
    "Understanding Fibonacci retracement",
    "Managing emotions during market dips",
    "Using moving averages for trend analysis",
    "Recognizing chart patterns (head & shoulders, triangles)",
    "Understanding order types (market, limit, stop)",
    "How to use trading bots safely",
    "Analyzing on-chain metrics for trading",
]

SECURITY_TOPICS = [
    "Why you should never share your seed phrase",
    "How to spot phishing emails and fake websites",
    "Importance of hardware wallets for large holdings",
    "Enabling 2FA on all crypto accounts",
    "Avoiding clipboard malware attacks",
    "How to verify smart contract addresses",
    "Dangers of connecting to unknown DApps",
    "Protecting yourself from SIM swap attacks",
    "Using a VPN when accessing crypto accounts",
    "How to safely store your recovery phrase",
    "Recognizing fake customer support scams",
    "Understanding rug pulls in DeFi",
    "How to check if an exchange is legitimate",
    "Avoiding dusting attacks on your wallet",
    "Using multi-signature wallets for security",
    "How to revoke smart contract permissions",
    "Protecting against fake token scams",
    "Understanding honeypot contracts",
    "Safe practices for NFT minting",
    "How to verify Telegram/Discord admins",
]

DEFI_TOPICS = [
    "What is yield farming and how does it work",
    "Understanding impermanent loss in liquidity pools",
    "How automated market makers (AMMs) function",
    "What are flash loans in DeFi",
    "Understanding lending protocols like Aave",
    "How decentralized stablecoins maintain their peg",
    "What is liquidity mining",
    "Understanding governance tokens and DAOs",
    "How synthetic assets work in DeFi",
    "What are money markets in DeFi",
    "Understanding collateralization ratios",
    "How yield aggregators optimize returns",
    "What is total value locked (TVL)",
    "Understanding DeFi insurance protocols",
    "How perpetual futures work in DeFi",
    "What are liquidity provider (LP) tokens",
    "Understanding oracle networks in DeFi",
    "How algorithmic stablecoins function",
    "What is composability in DeFi",
    "Understanding DeFi derivatives",
]

MARKET_ANALYSIS_TOPICS = [
    "Bitcoin dominance and its market implications",
    "Understanding altcoin season indicators",
    "How macroeconomic factors affect crypto",
    "Reading the Fear and Greed Index",
    "Understanding market cycles (accumulation, markup, distribution)",
    "How institutional adoption impacts prices",
    "Analyzing on-chain metrics for market sentiment",
    "Understanding correlation between BTC and stocks",
    "How regulatory news affects crypto markets",
    "Reading exchange inflow/outflow data",
    "Understanding market cap vs circulating supply",
    "How stablecoin dominance indicates market health",
    "Analyzing whale wallet movements",
    "Understanding funding rates in futures",
    "How Bitcoin ETF approval affects markets",
    "Reading long/short ratio indicators",
    "Understanding market liquidity and slippage",
    "How mining difficulty affects Bitcoin price",
    "Analyzing developer activity for project health",
    "Understanding token unlock schedules impact",
]

CRYPTO_PROJECT_TOPICS = [
    "Ethereum: The world computer and smart contract platform",
    "Solana: High-speed blockchain for DeFi and NFTs",
    "Cardano: Peer-reviewed blockchain with PoS",
    "Polygon: Ethereum's scaling solution",
    "Chainlink: Decentralized oracle network",
    "Avalanche: Fast and scalable smart contract platform",
    "Polkadot: Multi-chain interoperability protocol",
    "Cosmos: Internet of blockchains",
    "Arbitrum: Ethereum Layer 2 scaling",
    "Optimism: Optimistic rollup for Ethereum",
    "The Graph: Indexing protocol for blockchain data",
    "Uniswap: Leading decentralized exchange",
    "Aave: Decentralized lending protocol",
    "Maker: Decentralized stablecoin DAI",
    "Curve Finance: Stablecoin exchange protocol",
    "Lido: Liquid staking solution",
    "Synthetix: Synthetic asset protocol",
    "Compound: Autonomous interest rate protocol",
    "Filecoin: Decentralized storage network",
    "Render Network: Distributed GPU rendering",
]

NFT_TOPICS = [
    "What are NFTs and how do they work",
    "Understanding NFT marketplaces (OpenSea, Blur)",
    "How NFT royalties work for creators",
    "What are dynamic NFTs that change over time",
    "Understanding NFT rarity and traits",
    "How to verify NFT authenticity",
    "What are soulbound tokens (SBTs)",
    "Understanding NFT utility beyond art",
    "How NFTs are used in gaming (play-to-earn)",
    "What are NFT fractionalization platforms",
    "Understanding NFT metadata and IPFS",
    "How music NFTs empower artists",
    "What are membership NFTs (access passes)",
    "Understanding NFT lending and borrowing",
    "How virtual land NFTs work in metaverse",
    "What are generative art NFTs",
    "Understanding NFT staking for rewards",
    "How NFT aggregators help find deals",
    "What are phygital NFTs (physical + digital)",
    "Understanding NFT wash trading risks",
]

BEGINNER_GUIDE_TOPICS = [
    "How to buy your first cryptocurrency",
    "Choosing between hot and cold wallets",
    "Understanding cryptocurrency exchanges",
    "How to set up a MetaMask wallet",
    "What is KYC and why exchanges require it",
    "How to safely transfer crypto between wallets",
    "Understanding transaction fees and confirmations",
    "How to read a blockchain explorer",
    "What to do if you send crypto to wrong address",
    "Understanding public and private keys",
    "How to backup your wallet properly",
    "Choosing your first cryptocurrencies to invest",
    "Understanding market orders vs limit orders",
    "How to track your crypto portfolio",
    "What is a testnet and why practice there",
    "Understanding crypto taxes and reporting",
    "How to spot legitimate crypto projects",
    "Setting up price alerts for cryptocurrencies",
    "Understanding crypto custody solutions",
    "How to participate in token sales safely",
]

TERMINOLOGY_TOPICS = [
    "HODL - Hold On for Dear Life",
    "FOMO - Fear Of Missing Out",
    "FUD - Fear, Uncertainty, and Doubt",
    "Whale - Large cryptocurrency holder",
    "Gas fees - Transaction costs on blockchain",
    "ATH - All-Time High price",
    "Bear market - Prolonged price decline",
    "Bull market - Prolonged price increase",
    "Satoshi - Smallest unit of Bitcoin",
    "Altcoin - Any cryptocurrency besides Bitcoin",
    "Staking - Locking crypto to earn rewards",
    "Mining - Validating transactions for rewards",
    "Airdrop - Free token distribution",
    "ICO - Initial Coin Offering",
    "Degen - Degenerate trader (risky behavior)",
    "Rekt - Suffering major losses",
    "Moon - Extreme price increase",
    "Diamond hands - Holding through volatility",
    "Paper hands - Selling at first sign of loss",
    "Rug pull - Scam where developers abandon project",
]


def get_random_topic(category: str) -> str:
    """Get a random topic from the specified category"""
    topic_map = {
        "crypto_education": CRYPTO_EDUCATION_TOPICS,
        "trading_tips": TRADING_TIPS_TOPICS,
        "crypto_security": SECURITY_TOPICS,
        "defi_explained": DEFI_TOPICS,
        "market_analysis": MARKET_ANALYSIS_TOPICS,
        "crypto_project": CRYPTO_PROJECT_TOPICS,
        "nft_knowledge": NFT_TOPICS,
        "beginner_guide": BEGINNER_GUIDE_TOPICS,
        "crypto_terminology": TERMINOLOGY_TOPICS,
    }
    
    topics = topic_map.get(category, [])
    if topics:
        return random.choice(topics)
    return ""


def get_varied_prompt(base_template: str, category: str) -> str:
    """Enhance a template with a specific random topic"""
    specific_topic = get_random_topic(category)
    
    if specific_topic:
        # Insert the specific topic at the beginning of the prompt
        return f"Focus on this specific topic: '{specific_topic}'. {base_template}"
    
    return base_template


def get_topic_and_varied_prompt(base_template: str, category: str) -> tuple[str, str]:
    """Return both the selected topic and the enhanced prompt."""
    specific_topic = get_random_topic(category)
    if specific_topic:
        prompt = f"Focus on this specific topic: '{specific_topic}'. {base_template}"
        return specific_topic, prompt
    return "Cryptocurrency", base_template
