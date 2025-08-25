#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# Local imports
from config import Config
from database.models import DatabaseManager
from services.ai_service import AIService
from services.file_service import FileService
from utils.language import get_text, get_language_keyboard, get_main_menu_keyboard, get_back_keyboard

# Handlers import
from handlers.employer import EmployerHandlers
from handlers.jobseeker import JobseekerHandlers
router = Router()

# Bot va Dispatcher yaratish
bot = Bot(token=Config.TELEGRAM_BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
main_router = Router()

# Servislar
db = DatabaseManager()
ai_service = AIService(Config.OPENAI_API_KEY)
file_service = FileService(Config.FILES_BASE_PATH)

# Handlerlar
employer_handlers = EmployerHandlers(bot, db, ai_service, file_service)
jobseeker_handlers = JobseekerHandlers(bot, db, ai_service, file_service)

# Logging sozlash
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Config.LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__) # logging.getLogger(__name__)

# States - Foydalanuvchi holatlari
class EmployerStates(StatesGroup):
    CREATING_COMPANY_NAME = State()
    CREATING_COMPANY_DESC = State()
    CREATING_VACANCY_TITLE = State()
    CREATING_VACANCY_DESC = State()
    CREATING_VACANCY_REQ = State()
    CREATING_VACANCY_RESP = State()
    CREATING_SALARY = State()
    CREATING_WORK_HOURS = State()
    CREATING_WORK_DAYS = State()
    CREATING_WORK_LOCATION = State()
    CREATING_CRITERIA_SKILLS = State()
    CREATING_CRITERIA_EXP = State()
    CREATING_CRITERIA_EDU = State()
    CREATING_CRITERIA_LANG = State()
    CREATING_CRITERIA_ADD = State()
    CREATING_QUESTIONS = State()

class JobseekerStates(StatesGroup):
    UPLOADING_RESUME = State()
    ANSWERING_QUESTIONS = State()
    PROVIDING_INFO = State()

# Yordamchi funksiyalar
def get_user_language(user_id: int) -> str:
    """Foydalanuvchi tilini olish"""
    user = db.get_user_by_telegram_id(user_id)
    return user['language'] if user else Config.DEFAULT_LANGUAGE

async def get_user_info(message: Message) -> tuple:
    """Foydalanuvchi ma'lumotlarini olish"""
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    return user_id, username, first_name, last_name

# Start komandasi
@router.message(Command("start"))
async def start_command(message: Message):
    """Bot boshlanishi"""
    try:
        user_id, username, first_name, last_name = await get_user_info(message)
        
        # Foydalanuvchini bazaga yozish
        db.create_user(user_id, username, first_name, last_name)
        
        # Til tanlash
        text = get_text("welcome", Config.DEFAULT_LANGUAGE)
        keyboard = get_language_keyboard()
        
        await message.answer(text, reply_markup=keyboard)
        
        logger.info(f"Yangi foydalanuvchi boshladi: {user_id} (@{username})")
        
    except Exception as e:
        logger.error(f"Start komandasi xatoligi: {e}")
        await message.reply(get_text("error", Config.DEFAULT_LANGUAGE))

# Admin vakansiya komandasi
@router.message(Command("ad_vacancy"))
async def admin_vacancy_command(message: Message):
    """Maxfiy vakansiya yaratish komandasi"""
    try:
        user_id = message.from_user.id
        
        # Admin tekshirish (ixtiyoriy)
        if Config.is_admin(user_id):
            logger.info(f"Admin vakansiya yaratish: {user_id}")
        
        # Foydalanuvchini employer qilib belgilash
        db.update_user_role(user_id, 'employer')
        
        language = get_user_language(user_id)
        
        # Employer menyusiga o'tkazish
        await show_employer_menu(message.chat.id, language)
        
    except Exception as e:
        logger.error(f"Admin vakansiya komandasi xatoligi: {e}")

# Til tanlash callback
@router.callback_query(F.data.startswith('lang_'))
async def language_callback(callback: CallbackQuery):
    """Til tanlash callback"""
    try:
        user_id = callback.from_user.id
        selected_lang = callback.data.split('_')[1]  # lang_uz -> uz
        
        # Tilni yangilash
        user = db.get_user_by_telegram_id(user_id)
        if user:
            # Faqat til yangilash
            conn = db.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE users SET language = ? WHERE telegram_id = ?",
                (selected_lang, user_id)
            )
            conn.commit()
            conn.close()
        else:
            # Yangi foydalanuvchi yaratish
            db.create_user(user_id, language=selected_lang)
        
        # Xabarni o'chirish
        await callback.message.delete()
        
        # Asosiy menyu ko'rsatish
        text = get_text("language_selected", selected_lang) + "\n\n"
        text += get_text("choose_role", selected_lang)
        keyboard = get_main_menu_keyboard(selected_lang)
        
        await callback.message.answer(text, reply_markup=keyboard)
        
        logger.info(f"Til tanlandi: {user_id} -> {selected_lang}")
        await callback.answer()
        
    except Exception as e:
        logger.error(f"Til tanlash xatoligi: {e}")
        await callback.answer(get_text("error", "uz"))

# Rol tanlash callback
@router.callback_query(F.data.startswith('role_'))
async def role_callback(callback: CallbackQuery):
    """Rol tanlash callback"""
    try:
        user_id = callback.from_user.id
        role = callback.data.split('_')[1]  # role_employer -> employer
        language = get_user_language(user_id)
        
        # Rolni yangilash
        db.update_user_role(user_id, role)
        
        # Analytics
        db.add_analytics_event(f'role_selected_{role}', user_id)
        
        # Xabarni o'chirish
        await callback.message.delete()
        
        if role == 'employer':
            await show_employer_menu(callback.message.chat.id, language)
        elif role == 'jobseeker':
            await show_jobseeker_menu(callback.message.chat.id, language)
        
        logger.info(f"Rol tanlandi: {user_id} -> {role}")
        await callback.answer()
        
    except Exception as e:
        logger.error(f"Rol tanlash xatoligi: {e}")
        await callback.answer(get_text("error", language))

async def show_employer_menu(chat_id: int, language: str):
    """Ish beruvchi menyusini ko'rsatish"""
    try:
        text = get_text("employer_menu", language)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=get_text("create_vacancy", language), 
                    callback_data="employer_create_vacancy"
                )
            ],
            [
                InlineKeyboardButton(
                    text=get_text("my_vacancies", language), 
                    callback_data="employer_vacancies"
                )
            ],
            [
                InlineKeyboardButton(
                    text=get_text("applications", language), 
                    callback_data="employer_applications"
                )
            ],
            [
                InlineKeyboardButton(
                    text=get_text("btn_back", language), 
                    callback_data="back_main"
                )
            ]
        ])
        
        await bot.send_message(chat_id, text, reply_markup=keyboard)
        
    except Exception as e:
        logger.error(f"Employer menyu xatoligi: {e}")

async def show_jobseeker_menu(chat_id: int, language: str):
    """Ishga topshiruvchi menyusini ko'rsatish"""
    try:
        text = get_text("jobseeker_menu", language)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=get_text("find_jobs", language), 
                    callback_data="jobseeker_find_jobs"
                )
            ],
            [
                InlineKeyboardButton(
                    text=get_text("my_applications", language), 
                    callback_data="jobseeker_applications"
                )
            ],
            [
                InlineKeyboardButton(
                    text=get_text("btn_back", language), 
                    callback_data="back_main"
                )
            ]
        ])
        
        await bot.send_message(chat_id, text, reply_markup=keyboard)
        
    except Exception as e:
        logger.error(f"Jobseeker menyu xatoligi: {e}")

# Asosiy menyuga qaytish
@router.callback_query(F.data == 'back_main')
async def back_to_main(callback: CallbackQuery):
    """Asosiy menyuga qaytish"""
    try:
        user_id = callback.from_user.id
        language = get_user_language(user_id)
        
        # Xabarni o'chirish
        await callback.message.delete()
        
        # Asosiy menyu
        text = get_text("choose_role", language)
        keyboard = get_main_menu_keyboard(language)
        
        await callback.message.answer(text, reply_markup=keyboard)
        await callback.answer()
        
    except Exception as e:
        logger.error(f"Asosiy menyuga qaytish xatoligi: {e}")

# Employer callbacks
@router.callback_query(F.data == 'employer_create_vacancy')
async def start_vacancy_creation(callback: CallbackQuery, state: FSMContext):
    """Vakansiya yaratishni boshlash"""
    try:
        user_id = callback.from_user.id
        language = get_user_language(user_id)
        
        # State o'rnatish
        await state.set_state(EmployerStates.CREATING_COMPANY_NAME)
        
        # Birinchi savol
        text = get_text("creating_vacancy", language) + "\n\n"
        text += get_text("company_name", language)
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=get_text("btn_cancel", language), 
                    callback_data="cancel_vacancy"
                )
            ]
        ])
        
        await callback.message.edit_text(text, reply_markup=keyboard)
        await callback.answer()
        
    except Exception as e:
        logger.error(f"Vakansiya yaratishni boshlash xatoligi: {e}")

# Vakansiya yaratish - kompaniya nomi
@router.message(StateFilter(EmployerStates.CREATING_COMPANY_NAME))
async def handle_company_name(message: Message, state: FSMContext):
    """Kompaniya nomini qayta ishlash"""
    try:
        company_name = message.text.strip()
        language = get_user_language(message.from_user.id)
        
        if len(company_name) < 2:
            await message.reply("❌ Kompaniya nomi juda qisqa!")
            return
        
        # Ma'lumotni saqlash
        await state.update_data(company_name=company_name)
        await state.set_state(EmployerStates.CREATING_COMPANY_DESC)
        
        # Keyingi savol
        text = get_text("company_description", language)
        await message.answer(text)
        
    except Exception as e:
        logger.error(f"Kompaniya nomi xatoligi: {e}")

# Vakansiya yaratish - kompaniya tavsifi
@router.message(StateFilter(EmployerStates.CREATING_COMPANY_DESC))
async def handle_company_description(message: Message, state: FSMContext):
    """Kompaniya tavsifini qayta ishlash"""
    try:
        company_description = message.text.strip()
        language = get_user_language(message.from_user.id)
        
        # Ma'lumotni saqlash
        await state.update_data(company_description=company_description)
        await state.set_state(EmployerStates.CREATING_VACANCY_TITLE)
        
        # Keyingi savol
        text = get_text("vacancy_title", language)
        await message.answer(text)
        
    except Exception as e:
        logger.error(f"Kompaniya tavsifi xatoligi: {e}")

# Vakansiya yaratish - vakansiya nomi
@router.message(StateFilter(EmployerStates.CREATING_VACANCY_TITLE))
async def handle_vacancy_title(message: Message, state: FSMContext):
    """Vakansiya nomini qayta ishlash"""
    try:
        vacancy_title = message.text.strip()
        language = get_user_language(message.from_user.id)
        
        if len(vacancy_title) < 3:
            await message.reply("❌ Vakansiya nomi juda qisqa!")
            return
        
        # Ma'lumotni saqlash
        await state.update_data(vacancy_title=vacancy_title)
        await state.set_state(EmployerStates.CREATING_VACANCY_DESC)
        
        # Keyingi savol
        text = get_text("vacancy_description", language)
        await message.answer(text)
        
    except Exception as e:
        logger.error(f"Vakansiya nomi xatoligi: {e}")

# Admin komandalar
@router.message(Command("admin"))
async def admin_command(message: Message):
    """Admin panel"""
    try:
        user_id = message.from_user.id
        
        if not Config.is_admin(user_id):
            await message.reply(get_text("access_denied", get_user_language(user_id)))
            return
        
        language = get_user_language(user_id)
        await show_admin_panel(message.chat.id, language)
        
    except Exception as e:
        logger.error(f"Admin komandasi xatoligi: {e}")

async def show_admin_panel(chat_id: int, language: str):
    """Admin panelni ko'rsatish"""
    try:
        text = get_text("admin_menu", language)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=get_text("analytics", language), 
                    callback_data="admin_analytics"
                )
            ]
        ])
        
        await bot.send_message(chat_id, text, reply_markup=keyboard)
        
    except Exception as e:
        logger.error(f"Admin panel xatoligi: {e}")

@router.callback_query(F.data == 'admin_analytics')
async def admin_analytics(callback: CallbackQuery):
    """Admin analitika"""
    try:
        user_id = callback.from_user.id
        
        if not Config.is_admin(user_id):
            await callback.answer(get_text("access_denied", "uz"))
            return
        
        language = get_user_language(user_id)
        stats = db.get_analytics_summary()
        
        from datetime import datetime
        today = datetime.now().strftime("%d.%m.%Y")
        
        text = get_text("analytics_data", language).format(
            stats.get('total_users', 0),
            stats.get('employers', 0),
            stats.get('jobseekers', 0),
            stats.get('total_vacancies', 0),
            stats.get('active_vacancies', 0),
            stats.get('archived_vacancies', 0),
            stats.get('total_applications', 0),
            stats.get('accepted_applications', 0),
            stats.get('total_applications', 0) - stats.get('accepted_applications', 0),
            today
        )
        
        await callback.answer()
        await callback.message.answer(text)
        
    except Exception as e:
        logger.error(f"Admin analitika xatoligi: {e}")
        await callback.answer(get_text("error", "uz"))

# Noma'lum xabarlar uchun handler
@router.message()
async def unknown_message(message: Message):
    """Noma'lum xabarlar uchun"""
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id)
        
        # Foydalanuvchini tekshirish
        user = db.get_user_by_telegram_id(user_id)
        if not user:
            # Yangi foydalanuvchi - start komandasi
            text = get_text("welcome", Config.DEFAULT_LANGUAGE)
            keyboard = get_language_keyboard()
            await message.answer(text, reply_markup=keyboard)
            return
        
        # Rol tekshirish
        if not user.get('role'):
            text = get_text("choose_role", language)
            keyboard = get_main_menu_keyboard(language)
            await message.answer(text, reply_markup=keyboard)
            return
        
        await message.reply(get_text("invalid_command", language))
        
    except Exception as e:
        logger.error(f"Noma'lum xabar xatoligi: {e}")

async def main():
    """Asosiy funksiya"""
    try:
        # Konfiguratsiyani tekshirish
        config_errors = Config.validate_config()
        if config_errors:
            print("❌ Konfiguratsiya xatoliklari:")
            for error in config_errors:
                print(f"  • {error}")
            print("\n💡 Iltimos config.py faylini to'g'ri sozlang.")
            sys.exit(1)
        
        # Database tekshirish
        db.init_db()
        print("✅ Database tayyor")
        
        # Fayllar papkasi
        import os
        if not os.path.exists(Config.FILES_BASE_PATH):
            os.makedirs(Config.FILES_BASE_PATH)
        print("✅ Fayllar papkasi tayyor")
        
        # AI servisini tekshirish
        print("🤖 AI servisi tayyor")
        
        # Router ni dispatcher ga qo'shish
        dp.include_router(router)
        
        logger.info("Bot ishga tushdi")
        print("🚀 Bot ishga tushdi!")
        bot_info = await bot.get_me()
        print(f"📱 Bot username: @{bot_info.username}")
        print("⏹️ To'xtatish uchun Ctrl+C bosing")
        
        # Webhook tozalash va polling boshlash
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
        
    except KeyboardInterrupt:
        logger.info("Bot to'xtatildi (Ctrl+C)")
        print("\n👋 Bot to'xtatildi")
    except Exception as e:
        logger.error(f"Bot ishga tushirishda xatolik: {e}")
        print(f"❌ Bot ishga tushirishda xatolik: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())