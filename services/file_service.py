# import os
# import shutil
# from typing import Optional
# import logging
# from services.ai_service import validate_file_format, get_file_size_mb, create_safe_filename

# class FileService:
#     def __init__(self, base_path: str = "files"):
#         """Fayl boshqaruvi servisi"""
#         self.base_path = base_path
#         self.resume_path = os.path.join(base_path, "resumes")
#         self.temp_path = os.path.join(base_path, "temp")
#         self.max_file_size_mb = 10  # Maksimal fayl hajmi MB da
        
#         # Logging sozlash
#         logging.basicConfig(level=logging.INFO)
#         self.logger = logging.getLogger(__name__)
        
#         # Papkalarni yaratish
#         self._create_directories()
    
#     def _create_directories(self):
#         """Kerakli papkalarni yaratish"""
#         directories = [self.base_path, self.resume_path, self.temp_path]
        
#         for directory in directories:
#             if not os.path.exists(directory):
#                 os.makedirs(directory)
#                 self.logger.info(f"Papka yaratildi: {directory}")
    
#     def save_resume_file(self, file_info, user_id: int, file_content: bytes) -> Optional[str]:
#         """Resume faylni saqlash"""
#         try:
#             original_filename = file_info.file_name
            
#             # Fayl formatini tekshirish
#             if not validate_file_format(original_filename):
#                 self.logger.error(f"Noto'g'ri fayl formati: {original_filename}")
#                 return None
            
#             # Xavfsiz fayl nomi yaratish
#             safe_filename = create_safe_filename(original_filename, user_id)
#             file_path = os.path.join(self.resume_path, safe_filename)
            
#             # Faylni saqlash
#             with open(file_path, 'wb') as f:
#                 f.write(file_content)
            
#             # Fayl hajmini tekshirish
#             file_size = get_file_size_mb(file_path)
#             if file_size > self.max_file_size_mb:
#                 self.logger.error(f"Fayl juda katta: {file_size}MB")
#                 self.delete_file(file_path)
#                 return None
            
#             self.logger.info(f"Resume saqlandi: {file_path} ({file_size}MB)")
#             return file_path
            
#         except Exception as e:
#             self.logger.error(f"Resume saqlashda xatolik: {e}")
#             return None
    
#     def get_resume_path(self, filename: str) -> str:
#         """Resume fayl yo'lini qaytarish"""
#         return os.path.join(self.resume_path, filename)
    
#     def file_exists(self, file_path: str) -> bool:
#         """Fayl mavjudligini tekshirish"""
#         return os.path.exists(file_path)
    
#     def delete_file(self, file_path: str) -> bool:
#         """Faylni o'chirish"""
#         try:
#             if self.file_exists(file_path):
#                 os.remove(file_path)
#                 self.logger.info(f"Fayl o'chirildi: {file_path}")
#                 return True
#             return False
#         except Exception as e:
#             self.logger.error(f"Faylni o'chirishda xatolik: {e}")
#             return False
    
#     def copy_file(self, source_path: str, destination_path: str) -> bool:
#         """Faylni nusxalash"""
#         try:
#             shutil.copy2(source_path, destination_path)
#             self.logger.info(f"Fayl nusxalandi: {source_path} -> {destination_path}")
#             return True
#         except Exception as e:
#             self.logger.error(f"Faylni nusxalashda xatolik: {e}")
#             return False
    
#     def get_file_info(self, file_path: str) -> dict:
#         """Fayl haqida ma'lumot olish"""
#         try:
#             if not self.file_exists(file_path):
#                 return {}
            
#             stat = os.stat(file_path)
#             filename = os.path.basename(file_path)
            
#             return {
#                 "filename": filename,
#                 "size_bytes": stat.st_size,
#                 "size_mb": get_file_size_mb(file_path),
#                 "created_time": stat.st_ctime,
#                 "modified_time": stat.st_mtime
#             }
#         except Exception as e:
#             self.logger.error(f"Fayl ma'lumotlarini olishda xatolik: {e}")
#             return {}
    
#     def cleanup_old_files(self, days: int = 30):
#         """Eski fayllarni tozalash"""
#         import time
        
#         try:
#             current_time = time.time()
#             cutoff_time = current_time - (days * 24 * 60 * 60)
            
#             deleted_count = 0
            
#             for root, dirs, files in os.walk(self.base_path):
#                 for file in files:
#                     file_path = os.path.join(root, file)
#                     try:
#                         if os.path.getctime(file_path) < cutoff_time:
#                             os.remove(file_path)
#                             deleted_count += 1
#                     except:
#                         continue
            
#             self.logger.info(f"Tozalandi {deleted_count} ta eski fayl")
#             return deleted_count
            
#         except Exception as e:
#             self.logger.error(f"Fayllarni tozalashda xatolik: {e}")
#             return 0
    
#     def get_storage_stats(self) -> dict:
#         """Xotira statistikasi"""
#         try:
#             stats = {
#                 "total_files": 0,
#                 "total_size_mb": 0,
#                 "resume_count": 0,
#                 "resume_size_mb": 0
#             }
            
#             # Barcha fayllar
#             for root, dirs, files in os.walk(self.base_path):
#                 for file in files:
#                     file_path = os.path.join(root, file)
#                     try:
#                         size = get_file_size_mb(file_path)
#                         stats["total_files"] += 1
#                         stats["total_size_mb"] += size
                        
#                         # Resume fayllar
#                         if root == self.resume_path:
#                             stats["resume_count"] += 1
#                             stats["resume_size_mb"] += size
#                     except:
#                         continue
            
#             return stats
            
#         except Exception as e:
#             self.logger.error(f"Statistika olishda xatolik: {e}")
#             return {}

# # Yordamchi funksiyalar
# def format_file_size(size_mb: float) -> str:
#     """Fayl hajmini formatlash"""
#     if size_mb < 1:
#         return f"{size_mb * 1024:.0f} KB"
#     elif size_mb < 1024:
#         return f"{size_mb:.1f} MB"
#     else:
#         return f"{size_mb / 1024:.1f} GB"

# def get_file_extension(filename: str) -> str:
#     """Fayl kengaytmasini olish"""
#     return os.path.splitext(filename)[1].lower()

# def is_valid_resume_file(filename: str, max_size_mb: float = 10) -> tuple[bool, str]:
#     """Resume fayl validligini tekshirish"""
#     # Format tekshirish
#     if not validate_file_format(filename):
#         return False, "Noto'g'ri fayl formati. Faqat PDF, DOC, DOCX fayllar qabul qilinadi."
    
#     return True, "OK"


# -*- coding: utf-8 -*-

import asyncio
import os
import aiofiles
import aiofiles.os
import logging
import time
import hashlib
import mimetypes
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, Tuple
from contextlib import asynccontextmanager
import tempfile

# Third-party imports
import magic  # MIME type detection

# Local imports
from config import Config

# Logger setup
logger = logging.getLogger(__name__)

# ===========================================
# FILE SERVICE CLASS - Professional Version
# ===========================================

class FileService:
    """
    Professional fayl boshqaruvi servisi
    Async operations, security, validation, cleanup
    """
    
    def __init__(self, base_path: str = None):
        """FileService ni inicializatsiya qilish"""
        self.base_path = base_path or Config.FILES_BASE_PATH
        self.resume_path = os.path.join(self.base_path, "resumes")
        self.temp_path = os.path.join(self.base_path, "temp")
        self.backup_path = os.path.join(self.base_path, "backups")
        
        # File limits va settings
        self.max_file_size_bytes = Config.MAX_FILE_SIZE_BYTES
        self.allowed_extensions = Config.ALLOWED_FILE_EXTENSIONS
        self.allowed_mime_types = Config.ALLOWED_MIME_TYPES
        
        # Security settings
        self.quarantine_path = os.path.join(self.base_path, "quarantine")
        self.scan_enabled = True
        
        # Performance settings
        self.chunk_size = 1024 * 1024  # 1MB chunks
        self.max_concurrent_operations = 10
        
        # Initialize directories
        self.ensure_directories()
        
        logger.info(f"FileService initialized: {self.base_path}")
    
    async def _initialize_directories(self):
        """Async directories yaratish"""
        try:
            directories = [
                self.base_path,
                self.resume_path,
                self.temp_path,
                self.backup_path,
                self.quarantine_path
            ]
            
            for directory in directories:
                await self.ensure_directory_exists(directory)
            
            logger.info("All directories initialized successfully")
            
        except Exception as e:
            logger.error(f"Directory initialization error: {e}")
    
    def ensure_directories(self):
        """Sync version - initialization uchun"""
        directories = [
            self.base_path,
            self.resume_path,
            self.temp_path,
            self.backup_path,
            self.quarantine_path
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
    
    # ===========================================
    # FILE SAVING AND VALIDATION
    # ===========================================
    
    async def save_resume_file(self, filename: str, user_id: int, file_content: bytes) -> Optional[str]:
        """Resume faylni async holda saqlash - Professional version"""
        try:
            # Pre-validation
            validation_result = await self._validate_file_content(filename, file_content)
            if not validation_result['valid']:
                logger.warning(f"File validation failed: {validation_result['reason']}")
                return None
            
            # Safe filename yaratish
            safe_filename = self._create_safe_filename(filename, user_id)
            final_path = os.path.join(self.resume_path, safe_filename)
            
            # Temp file orqali xavfsiz saqlash
            temp_path = await self._save_to_temp(file_content)
            if not temp_path:
                return None
            
            try:
                # Additional security scan
                if self.scan_enabled:
                    scan_result = await self._security_scan_file(temp_path, filename)
                    if not scan_result['safe']:
                        await self._quarantine_file(temp_path, safe_filename, scan_result['reason'])
                        return None
                
                # Atomic move to final location
                await aiofiles.os.rename(temp_path, final_path)
                
                # File metadata saqlash
                await self._save_file_metadata(final_path, user_id, filename)
                
                # Success logging
                file_size_mb = len(file_content) / (1024 * 1024)
                logger.info(f"Resume saved successfully: {safe_filename} ({file_size_mb:.2f}MB) for user {user_id}")
                
                return final_path
                
            except Exception as e:
                # Cleanup on failure
                await self._cleanup_temp_file(temp_path)
                raise e
                
        except Exception as e:
            logger.error(f"Resume saving error: {e}")
            return None
    
    async def _validate_file_content(self, filename: str, content: bytes) -> Dict[str, Any]:
        """File content va metadata validatsiyasi"""
        try:
            # Size validation
            if len(content) > self.max_file_size_bytes:
                return {
                    'valid': False,
                    'reason': f'File too large: {len(content)} bytes (max: {self.max_file_size_bytes})'
                }
            
            if len(content) < 100:  # Minimum file size
                return {
                    'valid': False,
                    'reason': 'File too small: likely corrupted or empty'
                }
            
            # Extension validation
            file_extension = Path(filename).suffix.lower()
            if file_extension not in self.allowed_extensions:
                return {
                    'valid': False,
                    'reason': f'Invalid extension: {file_extension}'
                }
            
            # MIME type validation
            detected_mime = magic.from_buffer(content, mime=True) if magic else None
            if detected_mime and detected_mime not in self.allowed_mime_types:
                return {
                    'valid': False,
                    'reason': f'Invalid MIME type: {detected_mime}'
                }
            
            # PDF/DOCX specific validation
            if file_extension == '.pdf':
                if not content.startswith(b'%PDF-'):
                    return {'valid': False, 'reason': 'Invalid PDF header'}
            elif file_extension in ['.docx', '.doc']:
                if file_extension == '.docx' and b'PK' not in content[:4]:
                    return {'valid': False, 'reason': 'Invalid DOCX structure'}
            
            return {
                'valid': True,
                'reason': 'File validation passed',
                'detected_mime': detected_mime,
                'size_bytes': len(content)
            }
            
        except Exception as e:
            logger.error(f"File validation error: {e}")
            return {'valid': False, 'reason': f'Validation error: {e}'}
    
    async def _save_to_temp(self, content: bytes) -> Optional[str]:
        """Faylni temp papkaga saqlash"""
        try:
            # Unique temp filename
            temp_filename = f"temp_{int(time.time())}_{hash(content) % 100000}.tmp"
            temp_path = os.path.join(self.temp_path, temp_filename)
            
            # Async file writing with chunks
            async with aiofiles.open(temp_path, 'wb') as f:
                # Write in chunks for better memory management
                for i in range(0, len(content), self.chunk_size):
                    chunk = content[i:i + self.chunk_size]
                    await f.write(chunk)
            
            return temp_path
            
        except Exception as e:
            logger.error(f"Temp file saving error: {e}")
            return None
    
    def _create_safe_filename(self, original_filename: str, user_id: int) -> str:
        """Xavfsiz va unique filename yaratish - Enhanced version"""
        if not original_filename:
            return f"resume_{user_id}_{int(time.time())}.pdf"
        
        # Basic sanitization
        safe_name = "".join(c for c in original_filename if c.isalnum() or c in "._-")
        
        # Length limitation
        name_part, extension = os.path.splitext(safe_name)
        if len(name_part) > 50:
            name_part = name_part[:50]
        
        # Add user_id, timestamp and random component for uniqueness
        timestamp = int(time.time())
        random_suffix = hash(f"{user_id}_{timestamp}_{original_filename}") % 10000
        
        return f"resume_{user_id}_{timestamp}_{random_suffix}_{name_part}{extension}"
    
    async def _security_scan_file(self, file_path: str, original_name: str) -> Dict[str, Any]:
        """File security scanning"""
        try:
            # Basic security checks
            scan_results = {
                'safe': True,
                'reason': 'Passed security scan',
                'checks': []
            }
            
            # File size double-check
            file_size = await self._get_file_size_async(file_path)
            if file_size > self.max_file_size_bytes:
                scan_results['safe'] = False
                scan_results['reason'] = 'File size exceeds limit after saving'
                return scan_results
            
            # Malicious filename patterns
            dangerous_patterns = ['../', '..\\', '<script', 'javascript:', 'vbscript:']
            for pattern in dangerous_patterns:
                if pattern in original_name.lower():
                    scan_results['safe'] = False
                    scan_results['reason'] = f'Dangerous pattern found: {pattern}'
                    return scan_results
            
            # Check for executable extensions embedded
            executable_extensions = ['.exe', '.bat', '.cmd', '.scr', '.com', '.pif']
            for ext in executable_extensions:
                if ext in original_name.lower():
                    scan_results['safe'] = False
                    scan_results['reason'] = f'Executable extension found: {ext}'
                    return scan_results
            
            scan_results['checks'] = ['size_check', 'pattern_check', 'extension_check']
            return scan_results
            
        except Exception as e:
            logger.error(f"Security scan error: {e}")
            return {'safe': False, 'reason': f'Scan error: {e}'}
    
    async def _quarantine_file(self, file_path: str, filename: str, reason: str):
        """Xavfli faylni karantinga o'tkazish"""
        try:
            quarantine_filename = f"quarantined_{int(time.time())}_{filename}"
            quarantine_full_path = os.path.join(self.quarantine_path, quarantine_filename)
            
            await aiofiles.os.rename(file_path, quarantine_full_path)
            
            # Log quarantine action
            logger.warning(f"File quarantined: {filename} -> {quarantine_filename}, Reason: {reason}")
            
            # Save quarantine metadata
            metadata = {
                'original_filename': filename,
                'quarantine_time': datetime.now().isoformat(),
                'reason': reason,
                'quarantine_path': quarantine_full_path
            }
            
            metadata_path = quarantine_full_path + '.meta'
            async with aiofiles.open(metadata_path, 'w') as f:
                import json
                await f.write(json.dumps(metadata, indent=2))
            
        except Exception as e:
            logger.error(f"Quarantine error: {e}")
    
    async def _save_file_metadata(self, file_path: str, user_id: int, original_filename: str):
        """File metadata saqlash"""
        try:
            metadata = {
                'user_id': user_id,
                'original_filename': original_filename,
                'saved_filename': os.path.basename(file_path),
                'saved_time': datetime.now().isoformat(),
                'file_size': await self._get_file_size_async(file_path),
                'file_hash': await self._calculate_file_hash(file_path)
            }
            
            metadata_path = file_path + '.meta'
            async with aiofiles.open(metadata_path, 'w') as f:
                import json
                await f.write(json.dumps(metadata, indent=2))
            
        except Exception as e:
            logger.error(f"Metadata saving error: {e}")
    
    # ===========================================
    # FILE OPERATIONS
    # ===========================================
    
    async def file_exists_async(self, file_path: str) -> bool:
        """Async file existence check"""
        try:
            return await aiofiles.os.path.exists(file_path)
        except Exception:
            return False
    
    async def delete_file_async(self, file_path: str, backup: bool = True) -> bool:
        """Async file deletion with optional backup"""
        try:
            if not await self.file_exists_async(file_path):
                return False
            
            # Create backup if requested
            if backup:
                await self._backup_file(file_path)
            
            # Delete main file
            await aiofiles.os.remove(file_path)
            
            # Delete metadata if exists
            metadata_path = file_path + '.meta'
            if await self.file_exists_async(metadata_path):
                await aiofiles.os.remove(metadata_path)
            
            logger.info(f"File deleted: {file_path}")
            return True
            
        except Exception as e:
            logger.error(f"File deletion error: {e}")
            return False
    
    async def copy_file_async(self, source_path: str, destination_path: str) -> bool:
        """Async file copying"""
        try:
            await self.ensure_directory_exists(os.path.dirname(destination_path))
            
            async with aiofiles.open(source_path, 'rb') as src:
                async with aiofiles.open(destination_path, 'wb') as dst:
                    while chunk := await src.read(self.chunk_size):
                        await dst.write(chunk)
            
            logger.info(f"File copied: {source_path} -> {destination_path}")
            return True
            
        except Exception as e:
            logger.error(f"File copying error: {e}")
            return False
    
    async def move_file_async(self, source_path: str, destination_path: str) -> bool:
        """Async file moving"""
        try:
            await self.ensure_directory_exists(os.path.dirname(destination_path))
            await aiofiles.os.rename(source_path, destination_path)
            
            logger.info(f"File moved: {source_path} -> {destination_path}")
            return True
            
        except Exception as e:
            logger.error(f"File moving error: {e}")
            return False
    
    async def _backup_file(self, file_path: str):
        """File backup yaratish"""
        try:
            filename = os.path.basename(file_path)
            backup_filename = f"backup_{int(time.time())}_{filename}"
            backup_full_path = os.path.join(self.backup_path, backup_filename)
            
            await self.copy_file_async(file_path, backup_full_path)
            
        except Exception as e:
            logger.error(f"Backup creation error: {e}")
    
    # ===========================================
    # FILE INFO AND STATISTICS
    # ===========================================
    
    async def get_file_info_async(self, file_path: str) -> Dict[str, Any]:
        """Async file information"""
        try:
            if not await self.file_exists_async(file_path):
                return {}
            
            stat = await aiofiles.os.stat(file_path)
            filename = os.path.basename(file_path)
            
            # Load metadata if available
            metadata = await self._load_file_metadata(file_path)
            
            info = {
                "filename": filename,
                "path": file_path,
                "size_bytes": stat.st_size,
                "size_mb": round(stat.st_size / (1024 * 1024), 2),
                "created_time": datetime.fromtimestamp(stat.st_ctime).isoformat(),
                "modified_time": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "extension": Path(filename).suffix.lower(),
                "mime_type": mimetypes.guess_type(filename)
            }
            
            # Add metadata if available
            if metadata:
                info.update({
                    "original_filename": metadata.get('original_filename'),
                    "user_id": metadata.get('user_id'),
                    "upload_time": metadata.get('saved_time'),
                    "file_hash": metadata.get('file_hash')
                })
            
            return info
            
        except Exception as e:
            logger.error(f"File info error: {e}")
            return {}
    
    async def _load_file_metadata(self, file_path: str) -> Optional[Dict[str, Any]]:
        """File metadata ni yuklash"""
        try:
            metadata_path = file_path + '.meta'
            if await self.file_exists_async(metadata_path):
                async with aiofiles.open(metadata_path, 'r') as f:
                    content = await f.read()
                    import json
                    return json.loads(content)
            return None
            
        except Exception as e:
            logger.error(f"Metadata loading error: {e}")
            return None
    
    async def get_storage_stats_async(self) -> Dict[str, Any]:
        """Async storage statistics"""
        try:
            stats = {
                "total_files": 0,
                "total_size_bytes": 0,
                "total_size_mb": 0,
                "directories": {}
            }
            
            # Analyze each directory
            directories_to_check = {
                "resumes": self.resume_path,
                "temp": self.temp_path,
                "backups": self.backup_path,
                "quarantine": self.quarantine_path
            }
            
            for dir_name, dir_path in directories_to_check.items():
                dir_stats = await self._get_directory_stats(dir_path)
                stats["directories"][dir_name] = dir_stats
                stats["total_files"] += dir_stats["file_count"]
                stats["total_size_bytes"] += dir_stats["total_size_bytes"]
            
            stats["total_size_mb"] = round(stats["total_size_bytes"] / (1024 * 1024), 2)
            
            # Additional metadata
            stats["last_updated"] = datetime.now().isoformat()
            stats["free_space_mb"] = await self._get_free_space_mb()
            
            return stats
            
        except Exception as e:
            logger.error(f"Storage stats error: {e}")
            return {}
    
    async def _get_directory_stats(self, directory: str) -> Dict[str, Any]:
        """Directory statistics"""
        try:
            if not await aiofiles.os.path.exists(directory):
                return {"file_count": 0, "total_size_bytes": 0}
            
            file_count = 0
            total_size = 0
            
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if not file.endswith('.meta'):  # Skip metadata files
                        file_path = os.path.join(root, file)
                        try:
                            size = await self._get_file_size_async(file_path)
                            total_size += size
                            file_count += 1
                        except Exception:
                            continue
            
            return {
                "file_count": file_count,
                "total_size_bytes": total_size,
                "total_size_mb": round(total_size / (1024 * 1024), 2)
            }
            
        except Exception as e:
            logger.error(f"Directory stats error: {e}")
            return {"file_count": 0, "total_size_bytes": 0}
    
    async def _get_file_size_async(self, file_path: str) -> int:
        """Async file size"""
        try:
            stat = await aiofiles.os.stat(file_path)
            return stat.st_size
        except Exception:
            return 0
    
    async def _get_free_space_mb(self) -> float:
        """Free disk space in MB"""
        try:
            statvfs = os.statvfs(self.base_path)
            free_space_bytes = statvfs.f_frsize * statvfs.f_bavail
            return round(free_space_bytes / (1024 * 1024), 2)
        except Exception:
            return 0.0
    
    # ===========================================
    # CLEANUP AND MAINTENANCE
    # ===========================================
    
    async def cleanup_old_files_async(self, days: int = 30, dry_run: bool = False) -> Dict[str, Any]:
        """Async eski fayllarni tozalash"""
        try:
            cutoff_time = time.time() - (days * 24 * 60 * 60)
            cleanup_stats = {
                "deleted_files": 0,
                "freed_space_mb": 0,
                "errors": 0,
                "deleted_paths": []
            }
            
            directories_to_clean = [self.temp_path, self.backup_path]
            
            for directory in directories_to_clean:
                if not await aiofiles.os.path.exists(directory):
                    continue
                
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        file_path = os.path.join(root, file)
                        try:
                            stat = await aiofiles.os.stat(file_path)
                            if stat.st_ctime < cutoff_time:
                                file_size = stat.st_size
                                
                                if not dry_run:
                                    await aiofiles.os.remove(file_path)
                                
                                cleanup_stats["deleted_files"] += 1
                                cleanup_stats["freed_space_mb"] += file_size / (1024 * 1024)
                                cleanup_stats["deleted_paths"].append(file_path)
                                
                        except Exception as e:
                            cleanup_stats["errors"] += 1
                            logger.error(f"Cleanup error for {file_path}: {e}")
            
            cleanup_stats["freed_space_mb"] = round(cleanup_stats["freed_space_mb"], 2)
            
            if not dry_run:
                logger.info(f"Cleanup completed: {cleanup_stats['deleted_files']} files, "
                           f"{cleanup_stats['freed_space_mb']} MB freed")
            
            return cleanup_stats
            
        except Exception as e:
            logger.error(f"Cleanup error: {e}")
            return {"error": str(e)}
    
    async def cleanup_temp_files_async(self) -> int:
        """Temp fayllarni tozalash"""
        try:
            deleted_count = 0
            
            if await aiofiles.os.path.exists(self.temp_path):
                for file in os.listdir(self.temp_path):
                    if file.endswith('.tmp'):
                        file_path = os.path.join(self.temp_path, file)
                        try:
                            await aiofiles.os.remove(file_path)
                            deleted_count += 1
                        except Exception:
                            continue
            
            logger.info(f"Temp cleanup: {deleted_count} files deleted")
            return deleted_count
            
        except Exception as e:
            logger.error(f"Temp cleanup error: {e}")
            return 0
    
    async def _cleanup_temp_file(self, temp_path: str):
        """Temp faylni tozalash"""
        try:
            if await self.file_exists_async(temp_path):
                await aiofiles.os.remove(temp_path)
        except Exception as e:
            logger.error(f"Temp file cleanup error: {e}")
    
    # ===========================================
    # UTILITY METHODS
    # ===========================================
    
    async def ensure_directory_exists(self, directory_path: str):
        """Directory mavjudligini ta'minlash"""
        try:
            Path(directory_path).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            logger.error(f"Directory creation error: {e}")
    
    async def _calculate_file_hash(self, file_path: str) -> str:
        """File hash hisoblaah (integrity check uchun)"""
        try:
            hash_sha256 = hashlib.sha256()
            
            async with aiofiles.open(file_path, 'rb') as f:
                while chunk := await f.read(self.chunk_size):
                    hash_sha256.update(chunk)
            
            return hash_sha256.hexdigest()
            
        except Exception as e:
            logger.error(f"Hash calculation error: {e}")
            return ""
    
    @asynccontextmanager
    async def temporary_file(self, suffix: str = '.tmp'):
        """Temporary file context manager"""
        temp_path = None
        try:
            temp_fd, temp_path = tempfile.mkstemp(suffix=suffix, dir=self.temp_path)
            os.close(temp_fd)  # Close file descriptor, keep path
            yield temp_path
        finally:
            if temp_path and await self.file_exists_async(temp_path):
                await self._cleanup_temp_file(temp_path)


# ===========================================
# HELPER FUNCTIONS - Enhanced
# ===========================================

def format_file_size(size_bytes: int) -> str:
    """Fayl hajmini human-readable formatda ko'rsatish"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


def get_file_extension(filename: str) -> str:
    """Fayl extension ni olish"""
    return Path(filename).suffix.lower()


def is_valid_resume_filename(filename: str) -> Tuple[bool, str]:
    """Resume filename validation"""
    if not filename:
        return False, "Filename is empty"
    
    # Length check
    if len(filename) > 255:
        return False, "Filename too long"
    
    # Extension check
    extension = get_file_extension(filename)
    if extension not in Config.ALLOWED_FILE_EXTENSIONS:
        allowed = ", ".join(Config.ALLOWED_FILE_EXTENSIONS)
        return False, f"Invalid file type. Allowed: {allowed}"
    
    # Dangerous characters
    dangerous_chars = ['<', '>', ':', '"', '|', '?', '*', '\0']
    if any(char in filename for char in dangerous_chars):
        return False, "Filename contains dangerous characters"
    
    return True, "Valid filename"


async def validate_file_integrity(file_path: str, expected_hash: str = None) -> bool:
    """File integrity validation"""
    try:
        if not os.path.exists(file_path):
            return False
        
        if expected_hash:
            file_service = FileService()
            actual_hash = await file_service._calculate_file_hash(file_path)
            return actual_hash == expected_hash
        
        # Basic integrity check - file readable
        async with aiofiles.open(file_path, 'rb') as f:
            await f.read(1)  # Try to read at least 1 byte
        
        return True
        
    except Exception as e:
        logger.error(f"File integrity check failed: {e}")
        return False


# Factory function
def create_file_service() -> FileService:
    """FileService yaratish - factory pattern"""
    return FileService(Config.FILES_BASE_PATH)


# Scheduled cleanup task
async def scheduled_cleanup_task(file_service: FileService, interval_hours: int = 24):
    """Scheduled cleanup task"""
    while True:
        try:
            logger.info("Starting scheduled cleanup...")
            
            # Clean temp files
            await file_service.cleanup_temp_files_async()
            
            # Clean old backups (7 days)
            await file_service.cleanup_old_files_async(days=7)
            
            # Get storage stats
            stats = await file_service.get_storage_stats_async()
            logger.info(f"Storage stats: {stats['total_files']} files, {stats['total_size_mb']} MB")
            
            # Sleep until next cleanup
            await asyncio.sleep(interval_hours * 3600)
            
        except Exception as e:
            logger.error(f"Scheduled cleanup error: {e}")
            await asyncio.sleep(3600)  # Retry in 1 hour
