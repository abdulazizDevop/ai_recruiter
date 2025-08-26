# import os
# from typing import List
# from dotenv import load_dotenv

# load_dotenv()

# class Config:
#     """Bot konfiguratsiyasi"""
    
#     # Telegram Bot Token
#     TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'your_bot_token_here')
    
#     # OpenAI API Key
#     OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key_here')
    
#     # Database
#     DATABASE_URL = os.getenv('DATABASE_URL', 'job_bot.db')
    
#     # File Storage
#     FILES_BASE_PATH = os.getenv('FILES_PATH', 'files')
#     MAX_FILE_SIZE_MB = int(os.getenv('MAX_FILE_SIZE_MB', '10'))
    
#     # AI Settings
#     OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o')
#     MIN_MATCH_PERCENTAGE = int(os.getenv('MIN_MATCH_PERCENTAGE', '60'))
#     MIN_INTERVIEW_SCORE = int(os.getenv('MIN_INTERVIEW_SCORE', '70'))
    
#     # Admin Users (Telegram IDs)
#     ADMIN_USERS: List[int] = [
#         int(os.getenv('ADMIN_USERS', '0')),
#     ]
    
#     # Allowed File Formats
#     ALLOWED_FILE_EXTENSIONS = ['.pdf', '.doc', '.docx']
    
#     # Languages
#     DEFAULT_LANGUAGE = 'uz'
#     SUPPORTED_LANGUAGES = ['uz', 'ru']
    
#     # Bot Settings
#     WEBHOOK_URL = os.getenv('WEBHOOK_URL', None)  # Production uchun
#     WEBHOOK_PORT = int(os.getenv('WEBHOOK_PORT', '8443'))
    
#     # Logging
#     LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
#     LOG_FILE = os.getenv('LOG_FILE', 'bot.log')
    
#     # Session Settings
#     SESSION_TIMEOUT_MINUTES = int(os.getenv('SESSION_TIMEOUT', '60'))
    
#     # Interview Settings
#     MAX_QUESTIONS_COUNT = int(os.getenv('MAX_QUESTIONS', '7'))
#     MIN_QUESTIONS_COUNT = int(os.getenv('MIN_QUESTIONS', '3'))
    
#     @classmethod
#     def validate_config(cls) -> List[str]:
#         """Konfiguratsiyani tekshirish"""
#         errors = []
        
#         if not cls.TELEGRAM_BOT_TOKEN or cls.TELEGRAM_BOT_TOKEN == 'your_bot_token_here':
#             errors.append("TELEGRAM_BOT_TOKEN o'rnatilmagan")
        
#         if not cls.OPENAI_API_KEY or cls.OPENAI_API_KEY == 'your_openai_api_key_here':
#             errors.append("OPENAI_API_KEY o'rnatilmagan")
        
#         if not cls.ADMIN_USERS or cls.ADMIN_USERS == [123456789]:
#             errors.append("ADMIN_USERS ro'yxati to'ldirilmagan")
        
#         return errors
    
#     @classmethod
#     def is_admin(cls, user_id: int) -> bool:
#         """Admin tekshirish"""
#         return user_id in cls.ADMIN_USERS



import os
import logging
from typing import List, Optional
from dotenv import load_dotenv
from pathlib import Path

# .env faylni yuklash
load_dotenv()

class Config:
    """Bot konfiguratsiyasi - Professional version"""
    
    # ===========================================
    # ASOSIY SOZLAMALAR
    # ===========================================
    
    # Telegram Bot Token (majburiy)
    TELEGRAM_BOT_TOKEN: str = os.getenv('TELEGRAM_BOT_TOKEN', '')
    
    # OpenAI API Key (majburiy)
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', '')
    
    # Database
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'job_bot.db')
    
    # ===========================================
    # FILE VA STORAGE SOZLAMALARI  
    # ===========================================
    
    # File storage yo'li
    FILES_BASE_PATH: str = os.getenv('FILES_PATH', 'files')
    RESUMES_FOLDER: str = os.path.join(FILES_BASE_PATH, 'resumes')
    
    # File limitlari
    MAX_FILE_SIZE_MB: int = int(os.getenv('MAX_FILE_SIZE_MB', '10'))
    MAX_FILE_SIZE_BYTES: int = MAX_FILE_SIZE_MB * 1024 * 1024
    
    # Ruxsat etilgan file formatlari
    ALLOWED_FILE_EXTENSIONS: List[str] = ['.pdf', '.doc', '.docx']
    ALLOWED_MIME_TYPES: List[str] = [
        'application/pdf',
        'application/msword', 
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    ]
    
    # ===========================================
    # AI VA TAHLIL SOZLAMALARI
    # ===========================================
    
    # OpenAI model
    OPENAI_MODEL: str = os.getenv('OPENAI_MODEL', 'gpt-4o')
    OPENAI_MAX_TOKENS: int = int(os.getenv('OPENAI_MAX_TOKENS', '4000'))
    OPENAI_TEMPERATURE: float = float(os.getenv('OPENAI_TEMPERATURE', '0.3'))
    
    # AI tahlil chegaralari
    MIN_MATCH_PERCENTAGE: int = int(os.getenv('MIN_MATCH_PERCENTAGE', '60'))
    MIN_INTERVIEW_SCORE: int = int(os.getenv('MIN_INTERVIEW_SCORE', '70'))
    
    # Resume parsing settings
    USE_DIRECT_FILE_UPLOAD: bool = os.getenv('USE_DIRECT_FILE', 'true').lower() == 'true'
    USE_HYBRID_PARSING: bool = os.getenv('USE_HYBRID_PARSING', 'true').lower() == 'true'
    
    # ===========================================
    # FOYDALANUVCHI VA RUXSATLAR
    # ===========================================
    
    # Admin foydalanuvchilar (Telegram ID lar)
    ADMIN_USERS: List[int] = [
        int(x.strip()) for x in os.getenv('ADMIN_USERS', '').split(',') 
        if x.strip().isdigit()
    ]
    
    # ===========================================
    # TIL VA LOCALIZATION
    # ===========================================
    
    # Tillar
    DEFAULT_LANGUAGE: str = 'uz'
    SUPPORTED_LANGUAGES: List[str] = ['uz', 'ru']
    
    # ===========================================
    # SESSION VA INTERVIEW SOZLAMALARI
    # ===========================================
    
    # Session sozlamalari
    SESSION_TIMEOUT_MINUTES: int = int(os.getenv('SESSION_TIMEOUT', '60'))
    
    # Interview sozlamalari  
    MAX_QUESTIONS_COUNT: int = int(os.getenv('MAX_QUESTIONS', '7'))
    MIN_QUESTIONS_COUNT: int = int(os.getenv('MIN_QUESTIONS', '3'))
    
    # Savol-javob timeout (soniyalar)
    QUESTION_TIMEOUT_SECONDS: int = int(os.getenv('QUESTION_TIMEOUT', '300'))  # 5 daqiqa
    
    # ===========================================
    # LOGGING VA DEBUG
    # ===========================================
    
    # Logging sozlamalari
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE: str = os.getenv('LOG_FILE', 'logs/bot.log')
    LOG_MAX_SIZE_MB: int = int(os.getenv('LOG_MAX_SIZE', '50'))
    LOG_BACKUP_COUNT: int = int(os.getenv('LOG_BACKUP_COUNT', '5'))
    
    # Debug rejimi
    DEBUG_MODE: bool = os.getenv('DEBUG', 'false').lower() == 'true'
    
    # ===========================================
    # PERFORMANCE VA RATE LIMITING
    # ===========================================
    
    # Rate limiting (bir foydalanuvchi uchun)
    MAX_REQUESTS_PER_MINUTE: int = int(os.getenv('MAX_REQUESTS_PER_MINUTE', '10'))
    MAX_APPLICATIONS_PER_DAY: int = int(os.getenv('MAX_APPLICATIONS_PER_DAY', '5'))
    
    # OpenAI API rate limiting
    OPENAI_MAX_REQUESTS_PER_MINUTE: int = int(os.getenv('OPENAI_RPM', '50'))
    
    # ===========================================
    # METODLAR
    # ===========================================
    
    @classmethod
    def validate_config(cls) -> List[str]:
        """Konfiguratsiyani tekshirish va xatoliklarni qaytarish"""
        errors = []
        
        # Majburiy sozlamalarni tekshirish
        if not cls.TELEGRAM_BOT_TOKEN:
            errors.append("❌ TELEGRAM_BOT_TOKEN o'rnatilmagan (.env faylini tekshiring)")
        
        if not cls.OPENAI_API_KEY:
            errors.append("❌ OPENAI_API_KEY o'rnatilmagan (.env faylini tekshiring)")
        
        if not cls.ADMIN_USERS:
            errors.append("⚠️  ADMIN_USERS ro'yxati bo'sh (analytics ishlamaydi)")
        
        # Papka mavjudligini tekshirish
        Path(cls.FILES_BASE_PATH).mkdir(parents=True, exist_ok=True)
        Path(cls.RESUMES_FOLDER).mkdir(parents=True, exist_ok=True)
        Path(os.path.dirname(cls.LOG_FILE)).mkdir(parents=True, exist_ok=True)
        
        # Qiymatlarni tekshirish
        if cls.MIN_MATCH_PERCENTAGE < 0 or cls.MIN_MATCH_PERCENTAGE > 100:
            errors.append("❌ MIN_MATCH_PERCENTAGE 0-100 oralig'ida bo'lishi kerak")
            
        if cls.MAX_FILE_SIZE_MB > 50:
            errors.append("⚠️  MAX_FILE_SIZE_MB juda katta (50MB dan oshmasin)")
        
        return errors
    
    @classmethod  
    def is_admin(cls, user_id: int) -> bool:
        """Foydalanuvchi admin ekanligini tekshirish"""
        return user_id in cls.ADMIN_USERS
    
    @classmethod
    def setup_logging(cls):
        """Logging tizimini sozlash"""
        from logging.handlers import RotatingFileHandler
        
        # Log papkasini yaratish
        log_dir = os.path.dirname(cls.LOG_FILE)
        Path(log_dir).mkdir(parents=True, exist_ok=True)
        
        # Logging format
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # File handler
        file_handler = RotatingFileHandler(
            cls.LOG_FILE,
            maxBytes=cls.LOG_MAX_SIZE_MB * 1024 * 1024,
            backupCount=cls.LOG_BACKUP_COUNT
        )
        file_handler.setFormatter(formatter)
        
        # Console handler  
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        
        # Root logger sozlash
        logger = logging.getLogger()
        logger.setLevel(getattr(logging, cls.LOG_LEVEL.upper()))
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    @classmethod
    def get_file_path(cls, filename: str, subfolder: str = 'resumes') -> str:
        """File yo'lini olish"""
        folder_path = os.path.join(cls.FILES_BASE_PATH, subfolder)
        Path(folder_path).mkdir(parents=True, exist_ok=True)
        return os.path.join(folder_path, filename)
    
    @classmethod
    def is_file_allowed(cls, filename: str) -> bool:
        """File formatini tekshirish"""
        return any(filename.lower().endswith(ext) for ext in cls.ALLOWED_FILE_EXTENSIONS)
    
    @classmethod  
    def get_openai_config(cls) -> dict:
        """OpenAI API uchun sozlamalar"""
        return {
            'api_key': cls.OPENAI_API_KEY,
            'model': cls.OPENAI_MODEL,
            'max_tokens': cls.OPENAI_MAX_TOKENS,
            'temperature': cls.OPENAI_TEMPERATURE
        }

# Singleton pattern uchun instance
config = Config()

# Sozlamalarni tekshirish
def validate_and_setup():
    """Sozlamalarni tekshirish va tizimni sozlash"""
    errors = config.validate_config()
    
    if errors:
        print("🔴 Konfiguratsiya xatoliklari:")
        for error in errors:
            print(f"  {error}")
        
        # Kritik xatolik bor-yo'qligini tekshirish  
        critical_errors = [e for e in errors if "❌" in e]
        if critical_errors:
            print("\n💀 Kritik xatoliklar tufayli bot ishga tushmaydi!")
            exit(1)
        else:
            print("\n⚠️  Ba'zi sozlamalar noto'g'ri, lekin bot ishlashi mumkin")
    
    # Logging ni sozlash
    config.setup_logging()
    
    print("✅ Konfiguratsiya muvaffaqiyatli tekshirildi")
    print(f"📊 Admin foydalanuvchilar: {len(config.ADMIN_USERS)}")
    print(f"🤖 OpenAI model: {config.OPENAI_MODEL}")
    print(f"📁 Fayllar papkasi: {config.FILES_BASE_PATH}")

if __name__ == "__main__":
    # Test rejimi
    validate_and_setup()
