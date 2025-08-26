# # -*- coding: utf-8 -*-

# import json
# from aiogram import Router, F
# from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.filters import StateFilter
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# from utils.language import get_text

# # Employer holatlari
# class EmployerStates(StatesGroup):
#     CREATING_COMPANY_NAME = State()
#     CREATING_COMPANY_DESC = State()
#     CREATING_VACANCY_TITLE = State()
#     CREATING_VACANCY_DESC = State()
#     CREATING_VACANCY_REQ = State()
#     CREATING_VACANCY_RESP = State()
#     CREATING_SALARY = State()
#     CREATING_WORK_HOURS = State()
#     CREATING_WORK_DAYS = State()
#     CREATING_WORK_LOCATION = State()
#     CREATING_CRITERIA_SKILLS = State()
#     CREATING_CRITERIA_EXP = State()
#     CREATING_CRITERIA_EDU = State()
#     CREATING_CRITERIA_LANG = State()
#     CREATING_CRITERIA_ADD = State()
#     CREATING_QUESTIONS = State()

# class EmployerHandlers:
#     def __init__(self, bot, db, ai_service, file_service):
#         self.bot = bot
#         self.db = db
#         self.ai_service = ai_service
#         self.file_service = file_service
#         self.router = Router()
        
#         # Handlerlarni ro'yxatga olish
#         self.register_handlers()
    
#     def get_user_language(self, user_id: int) -> str:
#         """Foydalanuvchi tilini olish"""
#         user = self.db.get_user_by_telegram_id(user_id)
#         return user['language'] if user else 'uz'
    
#     def register_handlers(self):
#         """Employer handlerlarini ro'yxatga olish"""
        
#         # Employer callback handlerni ro'yxatga olish
#         @self.router.callback_query(F.data.startswith('employer_'))
#         async def employer_callbacks(callback: CallbackQuery, state: FSMContext):
#             """Employer callback handleri"""
#             try:
#                 action = callback.data.replace('employer_', '')
#                 user_id = callback.from_user.id
#                 language = self.get_user_language(user_id)
                
#                 if action == 'create_vacancy':
#                     await self.start_vacancy_creation(callback, state, language)
#                 elif action == 'vacancies':
#                     await self.show_my_vacancies(callback.message.chat.id, user_id, language)
#                 elif action == 'applications':
#                     await self.show_applications(callback.message.chat.id, user_id, language)
                
#                 await callback.answer()
                
#             except Exception as e:
#                 print(f"Employer callback xatoligi: {e}")
#                 await callback.answer(get_text("error", "uz"))
        
#         # Vakansiya yaratish bo'yicha message handlerlar
#         @self.router.message(StateFilter(EmployerStates.CREATING_COMPANY_NAME))
#         async def handle_company_name(message: Message, state: FSMContext):
#             await self.handle_company_name(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_COMPANY_DESC))
#         async def handle_company_description(message: Message, state: FSMContext):
#             await self.handle_company_description(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_VACANCY_TITLE))
#         async def handle_vacancy_title(message: Message, state: FSMContext):
#             await self.handle_vacancy_title(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_VACANCY_DESC))
#         async def handle_vacancy_description(message: Message, state: FSMContext):
#             await self.handle_vacancy_description(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_VACANCY_REQ))
#         async def handle_vacancy_requirements(message: Message, state: FSMContext):
#             await self.handle_vacancy_requirements(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_VACANCY_RESP))
#         async def handle_vacancy_responsibilities(message: Message, state: FSMContext):
#             await self.handle_vacancy_responsibilities(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_SALARY))
#         async def handle_salary_range(message: Message, state: FSMContext):
#             await self.handle_salary_range(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_WORK_HOURS))
#         async def handle_work_hours(message: Message, state: FSMContext):
#             await self.handle_work_hours(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_WORK_DAYS))
#         async def handle_work_days(message: Message, state: FSMContext):
#             await self.handle_work_days(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_WORK_LOCATION))
#         async def handle_work_location(message: Message, state: FSMContext):
#             await self.handle_work_location(message, state)
        
#         # Kriteriya handlerlar
#         @self.router.message(StateFilter(EmployerStates.CREATING_CRITERIA_SKILLS))
#         async def handle_criteria_skills(message: Message, state: FSMContext):
#             await self.handle_criteria_skills(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_CRITERIA_EXP))
#         async def handle_criteria_experience(message: Message, state: FSMContext):
#             await self.handle_criteria_experience(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_CRITERIA_EDU))
#         async def handle_criteria_education(message: Message, state: FSMContext):
#             await self.handle_criteria_education(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_CRITERIA_LANG))
#         async def handle_criteria_languages(message: Message, state: FSMContext):
#             await self.handle_criteria_languages(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_CRITERIA_ADD))
#         async def handle_criteria_additional(message: Message, state: FSMContext):
#             await self.handle_criteria_additional(message, state)
        
#         @self.router.message(StateFilter(EmployerStates.CREATING_QUESTIONS))
#         async def handle_question_input(message: Message, state: FSMContext):
#             await self.handle_question_input(message, state)
        
#         # Savollar soni tanlash
#         @self.router.callback_query(F.data.startswith('questions_count_'))
#         async def questions_count_callback(callback: CallbackQuery, state: FSMContext):
#             await self.handle_questions_count_callback(callback, state)
        
#         # Vakansiya ko'rish va boshqarish
#         @self.router.callback_query(F.data.startswith('view_vacancy_'))
#         async def view_vacancy_callback(callback: CallbackQuery):
#             await self.view_vacancy_callback(callback)
        
#         # Vakansiya arxivlash/faollashtirish
#         @self.router.callback_query(F.data.startswith('archive_vacancy_'))
#         async def archive_vacancy_callback(callback: CallbackQuery):
#             await self.archive_vacancy_callback(callback)
        
#         @self.router.callback_query(F.data.startswith('activate_vacancy_'))
#         async def activate_vacancy_callback(callback: CallbackQuery):
#             await self.activate_vacancy_callback(callback)
        
#         # Arizalarni ko'rish
#         @self.router.callback_query(F.data.startswith('view_application_'))
#         async def view_application_callback(callback: CallbackQuery):
#             await self.view_application_callback(callback)
        
#         # Bekor qilish
#         @self.router.callback_query(F.data == 'cancel_vacancy')
#         async def cancel_vacancy(callback: CallbackQuery, state: FSMContext):
#             await state.clear()
#             language = self.get_user_language(callback.from_user.id)
#             await self.show_employer_menu(callback.message.chat.id, language)
#             await callback.answer()
    
#     async def start_vacancy_creation(self, callback: CallbackQuery, state: FSMContext, language: str):
#         """Vakansiya yaratishni boshlash"""
#         try:
#             # State o'rnatish
#             await state.set_state(EmployerStates.CREATING_COMPANY_NAME)
            
#             # Birinchi savol
#             text = get_text("creating_vacancy", language) + "\n\n"
#             text += get_text("company_name", language)
            
#             keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                 [
#                     InlineKeyboardButton(
#                         text=get_text("btn_cancel", language), 
#                         callback_data="cancel_vacancy"
#                     )
#                 ]
#             ])
            
#             await callback.message.edit_text(text, reply_markup=keyboard)
            
#         except Exception as e:
#             print(f"Vakansiya yaratishni boshlash xatoligi: {e}")
    
#     async def handle_company_name(self, message: Message, state: FSMContext):
#         """Kompaniya nomini qayta ishlash"""
#         try:
#             company_name = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             if len(company_name) < 2:
#                 await message.reply("❌ Kompaniya nomi juda qisqa!")
#                 return
            
#             # Ma'lumotni saqlash
#             await state.update_data(company_name=company_name)
#             await state.set_state(EmployerStates.CREATING_COMPANY_DESC)
            
#             # Keyingi savol
#             text = get_text("company_description", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Kompaniya nomi xatoligi: {e}")
    
#     async def handle_company_description(self, message: Message, state: FSMContext):
#         """Kompaniya tavsifini qayta ishlash"""
#         try:
#             company_description = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(company_description=company_description)
#             await state.set_state(EmployerStates.CREATING_VACANCY_TITLE)
            
#             # Keyingi savol
#             text = get_text("vacancy_title", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Kompaniya tavsifi xatoligi: {e}")
    
#     async def handle_vacancy_title(self, message: Message, state: FSMContext):
#         """Vakansiya nomini qayta ishlash"""
#         try:
#             vacancy_title = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             if len(vacancy_title) < 3:
#                 await message.reply("❌ Vakansiya nomi juda qisqa!")
#                 return
            
#             # Ma'lumotni saqlash
#             await state.update_data(vacancy_title=vacancy_title)
#             await state.set_state(EmployerStates.CREATING_VACANCY_DESC)
            
#             # Keyingi savol
#             text = get_text("vacancy_description", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Vakansiya nomi xatoligi: {e}")
    
#     async def handle_vacancy_description(self, message: Message, state: FSMContext):
#         """Vakansiya tavsifini qayta ishlash"""
#         try:
#             vacancy_description = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(vacancy_description=vacancy_description)
#             await state.set_state(EmployerStates.CREATING_VACANCY_REQ)
            
#             # Keyingi savol
#             text = get_text("vacancy_requirements", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Vakansiya tavsifi xatoligi: {e}")
    
#     async def handle_vacancy_requirements(self, message: Message, state: FSMContext):
#         """Vakansiya talablarini qayta ishlash"""
#         try:
#             requirements = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(requirements=requirements)
#             await state.set_state(EmployerStates.CREATING_VACANCY_RESP)
            
#             # Keyingi savol
#             text = get_text("vacancy_responsibilities", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Vakansiya talablari xatoligi: {e}")
    
#     async def handle_vacancy_responsibilities(self, message: Message, state: FSMContext):
#         """Vakansiya majburiyatlarini qayta ishlash"""
#         try:
#             responsibilities = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(responsibilities=responsibilities)
#             await state.set_state(EmployerStates.CREATING_SALARY)
            
#             # Keyingi savol
#             text = get_text("salary_range", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Vakansiya majburiyatlari xatoligi: {e}")
    
#     async def handle_salary_range(self, message: Message, state: FSMContext):
#         """Ish haqqi oralig'ini qayta ishlash"""
#         try:
#             salary_text = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(salary_range=salary_text)
#             await state.set_state(EmployerStates.CREATING_WORK_HOURS)
            
#             # Keyingi savol
#             text = get_text("work_hours", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Ish haqqi xatoligi: {e}")
    
#     async def handle_work_hours(self, message: Message, state: FSMContext):
#         """Ish soatlarini qayta ishlash"""
#         try:
#             work_hours = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(work_hours=work_hours)
#             await state.set_state(EmployerStates.CREATING_WORK_DAYS)
            
#             # Keyingi savol
#             text = get_text("work_days", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Ish soatlari xatoligi: {e}")
    
#     async def handle_work_days(self, message: Message, state: FSMContext):
#         """Ish kunlarini qayta ishlash"""
#         try:
#             work_days = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(work_days=work_days)
#             await state.set_state(EmployerStates.CREATING_WORK_LOCATION)
            
#             # Keyingi savol
#             text = get_text("work_location", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Ish kunlari xatoligi: {e}")
    
#     async def handle_work_location(self, message: Message, state: FSMContext):
#         """Ish joyini qayta ishlash"""
#         try:
#             work_location = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(work_location=work_location)
#             await state.set_state(EmployerStates.CREATING_CRITERIA_SKILLS)
            
#             # AI kriteriylarga o'tish
#             text = get_text("ai_criteria", language) + "\n\n"
#             text += get_text("criteria_skills", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Ish joyi xatoligi: {e}")
    
#     async def handle_criteria_skills(self, message: Message, state: FSMContext):
#         """Ko'nikmalar kriteriyasini qayta ishlash"""
#         try:
#             skills = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(criteria_skills=skills)
#             await state.set_state(EmployerStates.CREATING_CRITERIA_EXP)
            
#             # Keyingi savol
#             text = get_text("criteria_experience", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Ko'nikmalar kriteriyas xatoligi: {e}")
    
#     async def handle_criteria_experience(self, message: Message, state: FSMContext):
#         """Tajriba kriteriyasini qayta ishlash"""
#         try:
#             experience = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(criteria_experience=experience)
#             await state.set_state(EmployerStates.CREATING_CRITERIA_EDU)
            
#             # Keyingi savol
#             text = get_text("criteria_education", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Tajriba kriteriyasi xatoligi: {e}")
    
#     async def handle_criteria_education(self, message: Message, state: FSMContext):
#         """Ta'lim kriteriyasini qayta ishlash"""
#         try:
#             education = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(criteria_education=education)
#             await state.set_state(EmployerStates.CREATING_CRITERIA_LANG)
            
#             # Keyingi savol
#             text = get_text("criteria_languages", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Ta'lim kriteriyasi xatoligi: {e}")
    
#     async def handle_criteria_languages(self, message: Message, state: FSMContext):
#         """Tillar kriteriyasini qayta ishlash"""
#         try:
#             languages_req = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(criteria_languages=languages_req)
#             await state.set_state(EmployerStates.CREATING_CRITERIA_ADD)
            
#             # Keyingi savol
#             text = get_text("criteria_additional", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Tillar kriteriyasi xatoligi: {e}")
    
#     async def handle_criteria_additional(self, message: Message, state: FSMContext):
#         """Qo'shimcha kriteriyalarni qayta ishlash"""
#         try:
#             additional = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(criteria_additional=additional)
            
#             # Savollar sonini so'rash
#             text = get_text("interview_questions", language)
            
#             keyboard = InlineKeyboardMarkup(inline_keyboard=[])
#             for i in range(1, 6):  # 1-5 gacha savollar
#                 keyboard.inline_keyboard.append([
#                     InlineKeyboardButton(
#                         text=f"{i} ta savol", 
#                         callback_data=f"questions_count_{i}"
#                     )
#                 ])
            
#             await message.answer(text, reply_markup=keyboard)
            
#         except Exception as e:
#             print(f"Qo'shimcha kriteriyalar xatoligi: {e}")
    
#     async def handle_questions_count_callback(self, callback: CallbackQuery, state: FSMContext):
#         """Savollar sonini callback orqali qayta ishlash"""
#         try:
#             questions_count = int(callback.data.split('_')[2])  # questions_count_3 -> 3
#             language = self.get_user_language(callback.from_user.id)
            
#             # Ma'lumotni saqlash
#             await state.update_data(
#                 questions_count=questions_count,
#                 questions=[],
#                 current_question=1
#             )
#             await state.set_state(EmployerStates.CREATING_QUESTIONS)
            
#             # Birinchi savolni so'rash
#             text = get_text("question_prompt", language).format(1)
#             await callback.message.edit_text(text)
#             await callback.answer()
            
#         except Exception as e:
#             print(f"Savollar soni callback xatoligi: {e}")
    
#     async def handle_question_input(self, message: Message, state: FSMContext):
#         """Savol matnini qayta ishlash"""
#         try:
#             question_text = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             if len(question_text) < 5:
#                 await message.reply("❌ Savol juda qisqa!")
#                 return
            
#             # Mavjud ma'lumotlarni olish
#             data = await state.get_data()
#             questions = data.get('questions', [])
#             questions_count = data.get('questions_count', 3)
#             current_question = data.get('current_question', 1)
            
#             # Savolni qo'shish
#             questions.append(question_text)
            
#             if len(questions) < questions_count:
#                 # Keyingi savol
#                 current_question += 1
#                 await state.update_data(
#                     questions=questions,
#                     current_question=current_question
#                 )
                
#                 text = get_text("question_prompt", language).format(current_question)
#                 await message.answer(text)
#             else:
#                 # Barcha savollar tugadi - vakansiyani saqlash
#                 await state.update_data(questions=questions)
#                 await self.complete_vacancy_creation(message, state, language)
            
#         except Exception as e:
#             print(f"Savol kiritish xatoligi: {e}")
    
#     async def complete_vacancy_creation(self, message: Message, state: FSMContext, language: str):
#         """Vakansiya yaratishni yakunlash"""
#         try:
#             data = await state.get_data()
#             user_id = message.from_user.id
            
#             # Avval kompaniyani yaratish yoki topish
#             user = self.db.get_user_by_telegram_id(user_id)
#             company_id = self.db.create_company(
#                 data['company_name'],
#                 data['company_description'],
#                 user['id']
#             )
            
#             # Kriteriyalarni formatlash
#             criteria = {
#                 'skills': data.get('criteria_skills', ''),
#                 'experience': data.get('criteria_experience', ''),
#                 'education': data.get('criteria_education', ''),
#                 'languages': data.get('criteria_languages', ''),
#                 'additional': data.get('criteria_additional', '')
#             }
            
#             # Vakansiyani yaratish
#             vacancy_data = {
#                 'company_id': company_id,
#                 'employer_id': user['id'],
#                 'title': data['vacancy_title'],
#                 'description': data['vacancy_description'],
#                 'requirements': data['requirements'],
#                 'responsibilities': data['responsibilities'],
#                 'salary_from': None,  # Keyinchalik parse qilish
#                 'salary_to': None,
#                 'work_hours': data['work_hours'],
#                 'work_days': data['work_days'],
#                 'location': data['work_location'],
#                 'criteria': criteria,
#                 'questions': data['questions']
#             }
            
#             vacancy_id = self.db.create_vacancy(vacancy_data)
            
#             # State ni tozalash
#             await state.clear()
            
#             # Muvaffaqiyat xabari
#             from datetime import datetime
#             text = get_text("vacancy_created", language).format(
#                 data['vacancy_title'],
#                 data['company_name'],
#                 datetime.now().strftime("%d.%m.%Y")
#             )
            
#             keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                 [
#                     InlineKeyboardButton(
#                         text=get_text("my_vacancies", language),
#                         callback_data="employer_vacancies"
#                     )
#                 ],
#                 [
#                     InlineKeyboardButton(
#                         text=get_text("btn_back", language),
#                         callback_data="back_main"
#                     )
#                 ]
#             ])
            
#             await message.answer(text, reply_markup=keyboard)
            
#         except Exception as e:
#             print(f"Vakansiya yaratishni yakunlash xatoligi: {e}")
#             await message.answer(get_text("error", language))
    
#     async def show_my_vacancies(self, chat_id: int, user_id: int, language: str):
#         """Mening vakansiyalarimni ko'rsatish"""
#         try:
#             user = self.db.get_user_by_telegram_id(user_id)
#             companies = self.db.get_companies_by_employer(user['id'])
            
#             if not companies:
#                 text = get_text("no_vacancies", language)
#                 keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                     [
#                         InlineKeyboardButton(
#                             text=get_text("create_vacancy", language),
#                             callback_data="employer_create_vacancy"
#                         )
#                     ]
#                 ])
#                 await self.bot.send_message(chat_id, text, reply_markup=keyboard)
#                 return
            
#             text = get_text("vacancy_list", language) + "\n\n"
#             keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
#             for company in companies:
#                 vacancies = self.db.get_vacancies_by_company(company['id'])
#                 if vacancies:
#                     for vacancy in vacancies:
#                         status_text = get_text("vacancy_status_active", language) if vacancy['status'] == 'active' else get_text("vacancy_status_archived", language)
#                         button_text = f"{vacancy['title']} ({status_text})"
#                         keyboard.inline_keyboard.append([
#                             InlineKeyboardButton(
#                                 text=button_text,
#                                 callback_data=f"view_vacancy_{vacancy['id']}"
#                             )
#                         ])
            
#             keyboard.inline_keyboard.append([
#                 InlineKeyboardButton(
#                     text=get_text("btn_back", language),
#                     callback_data="back_main"
#                 )
#             ])
            
#             await self.bot.send_message(chat_id, text, reply_markup=keyboard)
            
#         except Exception as e:
#             print(f"Vakansiyalar ro'yxati xatoligi: {e}")
    
#     async def show_applications(self, chat_id: int, user_id: int, language: str):
#         """Kelgan arizalarni ko'rsatish"""
#         try:
#             user = self.db.get_user_by_telegram_id(user_id)
#             applications = self.db.get_applications_for_employer(user['id'])
            
#             if not applications:
#                 text = get_text("no_applications", language)
#                 await self.bot.send_message(chat_id, text)
#                 return
            
#             text = get_text("applications_list", language) + "\n\n"
#             keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
#             for app in applications:
#                 button_text = f"{app['vacancy_title']} - {app['first_name'] or app['username']}"
#                 keyboard.inline_keyboard.append([
#                     InlineKeyboardButton(
#                         text=button_text,
#                         callback_data=f"view_application_{app['id']}"
#                     )
#                 ])
            
#             keyboard.inline_keyboard.append([
#                 InlineKeyboardButton(
#                     text=get_text("btn_back", language),
#                     callback_data="back_main"
#                 )
#             ])
            
#             await self.bot.send_message(chat_id, text, reply_markup=keyboard)
            
#         except Exception as e:
#             print(f"Arizalar ro'yxati xatoligi: {e}")
    
#     async def view_vacancy_callback(self, callback: CallbackQuery):
#         """Vakansiyani ko'rish callback"""
#         try:
#             vacancy_id = int(callback.data.split('_')[2])  # view_vacancy_123 -> 123
#             language = self.get_user_language(callback.from_user.id)
            
#             vacancy = self.db.get_vacancy_by_id(vacancy_id)
#             if not vacancy:
#                 await callback.answer("Vakansiya topilmadi!")
#                 return
            
#             # Vakansiya ma'lumotlarini ko'rsatish
#             text = get_text("vacancy_details", language).format(
#                 vacancy['title'],
#                 vacancy.get('company_name', 'N/A'),  # Kompaniya nomini qo'shish kerak
#                 vacancy['description'],
#                 vacancy['requirements'],
#                 vacancy['responsibilities'],
#                 vacancy.get('salary_range', 'N/A'),
#                 vacancy.get('work_hours', 'N/A'),
#                 vacancy.get('work_days', 'N/A'),
#                 vacancy.get('location', 'N/A')
#             )
            
#             # Boshqaruv tugmalari
#             keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
#             if vacancy['status'] == 'active':
#                 keyboard.inline_keyboard.append([
#                     InlineKeyboardButton(
#                         text=get_text("archive_vacancy", language),
#                         callback_data=f"archive_vacancy_{vacancy_id}"
#                     )
#                 ])
#             else:
#                 keyboard.inline_keyboard.append([
#                     InlineKeyboardButton(
#                         text=get_text("activate_vacancy", language),
#                         callback_data=f"activate_vacancy_{vacancy_id}"
#                     )
#                 ])
            
#             keyboard.inline_keyboard.append([
#                 InlineKeyboardButton(
#                     text=get_text("btn_back", language),
#                     callback_data="employer_vacancies"
#                 )
#             ])
            
#             await callback.message.edit_text(text, reply_markup=keyboard)
#             await callback.answer()
            
#         except Exception as e:
#             print(f"Vakansiyani ko'rish xatoligi: {e}")
#             await callback.answer("Xatolik yuz berdi!")
    
#     async def archive_vacancy_callback(self, callback: CallbackQuery):
#         """Vakansiyani arxivlash"""
#         try:
#             vacancy_id = int(callback.data.split('_')[2])
#             language = self.get_user_language(callback.from_user.id)
            
#             self.db.update_vacancy_status(vacancy_id, 'archived')
            
#             await callback.answer("✅ Vakansiya arxivlandi!")
#             # Vakansiyani qaytadan ko'rsatish
#             await self.view_vacancy_callback(callback)
            
#         except Exception as e:
#             print(f"Vakansiyani arxivlash xatoligi: {e}")
#             await callback.answer("Xatolik yuz berdi!")
    
#     async def activate_vacancy_callback(self, callback: CallbackQuery):
#         """Vakansiyani faollashtirish"""
#         try:
#             vacancy_id = int(callback.data.split('_')[2])
#             language = self.get_user_language(callback.from_user.id)
            
#             self.db.update_vacancy_status(vacancy_id, 'active')
            
#             await callback.answer("✅ Vakansiya faollashtirildi!")
#             # Vakansiyani qaytadan ko'rsatish
#             await self.view_vacancy_callback(callback)
            
#         except Exception as e:
#             print(f"Vakansiyani faollashtirish xatoligi: {e}")
#             await callback.answer("Xatolik yuz berdi!")
    
#     async def view_application_callback(self, callback: CallbackQuery):
#         """Arizani ko'rish"""
#         try:
#             application_id = int(callback.data.split('_')[2])
#             language = self.get_user_language(callback.from_user.id)
            
#             # Application ma'lumotlarini olish (keyinchalik implement qilamiz)
#             await callback.answer("Bu funksiya hali ishlab chiqilmoqda!")
            
#         except Exception as e:
#             print(f"Arizani ko'rish xatoligi: {e}")
#             await callback.answer("Xatolik yuz berdi!")
    
#     async def show_employer_menu(self, chat_id: int, language: str):
#         """Employer menyusini ko'rsatish"""
#         try:
#             text = get_text("employer_menu", language)
#             keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                 [
#                     InlineKeyboardButton(
#                         text=get_text("create_vacancy", language), 
#                         callback_data="employer_create_vacancy"
#                     )
#                 ],
#                 [
#                     InlineKeyboardButton(
#                         text=get_text("my_vacancies", language), 
#                         callback_data="employer_vacancies"
#                     )
#                 ],
#                 [
#                     InlineKeyboardButton(
#                         text=get_text("applications", language), 
#                         callback_data="employer_applications"
#                     )
#                 ],
#                 [
#                     InlineKeyboardButton(
#                         text=get_text("btn_back", language), 
#                         callback_data="back_main"
#                     )
#                 ]
#             ])
            
#             await self.bot.send_message(chat_id, text, reply_markup=keyboard)
            
#         except Exception as e:
#             print(f"Employer menyu xatoligi: {e}")
            
# -*- coding: utf-8 -*-

import json
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List

# Aiogram imports
from aiogram import Router, F
from aiogram.types import (
    CallbackQuery, Message, InlineKeyboardMarkup, 
    InlineKeyboardButton, FSInputFile
)
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Local imports
from utils.languages import get_text
from config import Config

# Logger
logger = logging.getLogger(__name__)

# ===========================================
# EMPLOYER STATES - Yangi Database uchun
# ===========================================

class EmployerStates(StatesGroup):
    """Ish beruvchi holatlari - Vakansiya yaratish jarayoni"""
    
    # Kompaniya ma'lumotlari
    COMPANY_NAME = State()
    COMPANY_DESCRIPTION = State()
    COMPANY_WEBSITE = State()
    COMPANY_LOCATION = State()
    
    # Vakansiya asosiy ma'lumotlari
    VACANCY_TITLE = State()
    VACANCY_DESCRIPTION = State()
    VACANCY_REQUIREMENTS = State()
    VACANCY_RESPONSIBILITIES = State()
    
    # Ish sharoitlari
    WORK_TYPE = State()          # remote, office, hybrid
    WORK_SCHEDULE = State()      # full-time, part-time, contract
    SALARY_RANGE = State()
    LOCATION = State()
    EXPERIENCE_YEARS = State()
    
    # AI Kriteriya va Prompt
    AI_CRITERIA_SKILLS = State()
    AI_CRITERIA_EXPERIENCE = State()
    AI_CRITERIA_EDUCATION = State()
    AI_CRITERIA_LANGUAGES = State()
    AI_CRITERIA_ADDITIONAL = State()
    AI_PROMPT_CREATION = State()
    
    # Interview savollari
    INTERVIEW_QUESTIONS_COUNT = State()
    INTERVIEW_QUESTIONS_INPUT = State()
    
    # Yakuniy tasdiqlash
    FINAL_CONFIRMATION = State()

# ===========================================
# EMPLOYER HANDLERS CLASS
# ===========================================

class EmployerHandlers:
    """Ish beruvchi handlerlari - Professional version"""
    
    def __init__(self, bot, crud, ai_service, file_service):
        self.bot = bot
        self.crud = crud
        self.ai_service = ai_service
        self.file_service = file_service
        self.router = Router()
        
        # Handlerlarni ro'yxatga olish
        self.register_handlers()
    
    def get_user_language(self, user_id: int) -> str:
        """Foydalanuvchi tilini olish"""
        try:
            user = self.crud['user'].get_user_by_telegram_id(user_id)
            return user.get('language_code', Config.DEFAULT_LANGUAGE) if user else Config.DEFAULT_LANGUAGE
        except Exception as e:
            logger.error(f"Til olishda xatolik: {e}")
            return Config.DEFAULT_LANGUAGE
    
    def get_user_by_telegram_id(self, telegram_id: int) -> Optional[Dict[str, Any]]:
        """Foydalanuvchini telegram ID orqali olish"""
        try:
            return self.crud['user'].get_user_by_telegram_id(telegram_id)
        except Exception as e:
            logger.error(f"Foydalanuvchi olishda xatolik: {e}")
            return None
    
    # ===========================================
    # HANDLERS REGISTRATION
    # ===========================================
    
    def register_handlers(self):
        """Barcha handlerlarni ro'yxatga olish"""
        
        # Employer callback handlers
        @self.router.callback_query(F.data.startswith('employer_'))
        async def employer_callbacks(callback: CallbackQuery, state: FSMContext):
            await self.handle_employer_callbacks(callback, state)
        
        # Vakansiya yaratish - Message handlers
        # Kompaniya ma'lumotlari
        @self.router.message(StateFilter(EmployerStates.COMPANY_NAME))
        async def handle_company_name(message: Message, state: FSMContext):
            await self.handle_company_name(message, state)
        
        @self.router.message(StateFilter(EmployerStates.COMPANY_DESCRIPTION))
        async def handle_company_description(message: Message, state: FSMContext):
            await self.handle_company_description(message, state)
        
        @self.router.message(StateFilter(EmployerStates.COMPANY_WEBSITE))
        async def handle_company_website(message: Message, state: FSMContext):
            await self.handle_company_website(message, state)
        
        @self.router.message(StateFilter(EmployerStates.COMPANY_LOCATION))
        async def handle_company_location(message: Message, state: FSMContext):
            await self.handle_company_location(message, state)
        
        # Vakansiya ma'lumotlari
        @self.router.message(StateFilter(EmployerStates.VACANCY_TITLE))
        async def handle_vacancy_title(message: Message, state: FSMContext):
            await self.handle_vacancy_title(message, state)
        
        @self.router.message(StateFilter(EmployerStates.VACANCY_DESCRIPTION))
        async def handle_vacancy_description(message: Message, state: FSMContext):
            await self.handle_vacancy_description(message, state)
        
        @self.router.message(StateFilter(EmployerStates.VACANCY_REQUIREMENTS))
        async def handle_vacancy_requirements(message: Message, state: FSMContext):
            await self.handle_vacancy_requirements(message, state)
        
        @self.router.message(StateFilter(EmployerStates.VACANCY_RESPONSIBILITIES))
        async def handle_vacancy_responsibilities(message: Message, state: FSMContext):
            await self.handle_vacancy_responsibilities(message, state)
        
        # Ish sharoitlari
        @self.router.message(StateFilter(EmployerStates.SALARY_RANGE))
        async def handle_salary_range(message: Message, state: FSMContext):
            await self.handle_salary_range(message, state)
        
        @self.router.message(StateFilter(EmployerStates.LOCATION))
        async def handle_location(message: Message, state: FSMContext):
            await self.handle_location(message, state)
        
        @self.router.message(StateFilter(EmployerStates.EXPERIENCE_YEARS))
        async def handle_experience_years(message: Message, state: FSMContext):
            await self.handle_experience_years(message, state)
        
        # AI Kriteriyalar
        @self.router.message(StateFilter(EmployerStates.AI_CRITERIA_SKILLS))
        async def handle_ai_criteria_skills(message: Message, state: FSMContext):
            await self.handle_ai_criteria_skills(message, state)
        
        @self.router.message(StateFilter(EmployerStates.AI_CRITERIA_EXPERIENCE))
        async def handle_ai_criteria_experience(message: Message, state: FSMContext):
            await self.handle_ai_criteria_experience(message, state)
        
        @self.router.message(StateFilter(EmployerStates.AI_CRITERIA_EDUCATION))
        async def handle_ai_criteria_education(message: Message, state: FSMContext):
            await self.handle_ai_criteria_education(message, state)
        
        @self.router.message(StateFilter(EmployerStates.AI_CRITERIA_LANGUAGES))
        async def handle_ai_criteria_languages(message: Message, state: FSMContext):
            await self.handle_ai_criteria_languages(message, state)
        
        @self.router.message(StateFilter(EmployerStates.AI_CRITERIA_ADDITIONAL))
        async def handle_ai_criteria_additional(message: Message, state: FSMContext):
            await self.handle_ai_criteria_additional(message, state)
        
        @self.router.message(StateFilter(EmployerStates.AI_PROMPT_CREATION))
        async def handle_ai_prompt_creation(message: Message, state: FSMContext):
            await self.handle_ai_prompt_creation(message, state)
        
        # Interview savollari
        @self.router.message(StateFilter(EmployerStates.INTERVIEW_QUESTIONS_INPUT))
        async def handle_interview_questions_input(message: Message, state: FSMContext):
            await self.handle_interview_questions_input(message, state)
        
        # Callback handlers
        @self.router.callback_query(F.data.startswith('work_type_'))
        async def work_type_callback(callback: CallbackQuery, state: FSMContext):
            await self.handle_work_type_callback(callback, state)
        
        @self.router.callback_query(F.data.startswith('work_schedule_'))
        async def work_schedule_callback(callback: CallbackQuery, state: FSMContext):
            await self.handle_work_schedule_callback(callback, state)
        
        @self.router.callback_query(F.data.startswith('questions_count_'))
        async def questions_count_callback(callback: CallbackQuery, state: FSMContext):
            await self.handle_questions_count_callback(callback, state)
        
        @self.router.callback_query(F.data.startswith('confirm_vacancy_'))
        async def confirm_vacancy_callback(callback: CallbackQuery, state: FSMContext):
            await self.handle_confirm_vacancy_callback(callback, state)
        
        # Vakansiya boshqaruvi
        @self.router.callback_query(F.data.startswith('view_vacancy_'))
        async def view_vacancy_callback(callback: CallbackQuery):
            await self.handle_view_vacancy_callback(callback)
        
        @self.router.callback_query(F.data.startswith('manage_vacancy_'))
        async def manage_vacancy_callback(callback: CallbackQuery):
            await self.handle_manage_vacancy_callback(callback)
        
        # Arizalarni ko'rish
        @self.router.callback_query(F.data.startswith('view_application_'))
        async def view_application_callback(callback: CallbackQuery):
            await self.handle_view_application_callback(callback)
        
        # Bekor qilish
        @self.router.callback_query(F.data == 'cancel_vacancy')
        async def cancel_vacancy(callback: CallbackQuery, state: FSMContext):
            await self.handle_cancel_vacancy(callback, state)
    
    # ===========================================
    # MAIN CALLBACK HANDLER
    # ===========================================
    
    async def handle_callback(self, callback: CallbackQuery, state: FSMContext):
        """Employer callback handlerlarini boshqarish"""
        try:
            await self.handle_employer_callbacks(callback, state)
        except Exception as e:
            logger.error(f"Employer callback xatoligi: {e}")
            await callback.answer("❌ Xatolik yuz berdi")
    
    async def handle_message(self, message: Message, state: FSMContext):
        """Employer message handlerlarini boshqarish"""
        # Bu yerda specific message handling bo'ladi
        # Hozircha register_handlers da handle qilinadi
        pass
    
    async def handle_employer_callbacks(self, callback: CallbackQuery, state: FSMContext):
        """Employer callback handlerini asosiy boshqaruvchi"""
        try:
            action = callback.data.replace('employer_', '')
            user_id = callback.from_user.id
            language = self.get_user_language(user_id)
            
            # Analytics
            user = self.get_user_by_telegram_id(user_id)
            if user:
                self.crud['analytics'].log_user_action(
                    user_id=user['user_id'], 
                    action=f'employer_{action}'
                )
            
            if action == 'create_vacancy':
                await self.start_vacancy_creation(callback, state, language)
            elif action == 'vacancies':
                await self.show_my_vacancies(callback.message.chat.id, user_id, language)
            elif action == 'applications':
                await self.show_applications(callback.message.chat.id, user_id, language)
            elif action == 'analytics':
                await self.show_employer_analytics(callback.message.chat.id, user_id, language)
            
            await callback.answer()
            
        except Exception as e:
            logger.error(f"Employer callback xatoligi: {e}")
            await callback.answer("❌ Xatolik yuz berdi")
    
    # ===========================================
    # VACANCY CREATION PROCESS
    # ===========================================
    
    async def start_vacancy_creation(self, callback: CallbackQuery, state: FSMContext, language: str):
        """Vakansiya yaratishni boshlash"""
        try:
            # State o'rnatish va boshlang'ich ma'lumotlarni saqlash
            await state.set_state(EmployerStates.COMPANY_NAME)
            await state.update_data(
                employer_id=callback.from_user.id,
                created_at=datetime.now().isoformat()
            )
            
            # Birinchi savol
            text = get_text("creating_vacancy", language) + "\n\n"
            text += get_text("company_name_prompt", language)
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("btn_cancel", language), 
                        callback_data="cancel_vacancy"
                    )
                ]
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard)
            logger.info(f"Vakansiya yaratish boshlandi: {callback.from_user.id}")
            
        except Exception as e:
            logger.error(f"Vakansiya yaratishni boshlash xatoligi: {e}")
            await callback.message.edit_text(get_text("error", language))
    
    # ===========================================
    # COMPANY INFORMATION HANDLERS
    # ===========================================
    
    async def handle_company_name(self, message: Message, state: FSMContext):
        """Kompaniya nomini qayta ishlash"""
        try:
            company_name = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Validatsiya
            if len(company_name) < 2:
                await message.reply(get_text("company_name_too_short", language))
                return
            
            if len(company_name) > 100:
                await message.reply(get_text("company_name_too_long", language))
                return
            
            # Ma'lumotni saqlash
            await state.update_data(company_name=company_name)
            await state.set_state(EmployerStates.COMPANY_DESCRIPTION)
            
            # Keyingi savol
            text = get_text("company_description_prompt", language)
            await message.answer(text)
            
            logger.info(f"Kompaniya nomi kiritildi: {message.from_user.id} - {company_name}")
            
        except Exception as e:
            logger.error(f"Kompaniya nomi xatoligi: {e}")
            language = self.get_user_language(message.from_user.id)
            await message.reply(get_text("error", language))
    
    async def handle_company_description(self, message: Message, state: FSMContext):
        """Kompaniya tavsifini qayta ishlash"""
        try:
            company_description = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Validatsiya
            if len(company_description) < 10:
                await message.reply(get_text("company_description_too_short", language))
                return
            
            # Ma'lumotni saqlash
            await state.update_data(company_description=company_description)
            await state.set_state(EmployerStates.COMPANY_WEBSITE)
            
            # Keyingi savol
            text = get_text("company_website_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"Kompaniya tavsifi xatoligi: {e}")
    
    async def handle_company_website(self, message: Message, state: FSMContext):
        """Kompaniya veb-saytini qayta ishlash"""
        try:
            website = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Veb-sayt ixtiyoriy, lekin agar kiritilsa validatsiya qilish
            if website.lower() in ['yo\'q', 'нет', 'no', '-', 'mavjud emas']:
                website = None
            elif website and not (website.startswith('http://') or website.startswith('https://')):
                website = 'https://' + website
            
            # Ma'lumotni saqlash
            await state.update_data(company_website=website)
            await state.set_state(EmployerStates.COMPANY_LOCATION)
            
            # Keyingi savol
            text = get_text("company_location_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"Kompaniya veb-sayti xatoligi: {e}")
    
    async def handle_company_location(self, message: Message, state: FSMContext):
        """Kompaniya joylashuvi"""
        try:
            location = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(company_location=location)
            await state.set_state(EmployerStates.VACANCY_TITLE)
            
            # Vakansiya ma'lumotlariga o'tish
            text = get_text("vacancy_section_start", language) + "\n\n"
            text += get_text("vacancy_title_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"Kompaniya joylashuvi xatoligi: {e}")
    
    # ===========================================
    # VACANCY INFORMATION HANDLERS
    # ===========================================
    
    async def handle_vacancy_title(self, message: Message, state: FSMContext):
        """Vakansiya nomini qayta ishlash"""
        try:
            vacancy_title = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Validatsiya
            if len(vacancy_title) < 3:
                await message.reply(get_text("vacancy_title_too_short", language))
                return
            
            if len(vacancy_title) > 150:
                await message.reply(get_text("vacancy_title_too_long", language))
                return
            
            # Ma'lumotni saqlash
            await state.update_data(vacancy_title=vacancy_title)
            await state.set_state(EmployerStates.VACANCY_DESCRIPTION)
            
            # Keyingi savol
            text = get_text("vacancy_description_prompt", language)
            await message.answer(text)
            
            logger.info(f"Vakansiya nomi kiritildi: {message.from_user.id} - {vacancy_title}")
            
        except Exception as e:
            logger.error(f"Vakansiya nomi xatoligi: {e}")
    
    async def handle_vacancy_description(self, message: Message, state: FSMContext):
        """Vakansiya tavsifini qayta ishlash"""
        try:
            vacancy_description = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Validatsiya
            if len(vacancy_description) < 20:
                await message.reply(get_text("vacancy_description_too_short", language))
                return
            
            # Ma'lumotni saqlash
            await state.update_data(vacancy_description=vacancy_description)
            await state.set_state(EmployerStates.VACANCY_REQUIREMENTS)
            
            # Keyingi savol
            text = get_text("vacancy_requirements_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"Vakansiya tavsifi xatoligi: {e}")
    
    async def handle_vacancy_requirements(self, message: Message, state: FSMContext):
        """Vakansiya talablarini qayta ishlash"""
        try:
            requirements = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(requirements=requirements)
            await state.set_state(EmployerStates.VACANCY_RESPONSIBILITIES)
            
            # Keyingi savol
            text = get_text("vacancy_responsibilities_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"Vakansiya talablari xatoligi: {e}")
    
    async def handle_vacancy_responsibilities(self, message: Message, state: FSMContext):
        """Vakansiya majburiyatlarini qayta ishlash"""
        try:
            responsibilities = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(responsibilities=responsibilities)
            await state.set_state(EmployerStates.WORK_TYPE)
            
            # Ish turini tanlash
            text = get_text("work_type_prompt", language)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("work_type_remote", language),
                        callback_data="work_type_remote"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=get_text("work_type_office", language),
                        callback_data="work_type_office"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=get_text("work_type_hybrid", language),
                        callback_data="work_type_hybrid"
                    )
                ]
            ])
            
            await message.answer(text, reply_markup=keyboard)
            
        except Exception as e:
            logger.error(f"Vakansiya majburiyatlari xatoligi: {e}")
    
    # ===========================================
    # WORK CONDITIONS HANDLERS
    # ===========================================
    
    async def handle_work_type_callback(self, callback: CallbackQuery, state: FSMContext):
        """Ish turini tanlash callback"""
        try:
            work_type = callback.data.split('_')[2]  # work_type_remote -> remote
            language = self.get_user_language(callback.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(work_type=work_type)
            await state.set_state(EmployerStates.WORK_SCHEDULE)
            
            # Ish jadvalini tanlash
            text = get_text("work_schedule_prompt", language)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("work_schedule_full_time", language),
                        callback_data="work_schedule_full-time"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=get_text("work_schedule_part_time", language),
                        callback_data="work_schedule_part-time"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=get_text("work_schedule_contract", language),
                        callback_data="work_schedule_contract"
                    )
                ]
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard)
            await callback.answer()
            
        except Exception as e:
            logger.error(f"Ish turi callback xatoligi: {e}")
    
    async def handle_work_schedule_callback(self, callback: CallbackQuery, state: FSMContext):
        """Ish jadvalini tanlash callback"""
        try:
            work_schedule = callback.data.split('_')[2]  # work_schedule_full-time -> full-time
            language = self.get_user_language(callback.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(work_schedule=work_schedule)
            await state.set_state(EmployerStates.SALARY_RANGE)
            
            # Ish haqqi so'rash
            text = get_text("salary_range_prompt", language)
            await callback.message.edit_text(text)
            await callback.answer()
            
        except Exception as e:
            logger.error(f"Ish jadvali callback xatoligi: {e}")
    
    async def handle_salary_range(self, message: Message, state: FSMContext):
        """Ish haqqi oralig'ini qayta ishlash"""
        try:
            salary_text = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ish haqqini parse qilish (ixtiyoriy)
            salary_min = None
            salary_max = None
            
            # Simple parsing - kelajakda yaxshilanishi mumkin
            if '-' in salary_text:
                try:
                    parts = salary_text.replace(' ', '').split('-')
                    if len(parts) == 2:
                        salary_min = int(''.join(filter(str.isdigit, parts[0])))
                        salary_max = int(''.join(filter(str.isdigit, parts[1])))
                except:
                    pass
            
            # Ma'lumotni saqlash
            await state.update_data(
                salary_text=salary_text,
                salary_min=salary_min,
                salary_max=salary_max
            )
            await state.set_state(EmployerStates.LOCATION)
            
            # Ish joyi so'rash
            text = get_text("work_location_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"Ish haqqi xatoligi: {e}")
    
    async def handle_location(self, message: Message, state: FSMContext):
        """Ish joyini qayta ishlash"""
        try:
            location = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(location=location)
            await state.set_state(EmployerStates.EXPERIENCE_YEARS)
            
            # Tajriba so'rash
            text = get_text("experience_years_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"Ish joyi xatoligi: {e}")
    
    async def handle_experience_years(self, message: Message, state: FSMContext):
        """Tajriba yillarini qayta ishlash"""
        try:
            experience_text = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Tajribani raqam sifatida parse qilish
            experience_years = 0
            try:
                experience_years = int(''.join(filter(str.isdigit, experience_text)))
            except:
                if any(word in experience_text.lower() for word in ['yo\'q', 'нет', 'no']):
                    experience_years = 0
                else:
                    experience_years = 1  # Default
            
            # Ma'lumotni saqlash
            await state.update_data(
                experience_text=experience_text,
                experience_years=experience_years
            )
            await state.set_state(EmployerStates.AI_CRITERIA_SKILLS)
            
            # AI kriteriyalariga o'tish
            text = get_text("ai_criteria_section_start", language) + "\n\n"
            text += get_text("ai_criteria_skills_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"Tajriba yillari xatoligi: {e}")
    
    # ===========================================
    # AI CRITERIA HANDLERS  
    # ===========================================
    
    async def handle_ai_criteria_skills(self, message: Message, state: FSMContext):
        """AI kriteriya - Ko'nikmalar"""
        try:
            skills = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            await state.update_data(ai_criteria_skills=skills)
            await state.set_state(EmployerStates.AI_CRITERIA_EXPERIENCE)
            
            text = get_text("ai_criteria_experience_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"AI kriteriya skills xatoligi: {e}")
    
    async def handle_ai_criteria_experience(self, message: Message, state: FSMContext):
        """AI kriteriya - Tajriba"""
        try:
            experience = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            await state.update_data(ai_criteria_experience=experience)
            await state.set_state(EmployerStates.AI_CRITERIA_EDUCATION)
            
            text = get_text("ai_criteria_education_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"AI kriteriya experience xatoligi: {e}")
    
    async def handle_ai_criteria_education(self, message: Message, state: FSMContext):
        """AI kriteriya - Ta'lim"""
        try:
            education = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            await state.update_data(ai_criteria_education=education)
            await state.set_state(EmployerStates.AI_CRITERIA_LANGUAGES)
            
            text = get_text("ai_criteria_languages_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"AI kriteriya education xatoligi: {e}")
    
    async def handle_ai_criteria_languages(self, message: Message, state: FSMContext):
        """AI kriteriya - Tillar"""
        try:
            languages_req = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            await state.update_data(ai_criteria_languages=languages_req)
            await state.set_state(EmployerStates.AI_CRITERIA_ADDITIONAL)
            
            text = get_text("ai_criteria_additional_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"AI kriteriya languages xatoligi: {e}")
    
    async def handle_ai_criteria_additional(self, message: Message, state: FSMContext):
        """AI kriteriya - Qo'shimcha"""
        try:
            additional = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            await state.update_data(ai_criteria_additional=additional)
            await state.set_state(EmployerStates.AI_PROMPT_CREATION)
            
            text = get_text("ai_prompt_creation_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"AI kriteriya additional xatoligi: {e}")
    
    async def handle_ai_prompt_creation(self, message: Message, state: FSMContext):
        """AI prompt yaratish"""
        try:
            ai_prompt = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            await state.update_data(ai_prompt=ai_prompt)
            await state.set_state(EmployerStates.INTERVIEW_QUESTIONS_COUNT)
            
            # Savollar sonini tanlash
            text = get_text("interview_questions_count_prompt", language)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
            for i in range(Config.MIN_QUESTIONS_COUNT, Config.MAX_QUESTIONS_COUNT + 1):
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(
                        text=f"{i} ta savol",
                        callback_data=f"questions_count_{i}"
                    )
                ])
            
            await message.answer(text, reply_markup=keyboard)
            
        except Exception as e:
            logger.error(f"AI prompt yaratish xatoligi: {e}")
    
    # ===========================================
    # INTERVIEW QUESTIONS HANDLERS
    # ===========================================
    
    async def handle_questions_count_callback(self, callback: CallbackQuery, state: FSMContext):
        """Savollar sonini tanlash"""
        try:
            questions_count = int(callback.data.split('_')[2])
            language = self.get_user_language(callback.from_user.id)
            
            await state.update_data(
                questions_count=questions_count,
                questions=[],
                current_question=1
            )
            await state.set_state(EmployerStates.INTERVIEW_QUESTIONS_COUNT)
            
            text = get_text("question_prompt", language).format(1)
            await callback.message.edit_text(text)
            await callback.answer()
            
        except Exception as e:
            logger.error(f"Savollar soni callback xatoligi: {e}") 

    async def handle_interview_questions_input(self, message: Message, state: FSMContext):
        """Interview savollarini kiritish"""
        try:
            question_text = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            if len(question_text) < 5:
                await message.reply("❌ Savol juda qisqa!")
                return
            
            # Mavjud ma'lumotlarni olish
            data = await state.get_data()
            questions = data.get('questions', [])
            questions_count = data.get('questions_count', 3)
            current_question = data.get('current_question', 1)
            
            # Savolni qo'shish
            questions.append(question_text)
            
            if len(questions) < questions_count:
                # Keyingi savol
                current_question += 1
                await state.update_data(
                    questions=questions,
                    current_question=current_question
                )
                
                text = get_text("question_prompt", language).format(current_question)
                await message.answer(text)
            else:
                # Barcha savollar tugadi - yakuniy tasdiqlash
                await state.update_data(questions=questions)
                await self.show_final_confirmation(message, state, language)
            
        except Exception as e:
            print(f"Interview savollar kiritish xatoligi: {e}")

    async def show_final_confirmation(self, message: Message, state: FSMContext, language: str):
        """Yakuniy tasdiqlash ko'rsatish"""
        try:
            data = await state.get_data()
            
            # F-string muammosini hal qilish uchun alohida o'zgaruvchilar
            company_name = data.get('company_name', 'N/A')
            vacancy_title = data.get('vacancy_title', 'N/A')
            location = data.get('work_location', 'N/A')
            salary_text = data.get('salary_range', 'N/A')
            questions_count = data.get('questions_count', 0)
            
            # Work type va schedule uchun xavfsiz usul
            work_type = data.get('work_type', 'full_time')
            work_schedule = data.get('work_schedule', 'office')
            
            # Vakansiya preview yaratish
            text = "📋 Vakansiya tasdiqlanishi:\n\n"
            text += f"🏢 Kompaniya: {company_name}\n"
            text += f"💼 Lavozim: {vacancy_title}\n"
            text += f"📍 Joylashuv: {location}\n"
            text += f"💰 Maosh: {salary_text}\n"
            text += f"⏰ Ish turi: {work_type}\n"
            text += f"📅 Jadval: {work_schedule}\n"
            text += f"🎯 Savollar soni: {questions_count}\n\n"
            text += "Vakansiyani yaratishni tasdiqlaysizmi?"
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="✅ Ha, yaratish",
                        callback_data="confirm_vacancy_yes"
                    ),
                    InlineKeyboardButton(
                        text="❌ Yo'q, bekor qilish",
                        callback_data="confirm_vacancy_no"
                    )
                ]
            ])
            
            await message.answer(text, reply_markup=keyboard)
            
        except Exception as e:
            print(f"Yakuniy tasdiqlash xatoligi: {e}")
            await message.answer("❌ Xatolik yuz berdi")
    
    async def handle_confirm_vacancy_callback(self, callback: CallbackQuery, state: FSMContext):
        """Vakansiya tasdiqlash callback"""
        try:
            confirm = callback.data.split('_')[2]  # confirm_vacancy_yes -> yes
            language = self.get_user_language(callback.from_user.id)
            
            if confirm == 'yes':
                await self.complete_vacancy_creation(callback, state, language)
            else:
                await self.handle_cancel_vacancy(callback, state)
            
        except Exception as e:
            logger.error(f"Vakansiya tasdiqlash callback xatoligi: {e}")
    
    async def complete_vacancy_creation(self, callback: CallbackQuery, state: FSMContext, language: str):
        """Vakansiya yaratishni yakunlash va saqlash"""
        try:
            data = await state.get_data()
            user = self.get_user_by_telegram_id(callback.from_user.id)
            
            if not user:
                await callback.message.edit_text(get_text("user_not_found", language))
                return
            
            # Kompaniyani yaratish
            company_id = self.crud['company'].create_company(
                name=data['company_name'],
                description=data['company_description'],
                employer_id=user['user_id'],
                website=data.get('company_website'),
                location=data.get('company_location')
            )
            
            # AI kriteriyalarni formatlash
            ai_criteria = {
                'skills': data.get('ai_criteria_skills', ''),
                'experience': data.get('ai_criteria_experience', ''),
                'education': data.get('ai_criteria_education', ''),
                'languages': data.get('ai_criteria_languages', ''),
                'additional': data.get('ai_criteria_additional', '')
            }
            
            # Vakansiyani yaratish
            vacancy_id = self.crud['vacancy'].create_vacancy(
                company_id=company_id,
                title=data['vacancy_title'],
                description=data['vacancy_description'],
                requirements=data['requirements'],
                responsibilities=data['responsibilities'],
                work_type=data['work_type'],
                work_schedule=data['work_schedule'],
                salary_min=data.get('salary_min'),
                salary_max=data.get('salary_max'),
                location=data['location'],
                experience_years=data.get('experience_years', 0),
                ai_criteria=ai_criteria,
                ai_prompt=data.get('ai_prompt', ''),
                questions=data.get('questions', [])
            )
            
            # Analytics
            self.crud['analytics'].log_user_action(
                user_id=user['user_id'],
                action='vacancy_created',
                data={
                    'vacancy_id': vacancy_id,
                    'company_id': company_id,
                    'title': data['vacancy_title']
                }
            )
            
            # State ni tozalash
            await state.clear()
            
            # Muvaffaqiyat xabari
            text = get_text("vacancy_created_success", language).format(
                title=data['vacancy_title'],
                company=data['company_name'],
                date=datetime.now().strftime("%d.%m.%Y %H:%M")
            )
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("view_vacancy", language),
                        callback_data=f"view_vacancy_{vacancy_id}"
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
                        text=get_text("create_new_vacancy", language),
                        callback_data="employer_create_vacancy"
                    )
                ]
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard)
            await callback.answer("✅ Vakansiya muvaffaqiyatli yaratildi!")
            
            logger.info(f"Vakansiya yaratildi: {callback.from_user.id} - {vacancy_id}")
            
        except Exception as e:
            logger.error(f"Vakansiya yaratishni yakunlash xatoligi: {e}")
            await callback.message.edit_text(get_text("error", language))
    
    # ===========================================
    # VACANCY MANAGEMENT
    # ===========================================
    
    async def show_my_vacancies(self, chat_id: int, user_id: int, language: str):
        """Mening vakansiyalarimni ko'rsatish"""
        try:
            user = self.get_user_by_telegram_id(user_id)
            if not user:
                await self.bot.send_message(chat_id, get_text("user_not_found", language))
                return
            
            # Foydalanuvchining kompaniyalari va vakansiyalarini olish
            companies = self.crud['company'].get_companies_by_employer(user['user_id'])
            
            if not companies:
                text = get_text("no_companies_found", language)
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=get_text("create_vacancy", language),
                            callback_data="employer_create_vacancy"
                        )
                    ]
                ])
                await self.bot.send_message(chat_id, text, reply_markup=keyboard)
                return
            
            # Vakansiyalar ro'yxatini yaratish
            text = get_text("my_vacancies_list", language) + "\n\n"
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
            vacancy_count = 0
            for company in companies:
                vacancies = self.crud['vacancy'].get_active_vacancies_by_company(company['company_id'])
                for vacancy in vacancies:
                    vacancy_count += 1
                    status_emoji = "🟢" if vacancy['status'] == 'active' else "🔴"
                    button_text = f"{status_emoji} {vacancy['title']}"
                    
                    keyboard.inline_keyboard.append([
                        InlineKeyboardButton(
                            text=button_text,
                            callback_data=f"view_vacancy_{vacancy['vacancy_id']}"
                        )
                    ])
            
            if vacancy_count == 0:
                text = get_text("no_vacancies_found", language)
            else:
                text += get_text("total_vacancies", language).format(vacancy_count)
            
            # Navigatsiya tugmalari
            keyboard.inline_keyboard.extend([
                [
                    InlineKeyboardButton(
                        text=get_text("create_vacancy", language),
                        callback_data="employer_create_vacancy"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=get_text("btn_back", language),
                        callback_data="back_main"
                    )
                ]
            ])
            
            await self.bot.send_message(chat_id, text, reply_markup=keyboard)
            
        except Exception as e:
            logger.error(f"Vakansiyalar ro'yxati xatoligi: {e}")
            await self.bot.send_message(chat_id, get_text("error", language))
    
    async def show_applications(self, chat_id: int, user_id: int, language: str):
        """Kelgan arizalarni ko'rsatish"""
        try:
            user = self.get_user_by_telegram_id(user_id)
            if not user:
                await self.bot.send_message(chat_id, get_text("user_not_found", language))
                return
            
            # Ish beruvchi uchun arizalarni olish
            applications = self.crud['application'].get_applications_for_employer(user['user_id'])
            
            if not applications:
                text = get_text("no_applications_found", language)
                await self.bot.send_message(chat_id, text)
                return
            
            text = get_text("applications_list", language) + "\n\n"
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
            for app in applications:
                # Application statusiga qarab emoji
                status_emoji = {
                    'pending': '🟡',
                    'ai_screening': '🔄',
                    'interview': '💬',
                    'accepted': '✅',
                    'rejected': '❌'
                }.get(app['status'], '❓')
                
                button_text = f"{status_emoji} {app['vacancy_title']} - {app.get('applicant_name', 'N/A')}"
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(
                        text=button_text,
                        callback_data=f"view_application_{app['application_id']}"
                    )
                ])
            
            keyboard.inline_keyboard.append([
                InlineKeyboardButton(
                    text=get_text("btn_back", language),
                    callback_data="back_main"
                )
            ])
            
            await self.bot.send_message(chat_id, text, reply_markup=keyboard)
            
        except Exception as e:
            logger.error(f"Arizalar ro'yxati xatoligi: {e}")
    
    async def show_employer_analytics(self, chat_id: int, user_id: int, language: str):
        """Ish beruvchi analitikasini ko'rsatish"""
        try:
            user = self.get_user_by_telegram_id(user_id)
            if not user:
                await self.bot.send_message(chat_id, get_text("user_not_found", language))
                return
            
            # Statistikani olish
            stats = self.crud['analytics'].get_employer_stats(user['user_id'])
            
            text = get_text("employer_analytics", language) + "\n\n"
            text += f"📊 {get_text('total_vacancies', language)}: {stats.get('total_vacancies', 0)}\n"
            text += f"📨 {get_text('total_applications', language)}: {stats.get('total_applications', 0)}\n"
            text += f"✅ {get_text('accepted_applications', language)}: {stats.get('accepted_applications', 0)}\n"
            text += f"❌ {get_text('rejected_applications', language)}: {stats.get('rejected_applications', 0)}\n"
            text += f"📅 {get_text('date', language)}: {datetime.now().strftime('%d.%m.%Y')}"
            
            await self.bot.send_message(chat_id, text)
            
        except Exception as e:
            logger.error(f"Employer analitikasi xatoligi: {e}")
    
    # ===========================================
    # UTILITY HANDLERS
    # ===========================================
    
    async def handle_view_vacancy_callback(self, callback: CallbackQuery):
        """Vakansiyani ko'rish callback"""
        try:
            vacancy_id = int(callback.data.split('_')[2])
            language = self.get_user_language(callback.from_user.id)
            
            vacancy = self.crud['vacancy'].get_vacancy_by_id(vacancy_id)
            if not vacancy:
                await callback.answer(get_text("vacancy_not_found", language))
                return
            
            # Vacancy details ni formatlar bilan ko'rsatish
            text = get_text("vacancy_full_details", language).format(
                title=vacancy['title'],
                description=vacancy['description'],
                requirements=vacancy['requirements'],
                responsibilities=vacancy['responsibilities'],
                work_type=get_text(f"work_type_{vacancy['work_type']}", language),
                work_schedule=get_text(f"work_schedule_{vacancy['work_schedule']}", language),
                location=vacancy['location'],
                experience=vacancy['experience_years']
            )
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("manage_vacancy", language),
                        callback_data=f"manage_vacancy_{vacancy_id}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=get_text("btn_back", language),
                        callback_data="employer_vacancies"
                    )
                ]
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard, parse_mode='Markdown')
            await callback.answer()
            
        except Exception as e:
            logger.error(f"Vakansiyani ko'rish callback xatoligi: {e}")
    
    async def handle_manage_vacancy_callback(self, callback: CallbackQuery):
        """Vakansiyani boshqarish callback"""
        try:
            vacancy_id = int(callback.data.split('_')[2])
            language = self.get_user_language(callback.from_user.id)
            
            vacancy = self.crud['vacancy'].get_vacancy_by_id(vacancy_id)
            if not vacancy:
                await callback.answer(get_text("vacancy_not_found", language))
                return
            
            text = get_text("manage_vacancy_options", language)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
            # Status ga qarab tugmalar
            if vacancy['status'] == 'active':
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(
                        text=get_text("archive_vacancy", language),
                        callback_data=f"archive_vacancy_{vacancy_id}"
                    )
                ])
            else:
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(
                        text=get_text("activate_vacancy", language),
                        callback_data=f"activate_vacancy_{vacancy_id}"
                    )
                ])
            
            keyboard.inline_keyboard.extend([
                [
                    InlineKeyboardButton(
                        text=get_text("view_applications", language),
                        callback_data=f"vacancy_applications_{vacancy_id}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=get_text("btn_back", language),
                        callback_data=f"view_vacancy_{vacancy_id}"
                    )
                ]
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard)
            await callback.answer()
            
        except Exception as e:
            logger.error(f"Vakansiyani boshqarish callback xatoligi: {e}")
    
    async def handle_view_application_callback(self, callback: CallbackQuery):
        """Arizani ko'rish callback"""
        try:
            application_id = int(callback.data.split('_')[2])
            language = self.get_user_language(callback.from_user.id)
            
            # Bu yerda application details ko'rsatish
            # Hozircha placeholder
            await callback.answer(get_text("feature_coming_soon", language))
            
        except Exception as e:
            logger.error(f"Arizani ko'rish callback xatoligi: {e}")
    
    async def handle_cancel_vacancy(self, callback: CallbackQuery, state: FSMContext):
        """Vakansiya yaratishni bekor qilish"""
        try:
            language = self.get_user_language(callback.from_user.id)
            
            await state.clear()
            
            text = get_text("vacancy_creation_cancelled", language)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("back_to_menu", language),
                        callback_data="back_main"
                    )
                ]
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard)
            await callback.answer()
            
        except Exception as e:
            logger.error(f"Vakansiya bekor qilish xatoligi: {e}")
