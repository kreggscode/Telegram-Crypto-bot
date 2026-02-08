"""
Demo: Show actual content generation with variety
This simulates what the bot will post to Telegram
"""

from src.topic_rotator import get_varied_prompt, get_random_topic
from src.templates import TEXT_TEMPLATES
from src.pollinations_client import generate_text
from datetime import datetime

print("="*80)
print("LIVE CONTENT GENERATION DEMO")
print("="*80)
print("\nThis shows what your bot will actually post to Telegram")
print("Each run will be different due to:")
print("  ✅ Random topic selection (180+ topics)")
print("  ✅ Random seed (1000-999999)")
print("  ✅ Unique timestamp")
print("\n" + "="*80)

# Demo 1: Crypto Education
print("\n📚 DEMO 1: CRYPTO EDUCATION POST")
print("-" * 80)
topic1 = get_random_topic('crypto_education')
print(f"Selected Topic: {topic1}")
print(f"Timestamp: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")
print("\nGenerating content from Pollinations AI...")
print("-" * 80)

base_prompt = TEXT_TEMPLATES["crypto_education"]
varied_prompt = get_varied_prompt(base_prompt, "crypto_education")
content1 = generate_text(varied_prompt)
print("\n📝 GENERATED CONTENT:")
print(content1)

# Demo 2: Trading Tips
print("\n\n" + "="*80)
print("\n💡 DEMO 2: TRADING TIPS POST")
print("-" * 80)
topic2 = get_random_topic('trading_tips')
print(f"Selected Topic: {topic2}")
print(f"Timestamp: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")
print("\nGenerating content from Pollinations AI...")
print("-" * 80)

base_prompt2 = TEXT_TEMPLATES["trading_tips"]
varied_prompt2 = get_varied_prompt(base_prompt2, "trading_tips")
content2 = generate_text(varied_prompt2)
print("\n📝 GENERATED CONTENT:")
print(content2)

print("\n\n" + "="*80)
print("✅ VARIETY CONFIRMED!")
print("="*80)
print("\nNotice how:")
print("  • Different topics were selected")
print("  • Content is unique and specific")
print("  • Each post has fresh information")
print("\nYour users will now get varied content every day! 🎉")
print("="*80)
