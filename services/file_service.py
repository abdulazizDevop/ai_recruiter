import os
import shutil
from typing import Optional
import logging
from services.ai_service import validate_file_format, get_file_size_mb, create_safe_filename

class FileService:
    def __init__(self, base_path: str = "files"):
        """Fayl boshqaruvi servisi"""
        self.base_path = base_path
        self.resume_path = os.path.join(base_path, "resumes")
        self.temp_path = os.path.join(base_path, "temp")
        self.max_file_size_mb = 10  # Maksimal fayl hajmi MB da
        
        # Logging sozlash
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Papkalarni yaratish
        self._create_directories()
    
    def _create_directories(self):
        """Kerakli papkalarni yaratish"""
        directories = [self.base_path, self.resume_path, self.temp_path]
        
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
                self.logger.info(f"Papka yaratildi: {directory}")
    
    def save_resume_file(self, file_info, user_id: int, file_content: bytes) -> Optional[str]:
        """Resume faylni saqlash"""
        try:
            original_filename = file_info.file_name
            
            # Fayl formatini tekshirish
            if not validate_file_format(original_filename):
                self.logger.error(f"Noto'g'ri fayl formati: {original_filename}")
                return None
            
            # Xavfsiz fayl nomi yaratish
            safe_filename = create_safe_filename(original_filename, user_id)
            file_path = os.path.join(self.resume_path, safe_filename)
            
            # Faylni saqlash
            with open(file_path, 'wb') as f:
                f.write(file_content)
            
            # Fayl hajmini tekshirish
            file_size = get_file_size_mb(file_path)
            if file_size > self.max_file_size_mb:
                self.logger.error(f"Fayl juda katta: {file_size}MB")
                self.delete_file(file_path)
                return None
            
            self.logger.info(f"Resume saqlandi: {file_path} ({file_size}MB)")
            return file_path
            
        except Exception as e:
            self.logger.error(f"Resume saqlashda xatolik: {e}")
            return None
    
    def get_resume_path(self, filename: str) -> str:
        """Resume fayl yo'lini qaytarish"""
        return os.path.join(self.resume_path, filename)
    
    def file_exists(self, file_path: str) -> bool:
        """Fayl mavjudligini tekshirish"""
        return os.path.exists(file_path)
    
    def delete_file(self, file_path: str) -> bool:
        """Faylni o'chirish"""
        try:
            if self.file_exists(file_path):
                os.remove(file_path)
                self.logger.info(f"Fayl o'chirildi: {file_path}")
                return True
            return False
        except Exception as e:
            self.logger.error(f"Faylni o'chirishda xatolik: {e}")
            return False
    
    def copy_file(self, source_path: str, destination_path: str) -> bool:
        """Faylni nusxalash"""
        try:
            shutil.copy2(source_path, destination_path)
            self.logger.info(f"Fayl nusxalandi: {source_path} -> {destination_path}")
            return True
        except Exception as e:
            self.logger.error(f"Faylni nusxalashda xatolik: {e}")
            return False
    
    def get_file_info(self, file_path: str) -> dict:
        """Fayl haqida ma'lumot olish"""
        try:
            if not self.file_exists(file_path):
                return {}
            
            stat = os.stat(file_path)
            filename = os.path.basename(file_path)
            
            return {
                "filename": filename,
                "size_bytes": stat.st_size,
                "size_mb": get_file_size_mb(file_path),
                "created_time": stat.st_ctime,
                "modified_time": stat.st_mtime
            }
        except Exception as e:
            self.logger.error(f"Fayl ma'lumotlarini olishda xatolik: {e}")
            return {}
    
    def cleanup_old_files(self, days: int = 30):
        """Eski fayllarni tozalash"""
        import time
        
        try:
            current_time = time.time()
            cutoff_time = current_time - (days * 24 * 60 * 60)
            
            deleted_count = 0
            
            for root, dirs, files in os.walk(self.base_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        if os.path.getctime(file_path) < cutoff_time:
                            os.remove(file_path)
                            deleted_count += 1
                    except:
                        continue
            
            self.logger.info(f"Tozalandi {deleted_count} ta eski fayl")
            return deleted_count
            
        except Exception as e:
            self.logger.error(f"Fayllarni tozalashda xatolik: {e}")
            return 0
    
    def get_storage_stats(self) -> dict:
        """Xotira statistikasi"""
        try:
            stats = {
                "total_files": 0,
                "total_size_mb": 0,
                "resume_count": 0,
                "resume_size_mb": 0
            }
            
            # Barcha fayllar
            for root, dirs, files in os.walk(self.base_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        size = get_file_size_mb(file_path)
                        stats["total_files"] += 1
                        stats["total_size_mb"] += size
                        
                        # Resume fayllar
                        if root == self.resume_path:
                            stats["resume_count"] += 1
                            stats["resume_size_mb"] += size
                    except:
                        continue
            
            return stats
            
        except Exception as e:
            self.logger.error(f"Statistika olishda xatolik: {e}")
            return {}

# Yordamchi funksiyalar
def format_file_size(size_mb: float) -> str:
    """Fayl hajmini formatlash"""
    if size_mb < 1:
        return f"{size_mb * 1024:.0f} KB"
    elif size_mb < 1024:
        return f"{size_mb:.1f} MB"
    else:
        return f"{size_mb / 1024:.1f} GB"

def get_file_extension(filename: str) -> str:
    """Fayl kengaytmasini olish"""
    return os.path.splitext(filename)[1].lower()

def is_valid_resume_file(filename: str, max_size_mb: float = 10) -> tuple[bool, str]:
    """Resume fayl validligini tekshirish"""
    # Format tekshirish
    if not validate_file_format(filename):
        return False, "Noto'g'ri fayl formati. Faqat PDF, DOC, DOCX fayllar qabul qilinadi."
    
    return True, "OK"