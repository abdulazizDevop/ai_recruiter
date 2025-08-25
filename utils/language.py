# -*- coding: utf-8 -*-

class Languages:
    UZ = "uz"
    RU = "ru"

# O'zbek tili
UZ_TEXTS = {
    # Umumiy
    "welcome": "🤖 Botga xush kelibsiz!\n\n📋 Bu bot ish beruvchilar va ishga topshiruvchilar uchun mo'ljallangan.\n\nTilni tanlang:",
    "language_selected": "✅ Til tanlandi!",
    "back": "🔙 Orqaga",
    "cancel": "❌ Bekor qilish",
    "next": "➡️ Keyingisi",
    "save": "💾 Saqlash",
    "error": "❌ Xatolik yuz berdi. Qaytadan urinib ko'ring.",
    "success": "✅ Muvaffaqiyatli!",
    
    # Til tanlash
    "uzbek": "🇺🇿 O'zbek",
    "russian": "🇷🇺 Русский",
    
    # Asosiy menyu
    "main_menu": "🏠 Asosiy menyu",
    "choose_role": "🎭 Rolni tanlang:",
    "employer": "👔 Ish beruvchi",
    "jobseeker": "👤 Ishga topshiruvchi",
    "admin_panel": "⚙️ Admin panel",
    
    # Ish beruvchi menyusi
    "employer_menu": "👔 Ish beruvchi menyusi",
    "create_vacancy": "➕ Vakansiya yaratish",
    "my_vacancies": "📋 Mening vakansiyalarim",
    "applications": "📬 Kelgan arizalar",
    "my_companies": "🏢 Mening kompaniyalarim",
    
    # Vakansiya yaratish
    "creating_vacancy": "📝 Vakansiya yaratish\n\nBu jarayon bir necha bosqichdan iborat:",
    "company_name": "🏢 Kompaniya nomini kiriting:",
    "company_description": "📄 Kompaniya tavsifini kiriting:",
    "vacancy_title": "📌 Vakansiya nomini kiriting:",
    "vacancy_description": "📝 Vakansiya tavsifini kiriting:",
    "vacancy_requirements": "📋 Talablarni kiriting:",
    "vacancy_responsibilities": "⚡ Majburiyatlarni kiriting:",
    "salary_range": "💰 Ish haqqi oralig'ini kiriting (masalan: 5000000-8000000) yoki 'Kelishilgan' deb yozing:",
    "work_hours": "🕒 Ish soatlarini kiriting (masalan: 9:00-18:00):",
    "work_days": "📅 Ish kunlarini kiriting (masalan: Dushanba-Juma):",
    "work_location": "📍 Ish joyini kiriting:",
    
    # AI kriteriyalar
    "ai_criteria": "🤖 Resume tahlili uchun kriteriyalar\n\nAI quyidagi kriteriyalar asosida resume ni tahlil qiladi:",
    "criteria_skills": "💻 Qanday ko'nikmalar bo'lishi kerak? (vergul bilan ajrating):",
    "criteria_experience": "📈 Qancha yillik tajriba kerak?",
    "criteria_education": "🎓 Ta'lim darajasi (bakalavr, magistr, va h.k.):",
    "criteria_languages": "🌍 Qanday tillarni bilishi kerak?",
    "criteria_additional": "➕ Qo'shimcha kriteriyalar:",
    
    # Savol-javob
    "interview_questions": "❓ Suhbat savollari\n\nNechta savol so'rashin? (1-5 orasida):",
    "question_prompt": "❓ {}-savol:",
    "questions_saved": "✅ Savol-javoblar saqlandi!",
    
    # Vakansiya yakunlash
    "vacancy_created": "🎉 Vakansiya muvaffaqiyatli yaratildi!\n\n📌 Nomi: {}\n🏢 Kompaniya: {}\n📅 Sana: {}",
    "vacancy_preview": "👀 Vakansiya ko'rinishi:\n\n📌 Nomi: {}\n🏢 Kompaniya: {}\n📝 Tavsif: {}\n📋 Talablar: {}\n💰 Ish haqqi: {}\n📍 Joy: {}",
    
    # Vakansiyalar ro'yxati
    "no_vacancies": "📭 Hozircha vakansiyalaringiz yo'q.",
    "vacancy_list": "📋 Vakansiyalar ro'yxati:",
    "vacancy_status_active": "🟢 Faol",
    "vacancy_status_archived": "🔴 Arxivlangan",
    "archive_vacancy": "📦 Arxivlash",
    "activate_vacancy": "🔄 Faollashtirish",
    
    # Kelgan arizalar
    "no_applications": "📭 Hozircha arizalar kelmagan.",
    "applications_list": "📬 Kelgan arizalar:",
    "application_from": "👤 Ariza beruvchi: {}",
    "application_date": "📅 Sana: {}",
    "application_vacancy": "📌 Vakansiya: {}",
    "application_status": "📊 Holat: {}",
    "view_application": "👁️ Ko'rish",
    "download_resume": "📄 Resume yuklab olish",
    
    # Ishga topshiruvchi menyusi
    "jobseeker_menu": "👤 Ishga topshiruvchi menyusi",
    "find_jobs": "🔍 Ish izlash",
    "my_applications": "📨 Mening arizalarim",
    
    # Ish izlash
    "select_company": "🏢 Kompaniyani tanlang:",
    "no_companies": "🏢 Hozircha kompaniyalar yo'q.",
    "select_vacancy": "📌 Vakansiyani tanlang:",
    "no_active_vacancies": "📭 Bu kompaniyada faol vakansiyalar yo'q.",
    
    # Vakansiya ko'rinishi
    "vacancy_details": """📌 Vakansiya: {}
🏢 Kompaniya: {}
📝 Tavsif: {}
📋 Talablar: {}
⚡ Majburiyatlar: {}
💰 Ish haqqi: {}
🕒 Ish soatlari: {}
📅 Ish kunlari: {}
📍 Ish joyi: {}""",
    "apply_now": "🚀 Hoziroq topshirish",
    "already_applied": "✅ Siz bu vakansiyaga allaqachon ariza bergansiz",
    
    # Resume yuklash
    "upload_resume": "📄 Resume faylini yuboring (PDF yoki DOC formatida):",
    "invalid_file": "❌ Noto'g'ri fayl formati. Faqat PDF yoki DOC fayllar qabul qilinadi.",
    "file_too_large": "❌ Fayl hajmi juda katta. Maksimal 10MB.",
    "resume_uploaded": "✅ Resume yuklandi!",
    
    # AI tahlili
    "analyzing_resume": "🔍 Resume tahlil qilinmoqda...",
    "ai_analyzing": "🤖 AI tahlil qilmoqda, biroz kutib turing...",
    "match_percentage": "📊 Moslik darajasi: {}%",
    "match_too_low": """❌ Afsuski, resume vakansiya talablariga mos kelmaydi.
    
📊 Moslik darajasi: {}%
🎯 Minimal darajasi: 60%

💡 Boshqa vakansiyalarga topshirishni xohlaysizmi?""",
    
    "match_good": """✅ Resume vakansiya talablariga mos keladi!
    
📊 Moslik darajasi: {}%

🎤 Endi sizga bir nechta savol beriladi. Tayyor bo'lsangiz 'Davom etish' tugmasini bosing.""",
    
    "continue": "➡️ Davom etish",
    
    # Suhbat savollari
    "interview_started": "🎤 Suhbat boshlandi!\n\nSavol {} / {}:",
    "question": "❓ {}",
    "answer_question": "💬 Javobingizni yozing:",
    "next_question": "➡️ Keyingi savol",
    "interview_completed": "✅ Suhbat yakunlandi!",
    
    # Suhbat natijalari
    "evaluating_answers": "🤖 Javoblar baholanmoqda...",
    "interview_success": """🎉 Tabriklaymiz! Suhbat muvaffaqiyatli o'tdi!
    
📊 Umumiy ball: {} / 100
✅ Sizni keyingi bosqichda kutamiz.

📞 Tez orada ish beruvchi siz bilan bog'lanadi.""",
    
    "interview_failed": """😔 Afsuski, bu safar siz tanlangansiz yo'q.
    
📊 Umumiy ball: {} / 100
🎯 Minimal ball: 70

💡 Boshqa vakansiyalarga topshirishda davom eting!""",
    
    # Qo'shimcha ma'lumotlar
    "additional_info": "📝 Qo'shimcha ma'lumotlar kerak:",
    "full_name": "👤 To'liq ismingizni kiriting:",
    "age": "🎂 Yoshingizni kiriting:",
    "phone_number": "📞 Telefon raqamingizni kiriting:",
    "email": "📧 Email manzilingizni kiriting:",
    "address": "📍 Yashash manzilingizni kiriting:",
    "info_saved": "✅ Ma'lumotlar saqlandi va ish beruvchiga yuborildi!",
    
    # Admin panel
    "admin_menu": "⚙️ Admin Panel",
    "analytics": "📊 Analitika",
    "system_stats": "📈 Tizim statistikasi",
    
    # Analitika
    "analytics_data": """📊 Tizim analitikasi:
    
👥 Foydalanuvchilar:
• Jami: {}
• Ish beruvchilar: {}
• Ishga topshiruvchilar: {}

📋 Vakansiyalar:
• Jami: {}
• Faol: {}
• Arxivlangan: {}

📨 Arizalar:
• Jami: {}
• Qabul qilingan: {}
• Rad etilgan: {}

📅 Bugun: {}""",
    
    # Xato xabarlar
    "session_expired": "⏰ Sessiya tugadi. Qaytadan boshlang.",
    "access_denied": "🚫 Ruxsat berilmagan.",
    "invalid_command": "❌ Noto'g'ri buyruq.",
    "processing": "⏳ Ishlov berilmoqda...",
    "please_wait": "⏳ Iltimos kutib turing...",
    
    # Tugmalar
    "btn_uzbek": "🇺🇿 O'zbek",
    "btn_russian": "🇷🇺 Русский",
    "btn_employer": "👔 Ish beruvchi",
    "btn_jobseeker": "👤 Ishga topshiruvchi",
    "btn_back": "🔙 Orqaga",
    "btn_cancel": "❌ Bekor qilish",
    "btn_continue": "➡️ Davom etish",
    "btn_save": "💾 Saqlash",
    "btn_apply": "🚀 Topshirish",
    "btn_view": "👁️ Ko'rish",
    "btn_download": "📥 Yuklab olish",
    "btn_archive": "📦 Arxivlash",
    "btn_activate": "🔄 Faollashtirish",
    "btn_yes": "✅ Ha",
    "btn_no": "❌ Yo'q",
}

# Rus tili
RU_TEXTS = {
    # Общие
    "welcome": "🤖 Добро пожаловать в бот!\n\n📋 Этот бот предназначен для работодателей и соискателей.\n\nВыберите язык:",
    "language_selected": "✅ Язык выбран!",
    "back": "🔙 Назад",
    "cancel": "❌ Отмена",
    "next": "➡️ Далее",
    "save": "💾 Сохранить",
    "error": "❌ Произошла ошибка. Попробуйте еще раз.",
    "success": "✅ Успешно!",
    
    # Выбор языка
    "uzbek": "🇺🇿 O'zbek",
    "russian": "🇷🇺 Русский",
    
    # Главное меню
    "main_menu": "🏠 Главное меню",
    "choose_role": "🎭 Выберите роль:",
    "employer": "👔 Работодатель",
    "jobseeker": "👤 Соискатель",
    "admin_panel": "⚙️ Админ панель",
    
    # Меню работодателя
    "employer_menu": "👔 Меню работодателя",
    "create_vacancy": "➕ Создать вакансию",
    "my_vacancies": "📋 Мои вакансии",
    "applications": "📬 Заявки",
    "my_companies": "🏢 Мои компании",
    
    # Создание вакансии
    "creating_vacancy": "📝 Создание вакансии\n\nПроцесс состоит из нескольких этапов:",
    "company_name": "🏢 Введите название компании:",
    "company_description": "📄 Введите описание компании:",
    "vacancy_title": "📌 Введите название вакансии:",
    "vacancy_description": "📝 Введите описание вакансии:",
    "vacancy_requirements": "📋 Введите требования:",
    "vacancy_responsibilities": "⚡ Введите обязанности:",
    "salary_range": "💰 Введите диапазон зарплаты (например: 5000000-8000000) или напишите 'Договорная':",
    "work_hours": "🕒 Введите рабочие часы (например: 9:00-18:00):",
    "work_days": "📅 Введите рабочие дни (например: Понедельник-Пятница):",
    "work_location": "📍 Введите место работы:",
    
    # AI критерии
    "ai_criteria": "🤖 Критерии для анализа резюме\n\nИИ будет анализировать резюме по следующим критериям:",
    "criteria_skills": "💻 Какие навыки должны быть? (разделите запятыми):",
    "criteria_experience": "📈 Сколько лет опыта требуется?",
    "criteria_education": "🎓 Уровень образования (бакалавр, магистр и т.д.):",
    "criteria_languages": "🌍 Какие языки должен знать?",
    "criteria_additional": "➕ Дополнительные критерии:",
    
    # Вопросы интервью
    "interview_questions": "❓ Вопросы собеседования\n\nСколько вопросов задать? (от 1 до 5):",
    "question_prompt": "❓ {}-й вопрос:",
    "questions_saved": "✅ Вопросы сохранены!",
    
    # Завершение вакансии
    "vacancy_created": "🎉 Вакансия успешно создана!\n\n📌 Название: {}\n🏢 Компания: {}\n📅 Дата: {}",
    "vacancy_preview": "👀 Предварительный просмотр вакансии:\n\n📌 Название: {}\n🏢 Компания: {}\n📝 Описание: {}\n📋 Требования: {}\n💰 Зарплата: {}\n📍 Место: {}",
    
    # Список вакансий
    "no_vacancies": "📭 У вас пока нет вакансий.",
    "vacancy_list": "📋 Список вакансий:",
    "vacancy_status_active": "🟢 Активная",
    "vacancy_status_archived": "🔴 Архивирована",
    "archive_vacancy": "📦 Архивировать",
    "activate_vacancy": "🔄 Активировать",
    
    # Заявки
    "no_applications": "📭 Заявки пока не поступали.",
    "applications_list": "📬 Список заявок:",
    "application_from": "👤 Заявитель: {}",
    "application_date": "📅 Дата: {}",
    "application_vacancy": "📌 Вакансия: {}",
    "application_status": "📊 Статус: {}",
    "view_application": "👁️ Посмотреть",
    "download_resume": "📄 Скачать резюме",
    
    # Меню соискателя
    "jobseeker_menu": "👤 Меню соискателя",
    "find_jobs": "🔍 Поиск работы",
    "my_applications": "📨 Мои заявки",
    
    # Поиск работы
    "select_company": "🏢 Выберите компанию:",
    "no_companies": "🏢 Компании пока отсутствуют.",
    "select_vacancy": "📌 Выберите вакансию:",
    "no_active_vacancies": "📭 В этой компании нет активных вакансий.",
    
    # Просмотр вакансии
    "vacancy_details": """📌 Вакансия: {}
🏢 Компания: {}
📝 Описание: {}
📋 Требования: {}
⚡ Обязанности: {}
💰 Зарплата: {}
🕒 Рабочие часы: {}
📅 Рабочие дни: {}
📍 Место работы: {}""",
    "apply_now": "🚀 Подать заявку",
    "already_applied": "✅ Вы уже подали заявку на эту вакансию",
    
    # Загрузка резюме
    "upload_resume": "📄 Отправьте файл резюме (в формате PDF или DOC):",
    "invalid_file": "❌ Неверный формат файла. Принимаются только PDF или DOC файлы.",
    "file_too_large": "❌ Файл слишком большой. Максимальный размер 10MB.",
    "resume_uploaded": "✅ Резюме загружено!",
    
    # AI анализ
    "analyzing_resume": "🔍 Анализ резюме...",
    "ai_analyzing": "🤖 ИИ анализирует, немного подождите...",
    "match_percentage": "📊 Процент соответствия: {}%",
    "match_too_low": """❌ К сожалению, резюме не соответствует требованиям вакансии.
    
📊 Процент соответствия: {}%
🎯 Минимальный процент: 60%

💡 Хотите подать заявку на другие вакансии?""",
    
    "match_good": """✅ Резюме соответствует требованиям вакансии!
    
📊 Процент соответствия: {}%

🎤 Теперь вам будет задано несколько вопросов. Если готовы, нажмите 'Продолжить'.""",
    
    "continue": "➡️ Продолжить",
    
    # Вопросы собеседования
    "interview_started": "🎤 Собеседование началось!\n\nВопрос {} из {}:",
    "question": "❓ {}",
    "answer_question": "💬 Напишите свой ответ:",
    "next_question": "➡️ Следующий вопрос",
    "interview_completed": "✅ Собеседование завершено!",
    
    # Результаты собеседования
    "evaluating_answers": "🤖 Оценка ответов...",
    "interview_success": """🎉 Поздравляем! Собеседование прошло успешно!
    
📊 Общий балл: {} / 100
✅ Ждем вас на следующем этапе.

📞 Работодатель скоро свяжется с вами.""",
    
    "interview_failed": """😔 К сожалению, на этот раз вы не прошли отбор.
    
📊 Общий балл: {} / 100
🎯 Минимальный балл: 70

💡 Продолжайте подавать заявки на другие вакансии!""",
    
    # Дополнительная информация
    "additional_info": "📝 Требуется дополнительная информация:",
    "full_name": "👤 Введите ваше полное имя:",
    "age": "🎂 Введите ваш возраст:",
    "phone_number": "📞 Введите номер телефона:",
    "email": "📧 Введите email адрес:",
    "address": "📍 Введите адрес проживания:",
    "info_saved": "✅ Информация сохранена и отправлена работодателю!",
    
    # Админ панель
    "admin_menu": "⚙️ Админ Панель",
    "analytics": "📊 Аналитика",
    "system_stats": "📈 Системная статистика",
    
    # Аналитика
    "analytics_data": """📊 Системная аналитика:
    
👥 Пользователи:
• Всего: {}
• Работодатели: {}
• Соискатели: {}

📋 Вакансии:
• Всего: {}
• Активные: {}
• Архивированные: {}

📨 Заявки:
• Всего: {}
• Принятые: {}
• Отклоненные: {}

📅 Сегодня: {}""",
    
    # Ошибки
    "session_expired": "⏰ Сессия истекла. Начните заново.",
    "access_denied": "🚫 Доступ запрещен.",
    "invalid_command": "❌ Неверная команда.",
    "processing": "⏳ Обработка...",
    "please_wait": "⏳ Пожалуйста, подождите...",
    
    # Кнопки
    "btn_uzbek": "🇺🇿 O'zbek",
    "btn_russian": "🇷🇺 Русский",
    "btn_employer": "👔 Работодатель",
    "btn_jobseeker": "👤 Соискатель",
    "btn_back": "🔙 Назад",
    "btn_cancel": "❌ Отмена",
    "btn_continue": "➡️ Продолжить",
    "btn_save": "💾 Сохранить",
    "btn_apply": "🚀 Подать заявку",
    "btn_view": "👁️ Посмотреть",
    "btn_download": "📥 Скачать",
    "btn_archive": "📦 Архивировать",
    "btn_activate": "🔄 Активировать",
    "btn_yes": "✅ Да",
    "btn_no": "❌ Нет",
}

import aiogram

def get_text(key, language="uz", **kwargs):
    """Belgilangan tilda matnni qaytaradi"""
    texts = UZ_TEXTS if language == Languages.UZ else RU_TEXTS
    text = texts.get(key, f"[{key}]")
    
    if kwargs:
        try:
            return text.format(**kwargs)
        except:
            return text
    return text

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu_keyboard(language="uz"):
    """Asosiy menyu tugmalari"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            # [InlineKeyboardButton(text=get_text("btn_employer", language), callback_data="role_employer")],
            [InlineKeyboardButton(text=get_text("btn_jobseeker", language), callback_data="role_jobseeker")]
        ]
    )


def get_back_keyboard(language="uz"):
    """Orqaga tugmasi"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=get_text("btn_back", language), callback_data="back_main")]
        ]
    )


def get_cancel_keyboard(language="uz"):
    """Bekor qilish tugmasi"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=get_text("btn_cancel", language), callback_data="cancel")]
        ]
    )


def get_language_keyboard():
    """Til tanlash tugmalari"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data="lang_uz"),
             InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")]
        ]
    )