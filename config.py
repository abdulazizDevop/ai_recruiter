import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Bot konfiguratsiyasi"""
    
    # Telegram Bot Token
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'your_bot_token_here')
    
    # OpenAI API Key
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key_here')
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'job_bot.db')
    
    # File Storage
    FILES_BASE_PATH = os.getenv('FILES_PATH', 'files')
    MAX_FILE_SIZE_MB = int(os.getenv('MAX_FILE_SIZE_MB', '10'))
    
    # AI Settings
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o')
    MIN_MATCH_PERCENTAGE = int(os.getenv('MIN_MATCH_PERCENTAGE', '60'))
    MIN_INTERVIEW_SCORE = int(os.getenv('MIN_INTERVIEW_SCORE', '70'))
    
    # Admin Users (Telegram IDs)
    ADMIN_USERS: List[int] = [
        int(os.getenv('ADMIN_USERS', '0')),
    ]
    
    # Allowed File Formats
    ALLOWED_FILE_EXTENSIONS = ['.pdf', '.doc', '.docx']
    
    # Languages
    DEFAULT_LANGUAGE = 'uz'
    SUPPORTED_LANGUAGES = ['uz', 'ru']
    
    # Bot Settings
    WEBHOOK_URL = os.getenv('WEBHOOK_URL', None)  # Production uchun
    WEBHOOK_PORT = int(os.getenv('WEBHOOK_PORT', '8443'))
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'bot.log')
    
    # Session Settings
    SESSION_TIMEOUT_MINUTES = int(os.getenv('SESSION_TIMEOUT', '60'))
    
    # Interview Settings
    MAX_QUESTIONS_COUNT = int(os.getenv('MAX_QUESTIONS', '5'))
    MIN_QUESTIONS_COUNT = int(os.getenv('MIN_QUESTIONS', '1'))
    
    @classmethod
    def validate_config(cls) -> List[str]:
        """Konfiguratsiyani tekshirish"""
        errors = []
        
        if not cls.TELEGRAM_BOT_TOKEN or cls.TELEGRAM_BOT_TOKEN == 'your_bot_token_here':
            errors.append("TELEGRAM_BOT_TOKEN o'rnatilmagan")
        
        if not cls.OPENAI_API_KEY or cls.OPENAI_API_KEY == 'your_openai_api_key_here':
            errors.append("OPENAI_API_KEY o'rnatilmagan")
        
        if not cls.ADMIN_USERS or cls.ADMIN_USERS == [123456789]:
            errors.append("ADMIN_USERS ro'yxati to'ldirilmagan")
        
        return errors
    
    @classmethod
    def is_admin(cls, user_id: int) -> bool:
        """Admin tekshirish"""
        return user_id in cls.ADMIN_USERS