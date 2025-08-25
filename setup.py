#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Job Bot - Setup Script
Loyihani birinchi marta o'rnatish uchun
"""

import os
import sys

def create_directory_structure():
    """Papka strukturasini yaratish"""
    directories = [
        'database',
        'services', 
        'handlers',
        'utils',
        'files',
        'files/resumes'
    ]
    
    print("📁 Papka strukturasi yaratilmoqda...")
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"   ✅ {directory}")
        else:
            print(f"   ⚠️ {directory} (mavjud)")

def create_init_files():
    """__init__.py fayllarini yaratish"""
    init_files = [
        'database/__init__.py',
        'services/__init__.py',
        'handlers/__init__.py', 
        'utils/__init__.py'
    ]
    
    print("\n📄 __init__.py fayllari yaratilmoqda...")
    for init_file in init_files:
        if not os.path.exists(init_file):
            with open(init_file, 'w', encoding='utf-8') as f:
                f.write(f'# {init_file.replace("/__init__.py", "")} package\n')
            print(f"   ✅ {init_file}")
        else:
            print(f"   ⚠️ {init_file} (mavjud)")

def create_env_template():
    """Environment template yaratish"""
    env_template = """# Bot Configuration
TELEGRAM_BOT_TOKEN=your_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here

# Database
DATABASE_URL=job_bot.db

# Files
FILES_PATH=files
MAX_FILE_SIZE_MB=10

# AI Settings
OPENAI_MODEL=gpt-4
MIN_MATCH_PERCENTAGE=60
MIN_INTERVIEW_SCORE=70

# Admin Users (telegram ID, vergul bilan ajratilgan)
ADMIN_USERS=123456789

# Logging
LOG_LEVEL=INFO
LOG_FILE=bot.log

# Session
SESSION_TIMEOUT=60

# Questions
MAX_QUESTIONS=5
MIN_QUESTIONS=1
"""
    
    print("\n⚙️ Environment template yaratilmoqda...")
    if not os.path.exists('.env'):
        with open('.env', 'w', encoding='utf-8') as f:
            f.write(env_template)
        print("   ✅ .env fayli yaratildi")
        print("   💡 Iltimos sozlamalarni to'ldiring!")
    else:
        print("   ⚠️ .env fayli allaqachon mavjud")

def show_next_steps():
    """Keyingi qadamlarni ko'rsatish"""
    print("\n" + "="*50)
    print("🎉 Setup muvaffaqiyatli yakunlandi!")
    print("="*50)
    print("\nKeyingi qadamlar:")
    print("1. 📝 .env faylini to'ldiring:")
    print("   - Telegram bot token (@BotFather)")
    print("   - OpenAI API key")
    print("   - Admin telegram ID")
    print()
    print("2. 📦 Kutubxonalarni o'rnating:")
    print("   pip install -r requirements.txt")
    print()
    print("3. 🚀 Botni ishga tushiring:")
    print("   python bot.py")
    print("   # yoki")
    print("   python run.py")
    print()
    print("4. 🧪 Testlash:")
    print("   - Botga /start yuboring") 
    print("   - Til tanlang")
    print("   - Rolni tanlang")
    print()
    print("📚 Qo'shimcha ma'lumot: README.md")
    print("="*50)

def main():
    """Asosiy setup funksiyasi"""
    print("🤖 Job Bot - Setup Script")
    print("Loyihani birinchi marta o'rnatish")
    print("="*40)
    
    # Python versiyasini tekshirish
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ talab qilinadi!")
        print(f"Sizda: Python {sys.version}")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} - OK")
    
    # Setup jarayoni
    create_directory_structure()
    create_init_files()
    create_env_template()
    
    # Keyingi qadamlar
    show_next_steps()

if __name__ == "__main__":
    main()