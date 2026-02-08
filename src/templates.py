"""
AI Prompt Templates for Cryptocurrency Content Generation
"""

TEXT_TEMPLATES = {
    "crypto_education": (
        "Explain a cryptocurrency or blockchain concept in simple terms for beginners. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** at the top\n"
        "- Use **bold text** for key terms\n"
        "- Add bullet points (•) for lists\n"
        "- Include blank lines between sections\n"
        "- Use emojis for visual appeal\n"
        "Topics: Bitcoin, Ethereum, DeFi, NFTs, smart contracts, mining, staking, wallets, etc. "
        "Make it educational and easy to read. Under 150 words."
    ),
    "trading_tips": (
        "Share a practical cryptocurrency trading tip for beginners or intermediate traders. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '💡 Trading Tip:' at the top\n"
        "- Use **bold text** for important points\n"
        "- Add bullet points (•) for tips\n"
        "- Include blank lines for readability\n"
        "- Use emojis\n"
        "Include risk management, technical analysis, or portfolio strategies. "
        "End with: ⚠️ *This is educational content, not financial advice.* "
        "Under 150 words."
    ),
    "crypto_security": (
        "Explain a cryptocurrency security best practice or common scam to avoid. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '🔐 Security Alert:' at the top\n"
        "- Use **bold text** for warnings\n"
        "- Add bullet points (•) for security tips\n"
        "- Include blank lines between sections\n"
        "- Use warning emojis (⚠️, 🚨)\n"
        "Topics: wallet security, private keys, 2FA, phishing, rug pulls, fake exchanges. "
        "Under 150 words."
    ),
    "defi_explained": (
        "Explain a DeFi (Decentralized Finance) concept in simple terms. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '🏦 DeFi Explained:' at the top\n"
        "- Use **bold text** for key concepts\n"
        "- Add bullet points (•) for features/benefits\n"
        "- Include blank lines for readability\n"
        "- Use emojis\n"
        "Topics: yield farming, liquidity pools, DEXs, lending protocols, stablecoins. "
        "Make it beginner-friendly. Under 150 words."
    ),
    "market_analysis": (
        "Provide a brief analysis of cryptocurrency market trends or sentiment. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '📊 Market Analysis:' at the top\n"
        "- Use **bold text** for key metrics\n"
        "- Add bullet points (•) for trends\n"
        "- Include blank lines between sections\n"
        "- Use emojis (📈, 📉, 💹)\n"
        "Discuss Bitcoin dominance, altcoin season, market cycles, or macro trends. "
        "Under 150 words."
    ),
    "crypto_project": (
        "Introduce a popular cryptocurrency project or blockchain platform. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** with project name at the top\n"
        "- Use **bold text** for key features\n"
        "- Add bullet points (•) for use cases\n"
        "- Include blank lines for readability\n"
        "- Use emojis\n"
        "Examples: Ethereum, Solana, Cardano, Polygon, Chainlink. "
        "Under 150 words."
    ),
    "nft_knowledge": (
        "Explain an NFT (Non-Fungible Token) concept or use case. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '🎨 NFT Knowledge:' at the top\n"
        "- Use **bold text** for key terms\n"
        "- Add bullet points (•) for examples\n"
        "- Include blank lines between sections\n"
        "- Use emojis\n"
        "Topics: what NFTs are, digital art, gaming, utility NFTs, marketplaces. "
        "Under 150 words."
    ),
    "crypto_news_summary": (
        "Create a brief, engaging summary of a cryptocurrency market update or trend. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '📰 Crypto Update:' at the top\n"
        "- Use **bold text** for key points\n"
        "- Add bullet points (•) if listing multiple items\n"
        "- Include blank lines for readability\n"
        "- Use emojis\n"
        "Focus on recent developments, regulatory news, or major updates. "
        "Under 150 words."
    ),
    "thread_explainer": (
        "Explain a cryptocurrency or blockchain topic in 4 short numbered sections. "
        "FORMAT STRICTLY AS:\n"
        "**[Topic Name] - A Thread 🧵**\n\n"
        "**1️⃣ What It Is:**\n[2-3 sentences]\n\n"
        "**2️⃣ How It Works:**\n[2-3 sentences]\n\n"
        "**3️⃣ Why It Matters:**\n[2-3 sentences]\n\n"
        "**4️⃣ Risks/Considerations:**\n[2-3 sentences]\n\n"
        "Use emojis and keep each section clear."
    ),
    "poll_question": (
        "Create ONE challenging cryptocurrency multiple-choice quiz question. "
        "STRICT FORMAT:\n"
        "Question: [The question text]\n"
        "A: [Option 1]\n"
        "B: [Option 2]\n"
        "C: [Option 3]\n"
        "D: [Option 4]\n"
        "Correct: [Answer Letter]\n"
        "Explanation: [Brief explanation of why that's correct]"
    ),
    "daily_challenge": (
        "Create a fun cryptocurrency quiz or challenge for learners. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '🎯 Daily Crypto Challenge:' at the top\n"
        "- Use **bold text** for the question\n"
        "- Include blank lines for readability\n"
        "- Use emojis\n"
        "- End with an encouraging message\n"
        "Make it engaging and educational. Under 150 words."
    ),
    "price_alert": (
        "Create an engaging message about a significant cryptocurrency price movement. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '🚨 Price Alert:' at the top\n"
        "- Use **bold text** for coin name and price\n"
        "- Include blank lines for readability\n"
        "- Use emojis (🚀📈📉💎)\n"
        "Keep it exciting but factual. Under 100 words."
    ),
    "beginner_guide": (
        "Create a beginner's guide snippet about getting started with cryptocurrency. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '👋 Beginner Guide:' at the top\n"
        "- Use **bold text** for important steps\n"
        "- Add bullet points (•) or numbered steps\n"
        "- Include blank lines between sections\n"
        "- Use emojis\n"
        "Topics: how to buy crypto, choosing a wallet, first steps, safety tips. "
        "Under 150 words."
    ),
    "crypto_terminology": (
        "Explain a common cryptocurrency term or slang in simple language. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** with the term at the top\n"
        "- Use **bold text** for the definition\n"
        "- Add an example in bullet point\n"
        "- Include blank lines for readability\n"
        "- Use emojis\n"
        "Examples: HODL, FOMO, FUD, whale, gas fees, ATH, bear/bull market. "
        "Under 100 words."
    )
}


IMAGE_TEMPLATES = {
    "bitcoin_gold": "golden Bitcoin coin floating in space with glowing blue blockchain network connections, futuristic digital art, dark background with neon accents",
    "crypto_trading": "futuristic cryptocurrency trading desk with multiple holographic charts showing candlesticks and price movements, cyberpunk aesthetic, neon green and blue",
    "blockchain_network": "abstract 3D visualization of blockchain network with glowing nodes and connections, purple and blue gradient, modern tech illustration",
    "ethereum_crystal": "ethereal Ethereum crystal logo with digital particles and smart contract code flowing around it, mystical tech aesthetic, vibrant colors",
    "defi_ecosystem": "decentralized finance ecosystem visualization with interconnected protocols and liquidity pools, modern infographic style, bright colors",
    "crypto_wallet": "secure digital cryptocurrency wallet with shield protection and multiple coin logos, professional illustration, blue and gold theme",
    "nft_gallery": "futuristic NFT art gallery with digital frames displaying various artworks, cyberpunk museum aesthetic, colorful and vibrant",
    "bull_market": "powerful bull made of golden light charging upward with cryptocurrency symbols, dynamic composition, green and gold colors",
    "bear_market": "majestic bear made of blue energy with downward trending charts, dramatic lighting, blue and red colors",
    "mining_rig": "high-tech cryptocurrency mining rig with glowing GPUs and flowing data streams, industrial cyberpunk aesthetic, blue lighting",
    "altcoin_universe": "cosmic space scene with various altcoin logos as planets orbiting around Bitcoin sun, creative digital art, vibrant space colors",
    "crypto_security": "digital fortress protecting cryptocurrency assets with encryption shields and security layers, professional tech illustration, blue and green",
}
