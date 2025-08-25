#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Job Bot ishga tushirish scripti
"""

import sys
import os
import subprocess

def check_python_version():
    """Python versiyasini tekshirish"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ talab qilinadi!")
        print(f"📍 Sizda: Python {sys.version}")
        sys.exit(1)
    print(f"✅ Python {sys.version} - OK")

def check_requirements():
    """Requirements.txt mavjudligini tekshirish"""
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt fayli topilmadi!")
        sys.exit(1)
    print("✅ requirements.txt - OK")

def check_env_file():
    """Environment fayl tekshirish"""
    if not os.path.exists('.env'):
        print("⚠️  .env fayli topilmadi!")
        print("💡 Config.py faylini ishga tushirib .env yarating:")
        print("   python config.py")
        return False
    print("✅ .env fayli - OK")
    return True

def install_requirements():
    """Kutubxonalarni o'rnatish"""
    try:
        print("📦 Kutubxonalar o'rnatilmoqda...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Kutubxonalar o'rnatildi")
    except subprocess.CalledProcessError:
        print("❌ Kutubxonalarni o'rnatishda xatolik!")
        sys.exit(1)

def create_directories():
    """Kerakli papkalarni yaratish"""
    directories = [
        'files',
        'files/resumes',
        'database',
        'services', 
        'handlers',
        'utils'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Yaratildi: {directory}")

def run_bot():
    """Botni ishga tushirish"""
    try:
        print("🚀 Bot ishga tushirilmoqda...")
        subprocess.run([sys.executable, "bot.py"])
    except KeyboardInterrupt:
        print("\n👋 Bot to'xtatildi")
    except Exception as e:
        print(f"❌ Bot ishga tushirishda xatolik: {e}")

def main():
    """Asosiy funksiya"""
    print("🤖 Job Bot - Ishga Tushirish Scripti")
    print("=" * 40)
    
    # Tekshiruvlar
    check_python_version()
    check_requirements()
    
    # Papkalarni yaratish
    create_directories()
    
    # Environment fayl tekshirish
    if not check_env_file():
        choice = input("📝 .env faylini yaratishni xohlaysizmi? (y/n): ")
        if choice.lower() in ['y', 'yes', 'ha']:
            try:
                subprocess.run([sys.executable, "config.py"])
                print("✅ .env fayli yaratildi")
                print("💡 Iltimos sozlamalarni to'ldiring va qaytadan ishga tushiring")
                sys.exit(0)
            except:
                print("❌ .env faylini yaratishda xatolik!")
                sys.exit(1)
        else:
            print("❌ .env fayli kerak!")
            sys.exit(1)
    
    # Kutubxonalar o'rnatish
    choice = input("📦 Kutubxonalarni o'rnatish kerakmi? (y/n): ")
    if choice.lower() in ['y', 'yes', 'ha']:
        install_requirements()
    
    print("=" * 40)
    print("🎉 Barcha tekshiruvlar o'tdi!")
    print("🚀 Bot ishga tushmoqda...")
    print("⏹️  To'xtatish uchun Ctrl+C bosing")
    print("=" * 40)
    
    # Botni ishga tushirish
    run_bot()

if __name__ == "__main__":
    main()