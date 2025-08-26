# # -*- coding: utf-8 -*-

# class Languages:
#     UZ = "uz"
#     RU = "ru"

# # O'zbek tili
# UZ_TEXTS = {
#     # Umumiy
#     "welcome": "🤖 Botga xush kelibsiz!\n\n📋 Bu bot ish beruvchilar va ishga topshiruvchilar uchun mo'ljallangan.\n\nTilni tanlang:",
#     "language_selected": "✅ Til tanlandi!",
#     "back": "🔙 Orqaga",
#     "cancel": "❌ Bekor qilish",
#     "next": "➡️ Keyingisi",
#     "save": "💾 Saqlash",
#     "error": "❌ Xatolik yuz berdi. Qaytadan urinib ko'ring.",
#     "success": "✅ Muvaffaqiyatli!",
    
#     # Til tanlash
#     "uzbek": "🇺🇿 O'zbek",
#     "russian": "🇷🇺 Русский",
    
#     # Asosiy menyu
#     "main_menu": "🏠 Asosiy menyu",
#     "choose_role": "🎭 Rolni tanlang:",
#     "employer": "👔 Ish beruvchi",
#     "jobseeker": "👤 Ishga topshiruvchi",
#     "admin_panel": "⚙️ Admin panel",
    
#     # Ish beruvchi menyusi
#     "employer_menu": "👔 Ish beruvchi menyusi",
#     "create_vacancy": "➕ Vakansiya yaratish",
#     "my_vacancies": "📋 Mening vakansiyalarim",
#     "applications": "📬 Kelgan arizalar",
#     "my_companies": "🏢 Mening kompaniyalarim",
    
#     # Vakansiya yaratish
#     "creating_vacancy": "📝 Vakansiya yaratish\n\nBu jarayon bir necha bosqichdan iborat:",
#     "company_name": "🏢 Kompaniya nomini kiriting:",
#     "company_description": "📄 Kompaniya tavsifini kiriting:",
#     "vacancy_title": "📌 Vakansiya nomini kiriting:",
#     "vacancy_description": "📝 Vakansiya tavsifini kiriting:",
#     "vacancy_requirements": "📋 Talablarni kiriting:",
#     "vacancy_responsibilities": "⚡ Majburiyatlarni kiriting:",
#     "salary_range": "💰 Ish haqqi oralig'ini kiriting (masalan: 5000000-8000000) yoki 'Kelishilgan' deb yozing:",
#     "work_hours": "🕒 Ish soatlarini kiriting (masalan: 9:00-18:00):",
#     "work_days": "📅 Ish kunlarini kiriting (masalan: Dushanba-Juma):",
#     "work_location": "📍 Ish joyini kiriting:",
    
#     # AI kriteriyalar
#     "ai_criteria": "🤖 Resume tahlili uchun kriteriyalar\n\nAI quyidagi kriteriyalar asosida resume ni tahlil qiladi:",
#     "criteria_skills": "💻 Qanday ko'nikmalar bo'lishi kerak? (vergul bilan ajrating):",
#     "criteria_experience": "📈 Qancha yillik tajriba kerak?",
#     "criteria_education": "🎓 Ta'lim darajasi (bakalavr, magistr, va h.k.):",
#     "criteria_languages": "🌍 Qanday tillarni bilishi kerak?",
#     "criteria_additional": "➕ Qo'shimcha kriteriyalar:",
    
#     # Savol-javob
#     "interview_questions": "❓ Suhbat savollari\n\nNechta savol so'rashin? (1-5 orasida):",
#     "question_prompt": "❓ {}-savol:",
#     "questions_saved": "✅ Savol-javoblar saqlandi!",
    
#     # Vakansiya yakunlash
#     "vacancy_created": "🎉 Vakansiya muvaffaqiyatli yaratildi!\n\n📌 Nomi: {}\n🏢 Kompaniya: {}\n📅 Sana: {}",
#     "vacancy_preview": "👀 Vakansiya ko'rinishi:\n\n📌 Nomi: {}\n🏢 Kompaniya: {}\n📝 Tavsif: {}\n📋 Talablar: {}\n💰 Ish haqqi: {}\n📍 Joy: {}",
    
#     # Vakansiyalar ro'yxati
#     "no_vacancies": "📭 Hozircha vakansiyalaringiz yo'q.",
#     "vacancy_list": "📋 Vakansiyalar ro'yxati:",
#     "vacancy_status_active": "🟢 Faol",
#     "vacancy_status_archived": "🔴 Arxivlangan",
#     "archive_vacancy": "📦 Arxivlash",
#     "activate_vacancy": "🔄 Faollashtirish",
    
#     # Kelgan arizalar
#     "no_applications": "📭 Hozircha arizalar kelmagan.",
#     "applications_list": "📬 Kelgan arizalar:",
#     "application_from": "👤 Ariza beruvchi: {}",
#     "application_date": "📅 Sana: {}",
#     "application_vacancy": "📌 Vakansiya: {}",
#     "application_status": "📊 Holat: {}",
#     "view_application": "👁️ Ko'rish",
#     "download_resume": "📄 Resume yuklab olish",
    
#     # Ishga topshiruvchi menyusi
#     "jobseeker_menu": "👤 Ishga topshiruvchi menyusi",
#     "find_jobs": "🔍 Ish izlash",
#     "my_applications": "📨 Mening arizalarim",
    
#     # Ish izlash
#     "select_company": "🏢 Kompaniyani tanlang:",
#     "no_companies": "🏢 Hozircha kompaniyalar yo'q.",
#     "select_vacancy": "📌 Vakansiyani tanlang:",
#     "no_active_vacancies": "📭 Bu kompaniyada faol vakansiyalar yo'q.",
    
#     # Vakansiya ko'rinishi
#     "vacancy_details": """📌 Vakansiya: {}
# 🏢 Kompaniya: {}
# 📝 Tavsif: {}
# 📋 Talablar: {}
# ⚡ Majburiyatlar: {}
# 💰 Ish haqqi: {}
# 🕒 Ish soatlari: {}
# 📅 Ish kunlari: {}
# 📍 Ish joyi: {}""",
#     "apply_now": "🚀 Hoziroq topshirish",
#     "already_applied": "✅ Siz bu vakansiyaga allaqachon ariza bergansiz",
    
#     # Resume yuklash
#     "upload_resume": "📄 Resume faylini yuboring (PDF yoki DOC formatida):",
#     "invalid_file": "❌ Noto'g'ri fayl formati. Faqat PDF yoki DOC fayllar qabul qilinadi.",
#     "file_too_large": "❌ Fayl hajmi juda katta. Maksimal 10MB.",
#     "resume_uploaded": "✅ Resume yuklandi!",
    
#     # AI tahlili
#     "analyzing_resume": "🔍 Resume tahlil qilinmoqda...",
#     "ai_analyzing": "🤖 AI tahlil qilmoqda, biroz kutib turing...",
#     "match_percentage": "📊 Moslik darajasi: {}%",
#     "match_too_low": """❌ Afsuski, resume vakansiya talablariga mos kelmaydi.
    
# 📊 Moslik darajasi: {}%
# 🎯 Minimal darajasi: 60%

# 💡 Boshqa vakansiyalarga topshirishni xohlaysizmi?""",
    
#     "match_good": """✅ Resume vakansiya talablariga mos keladi!
    
# 📊 Moslik darajasi: {}%

# 🎤 Endi sizga bir nechta savol beriladi. Tayyor bo'lsangiz 'Davom etish' tugmasini bosing.""",
    
#     "continue": "➡️ Davom etish",
    
#     # Suhbat savollari
#     "interview_started": "🎤 Suhbat boshlandi!\n\nSavol {} / {}:",
#     "question": "❓ {}",
#     "answer_question": "💬 Javobingizni yozing:",
#     "next_question": "➡️ Keyingi savol",
#     "interview_completed": "✅ Suhbat yakunlandi!",
    
#     # Suhbat natijalari
#     "evaluating_answers": "🤖 Javoblar baholanmoqda...",
#     "interview_success": """🎉 Tabriklaymiz! Suhbat muvaffaqiyatli o'tdi!
    
# 📊 Umumiy ball: {} / 100
# ✅ Sizni keyingi bosqichda kutamiz.

# 📞 Tez orada ish beruvchi siz bilan bog'lanadi.""",
    
#     "interview_failed": """😔 Afsuski, bu safar siz tanlangansiz yo'q.
    
# 📊 Umumiy ball: {} / 100
# 🎯 Minimal ball: 70

# 💡 Boshqa vakansiyalarga topshirishda davom eting!""",
    
#     # Qo'shimcha ma'lumotlar
#     "additional_info": "📝 Qo'shimcha ma'lumotlar kerak:",
#     "full_name": "👤 To'liq ismingizni kiriting:",
#     "age": "🎂 Yoshingizni kiriting:",
#     "phone_number": "📞 Telefon raqamingizni kiriting:",
#     "email": "📧 Email manzilingizni kiriting:",
#     "address": "📍 Yashash manzilingizni kiriting:",
#     "info_saved": "✅ Ma'lumotlar saqlandi va ish beruvchiga yuborildi!",
    
#     # Admin panel
#     "admin_menu": "⚙️ Admin Panel",
#     "analytics": "📊 Analitika",
#     "system_stats": "📈 Tizim statistikasi",
    
#     # Analitika
#     "analytics_data": """📊 Tizim analitikasi:
    
# 👥 Foydalanuvchilar:
# • Jami: {}
# • Ish beruvchilar: {}
# • Ishga topshiruvchilar: {}

# 📋 Vakansiyalar:
# • Jami: {}
# • Faol: {}
# • Arxivlangan: {}

# 📨 Arizalar:
# • Jami: {}
# • Qabul qilingan: {}
# • Rad etilgan: {}

# 📅 Bugun: {}""",
    
#     # Xato xabarlar
#     "session_expired": "⏰ Sessiya tugadi. Qaytadan boshlang.",
#     "access_denied": "🚫 Ruxsat berilmagan.",
#     "invalid_command": "❌ Noto'g'ri buyruq.",
#     "processing": "⏳ Ishlov berilmoqda...",
#     "please_wait": "⏳ Iltimos kutib turing...",
    
#     # Tugmalar
#     "btn_uzbek": "🇺🇿 O'zbek",
#     "btn_russian": "🇷🇺 Русский",
#     "btn_employer": "👔 Ish beruvchi",
#     "btn_jobseeker": "👤 Ishga topshiruvchi",
#     "btn_back": "🔙 Orqaga",
#     "btn_cancel": "❌ Bekor qilish",
#     "btn_continue": "➡️ Davom etish",
#     "btn_save": "💾 Saqlash",
#     "btn_apply": "🚀 Topshirish",
#     "btn_view": "👁️ Ko'rish",
#     "btn_download": "📥 Yuklab olish",
#     "btn_archive": "📦 Arxivlash",
#     "btn_activate": "🔄 Faollashtirish",
#     "btn_yes": "✅ Ha",
#     "btn_no": "❌ Yo'q",
# }

# # Rus tili
# RU_TEXTS = {
#     # Общие
#     "welcome": "🤖 Добро пожаловать в бот!\n\n📋 Этот бот предназначен для работодателей и соискателей.\n\nВыберите язык:",
#     "language_selected": "✅ Язык выбран!",
#     "back": "🔙 Назад",
#     "cancel": "❌ Отмена",
#     "next": "➡️ Далее",
#     "save": "💾 Сохранить",
#     "error": "❌ Произошла ошибка. Попробуйте еще раз.",
#     "success": "✅ Успешно!",
    
#     # Выбор языка
#     "uzbek": "🇺🇿 O'zbek",
#     "russian": "🇷🇺 Русский",
    
#     # Главное меню
#     "main_menu": "🏠 Главное меню",
#     "choose_role": "🎭 Выберите роль:",
#     "employer": "👔 Работодатель",
#     "jobseeker": "👤 Соискатель",
#     "admin_panel": "⚙️ Админ панель",
    
#     # Меню работодателя
#     "employer_menu": "👔 Меню работодателя",
#     "create_vacancy": "➕ Создать вакансию",
#     "my_vacancies": "📋 Мои вакансии",
#     "applications": "📬 Заявки",
#     "my_companies": "🏢 Мои компании",
    
#     # Создание вакансии
#     "creating_vacancy": "📝 Создание вакансии\n\nПроцесс состоит из нескольких этапов:",
#     "company_name": "🏢 Введите название компании:",
#     "company_description": "📄 Введите описание компании:",
#     "vacancy_title": "📌 Введите название вакансии:",
#     "vacancy_description": "📝 Введите описание вакансии:",
#     "vacancy_requirements": "📋 Введите требования:",
#     "vacancy_responsibilities": "⚡ Введите обязанности:",
#     "salary_range": "💰 Введите диапазон зарплаты (например: 5000000-8000000) или напишите 'Договорная':",
#     "work_hours": "🕒 Введите рабочие часы (например: 9:00-18:00):",
#     "work_days": "📅 Введите рабочие дни (например: Понедельник-Пятница):",
#     "work_location": "📍 Введите место работы:",
    
#     # AI критерии
#     "ai_criteria": "🤖 Критерии для анализа резюме\n\nИИ будет анализировать резюме по следующим критериям:",
#     "criteria_skills": "💻 Какие навыки должны быть? (разделите запятыми):",
#     "criteria_experience": "📈 Сколько лет опыта требуется?",
#     "criteria_education": "🎓 Уровень образования (бакалавр, магистр и т.д.):",
#     "criteria_languages": "🌍 Какие языки должен знать?",
#     "criteria_additional": "➕ Дополнительные критерии:",
    
#     # Вопросы интервью
#     "interview_questions": "❓ Вопросы собеседования\n\nСколько вопросов задать? (от 1 до 5):",
#     "question_prompt": "❓ {}-й вопрос:",
#     "questions_saved": "✅ Вопросы сохранены!",
    
#     # Завершение вакансии
#     "vacancy_created": "🎉 Вакансия успешно создана!\n\n📌 Название: {}\n🏢 Компания: {}\n📅 Дата: {}",
#     "vacancy_preview": "👀 Предварительный просмотр вакансии:\n\n📌 Название: {}\n🏢 Компания: {}\n📝 Описание: {}\n📋 Требования: {}\n💰 Зарплата: {}\n📍 Место: {}",
    
#     # Список вакансий
#     "no_vacancies": "📭 У вас пока нет вакансий.",
#     "vacancy_list": "📋 Список вакансий:",
#     "vacancy_status_active": "🟢 Активная",
#     "vacancy_status_archived": "🔴 Архивирована",
#     "archive_vacancy": "📦 Архивировать",
#     "activate_vacancy": "🔄 Активировать",
    
#     # Заявки
#     "no_applications": "📭 Заявки пока не поступали.",
#     "applications_list": "📬 Список заявок:",
#     "application_from": "👤 Заявитель: {}",
#     "application_date": "📅 Дата: {}",
#     "application_vacancy": "📌 Вакансия: {}",
#     "application_status": "📊 Статус: {}",
#     "view_application": "👁️ Посмотреть",
#     "download_resume": "📄 Скачать резюме",
    
#     # Меню соискателя
#     "jobseeker_menu": "👤 Меню соискателя",
#     "find_jobs": "🔍 Поиск работы",
#     "my_applications": "📨 Мои заявки",
    
#     # Поиск работы
#     "select_company": "🏢 Выберите компанию:",
#     "no_companies": "🏢 Компании пока отсутствуют.",
#     "select_vacancy": "📌 Выберите вакансию:",
#     "no_active_vacancies": "📭 В этой компании нет активных вакансий.",
    
#     # Просмотр вакансии
#     "vacancy_details": """📌 Вакансия: {}
# 🏢 Компания: {}
# 📝 Описание: {}
# 📋 Требования: {}
# ⚡ Обязанности: {}
# 💰 Зарплата: {}
# 🕒 Рабочие часы: {}
# 📅 Рабочие дни: {}
# 📍 Место работы: {}""",
#     "apply_now": "🚀 Подать заявку",
#     "already_applied": "✅ Вы уже подали заявку на эту вакансию",
    
#     # Загрузка резюме
#     "upload_resume": "📄 Отправьте файл резюме (в формате PDF или DOC):",
#     "invalid_file": "❌ Неверный формат файла. Принимаются только PDF или DOC файлы.",
#     "file_too_large": "❌ Файл слишком большой. Максимальный размер 10MB.",
#     "resume_uploaded": "✅ Резюме загружено!",
    
#     # AI анализ
#     "analyzing_resume": "🔍 Анализ резюме...",
#     "ai_analyzing": "🤖 ИИ анализирует, немного подождите...",
#     "match_percentage": "📊 Процент соответствия: {}%",
#     "match_too_low": """❌ К сожалению, резюме не соответствует требованиям вакансии.
    
# 📊 Процент соответствия: {}%
# 🎯 Минимальный процент: 60%

# 💡 Хотите подать заявку на другие вакансии?""",
    
#     "match_good": """✅ Резюме соответствует требованиям вакансии!
    
# 📊 Процент соответствия: {}%

# 🎤 Теперь вам будет задано несколько вопросов. Если готовы, нажмите 'Продолжить'.""",
    
#     "continue": "➡️ Продолжить",
    
#     # Вопросы собеседования
#     "interview_started": "🎤 Собеседование началось!\n\nВопрос {} из {}:",
#     "question": "❓ {}",
#     "answer_question": "💬 Напишите свой ответ:",
#     "next_question": "➡️ Следующий вопрос",
#     "interview_completed": "✅ Собеседование завершено!",
    
#     # Результаты собеседования
#     "evaluating_answers": "🤖 Оценка ответов...",
#     "interview_success": """🎉 Поздравляем! Собеседование прошло успешно!
    
# 📊 Общий балл: {} / 100
# ✅ Ждем вас на следующем этапе.

# 📞 Работодатель скоро свяжется с вами.""",
    
#     "interview_failed": """😔 К сожалению, на этот раз вы не прошли отбор.
    
# 📊 Общий балл: {} / 100
# 🎯 Минимальный балл: 70

# 💡 Продолжайте подавать заявки на другие вакансии!""",
    
#     # Дополнительная информация
#     "additional_info": "📝 Требуется дополнительная информация:",
#     "full_name": "👤 Введите ваше полное имя:",
#     "age": "🎂 Введите ваш возраст:",
#     "phone_number": "📞 Введите номер телефона:",
#     "email": "📧 Введите email адрес:",
#     "address": "📍 Введите адрес проживания:",
#     "info_saved": "✅ Информация сохранена и отправлена работодателю!",
    
#     # Админ панель
#     "admin_menu": "⚙️ Админ Панель",
#     "analytics": "📊 Аналитика",
#     "system_stats": "📈 Системная статистика",
    
#     # Аналитика
#     "analytics_data": """📊 Системная аналитика:
    
# 👥 Пользователи:
# • Всего: {}
# • Работодатели: {}
# • Соискатели: {}

# 📋 Вакансии:
# • Всего: {}
# • Активные: {}
# • Архивированные: {}

# 📨 Заявки:
# • Всего: {}
# • Принятые: {}
# • Отклоненные: {}

# 📅 Сегодня: {}""",
    
#     # Ошибки
#     "session_expired": "⏰ Сессия истекла. Начните заново.",
#     "access_denied": "🚫 Доступ запрещен.",
#     "invalid_command": "❌ Неверная команда.",
#     "processing": "⏳ Обработка...",
#     "please_wait": "⏳ Пожалуйста, подождите...",
    
#     # Кнопки
#     "btn_uzbek": "🇺🇿 O'zbek",
#     "btn_russian": "🇷🇺 Русский",
#     "btn_employer": "👔 Работодатель",
#     "btn_jobseeker": "👤 Соискатель",
#     "btn_back": "🔙 Назад",
#     "btn_cancel": "❌ Отмена",
#     "btn_continue": "➡️ Продолжить",
#     "btn_save": "💾 Сохранить",
#     "btn_apply": "🚀 Подать заявку",
#     "btn_view": "👁️ Посмотреть",
#     "btn_download": "📥 Скачать",
#     "btn_archive": "📦 Архивировать",
#     "btn_activate": "🔄 Активировать",
#     "btn_yes": "✅ Да",
#     "btn_no": "❌ Нет",
# }

# import aiogram

# def get_text(key, language="uz", **kwargs):
#     """Belgilangan tilda matnni qaytaradi"""
#     texts = UZ_TEXTS if language == Languages.UZ else RU_TEXTS
#     text = texts.get(key, f"[{key}]")
    
#     if kwargs:
#         try:
#             return text.format(**kwargs)
#         except:
#             return text
#     return text

# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# def get_main_menu_keyboard(language="uz"):
#     """Asosiy menyu tugmalari"""
#     return InlineKeyboardMarkup(
#         inline_keyboard=[
#             # [InlineKeyboardButton(text=get_text("btn_employer", language), callback_data="role_employer")],
#             [InlineKeyboardButton(text=get_text("btn_jobseeker", language), callback_data="role_jobseeker")]
#         ]
#     )


# def get_back_keyboard(language="uz"):
#     """Orqaga tugmasi"""
#     return InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text=get_text("btn_back", language), callback_data="back_main")]
#         ]
#     )


# def get_cancel_keyboard(language="uz"):
#     """Bekor qilish tugmasi"""
#     return InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text=get_text("btn_cancel", language), callback_data="cancel")]
#         ]
#     )


# def get_language_keyboard():
#     """Til tanlash tugmalari"""
#     return InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data="lang_uz"),
#              InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")]
#         ]
#     )



# -*- coding: utf-8 -*-

from enum import Enum, auto
from typing import Dict, Any, Optional, Union
from dataclasses import dataclass
import logging
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Logger
logger = logging.getLogger(__name__)

# ===========================================
# LANGUAGE CONSTANTS - Professional Enum
# ===========================================

class SupportedLanguages(Enum):
    """Qo'llab-quvvatlanuvchi tillar enum"""
    UZBEK = "uz"
    RUSSIAN = "ru"
    
    @classmethod
    def get_default(cls) -> 'SupportedLanguages':
        """Default tilni qaytarish"""
        return cls.UZBEK
    
    @classmethod
    def is_supported(cls, language_code: str) -> bool:
        """Til qo'llab-quvvatlanishini tekshirish"""
        return language_code in [lang.value for lang in cls]
    
    @classmethod
    def get_all_codes(cls) -> list:
        """Barcha til kodlarini qaytarish"""
        return [lang.value for lang in cls]

# Backward compatibility
class Languages:
    UZ = SupportedLanguages.UZBEK.value
    RU = SupportedLanguages.RUSSIAN.value

# ===========================================
# LANGUAGE TEXTS - Enhanced with Categories  
# ===========================================

@dataclass
class TextCategory:
    """Text kategoriyalari uchun dataclass"""
    general: Dict[str, str]
    navigation: Dict[str, str]
    auth: Dict[str, str]
    employer: Dict[str, str]
    jobseeker: Dict[str, str]
    admin: Dict[str, str]
    errors: Dict[str, str]
    buttons: Dict[str, str]

# O'zbek tili - kategoriyalar bo'yicha tashkillangan
UZ_TEXTS = {
    # ===========================================
    # GENERAL - Umumiy
    # ===========================================
    "welcome": "🤖 **Ish Topish Botiga xush kelibsiz!**\n\n📋 Bu bot ish beruvchilar va ishga topshiruvchilar uchun professional platforma.\n\n🌟 AI texnologiyasi yordamida resume tahlil qilish va suhbat o'tkazish imkoniyati mavjud.\n\n🔽 Tilni tanlang:",
    "language_selected": "✅ Til muvaffaqiyatli tanlandi!",
    "choose_role": "🎭 **Rolni tanlang:**\n\nSiz kim sifatida foydalanmoqchisiz?",
    "error": "❌ Xatolik yuz berdi. Iltimos, qaytadan urinib ko'ring.",
    "success": "✅ Muvaffaqiyatli bajarildi!",
    "processing": "⏳ Ishlov berilmoqda, biroz kuting...",
    "please_wait": "⏳ Iltimos, sabr qiling...",
    "feature_coming_soon": "🚧 Bu funksiya tez orada qo'shiladi!",
    
    # ===========================================
    # NAVIGATION - Navigatsiya
    # ===========================================
    "main_menu": "🏠 Asosiy menyu",
    "back_to_main": "🏠 Asosiy menyuga qaytish",
    "btn_back": "🔙 Orqaga",
    "btn_cancel": "❌ Bekor qilish",
    "btn_continue": "➡️ Davom etish",
    "btn_save": "💾 Saqlash",
    "btn_yes": "✅ Ha",
    "btn_no": "❌ Yo'q",
    
    # ===========================================
    # EMPLOYER - Ish beruvchi
    # ===========================================
    "employer_menu": "👔 **Ish beruvchi paneliga xush kelibsiz!**\n\nQuyidagi amallardan birini tanlang:",
    "create_vacancy": "➕ Yangi vakansiya yaratish",
    "my_vacancies": "📋 Mening vakansiyalarim",
    "applications": "📬 Kelgan arizalar",
    "analytics": "📊 Analitika va statistika",
    
    # Vakansiya yaratish - Enhanced
    "creating_vacancy": "📝 **Vakansiya yaratish jarayoni**\n\n🔹 Bu jarayon bir necha bosqichdan iborat\n🔹 Har bir ma'lumot diqqat bilan to'ldirilsin\n🔹 AI orqali nomzodlar avtomatik baholanadi",
    "company_name_prompt": "🏢 **Kompaniya nomini kiriting:**\n\n💡 *Masalan: \"IT Solutions LLC\" yoki \"Najot Ta'lim\"*",
    "company_description_prompt": "📄 **Kompaniya haqida batafsil ma'lumot bering:**\n\n💡 *Faoliyat sohasini, missiyasini va afzalliklarini yozing*",
    "company_website_prompt": "🌐 **Kompaniya veb-saytini kiriting:**\n\n💡 *Agar yo'q bo'lsa \"Yo'q\" deb yozing*",
    "company_location_prompt": "📍 **Kompaniya joylashuvi:**\n\n💡 *Masalan: \"Toshkent, Chilonzor tumani\"*",
    
    "vacancy_section_start": "📌 **Vakansiya ma'lumotlari**\n\nEndi vakansiya haqidagi asosiy ma'lumotlarni kiritamiz:",
    "vacancy_title_prompt": "📌 **Vakansiya nomini kiriting:**\n\n💡 *Masalan: \"Senior Python Developer\" yoki \"Marketing Menejeri\"*",
    "vacancy_description_prompt": "📝 **Vakansiya tavsifini kiriting:**\n\n💡 *Lavozim haqida batafsil ma'lumot, nima bilan shug'ullanishi kerak*",
    "vacancy_requirements_prompt": "📋 **Talablarni kiriting:**\n\n💡 *Texnik ko'nikmalar, tajriba, sertifikatlar va boshqa talablar*",
    "vacancy_responsibilities_prompt": "⚡ **Majburiyatlarni kiriting:**\n\n💡 *Kundalik vazifalar va mas'uliyatlar*",
    
    # Ish sharoitlari
    "work_type_prompt": "💼 **Ish turini tanlang:**",
    "work_type_remote": "🏠 Masofaviy ish",
    "work_type_office": "🏢 Ofisda ish",
    "work_type_hybrid": "🔄 Aralash rejim",
    
    "work_schedule_prompt": "📅 **Ish jadvalini tanlang:**",
    "work_schedule_full_time": "⏰ To'liq kunlik",
    "work_schedule_part_time": "🕐 Yarim kunlik",
    "work_schedule_contract": "📋 Shartnoma asosida",
    
    "salary_range_prompt": "💰 **Ish haqqini kiriting:**\n\n💡 *Masalan: \"5000000-8000000\" yoki \"Kelishilgan\"*",
    "work_location_prompt": "📍 **Ish joyini kiriting:**\n\n💡 *Aniq manzil yoki hudud nomi*",
    "experience_years_prompt": "📈 **Necha yillik tajriba kerak?**\n\n💡 *Masalan: \"2-3 yil\" yoki \"Tajribasiz ham bo'ladi\"*",
    
    # AI kriteriyalar - Enhanced
    "ai_criteria_section_start": "🤖 **AI tahlil kriteriylari**\n\nEndi resume avtomatik baholash uchun kriteriyalarni belgilaymiz:",
    "ai_criteria_skills_prompt": "💻 **Qanday ko'nikmalar bo'lishi kerak?**\n\n💡 *Masalan: \"Python, Django, PostgreSQL, Git\"*\n💡 *Vergul bilan ajrating*",
    "ai_criteria_experience_prompt": "📈 **Qanday tajriba kerak?**\n\n💡 *Masalan: \"Python bilan 2+ yil ish tajribasi\"*",
    "ai_criteria_education_prompt": "🎓 **Ta'lim talablari:**\n\n💡 *Masalan: \"Oliy ma'lumot, IT soha\"*",
    "ai_criteria_languages_prompt": "🌍 **Qanday tillar bilishi kerak?**\n\n💡 *Masalan: \"Ingliz tili (B2), O'zbek tili (ona tili)\"*",
    "ai_criteria_additional_prompt": "➕ **Qo'shimcha kriteriyalar:**\n\n💡 *Portfolio, GitHub, sertifikatlar va boshqa talablar*",
    "ai_prompt_creation_prompt": "🎯 **Maxsus tahlil yo'riqnomasi:**\n\n💡 *AI ga qo'shimcha ko'rsatmalar bering*\n💡 *Masalan: \"Portfolio mavjudligini e'tiborga oling\"*",
    
    # Interview savollari
    "interview_questions_count_prompt": "❓ **Suhbat savollari soni:**\n\nNechta savol berasiz?",
    "interview_question_input_prompt": "❓ **{current}/{total} - savolni kiriting:**\n\n💡 *Professional va aniq savol bering*",
    
    # Vakansiya yaratish yakunlash
    "vacancy_confirmation": "👀 **Vakansiya yaratish yakunlanmoqda**\n\nQuyidagi ma'lumotlarni tekshiring:",
    "vacancy_created_success": "🎉 **Vakansiya muvaffaqiyatli yaratildi!**\n\n📌 **Nomi:** {title}\n🏢 **Kompaniya:** {company}\n📅 **Yaratilgan:** {date}\n\n✅ Vakansiya faol holga o'tkazildi va nomzodlar ariza berishni boshlashlari mumkin!",
    
    # Vakansiya boshqaruvi
    "no_companies_found": "🏢 Sizda hali kompaniyalar yo'q.",
    "no_vacancies_found": "📭 Faol vakansiyalar topilmadi.",
    "my_vacancies_list": "📋 **Mening vakansiyalarim:**",
    "total_vacancies": "📊 Jami: {0} ta vakansiya",
    "vacancy_full_details": """📌 **{title}**
🏢 **Kompaniya:** {company_name}
📝 **Tavsif:** {description}
📋 **Talablar:** {requirements}
⚡ **Majburiyatlar:** {responsibilities}
💼 **Ish turi:** {work_type}
📅 **Ish jadvali:** {work_schedule}
📍 **Joylashuv:** {location}
📈 **Tajriba:** {experience_years} yil
💰 **Ish haqqi:** {salary}""",
    
    "manage_vacancy_options": "⚙️ **Vakansiyani boshqarish:**",
    "archive_vacancy": "📦 Arxivlash",
    "activate_vacancy": "🔄 Faollashtirish",
    "view_applications": "📨 Arizalarni ko'rish",
    
    # Arizalar
    "no_applications_found": "📭 Hozircha arizalar yo'q.",
    "applications_list": "📬 **Kelgan arizalar:**",
    "employer_analytics": "📊 **Ish beruvchi analitikasi:**",
    
    # ===========================================
    # JOBSEEKER - Ishga topshiruvchi
    # ===========================================
    "jobseeker_menu": "👤 **Ishga topshiruvchi paneliga xush kelibsiz!**\n\nQuyidagi amallardan birini tanlang:",
    "find_jobs": "🔍 Ish izlash",
    "my_applications": "📨 Mening arizalarim",
    
    # Company va vacancy browsing
    "no_active_companies": "🏢 Hozircha faol kompaniyalar yo'q.",
    "select_company": "🏢 **Kompaniyani tanlang:**",
    "available_companies": "📊 Mavjud kompaniyalar: {0} ta",
    "company_info": """🏢 **{name}**

📝 **Tavsif:** {description}

📊 **Vakansiyalar:** {vacancy_count} ta""",
    
    "no_active_vacancies": "📭 **{0}** kompaniyasida hozircha faol vakansiyalar yo'q.",
    "company_not_found": "🚫 Kompaniya topilmadi.",
    "vacancy_not_found": "🚫 Vakansiya topilmadi.",
    
    # Application process - Enhanced
    "already_applied": "✅ **Siz bu vakansiyaga allaqachon ariza bergansiz!**\n\nArizangizning holatini tekshirish uchun \"Mening arizalarim\" bo'limiga o'ting.",
    "daily_limit_exceeded": "⚠️ **Kunlik ariza limiti tugadi!**\n\nBir kunda maksimal {0} ta ariza berish mumkin.\nErtaga qayta urinib ko'ring.",
    
    "upload_resume_prompt": "📄 **Resume faylini yuklang:**",
    "supported_formats": "📋 **Qo'llab-quvvatlanadigan formatlar:** PDF, DOC, DOCX",
    "max_file_size": "📏 **Maksimal hajm**",
    
    # File handling messages
    "no_file_received": "❌ Fayl olinmadi. Iltimos, qaytadan yuklang.",
    "invalid_file_format": "❌ **Noto'g'ri fayl formati!**",
    "file_too_large": "❌ **Fayl juda katta!**\n\n📏 Joriy hajm: {current_size}MB\n📏 Maksimal: {max_size}MB",
    "file_save_error": "❌ Faylni saqlashda xatolik. Qaytadan urinib ko'ring.",
    "processing_resume": "📄 Resume yuklanmoqda...",
    "parsing_resume": "🔍 Resume tahlil qilinmoqda...",
    "analyzing_compatibility": "🤖 Vakansiya bilan moslik tekshirilmoqda...",
    "resume_parse_error": "❌ Resume ni o'qishda xatolik. Boshqa fayl yuklang.",
    "processing_error": "❌ Ishlov berishda xatolik yuz berdi.",
    
    # Compatibility analysis
    "compatibility_too_low": "😔 **Afsuski, resume vakansiya talablariga yetarlicha mos kelmaydi.**\n\n📊 **Moslik darajasi:** {score}%\n🎯 **Minimal talabi:** {min_required}%",
    "compatibility_good": "✅ **Ajoyib! Resume vakansiya talablariga mos keladi!**\n\n📊 **Moslik darajasi:** {score}%",
    "rejection_reasons": "❌ **Rad etish sabablari**",
    "strengths": "💪 **Kuchli tomonlar**",
    "find_other_jobs": "🔍 Boshqa ishlarni izlash",
    "continue_to_interview": "🎤 Suhbatga o'tish",
    
    # Interview process - Enhanced  
    "no_interview_questions": "✅ **Bu vakansiya uchun suhbat savollari belgilanmagan.**\n\nTo'g'ridan-to'g'ri qo'shimcha ma'lumotlar bosqichiga o'tamiz.",
    "interview_started": "🎤 **Suhbat boshlandi!**\n\n📊 **Savol:** {current} / {total}",
    "question_prompt": "❓ {}-savol:",
    "current_question": "❓ **Joriy savol**",
    "interview_instructions": "💡 **Eslatma:** Savolga batafsil va professional javob bering. Kamida 10 ta so'z yozing.",
    "interview_progress": "📈 **Jarayon:** {current} / {total} savol",
    
    "answer_too_short": "❌ Javob juda qisqa! Kamida 10 ta so'z yozing.",
    "answer_too_long": "❌ Javob juda uzun! Maksimal 1000 ta belgi.",
    
    "evaluating_interview": "🤖 **Suhbat javoblari baholanmoqda...**\n\nBir necha daqiqa vaqt ketishi mumkin.",
    "interview_passed": "🎉 **Tabriklaymiz! Suhbat muvaffaqiyatli o'tdi!**\n\n📊 **Umumiy ball:** {score}/100",
    "interview_failed": "😔 **Afsuski, suhbat minimal balga yetmadi.**\n\n📊 **Sizning ballingiz:** {score}/100\n🎯 **Minimal ball:** {min_required}/100",
    "positive_aspects": "✅ **Ijobiy tomonlar**",
    "improvement_areas": "📝 **Yaxshilanishi kerak bo'lgan sohalar**",
    "evaluation_error": "❌ Suhbat baholashda xatolik yuz berdi.",
    
    # Additional info collection
    "additional_info_intro": "📝 **Qo'shimcha ma'lumotlar**\n\nIsh beruvchi siz bilan bog'lanish uchun ba'zi ma'lumotlar kerak:",
    "full_name_prompt": "👤 **To'liq ismingizni kiriting:**",
    "age_prompt": "🎂 **Yoshingizni kiriting:** (16-80 oralig'ida)",
    "phone_prompt": "📞 **Telefon raqamingizni kiriting:**\n\n💡 *Masalan: +998901234567*",
    "email_prompt": "📧 **Email manzilingizni kiriting:**\n\n💡 *Masalan: example@gmail.com*",
    "address_prompt": "📍 **Yashash manzilingizni kiriting:**\n\n💡 *Shahar, tuman yoki to'liq manzil*",
    
    # Validation messages
    "name_too_short": "❌ Ism juda qisqa! Kamida 3 ta harf bo'lishi kerak.",
    "name_too_long": "❌ Ism juda uzun! Maksimal 100 ta belgi.",
    "invalid_name_format": "❌ Ismda faqat harflar, bo'shliq va tirnoq bo'lishi mumkin.",
    "invalid_age": "❌ Yoshni to'g'ri kiriting! (16-80 oralig'ida raqam)",
    "invalid_phone": "❌ Telefon raqamni to'g'ri formatda kiriting!",
    "invalid_email": "❌ Email manzilini to'g'ri formatda kiriting!",
    "address_too_short": "❌ Manzil juda qisqa! Kamida 5 ta belgi yozing.",
    
    # Application completion
    "application_completed": "🎉 **Ariza muvaffaqiyatli yuborildi!**\n\n📌 **Vakansiya:** {vacancy_title}\n📅 **Sana:** {date}\n\n✅ Ish beruvchi sizning ma'lumotlaringizni ko'rib chiqadi va tez orada javob beradi.",
    "completion_error": "❌ Arizani yakunlashda xatolik yuz berdi.",
    
    # Application management
    "no_applications_found": "📭 Sizda hali arizalar yo'q.",
    "my_applications_list": "📨 **Mening arizalarim:**",
    "total_applications": "📊 Jami: {0} ta ariza",
    "application_details": "📋 **Ariza tafsilotlari:**",
    "application_not_found": "🚫 Ariza topilmadi.",
    
    # Status messages
    "status_pending": "🟡 Kutilmoqda",
    "status_ai_screening": "🔄 AI tomonidan tekshirilmoqda", 
    "status_interview": "💬 Suhbat bosqichida",
    "status_accepted": "✅ Qabul qilindi",
    "status_rejected": "❌ Rad etildi",
    
    # Employer notifications
    "new_application_notification": "🎉 **Yangi nomzod!**",
    "company": "Kompaniya",
    "vacancy": "Vakansiya", 
    "applicant": "Nomzod",
    "compatibility": "Moslik",
    "phone": "Telefon",
    "email": "Email",
    "address": "Manzil",
    "age": "Yosh",
    "interview_score": "Suhbat bali",
    "applied_at": "Ariza bergan vaqti",
    "view_full_details_in_panel": "📊 To'liq ma'lumotlarni admin paneldan ko'ring.",
    
    # ===========================================
    # ADMIN PANEL
    # ===========================================
    "admin_menu": "⚙️ **Admin Panel**\n\nTizim boshqaruvi va monitoring:",
    "detailed_analytics": "📊 Batafsil analitika",
    "user_not_found": "🚫 Foydalanuvchi topilmadi.",
    
    # ===========================================
    # ERROR MESSAGES
    # ===========================================
    "session_expired": "⏰ Sessiya tugadi. /start buyrug'ini ishlatib qaytadan boshlang.",
    "access_denied": "🚫 **Ruxsat berilmagan!**\n\nBu funksiyadan foydalanish uchun maxsus ruxsatingiz yo'q.",
    "invalid_command": "❌ **Noma'lum buyruq!**\n\nIltimos, tugmalardan foydalaning yoki /start buyrug'ini ishlatib qaytadan boshlang.",
    "user_not_found": "🚫 Foydalanuvchi ma'lumotlari topilmadi.",
    "question_too_short": "❌ Savol juda qisqa! Kamida 5 ta so'z yozing.",
    
    # ===========================================  
    # BUTTONS - Enhanced
    # ===========================================
    "btn_uzbek": "🇺🇿 O'zbek",
    "btn_russian": "🇷🇺 Русский", 
    "btn_employer": "👔 Ish beruvchi",
    "btn_jobseeker": "👤 Ishga topshiruvchi",
    "btn_apply": "🚀 Ariza berish",
    "btn_view": "👁️ Ko'rish",
    "btn_download": "📥 Yuklab olish",
    "btn_archive": "📦 Arxivlash",
    "btn_activate": "🔄 Faollashtirish",
    "btn_confirm": "✅ Tasdiqlash",
    "create_new_vacancy": "➕ Yangi vakansiya",
    "view_vacancy": "👁️ Ko'rish",
    "find_more_jobs": "🔍 Boshqa ishlar",
    "back_to_menu": "🏠 Asosiy menyu",
    "vacancy_creation_cancelled": "❌ Vakansiya yaratish bekor qilindi.",
    "application_cancelled": "❌ Ariza berish bekor qilindi.",
    
    # ===========================================
    # UTILITY TEXTS
    # ===========================================
    "location_not_specified": "Ko'rsatilmagan",
    "salary_negotiable": "Kelishilgan",
    "salary_not_specified": "Ko'rsatilmagan", 
    "up_to": "Gacha",
    "no_description": "Tavsif mavjud emas",
    "position": "Lavozim",
    "location": "Joylashuv",
    "salary": "Ish haqqi",
    "work_type": "Ish turi",
    "work_schedule": "Ish jadvali",
    "questions_count": "Savollar soni",
    "confirmation_question": "Barcha ma'lumotlar to'g'rimi?",
    "date": "Sana",
}

# Rus tili - optimized version
RU_TEXTS = {
    # General
    "welcome": "🤖 **Добро пожаловать в бот по трудоустройству!**\n\n📋 Это профессиональная платформа для работодателей и соискателей.\n\n🌟 Доступны анализ резюме и собеседования с использованием ИИ.\n\n🔽 Выберите язык:",
    "language_selected": "✅ Язык успешно выбран!",
    "choose_role": "🎭 **Выберите роль:**\n\nКак вы хотите использовать бот?",
    "error": "❌ Произошла ошибка. Пожалуйста, попробуйте еще раз.",
    "success": "✅ Успешно выполнено!",
    "processing": "⏳ Обрабатывается, подождите...",
    "please_wait": "⏳ Пожалуйста, подождите...",
    "feature_coming_soon": "🚧 Эта функция скоро будет добавлена!",
    
    # Navigation
    "main_menu": "🏠 Главное меню",
    "back_to_main": "🏠 Вернуться в главное меню",
    "btn_back": "🔙 Назад", 
    "btn_cancel": "❌ Отмена",
    "btn_continue": "➡️ Продолжить",
    "btn_save": "💾 Сохранить",
    "btn_yes": "✅ Да",
    "btn_no": "❌ Нет",
    
    # Employer
    "employer_menu": "👔 **Добро пожаловать в панель работодателя!**\n\nВыберите одно из действий:",
    "create_vacancy": "➕ Создать новую вакансию",
    "my_vacancies": "📋 Мои вакансии",
    "applications": "📬 Заявки",
    "analytics": "📊 Аналитика и статистика",
    
    # Vacancy creation - key translations
    "creating_vacancy": "📝 **Процесс создания вакансии**\n\n🔹 Процесс состоит из нескольких этапов\n🔹 Заполните каждое поле внимательно\n🔹 Кандидаты будут оцениваться ИИ автоматически",
    "company_name_prompt": "🏢 **Введите название компании:**\n\n💡 *Например: \"IT Solutions LLC\" или \"Najot Ta'lim\"*",
    "vacancy_title_prompt": "📌 **Введите название вакансии:**\n\n💡 *Например: \"Senior Python Developer\" или \"Marketing Manager\"*",
    
    # Jobseeker
    "jobseeker_menu": "👤 **Добро пожаловать в панель соискателя!**\n\nВыберите одно из действий:",
    "find_jobs": "🔍 Поиск работы",
    "my_applications": "📨 Мои заявки",
    
    "select_company": "🏢 **Выберите компанию:**",
    "available_companies": "📊 Доступные компании: {0}",
    "upload_resume_prompt": "📄 **Загрузите файл резюме:**",
    "supported_formats": "📋 **Поддерживаемые форматы:** PDF, DOC, DOCX",
    "max_file_size": "📏 **Максимальный размер**",
    
    "compatibility_good": "✅ **Отлично! Резюме соответствует требованиям вакансии!**\n\n📊 **Уровень соответствия:** {score}%",
    "interview_started": "🎤 **Собеседование началось!**\n\n📊 **Вопрос:** {current} / {total}",
    "question_prompt": "❓ {}-вопрос:",
    
    "interview_questions_count_prompt": "❓ **Количество вопросов собеседования:**\n\nСколько вопросов зададите?",
    "interview_question_input_prompt": "❓ **{current}/{total} - введите вопрос:**\n\n💡 *Задайте профессиональный и точный вопрос*",
    
    # Admin
    "admin_menu": "⚙️ **Админ панель**\n\nУправление системой и мониторинг:",
    "access_denied": "🚫 **Доступ запрещен!**\n\nУ вас нет специального разрешения для использования этой функции.",
    
    # Buttons
    "btn_uzbek": "🇺🇿 O'zbek",
    "btn_russian": "🇷🇺 Русский",
    "btn_employer": "👔 Работодатель",
    "btn_jobseeker": "👤 Соискатель",
    "btn_apply": "🚀 Подать заявку",
    "btn_view": "👁️ Посмотреть",
    "application_completed": "🎉 **Заявка успешно отправлена!**\n\n📌 **Вакансия:** {vacancy_title}\n\n✅ Работодатель рассмотрит ваши данные и скоро ответит.",
    
    # Common keys that need translation
    "company_not_found": "🚫 Компания не найдена.",
    "vacancy_not_found": "🚫 Вакансия не найдена.",
    "invalid_command": "❌ **Неизвестная команда!**\n\nПожалуйста, используйте кнопки или команду /start для перезапуска.",
    "user_not_found": "🚫 Данные пользователя не найдены.",
}

# ===========================================
# TEXT RETRIEVAL FUNCTIONS - Enhanced
# ===========================================

def get_text(key: str, language: str = "uz", **kwargs) -> str:
    """
    Belgilangan tilda matnni qaytaradi - Enhanced version
    
    Args:
        key: Text kaliti
        language: Til kodi (uz/ru) 
        **kwargs: Format parametrlari
        
    Returns:
        Formatlangan matn
    """
    try:
        # Language validation
        if not SupportedLanguages.is_supported(language):
            language = SupportedLanguages.get_default().value
            logger.warning(f"Unsupported language, fallback to {language}")
        
        # Text selection
        texts = UZ_TEXTS if language == SupportedLanguages.UZBEK.value else RU_TEXTS
        text = texts.get(key)
        
        # Fallback handling
        if text is None:
            # Try opposite language as fallback
            fallback_texts = RU_TEXTS if language == SupportedLanguages.UZBEK.value else UZ_TEXTS
            text = fallback_texts.get(key)
            
            if text is None:
                logger.warning(f"Text key '{key}' not found in any language")
                return f"[{key}]"  # Debug mode
        
        # Format with parameters
        if kwargs:
            try:
                return text.format(**kwargs)
            except (KeyError, ValueError) as e:
                logger.error(f"Text formatting error for key '{key}': {e}")
                return text
        
        return text
        
    except Exception as e:
        logger.error(f"get_text error: {e}")
        return f"[ERROR: {key}]"

def get_all_texts(language: str = "uz") -> Dict[str, str]:
    """Barcha matnlarni qaytarish - debugging uchun"""
    texts = UZ_TEXTS if language == SupportedLanguages.UZBEK.value else RU_TEXTS
    return texts.copy()

def validate_translations() -> Dict[str, Any]:
    """Translation completeness validation"""
    uz_keys = set(UZ_TEXTS.keys())
    ru_keys = set(RU_TEXTS.keys())
    
    missing_in_ru = uz_keys - ru_keys
    missing_in_uz = ru_keys - uz_keys
    
    return {
        "total_uz": len(uz_keys),
        "total_ru": len(ru_keys),
        "missing_in_ru": list(missing_in_ru),
        "missing_in_uz": list(missing_in_uz),
        "completion_rate": len(ru_keys) / len(uz_keys) * 100 if uz_keys else 0
    }

# ===========================================
# KEYBOARD BUILDERS - Enhanced
# ===========================================

def get_language_keyboard() -> InlineKeyboardMarkup:
    """Til tanlash tugmalari - Enhanced"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🇺🇿 O'zbek", 
                    callback_data="lang_uz"
                ),
                InlineKeyboardButton(
                    text="🇷🇺 Русский", 
                    callback_data="lang_ru"
                )
            ]
        ]
    )

def get_main_menu_keyboard(language: str = "uz") -> InlineKeyboardMarkup:
    """Asosiy menyu tugmalari - Enhanced"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=get_text("btn_jobseeker", language), 
                    callback_data="role_jobseeker"
                )
            ]
        ]
    )

def get_back_keyboard(language: str = "uz", callback_data: str = "back_main") -> InlineKeyboardMarkup:
    """Orqaga tugmasi - Flexible"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=get_text("btn_back", language), 
                    callback_data=callback_data
                )
            ]
        ]
    )

def get_cancel_keyboard(language: str = "uz", callback_data: str = "cancel") -> InlineKeyboardMarkup:
    """Bekor qilish tugmasi"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=get_text("btn_cancel", language), 
                    callback_data=callback_data
                )
            ]
        ]
    )

def get_confirmation_keyboard(language: str = "uz", yes_callback: str = "confirm_yes", no_callback: str = "confirm_no") -> InlineKeyboardMarkup:
    """Tasdiqlash tugmalari"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=get_text("btn_yes", language), 
                    callback_data=yes_callback
                ),
                InlineKeyboardButton(
                    text=get_text("btn_no", language), 
                    callback_data=no_callback
                )
            ]
        ]
    )

# ===========================================
# UTILITY FUNCTIONS
# ===========================================

def format_user_role(role: str, language: str = "uz") -> str:
    """User role ni formatlash"""
    role_mapping = {
        "employer": get_text("btn_employer", language),
        "jobseeker": get_text("btn_jobseeker", language),
        "admin": "👨‍💼 Admin"
    }
    return role_mapping.get(role, role.title())

def get_status_emoji(status: str) -> str:
    """Status uchun emoji qaytarish"""
    status_emojis = {
        "pending": "🟡",
        "ai_screening": "🔄", 
        "interview": "💬",
        "accepted": "✅",
        "rejected": "❌",
        "active": "🟢",
        "archived": "🔴"
    }
    return status_emojis.get(status, "❓")

def format_file_size_text(size_mb: float, language: str = "uz") -> str:
    """File size ni human-readable formatda"""
    if size_mb < 1:
        return f"{size_mb * 1024:.0f} KB"
    elif size_mb < 1024:
        return f"{size_mb:.1f} MB"
    else:
        return f"{size_mb / 1024:.1f} GB"

# Development/Debug utilities
def get_translation_stats() -> str:
    """Translation statistics"""
    stats = validate_translations()
    return f"""📊 Translation Statistics:
🇺🇿 O'zbek: {stats['total_uz']} keys
🇷🇺 Russian: {stats['total_ru']} keys
📈 Completion: {stats['completion_rate']:.1f}%
❌ Missing in RU: {len(stats['missing_in_ru'])}
❌ Missing in UZ: {len(stats['missing_in_uz'])}"""

if __name__ == "__main__":
    # Test va validation
    print("🧪 Language Module Test")
    print(get_translation_stats())
    
    # Sample texts
    print(f"\n📝 Sample texts:")
    print(f"UZ: {get_text('welcome', 'uz')}")
    print(f"RU: {get_text('welcome', 'ru')}")
