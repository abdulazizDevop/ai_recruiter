# # -*- coding: utf-8 -*-

# import json
# import os
# from aiogram import Router, F
# from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.filters import StateFilter
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# from utils.language import get_text
# from services.ai_service import validate_file_format, get_file_size_mb
# from config import Config

# # Jobseeker holatlari
# class JobseekerStates(StatesGroup):
#     UPLOADING_RESUME = State()
#     ANSWERING_QUESTIONS = State()
#     PROVIDING_INFO_NAME = State()
#     PROVIDING_INFO_AGE = State()
#     PROVIDING_INFO_PHONE = State()
#     PROVIDING_INFO_EMAIL = State()
#     PROVIDING_INFO_ADDRESS = State()

# class JobseekerHandlers:
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
#         """Jobseeker handlerlarini ro'yxatga olish"""
        
#         # Jobseeker callback handlerni ro'yxatga olish
#         @self.router.callback_query(F.data.startswith('jobseeker_'))
#         async def jobseeker_callbacks(callback: CallbackQuery, state: FSMContext):
#             """Jobseeker callback handleri"""
#             try:
#                 action = callback.data.replace('jobseeker_', '')
#                 user_id = callback.from_user.id
#                 language = self.get_user_language(user_id)
                
#                 if action == 'find_jobs':
#                     await self.show_companies(callback.message.chat.id, language)
#                 elif action == 'applications':
#                     await self.show_my_applications(callback.message.chat.id, user_id, language)
                
#                 await callback.answer()
                
#             except Exception as e:
#                 print(f"Jobseeker callback xatoligi: {e}")
#                 await callback.answer(get_text("error", "uz"))
        
#         # Kompaniya tanlash
#         @self.router.callback_query(F.data.startswith('select_company_'))
#         async def select_company_callback(callback: CallbackQuery):
#             await self.select_company_callback(callback)
        
#         # Vakansiya tanlash
#         @self.router.callback_query(F.data.startswith('select_vacancy_'))
#         async def select_vacancy_callback(callback: CallbackQuery):
#             await self.select_vacancy_callback(callback)
        
#         # Vakansiyaga ariza berish
#         @self.router.callback_query(F.data.startswith('apply_vacancy_'))
#         async def apply_vacancy_callback(callback: CallbackQuery, state: FSMContext):
#             await self.apply_vacancy_callback(callback, state)
        
#         # Resume yuklash
#         @self.router.message(StateFilter(JobseekerStates.UPLOADING_RESUME), F.document)
#         async def handle_resume_upload(message: Message, state: FSMContext):
#             await self.handle_resume_upload(message, state)
        
#         # Suhbat savollari
#         @self.router.callback_query(F.data == 'start_interview')
#         async def start_interview_callback(callback: CallbackQuery, state: FSMContext):
#             await self.start_interview_callback(callback, state)
        
#         @self.router.message(StateFilter(JobseekerStates.ANSWERING_QUESTIONS))
#         async def handle_interview_answer(message: Message, state: FSMContext):
#             await self.handle_interview_answer(message, state)
        
#         # Qo'shimcha ma'lumotlar
#         @self.router.message(StateFilter(JobseekerStates.PROVIDING_INFO_NAME))
#         async def handle_full_name(message: Message, state: FSMContext):
#             await self.handle_full_name(message, state)
        
#         @self.router.message(StateFilter(JobseekerStates.PROVIDING_INFO_AGE))
#         async def handle_age(message: Message, state: FSMContext):
#             await self.handle_age(message, state)
        
#         @self.router.message(StateFilter(JobseekerStates.PROVIDING_INFO_PHONE))
#         async def handle_phone(message: Message, state: FSMContext):
#             await self.handle_phone(message, state)
        
#         @self.router.message(StateFilter(JobseekerStates.PROVIDING_INFO_EMAIL))
#         async def handle_email(message: Message, state: FSMContext):
#             await self.handle_email(message, state)
        
#         @self.router.message(StateFilter(JobseekerStates.PROVIDING_INFO_ADDRESS))
#         async def handle_address(message: Message, state: FSMContext):
#             await self.handle_address(message, state)
        
#         # Noto'g'ri fayl formati
#         @self.router.message(StateFilter(JobseekerStates.UPLOADING_RESUME))
#         async def handle_invalid_resume(message: Message):
#             language = self.get_user_language(message.from_user.id)
#             await message.reply(get_text("invalid_file", language))
    
#     async def show_companies(self, chat_id: int, language: str):
#         """Kompaniyalar ro'yxatini ko'rsatish"""
#         try:
#             companies = self.db.get_all_companies()
            
#             if not companies:
#                 text = get_text("no_companies", language)
#                 await self.bot.send_message(chat_id, text)
#                 return
            
#             text = get_text("select_company", language)
#             keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
#             for company in companies:
#                 keyboard.inline_keyboard.append([
#                     InlineKeyboardButton(
#                         text=f"🏢 {company['name']}",
#                         callback_data=f"select_company_{company['id']}"
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
#             print(f"Kompaniyalar ro'yxati xatoligi: {e}")
    
#     async def select_company_callback(self, callback: CallbackQuery):
#         """Kompaniya tanlash callback"""
#         try:
#             company_id = int(callback.data.split('_')[2])  # select_company_123 -> 123
#             language = self.get_user_language(callback.from_user.id)
            
#             # Kompaniya vakansiyalarini olish
#             vacancies = self.db.get_vacancies_by_company(company_id, 'active')
            
#             if not vacancies:
#                 text = get_text("no_active_vacancies", language)
#                 keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                     [
#                         InlineKeyboardButton(
#                             text=get_text("btn_back", language),
#                             callback_data="jobseeker_find_jobs"
#                         )
#                     ]
#                 ])
#                 await callback.message.edit_text(text, reply_markup=keyboard)
#                 await callback.answer()
#                 return
            
#             text = get_text("select_vacancy", language)
#             keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
#             for vacancy in vacancies:
#                 keyboard.inline_keyboard.append([
#                     InlineKeyboardButton(
#                         text=f"📌 {vacancy['title']}",
#                         callback_data=f"select_vacancy_{vacancy['id']}"
#                     )
#                 ])
            
#             keyboard.inline_keyboard.append([
#                 InlineKeyboardButton(
#                     text=get_text("btn_back", language),
#                     callback_data="jobseeker_find_jobs"
#                 )
#             ])
            
#             await callback.message.edit_text(text, reply_markup=keyboard)
#             await callback.answer()
            
#         except Exception as e:
#             print(f"Kompaniya tanlash xatoligi: {e}")
#             await callback.answer("Xatolik yuz berdi!")
    
#     async def select_vacancy_callback(self, callback: CallbackQuery):
#         """Vakansiya tanlash callback"""
#         try:
#             vacancy_id = int(callback.data.split('_')[2])  # select_vacancy_123 -> 123
#             language = self.get_user_language(callback.from_user.id)
#             user_id = callback.from_user.id
            
#             # Vakansiya ma'lumotlarini olish
#             vacancy = self.db.get_vacancy_by_id(vacancy_id)
#             if not vacancy:
#                 await callback.answer("Vakansiya topilmadi!")
#                 return
            
#             # Allaqachon ariza berganligini tekshirish
#             user = self.db.get_user_by_telegram_id(user_id)
#             if self.db.check_existing_application(vacancy_id, user['id']):
#                 text = get_text("already_applied", language)
#                 await callback.message.edit_text(text)
#                 await callback.answer()
#                 return
            
#             # Vakansiya tafsilotlarini ko'rsatish
#             company = self.db.get_companies_by_employer(vacancy['employer_id'])[0]  # Simplified
            
#             text = get_text("vacancy_details", language).format(
#                 vacancy['title'],
#                 company['name'],
#                 vacancy['description'],
#                 vacancy['requirements'],
#                 vacancy['responsibilities'],
#                 "Ko'rsatilmagan",  # salary - keyinchalik format qilamiz
#                 vacancy.get('work_hours', 'Ko\'rsatilmagan'),
#                 vacancy.get('work_days', 'Ko\'rsatilmagan'),
#                 vacancy.get('location', 'Ko\'rsatilmagan')
#             )
            
#             keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                 [
#                     InlineKeyboardButton(
#                         text=get_text("apply_now", language),
#                         callback_data=f"apply_vacancy_{vacancy_id}"
#                     )
#                 ],
#                 [
#                     InlineKeyboardButton(
#                         text=get_text("btn_back", language),
#                         callback_data=f"select_company_{vacancy['company_id']}"
#                     )
#                 ]
#             ])
            
#             await callback.message.edit_text(text, reply_markup=keyboard)
#             await callback.answer()
            
#         except Exception as e:
#             print(f"Vakansiya tanlash xatoligi: {e}")
#             await callback.answer("Xatolik yuz berdi!")
    
#     async def apply_vacancy_callback(self, callback: CallbackQuery, state: FSMContext):
#         """Vakansiyaga ariza berish"""
#         try:
#             vacancy_id = int(callback.data.split('_')[2])
#             language = self.get_user_language(callback.from_user.id)
            
#             # State ga vakansiya ID ni saqlash
#             await state.update_data(vacancy_id=vacancy_id)
#             await state.set_state(JobseekerStates.UPLOADING_RESUME)
            
#             # Resume yuklashni so'rash
#             text = get_text("upload_resume", language)
            
#             keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                 [
#                     InlineKeyboardButton(
#                         text=get_text("btn_cancel", language),
#                         callback_data="cancel_application"
#                     )
#                 ]
#             ])
            
#             await callback.message.edit_text(text, reply_markup=keyboard)
#             await callback.answer()
            
#         except Exception as e:
#             print(f"Ariza berish xatoligi: {e}")
#             await callback.answer("Xatolik yuz berdi!")
    
#     async def handle_resume_upload(self, message: Message, state: FSMContext):
#         """Resume fayl yuklashni qayta ishlash"""
#         try:
#             language = self.get_user_language(message.from_user.id)
            
#             # Fayl ma'lumotlarini olish
#             document = message.document
#             file_name = document.file_name
#             file_size = document.file_size
            
#             # Fayl formatini tekshirish
#             if not validate_file_format(file_name):
#                 await message.reply(get_text("invalid_file", language))
#                 return
            
#             # Fayl hajmini tekshirish
#             if file_size > Config.MAX_FILE_SIZE_MB * 1024 * 1024:  # MB to bytes
#                 await message.reply(get_text("file_too_large", language))
#                 return
            
#             # Faylni yuklab olish
#             processing_msg = await message.reply(get_text("processing", language))
            
#             file_info = await self.bot.get_file(document.file_id)
#             file_content = await self.bot.download_file(file_info.file_path)
            
#             # Faylni saqlash
#             file_path = self.file_service.save_resume_file(
#                 document, message.from_user.id, file_content.read()
#             )
            
#             if not file_path:
#                 await processing_msg.edit_text(get_text("error", language))
#                 return
            
#             # Resume ni tahlil qilish
#             await processing_msg.edit_text(get_text("ai_analyzing", language))
            
#             # State dan vakansiya ma'lumotlarini olish
#             data = await state.get_data()
#             vacancy_id = data['vacancy_id']
#             vacancy = self.db.get_vacancy_by_id(vacancy_id)
            
#             # Resume matnini chiqarish
#             resume_text = self.ai_service.extract_text_from_file(file_path)
            
#             if not resume_text:
#                 await processing_msg.edit_text("❌ Resume matnini o'qib bo'lmadi!")
#                 return
            
#             # AI tahlili
#             criteria = json.loads(vacancy['criteria']) if vacancy['criteria'] else {}
#             vacancy_info = {
#                 'title': vacancy['title'],
#                 'description': vacancy['description'],
#                 'requirements': vacancy['requirements']
#             }
            
#             analysis = self.ai_service.analyze_resume(resume_text, criteria, vacancy_info)
#             match_percentage = analysis.get('match_percentage', 0)
            
#             # State ga ma'lumotlarni saqlash
#             await state.update_data(
#                 resume_path=file_path,
#                 ai_analysis=analysis,
#                 match_percentage=match_percentage
#             )
            
#             # Natijani ko'rsatish
#             await processing_msg.delete()
            
#             if match_percentage < Config.MIN_MATCH_PERCENTAGE:
#                 # Moslik darajasi past
#                 text = get_text("match_too_low", language).format(match_percentage)
                
#                 keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                     [
#                         InlineKeyboardButton(
#                             text=get_text("find_jobs", language),
#                             callback_data="jobseeker_find_jobs"
#                         )
#                     ]
#                 ])
                
#                 await message.answer(text, reply_markup=keyboard)
#                 await state.clear()
#             else:
#                 # Moslik darajasi yaxshi - suhbatga o'tish
#                 text = get_text("match_good", language).format(match_percentage)
                
#                 keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                     [
#                         InlineKeyboardButton(
#                             text=get_text("continue", language),
#                             callback_data="start_interview"
#                         )
#                     ]
#                 ])
                
#                 await message.answer(text, reply_markup=keyboard)
            
#         except Exception as e:
#             print(f"Resume yuklash xatoligi: {e}")
#             await message.reply(get_text("error", language))
    
#     async def start_interview_callback(self, callback: CallbackQuery, state: FSMContext):
#         """Suhbatni boshlash"""
#         try:
#             language = self.get_user_language(callback.from_user.id)
            
#             # State dan ma'lumotlarni olish
#             data = await state.get_data()
#             vacancy_id = data['vacancy_id']
#             vacancy = self.db.get_vacancy_by_id(vacancy_id)
            
#             # Savollarni olish
#             questions = json.loads(vacancy['questions']) if vacancy['questions'] else []
            
#             if not questions:
#                 await callback.answer("Savollar topilmadi!")
#                 return
            
#             # State ga suhbat ma'lumotlarini saqlash
#             await state.update_data(
#                 questions=questions,
#                 answers=[],
#                 current_question=0
#             )
#             await state.set_state(JobseekerStates.ANSWERING_QUESTIONS)
            
#             # Birinchi savolni ko'rsatish
#             text = get_text("interview_started", language).format(1, len(questions))
#             text += "\n\n" + get_text("question", language).format(questions[0])
            
#             await callback.message.edit_text(text)
#             await callback.answer()
            
#         except Exception as e:
#             print(f"Suhbat boshlash xatoligi: {e}")
#             await callback.answer("Xatolik yuz berdi!")
    
#     async def handle_interview_answer(self, message: Message, state: FSMContext):
#         """Suhbat javobini qayta ishlash"""
#         try:
#             language = self.get_user_language(message.from_user.id)
#             answer = message.text.strip()
            
#             if len(answer) < 10:
#                 await message.reply("❌ Javob juda qisqa! Iltimos, batafsil javob bering.")
#                 return
            
#             # State dan ma'lumotlarni olish
#             data = await state.get_data()
#             questions = data['questions']
#             answers = data['answers']
#             current_question = data['current_question']
            
#             # Javobni saqlash
#             answers.append(answer)
#             current_question += 1
            
#             if current_question < len(questions):
#                 # Keyingi savol
#                 await state.update_data(
#                     answers=answers,
#                     current_question=current_question
#                 )
                
#                 text = get_text("interview_started", language).format(current_question + 1, len(questions))
#                 text += "\n\n" + get_text("question", language).format(questions[current_question])
                
#                 await message.answer(text)
#             else:
#                 # Barcha savollar tugadi - baholash
#                 await state.update_data(answers=answers)
#                 await self.evaluate_interview(message, state, language)
            
#         except Exception as e:
#             print(f"Suhbat javobi xatoligi: {e}")
#             await message.reply(get_text("error", language))
    
#     async def evaluate_interview(self, message: Message, state: FSMContext, language: str):
#         """Suhbat javoblarini baholash"""
#         try:
#             # Baholash jarayoni
#             processing_msg = await message.answer(get_text("evaluating_answers", language))
            
#             # State dan ma'lumotlarni olish
#             data = await state.get_data()
#             vacancy_id = data['vacancy_id']
#             questions = data['questions']
#             answers = data['answers']
            
#             # Vakansiya ma'lumotlarini olish
#             vacancy = self.db.get_vacancy_by_id(vacancy_id)
#             criteria = json.loads(vacancy['criteria']) if vacancy['criteria'] else {}
#             vacancy_info = {
#                 'title': vacancy['title'],
#                 'requirements': vacancy['requirements']
#             }
            
#             # AI baholash
#             evaluation = self.ai_service.evaluate_interview_answers(
#                 questions, answers, vacancy_info, criteria
#             )
            
#             total_score = evaluation.get('total_score', 0)
#             passed = evaluation.get('passed', False)
            
#             await processing_msg.delete()
            
#             if passed:
#                 # Muvaffaqiyatli
#                 text = get_text("interview_success", language).format(total_score)
                
#                 # Qo'shimcha ma'lumotlar so'rash
#                 await state.update_data(
#                     interview_evaluation=evaluation,
#                     interview_passed=True
#                 )
#                 await self.request_additional_info(message, state, language)
#             else:
#                 # Muvaffaqiyatsiz
#                 text = get_text("interview_failed", language).format(total_score)
                
#                 keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                     [
#                         InlineKeyboardButton(
#                             text=get_text("find_jobs", language),
#                             callback_data="jobseeker_find_jobs"
#                         )
#                     ]
#                 ])
                
#                 await message.answer(text, reply_markup=keyboard)
                
#                 # Application ni rad etilgan deb belgilash
#                 user = self.db.get_user_by_telegram_id(message.from_user.id)
#                 application_data = {
#                     'vacancy_id': vacancy_id,
#                     'jobseeker_id': user['id'],
#                     'resume_path': data['resume_path'],
#                     'ai_analysis': data['ai_analysis'],
#                     'match_percentage': data['match_percentage']
#                 }
                
#                 app_id = self.db.create_job_application(application_data)
#                 self.db.update_application_status(app_id, 'rejected', {
#                     'answers': answers,
#                     'score': total_score
#                 })
                
#                 await state.clear()
            
#         except Exception as e:
#             print(f"Suhbat baholash xatoligi: {e}")
#             await message.answer(get_text("error", language))
    
#     async def request_additional_info(self, message: Message, state: FSMContext, language: str):
#         """Qo'shimcha ma'lumotlar so'rash"""
#         try:
#             text = get_text("additional_info", language) + "\n\n"
#             text += get_text("full_name", language)
            
#             await state.set_state(JobseekerStates.PROVIDING_INFO_NAME)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Qo'shimcha ma'lumotlar so'rash xatoligi: {e}")
    
#     async def handle_full_name(self, message: Message, state: FSMContext):
#         """To'liq ismni qayta ishlash"""
#         try:
#             full_name = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             if len(full_name) < 3:
#                 await message.reply("❌ Ism juda qisqa!")
#                 return
            
#             await state.update_data(full_name=full_name)
#             await state.set_state(JobseekerStates.PROVIDING_INFO_AGE)
            
#             text = get_text("age", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"To'liq ism xatoligi: {e}")
    
#     async def handle_age(self, message: Message, state: FSMContext):
#         """Yoshni qayta ishlash"""
#         try:
#             age_text = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             try:
#                 age = int(age_text)
#                 if age < 16 or age > 80:
#                     raise ValueError
#             except ValueError:
#                 await message.reply("❌ Yoshni to'g'ri kiriting (16-80 oralig'ida)!")
#                 return
            
#             await state.update_data(age=age)
#             await state.set_state(JobseekerStates.PROVIDING_INFO_PHONE)
            
#             text = get_text("phone_number", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Yosh xatoligi: {e}")
    
#     async def handle_phone(self, message: Message, state: FSMContext):
#         """Telefon raqamini qayta ishlash"""
#         try:
#             phone = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Telefon raqam validatsiyasi (oddiy)
#             if len(phone) < 9:
#                 await message.reply("❌ Telefon raqamini to'g'ri kiriting!")
#                 return
            
#             await state.update_data(phone=phone)
#             await state.set_state(JobseekerStates.PROVIDING_INFO_EMAIL)
            
#             text = get_text("email", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Telefon raqam xatoligi: {e}")
    
#     async def handle_email(self, message: Message, state: FSMContext):
#         """Email ni qayta ishlash"""
#         try:
#             email = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
            
#             # Email validatsiyasi (oddiy)
#             if '@' not in email or '.' not in email:
#                 await message.reply("❌ Email manzilini to'g'ri kiriting!")
#                 return
            
#             await state.update_data(email=email)
#             await state.set_state(JobseekerStates.PROVIDING_INFO_ADDRESS)
            
#             text = get_text("address", language)
#             await message.answer(text)
            
#         except Exception as e:
#             print(f"Email xatoligi: {e}")
    
#     async def handle_address(self, message: Message, state: FSMContext):
#         """Manzilni qayta ishlash va arizani yakunlash"""
#         try:
#             address = message.text.strip()
#             language = self.get_user_language(message.from_user.id)
#             user_id = message.from_user.id
            
#             # Ma'lumotni saqlash
#             await state.update_data(address=address)
            
#             # Barcha ma'lumotlarni olish
#             data = await state.get_data()
            
#             # Job application yaratish
#             user = self.db.get_user_by_telegram_id(user_id)
            
#             application_data = {
#                 'vacancy_id': data['vacancy_id'],
#                 'jobseeker_id': user['id'],
#                 'resume_path': data['resume_path'],
#                 'ai_analysis': data['ai_analysis'],
#                 'match_percentage': data['match_percentage']
#             }
            
#             app_id = self.db.create_job_application(application_data)
            
#             # Suhbat natijalarini saqlash
#             self.db.update_application_status(app_id, 'accepted', {
#                 'answers': data['answers'],
#                 'score': data['interview_evaluation']['total_score']
#             })
            
#             # User profile yaratish yoki yangilash
#             profile_data = {
#                 'full_name': data['full_name'],
#                 'age': data['age'],
#                 'phone': data['phone'],
#                 'email': data['email'],
#                 'address': address
#             }
            
#             # Profile ma'lumotlarini saqlash (simplified)
#             # Bu yerda user_profiles jadvaliga yozish logikasi bo'lishi kerak
            
#             # Muvaffaqiyat xabari
#             text = get_text("info_saved", language)
            
#             keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                 [
#                     InlineKeyboardButton(
#                         text=get_text("find_jobs", language),
#                         callback_data="jobseeker_find_jobs"
#                     )
#                 ]
#             ])
            
#             await message.answer(text, reply_markup=keyboard)
            
#             # Ish beruvchiga xabar yuborish
#             await self.notify_employer(data, profile_data)
            
#             # State ni tozalash
#             await state.clear()
            
#         except Exception as e:
#             print(f"Manzil xatoligi: {e}")
#             await message.reply(get_text("error", language))
    
#     async def notify_employer(self, application_data: dict, profile_data: dict):
#         """Ish beruvchiga nomzod haqida xabar yuborish"""
#         try:
#             vacancy_id = application_data['vacancy_id']
#             vacancy = self.db.get_vacancy_by_id(vacancy_id)
            
#             # Ish beruvchi telegram ID sini olish
#             employer = self.db.get_user_by_telegram_id(vacancy['employer_id'])
            
#             if employer:
#                 language = employer.get('language', 'uz')
                
#                 # Xabar matni
#                 text = f"""🎉 Yangi nomzod!
                
# 📌 Vakansiya: {vacancy['title']}
# 👤 Nomzod: {profile_data['full_name']}
# 📊 Moslik: {application_data['match_percentage']}%
# 📞 Telefon: {profile_data['phone']}
# 📧 Email: {profile_data['email']}
# 📍 Manzil: {profile_data['address']}
# 🎂 Yosh: {profile_data['age']}

# Resume fayli va batafsil ma'lumotlar admin paneldan ko'rish mumkin."""
                
#                 await self.bot.send_message(employer['telegram_id'], text)
                
#         except Exception as e:
#             print(f"Ish beruvchiga xabar yuborish xatoligi: {e}")
    
#     async def show_my_applications(self, chat_id: int, user_id: int, language: str):
#         """Mening arizalarimni ko'rsatish"""
#         try:
#             # Bu funksiya keyinchalik implement qilinadi
#             text = "Bu funksiya hali ishlab chiqilmoqda!"
#             await self.bot.send_message(chat_id, text)
            
#         except Exception as e:
#             print(f"Arizalar ro'yxati xatoligi: {e}")


# -*- coding: utf-8 -*-

import json
import logging
import re
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
# JOBSEEKER STATES - Yangi Database uchun
# ===========================================

class JobseekerStates(StatesGroup):
    """Ishga topshiruvchi holatlari"""
    
    # Resume yuklash jarayoni
    UPLOADING_RESUME = State()
    RESUME_ANALYSIS_PENDING = State()
    
    # Interview jarayoni
    ANSWERING_QUESTIONS = State()
    INTERVIEW_EVALUATION = State()
    
    # Qo'shimcha ma'lumotlar
    PROVIDING_ADDITIONAL_INFO = State()
    PROVIDING_FULL_NAME = State()
    PROVIDING_AGE = State()
    PROVIDING_PHONE = State()
    PROVIDING_EMAIL = State()
    PROVIDING_ADDRESS = State()
    
    # Final confirmation
    FINAL_CONFIRMATION = State()

# ===========================================
# JOBSEEKER HANDLERS CLASS
# ===========================================

class JobseekerHandlers:
    """Ishga topshiruvchi handlerlari - Professional version"""
    
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
        
        # Jobseeker callback handlers
        @self.router.callback_query(F.data.startswith('jobseeker_'))
        async def jobseeker_callbacks(callback: CallbackQuery, state: FSMContext):
            await self.handle_jobseeker_callbacks(callback, state)
        
        # Company selection
        @self.router.callback_query(F.data.startswith('select_company_'))
        async def select_company_callback(callback: CallbackQuery):
            await self.handle_select_company_callback(callback)
        
        # Vacancy selection and application
        @self.router.callback_query(F.data.startswith('select_vacancy_'))
        async def select_vacancy_callback(callback: CallbackQuery):
            await self.handle_select_vacancy_callback(callback)
        
        @self.router.callback_query(F.data.startswith('apply_vacancy_'))
        async def apply_vacancy_callback(callback: CallbackQuery, state: FSMContext):
            await self.handle_apply_vacancy_callback(callback, state)
        
        # Resume upload handlers
        @self.router.message(StateFilter(JobseekerStates.UPLOADING_RESUME), F.document)
        async def handle_resume_upload(message: Message, state: FSMContext):
            await self.handle_resume_upload(message, state)
        
        @self.router.message(StateFilter(JobseekerStates.UPLOADING_RESUME))
        async def handle_invalid_resume_format(message: Message):
            await self.handle_invalid_resume_format(message)
        
        # Interview handlers
        @self.router.callback_query(F.data == 'start_interview')
        async def start_interview_callback(callback: CallbackQuery, state: FSMContext):
            await self.handle_start_interview_callback(callback, state)
        
        @self.router.message(StateFilter(JobseekerStates.ANSWERING_QUESTIONS))
        async def handle_interview_answer(message: Message, state: FSMContext):
            await self.handle_interview_answer(message, state)
        
        # Additional information handlers
        @self.router.callback_query(F.data == 'provide_additional_info')
        async def provide_additional_info_callback(callback: CallbackQuery, state: FSMContext):
            await self.handle_provide_additional_info_callback(callback, state)
        
        @self.router.message(StateFilter(JobseekerStates.PROVIDING_FULL_NAME))
        async def handle_full_name(message: Message, state: FSMContext):
            await self.handle_full_name(message, state)
        
        @self.router.message(StateFilter(JobseekerStates.PROVIDING_AGE))
        async def handle_age(message: Message, state: FSMContext):
            await self.handle_age(message, state)
        
        @self.router.message(StateFilter(JobseekerStates.PROVIDING_PHONE))
        async def handle_phone(message: Message, state: FSMContext):
            await self.handle_phone(message, state)
        
        @self.router.message(StateFilter(JobseekerStates.PROVIDING_EMAIL))
        async def handle_email(message: Message, state: FSMContext):
            await self.handle_email(message, state)
        
        @self.router.message(StateFilter(JobseekerStates.PROVIDING_ADDRESS))
        async def handle_address(message: Message, state: FSMContext):
            await self.handle_address(message, state)
        
        # Application management
        @self.router.callback_query(F.data.startswith('view_my_application_'))
        async def view_my_application_callback(callback: CallbackQuery):
            await self.handle_view_my_application_callback(callback)
        
        # Cancel handlers
        @self.router.callback_query(F.data == 'cancel_application')
        async def cancel_application(callback: CallbackQuery, state: FSMContext):
            await self.handle_cancel_application(callback, state)
    
    # ===========================================
    # MAIN CALLBACK HANDLER
    # ===========================================
    
    async def handle_callback(self, callback: CallbackQuery, state: FSMContext):
        """Jobseeker callback handlerlarini boshqarish"""
        try:
            await self.handle_jobseeker_callbacks(callback, state)
        except Exception as e:
            logger.error(f"Jobseeker callback xatoligi: {e}")
            await callback.answer("❌ Xatolik yuz berdi")
    
    async def handle_message(self, message: Message, state: FSMContext):
        """Jobseeker message handlerlarini boshqarish"""
        # Bu yerda specific message handling bo'ladi
        # Hozircha register_handlers da handle qilinadi
        pass
    
    async def handle_jobseeker_callbacks(self, callback: CallbackQuery, state: FSMContext):
        """Jobseeker callback handlerini asosiy boshqaruvchi"""
        try:
            action = callback.data.replace('jobseeker_', '')
            user_id = callback.from_user.id
            language = self.get_user_language(user_id)
            
            # Analytics
            user = self.get_user_by_telegram_id(user_id)
            if user:
                self.crud['analytics'].log_user_action(
                    user_id=user['user_id'], 
                    action=f'jobseeker_{action}'
                )
            
            if action == 'find_jobs':
                await self.show_companies(callback.message.chat.id, user_id, language)
            elif action == 'applications':
                await self.show_my_applications(callback.message.chat.id, user_id, language)
            
            await callback.answer()
            
        except Exception as e:
            logger.error(f"Jobseeker callback xatoligi: {e}")
            await callback.answer("❌ Xatolik yuz berdi")
    
    # ===========================================
    # COMPANY AND VACANCY BROWSING
    # ===========================================
    
    async def show_companies(self, chat_id: int, user_id: int, language: str):
        """Kompaniyalar ro'yxatini ko'rsatish"""
        try:
            # Aktiv vakansiyalari bo'lgan kompaniyalarni olish
            companies = self.crud['company'].get_companies_with_active_vacancies()
            
            if not companies:
                text = get_text("no_active_companies", language)
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=get_text("btn_back", language),
                            callback_data="back_main"
                        )
                    ]
                ])
                await self.bot.send_message(chat_id, text, reply_markup=keyboard)
                return
            
            text = get_text("select_company", language) + "\n\n"
            text += get_text("available_companies", language).format(len(companies))
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
            for company in companies:
                # Kompaniya vakansiyalari sonini ko'rsatish
                vacancy_count = self.crud['vacancy'].count_active_vacancies_by_company(company['company_id'])
                button_text = f"🏢 {company['name']} ({vacancy_count} ta vakansiya)"
                
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(
                        text=button_text,
                        callback_data=f"select_company_{company['company_id']}"
                    )
                ])
            
            keyboard.inline_keyboard.append([
                InlineKeyboardButton(
                    text=get_text("btn_back", language),
                    callback_data="back_main"
                )
            ])
            
            await self.bot.send_message(chat_id, text, reply_markup=keyboard)
            
            # Analytics
            user = self.get_user_by_telegram_id(user_id)
            if user:
                self.crud['analytics'].log_user_action(
                    user_id=user['user_id'], 
                    action='companies_viewed',
                    data={'companies_count': len(companies)}
                )
            
            logger.info(f"Kompaniyalar ko'rsatildi: {user_id}, {len(companies)} kompaniya")
            
        except Exception as e:
            logger.error(f"Kompaniyalar ro'yxati xatoligi: {e}")
            await self.bot.send_message(chat_id, get_text("error", language))
    
    async def handle_select_company_callback(self, callback: CallbackQuery):
        """Kompaniya tanlash callback"""
        try:
            company_id = int(callback.data.split('_')[2])
            language = self.get_user_language(callback.from_user.id)
            
            # Kompaniya ma'lumotlarini olish
            company = self.crud['company'].get_company_by_id(company_id)
            if not company:
                await callback.answer(get_text("company_not_found", language))
                return
            
            # Kompaniya vakansiyalarini olish
            vacancies = self.crud['vacancy'].get_active_vacancies_by_company(company_id)
            
            if not vacancies:
                text = get_text("no_active_vacancies", language).format(company['name'])
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=get_text("btn_back", language),
                            callback_data="jobseeker_find_jobs"
                        )
                    ]
                ])
                await callback.message.edit_text(text, reply_markup=keyboard)
                await callback.answer()
                return
            
            # Kompaniya va vakansiyalar ma'lumotini ko'rsatish
            text = get_text("company_info", language).format(
                name=company['name'],
                description=company.get('description', get_text("no_description", language)),
                vacancy_count=len(vacancies)
            )
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
            for vacancy in vacancies:
                # Vakansiya tugmasi
                salary_info = ""
                if vacancy.get('salary_min') and vacancy.get('salary_max'):
                    salary_info = f" 💰 {vacancy['salary_min']}-{vacancy['salary_max']}"
                elif vacancy.get('salary_min'):
                    salary_info = f" 💰 {vacancy['salary_min']}+"
                
                button_text = f"📌 {vacancy['title']}{salary_info}"
                
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(
                        text=button_text,
                        callback_data=f"select_vacancy_{vacancy['vacancy_id']}"
                    )
                ])
            
            keyboard.inline_keyboard.append([
                InlineKeyboardButton(
                    text=get_text("btn_back", language),
                    callback_data="jobseeker_find_jobs"
                )
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard, parse_mode='Markdown')
            await callback.answer()
            
            logger.info(f"Kompaniya tanlandi: {callback.from_user.id} - {company_id}")
            
        except Exception as e:
            logger.error(f"Kompaniya tanlash xatoligi: {e}")
            await callback.answer("❌ Xatolik yuz berdi")
    
    async def handle_select_vacancy_callback(self, callback: CallbackQuery):
        """Vakansiya tanlash callback"""
        try:
            vacancy_id = int(callback.data.split('_')[2])
            language = self.get_user_language(callback.from_user.id)
            user_id = callback.from_user.id
            
            # Vakansiya ma'lumotlarini olish
            vacancy = self.crud['vacancy'].get_vacancy_by_id(vacancy_id)
            if not vacancy:
                await callback.answer(get_text("vacancy_not_found", language))
                return
            
            # Kompaniya ma'lumotlarini olish
            company = self.crud['company'].get_company_by_id(vacancy['company_id'])
            
            # Allaqachon ariza berganligini tekshirish
            user = self.get_user_by_telegram_id(user_id)
            if user and self.crud['application'].check_existing_application(vacancy_id, user['user_id']):
                text = get_text("already_applied", language)
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=get_text("my_applications", language),
                            callback_data="jobseeker_applications"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text=get_text("btn_back", language),
                            callback_data=f"select_company_{vacancy['company_id']}"
                        )
                    ]
                ])
                await callback.message.edit_text(text, reply_markup=keyboard)
                await callback.answer()
                return
            
            # Vakansiya tafsilotlarini formatlash
            text = get_text("vacancy_full_details", language).format(
                title=vacancy['title'],
                company_name=company['name'] if company else "N/A",
                description=vacancy['description'],
                requirements=vacancy['requirements'],
                responsibilities=vacancy['responsibilities'],
                work_type=get_text(f"work_type_{vacancy['work_type']}", language) if vacancy.get('work_type') else "N/A",
                work_schedule=get_text(f"work_schedule_{vacancy['work_schedule']}", language) if vacancy.get('work_schedule') else "N/A",
                location=vacancy.get('location', get_text("location_not_specified", language)),
                experience_years=vacancy.get('experience_years', 0),
                salary=self._format_salary(vacancy, language)
            )
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("apply_now", language),
                        callback_data=f"apply_vacancy_{vacancy_id}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=get_text("btn_back", language),
                        callback_data=f"select_company_{vacancy['company_id']}"
                    )
                ]
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard, parse_mode='Markdown')
            await callback.answer()
            
            # Analytics
            if user:
                self.crud['analytics'].log_user_action(
                    user_id=user['user_id'], 
                    action='vacancy_viewed',
                    data={'vacancy_id': vacancy_id, 'company_id': vacancy['company_id']}
                )
            
            logger.info(f"Vakansiya ko'rildi: {user_id} - {vacancy_id}")
            
        except Exception as e:
            logger.error(f"Vakansiya tanlash xatoligi: {e}")
            await callback.answer("❌ Xatolik yuz berdi")
    
    def _format_salary(self, vacancy: Dict[str, Any], language: str) -> str:
        """Ish haqqini formatlash"""
        try:
            salary_min = vacancy.get('salary_min')
            salary_max = vacancy.get('salary_max')
            currency = vacancy.get('currency', 'UZS')
            
            if salary_min and salary_max:
                return f"{salary_min:,} - {salary_max:,} {currency}"
            elif salary_min:
                return f"{salary_min:,}+ {currency}"
            elif salary_max:
                return f"{get_text('up_to', language)} {salary_max:,} {currency}"
            else:
                return get_text("salary_negotiable", language)
        except Exception:
            return get_text("salary_not_specified", language)
    
    # ===========================================
    # APPLICATION PROCESS
    # ===========================================
    
    async def handle_apply_vacancy_callback(self, callback: CallbackQuery, state: FSMContext):
        """Vakansiyaga ariza berish boshlash"""
        try:
            vacancy_id = int(callback.data.split('_')[2])
            language = self.get_user_language(callback.from_user.id)
            user_id = callback.from_user.id
            
            # Qayta ariza berish oldini olish
            user = self.get_user_by_telegram_id(user_id)
            if user and self.crud['application'].check_existing_application(vacancy_id, user['user_id']):
                await callback.answer(get_text("already_applied", language))
                return
            
            # Kunlik ariza limitini tekshirish
            if user:
                daily_applications = self.crud['application'].count_daily_applications(user['user_id'])
                if daily_applications >= Config.MAX_APPLICATIONS_PER_DAY:
                    text = get_text("daily_limit_exceeded", language).format(Config.MAX_APPLICATIONS_PER_DAY)
                    await callback.message.edit_text(text)
                    await callback.answer()
                    return
            
            # State ga vakansiya ID ni saqlash
            await state.update_data(
                vacancy_id=vacancy_id,
                application_started_at=datetime.now().isoformat()
            )
            await state.set_state(JobseekerStates.UPLOADING_RESUME)
            
            # Resume yuklashni so'rash
            text = get_text("upload_resume_prompt", language)
            text += "\n\n" + get_text("supported_formats", language)
            text += f"\n📏 {get_text('max_file_size', language)}: {Config.MAX_FILE_SIZE_MB}MB"
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("btn_cancel", language),
                        callback_data="cancel_application"
                    )
                ]
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard)
            await callback.answer()
            
            # Analytics
            if user:
                self.crud['analytics'].log_user_action(
                    user_id=user['user_id'], 
                    action='application_started',
                    data={'vacancy_id': vacancy_id}
                )
            
            logger.info(f"Ariza jarayoni boshlandi: {user_id} - {vacancy_id}")
            
        except Exception as e:
            logger.error(f"Ariza berish boshlash xatoligi: {e}")
            await callback.answer("❌ Xatolik yuz berdi")
    
    async def handle_resume_upload(self, message: Message, state: FSMContext):
        """Resume fayl yuklashni qayta ishlash"""
        try:
            language = self.get_user_language(message.from_user.id)
            user_id = message.from_user.id
            
            # Fayl ma'lumotlarini olish
            document = message.document
            if not document:
                await message.reply(get_text("no_file_received", language))
                return
            
            file_name = document.file_name
            file_size = document.file_size
            
            # Fayl formatini tekshirish
            if not self._validate_file_format(file_name):
                await message.reply(get_text("invalid_file_format", language))
                return
            
            # Fayl hajmini tekshirish
            if file_size > Config.MAX_FILE_SIZE_BYTES:
                size_mb = file_size / (1024 * 1024)
                await message.reply(get_text("file_too_large", language).format(
                    current_size=f"{size_mb:.1f}",
                    max_size=Config.MAX_FILE_SIZE_MB
                ))
                return
            
            # Processing xabari
            processing_msg = await message.reply(get_text("processing_resume", language))
            
            try:
                # Faylni yuklab olish
                file_info = await self.bot.get_file(document.file_id)
                downloaded_file = await self.bot.download_file(file_info.file_path)
                
                # Faylni saqlash
                file_path = self.file_service.save_resume_file(
                    file_name, user_id, downloaded_file.read()
                )
                
                if not file_path:
                    await processing_msg.edit_text(get_text("file_save_error", language))
                    return
                
                # Resume ni parse qilish
                await processing_msg.edit_text(get_text("parsing_resume", language))
                
                parsed_data = await self.ai_service.parse_resume(file_path)
                if not parsed_data:
                    await processing_msg.edit_text(get_text("resume_parse_error", language))
                    return
                
                # Vakansiya kriteriyalari bilan taqqoslash
                await processing_msg.edit_text(get_text("analyzing_compatibility", language))
                
                data = await state.get_data()
                vacancy_id = data['vacancy_id']
                vacancy = self.crud['vacancy'].get_vacancy_by_id(vacancy_id)
                
                if not vacancy:
                    await processing_msg.edit_text(get_text("vacancy_not_found", language))
                    return
                
                # AI tahlil
                ai_analysis = await self.ai_service.analyze_resume_compatibility(
                    parsed_data, 
                    vacancy['ai_criteria'], 
                    vacancy['ai_prompt']
                )
                
                compatibility_score = ai_analysis.get('compatibility_score', 0)
                
                # Ma'lumotlarni state ga saqlash
                await state.update_data(
                    resume_file_path=file_path,
                    parsed_resume_data=parsed_data,
                    ai_analysis=ai_analysis,
                    compatibility_score=compatibility_score
                )
                
                await processing_msg.delete()
                
                # Natijani ko'rsatish
                if compatibility_score < Config.MIN_MATCH_PERCENTAGE:
                    # Moslik darajasi past
                    text = get_text("compatibility_too_low", language).format(
                        score=compatibility_score,
                        min_required=Config.MIN_MATCH_PERCENTAGE
                    )
                    
                    # Rad etish sabablarini ko'rsatish
                    if ai_analysis.get('rejection_reasons'):
                        text += "\n\n" + get_text("rejection_reasons", language) + ":\n"
                        for reason in ai_analysis['rejection_reasons']:
                            text += f"• {reason}\n"
                    
                    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text=get_text("find_other_jobs", language),
                                callback_data="jobseeker_find_jobs"
                            )
                        ]
                    ])
                    
                    await message.answer(text, reply_markup=keyboard)
                    
                    # Rad etilgan arizani saqlash
                    await self._save_rejected_application(user_id, state, "low_compatibility")
                    await state.clear()
                    
                else:
                    # Moslik darajasi yaxshi - interview ga o'tish
                    text = get_text("compatibility_good", language).format(
                        score=compatibility_score
                    )
                    
                    # AI tahlil natijalarini ko'rsatish
                    if ai_analysis.get('strengths'):
                        text += "\n\n✅ " + get_text("strengths", language) + ":\n"
                        for strength in ai_analysis['strengths'][:3]:  # Birinchi 3 ta
                            text += f"• {strength}\n"
                    
                    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text=get_text("continue_to_interview", language),
                                callback_data="start_interview"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text=get_text("btn_cancel", language),
                                callback_data="cancel_application"
                            )
                        ]
                    ])
                    
                    await message.answer(text, reply_markup=keyboard)
                
                # Analytics
                user = self.get_user_by_telegram_id(user_id)
                if user:
                    self.crud['analytics'].log_user_action(
                        user_id=user['user_id'], 
                        action='resume_analyzed',
                        data={
                            'vacancy_id': vacancy_id,
                            'compatibility_score': compatibility_score,
                            'file_size': file_size,
                            'file_name': file_name
                        }
                    )
                
                logger.info(f"Resume tahlil qilindi: {user_id}, moslik: {compatibility_score}%")
                
            except Exception as e:
                logger.error(f"Resume qayta ishlash xatoligi: {e}")
                await processing_msg.edit_text(get_text("processing_error", language))
                
        except Exception as e:
            logger.error(f"Resume yuklash xatoligi: {e}")
            await message.reply(get_text("error", language))
    
    async def handle_invalid_resume_format(self, message: Message):
        """Noto'g'ri fayl formatini handle qilish"""
        language = self.get_user_language(message.from_user.id)
        
        text = get_text("invalid_file_format", language)
        text += "\n\n" + get_text("supported_formats", language)
        text += f"\n📏 {get_text('max_file_size', language)}: {Config.MAX_FILE_SIZE_MB}MB"
        
        await message.reply(text)
    
    def _validate_file_format(self, filename: str) -> bool:
        """Fayl formatini tekshirish"""
        if not filename:
            return False
        
        file_extension = filename.lower().split('.')[-1]
        return f".{file_extension}" in Config.ALLOWED_FILE_EXTENSIONS
    
    # ===========================================
    # INTERVIEW PROCESS
    # ===========================================
    
    async def handle_start_interview_callback(self, callback: CallbackQuery, state: FSMContext):
        """Suhbatni boshlash callback"""
        try:
            language = self.get_user_language(callback.from_user.id)
            user_id = callback.from_user.id
            
            # State dan ma'lumotlarni olish
            data = await state.get_data()
            vacancy_id = data['vacancy_id']
            
            # Vakansiya savollarini olish
            vacancy = self.crud['vacancy'].get_vacancy_by_id(vacancy_id)
            if not vacancy:
                await callback.answer(get_text("vacancy_not_found", language))
                return
            
            questions = json.loads(vacancy.get('questions', '[]'))
            if not questions:
                # Savollar yo'q - to'g'ridan-to'g'ri qo'shimcha ma'lumotlarga o'tish
                await self._skip_to_additional_info(callback, state, language)
                return
            
            # Interview session yaratish
            interview_data = {
                'questions': questions,
                'answers': [],
                'current_question': 0,
                'started_at': datetime.now().isoformat()
            }
            
            await state.update_data(**interview_data)
            await state.set_state(JobseekerStates.ANSWERING_QUESTIONS)
            
            # Birinchi savolni ko'rsatish
            text = get_text("interview_started", language).format(
                current=1,
                total=len(questions)
            )
            text += "\n\n" + get_text("current_question", language) + f":\n\n{questions[0]}"
            text += "\n\n" + get_text("interview_instructions", language)
            
            await callback.message.edit_text(text)
            await callback.answer()
            
            # Analytics
            user = self.get_user_by_telegram_id(user_id)
            if user:
                self.crud['analytics'].log_user_action(
                    user_id=user['user_id'], 
                    action='interview_started',
                    data={'vacancy_id': vacancy_id, 'questions_count': len(questions)}
                )
            
            logger.info(f"Suhbat boshlandi: {user_id}, {len(questions)} savol")
            
        except Exception as e:
            logger.error(f"Suhbat boshlash xatoligi: {e}")
            await callback.answer("❌ Xatolik yuz berdi")
    
    async def handle_interview_answer(self, message: Message, state: FSMContext):
        """Suhbat javobini qayta ishlash"""
        try:
            language = self.get_user_language(message.from_user.id)
            user_id = message.from_user.id
            answer = message.text.strip()
            
            # Javob uzunligini tekshirish
            if len(answer) < 10:
                await message.reply(get_text("answer_too_short", language))
                return
            
            if len(answer) > 1000:
                await message.reply(get_text("answer_too_long", language))
                return
            
            # State dan ma'lumotlarni olish
            data = await state.get_data()
            questions = data.get('questions', [])
            answers = data.get('answers', [])
            current_question = data.get('current_question', 0)
            
            # Javobni saqlash
            answers.append({
                'question': questions[current_question],
                'answer': answer,
                'answered_at': datetime.now().isoformat()
            })
            
            current_question += 1
            
            if current_question < len(questions):
                # Keyingi savol
                await state.update_data(
                    answers=answers,
                    current_question=current_question
                )
                
                text = get_text("interview_progress", language).format(
                    current=current_question + 1,
                    total=len(questions)
                )
                text += "\n\n" + get_text("current_question", language) + f":\n\n{questions[current_question]}"
                
                await message.answer(text)
            else:
                # Barcha savollar tugadi - baholash
                await state.update_data(answers=answers)
                await self._evaluate_interview(message, state, language)
            
        except Exception as e:
            logger.error(f"Suhbat javobi xatoligi: {e}")
            await message.reply(get_text("error", language))
    
    async def _evaluate_interview(self, message: Message, state: FSMContext, language: str):
        """Suhbat javoblarini baholash"""
        try:
            # Baholash jarayoni
            processing_msg = await message.answer(get_text("evaluating_interview", language))
            user_id = message.from_user.id
            
            # State dan ma'lumotlarni olish
            data = await state.get_data()
            vacancy_id = data['vacancy_id']
            answers = data['answers']
            
            # Vakansiya ma'lumotlarini olish
            vacancy = self.crud['vacancy'].get_vacancy_by_id(vacancy_id)
            if not vacancy:
                await processing_msg.edit_text(get_text("vacancy_not_found", language))
                return
            
            # AI baholash
            evaluation_result = await self.ai_service.evaluate_interview_answers(
                answers, 
                vacancy['ai_criteria'], 
                vacancy['ai_prompt'],
                vacancy
            )
            
            interview_score = evaluation_result.get('overall_score', 0)
            passed = evaluation_result.get('passed', False)
            
            await processing_msg.delete()
            
            # Ma'lumotlarni state ga saqlash
            await state.update_data(
                interview_evaluation=evaluation_result,
                interview_score=interview_score,
                interview_passed=passed
            )
            
            if passed:
                # Suhbat muvaffaqiyatli
                text = get_text("interview_passed", language).format(score=interview_score)
                
                # Ijobiy taraflarni ko'rsatish
                if evaluation_result.get('positive_aspects'):
                    text += "\n\n✅ " + get_text("positive_aspects", language) + ":\n"
                    for aspect in evaluation_result['positive_aspects'][:3]:
                        text += f"• {aspect}\n"
                
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=get_text("provide_additional_info", language),
                            callback_data="provide_additional_info"
                        )
                    ]
                ])
                
                await message.answer(text, reply_markup=keyboard)
                
            else:
                # Suhbat muvaffaqiyatsiz
                text = get_text("interview_failed", language).format(
                    score=interview_score,
                    min_required=Config.MIN_INTERVIEW_SCORE
                )
                
                # Kamchiliklarni ko'rsatish
                if evaluation_result.get('improvement_areas'):
                    text += "\n\n📝 " + get_text("improvement_areas", language) + ":\n"
                    for area in evaluation_result['improvement_areas'][:3]:
                        text += f"• {area}\n"
                
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=get_text("find_other_jobs", language),
                            callback_data="jobseeker_find_jobs"
                        )
                    ]
                ])
                
                await message.answer(text, reply_markup=keyboard)
                
                # Rad etilgan arizani saqlash
                await self._save_rejected_application(user_id, state, "interview_failed")
                await state.clear()
            
            # Analytics
            user = self.get_user_by_telegram_id(user_id)
            if user:
                self.crud['analytics'].log_user_action(
                    user_id=user['user_id'], 
                    action='interview_evaluated',
                    data={
                        'vacancy_id': vacancy_id,
                        'interview_score': interview_score,
                        'passed': passed,
                        'answers_count': len(answers)
                    }
                )
            
            logger.info(f"Suhbat baholandi: {user_id}, ball: {interview_score}, o'tdi: {passed}")
            
        except Exception as e:
            logger.error(f"Suhbat baholash xatoligi: {e}")
            await message.answer(get_text("evaluation_error", language))
    
    async def _skip_to_additional_info(self, callback: CallbackQuery, state: FSMContext, language: str):
        """Savollar yo'q bo'lsa to'g'ridan-to'g'ri qo'shimcha ma'lumotlarga o'tish"""
        try:
            await state.update_data(
                interview_passed=True,
                interview_score=100,  # Savollar yo'q bo'lgani uchun maksimal ball
                interview_evaluation={'passed': True, 'overall_score': 100}
            )
            
            text = get_text("no_interview_questions", language)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("provide_additional_info", language),
                        callback_data="provide_additional_info"
                    )
                ]
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard)
            
        except Exception as e:
            logger.error(f"Qo'shimcha ma'lumotlarga o'tish xatoligi: {e}")
    
    # ===========================================
    # ADDITIONAL INFORMATION COLLECTION
    # ===========================================
    
    async def handle_provide_additional_info_callback(self, callback: CallbackQuery, state: FSMContext):
        """Qo'shimcha ma'lumot berish boshlash"""
        try:
            language = self.get_user_language(callback.from_user.id)
            
            text = get_text("additional_info_intro", language) + "\n\n"
            text += get_text("full_name_prompt", language)
            
            await state.set_state(JobseekerStates.PROVIDING_FULL_NAME)
            await callback.message.edit_text(text)
            await callback.answer()
            
        except Exception as e:
            logger.error(f"Qo'shimcha ma'lumot boshlash xatoligi: {e}")
    
    async def handle_full_name(self, message: Message, state: FSMContext):
        """To'liq ismni qayta ishlash"""
        try:
            full_name = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Validatsiya
            if len(full_name) < 3:
                await message.reply(get_text("name_too_short", language))
                return
            
            if len(full_name) > 100:
                await message.reply(get_text("name_too_long", language))
                return
            
            # Faqat harflar va bo'shliq
            if not re.match(r'^[a-zA-Zа-яА-Я\s\'`-]+$', full_name):
                await message.reply(get_text("invalid_name_format", language))
                return
            
            await state.update_data(full_name=full_name)
            await state.set_state(JobseekerStates.PROVIDING_AGE)
            
            text = get_text("age_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"To'liq ism xatoligi: {e}")
    
    async def handle_age(self, message: Message, state: FSMContext):
        """Yoshni qayta ishlash"""
        try:
            age_text = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            try:
                age = int(age_text)
                if age < 16 or age > 80:
                    raise ValueError
            except ValueError:
                await message.reply(get_text("invalid_age", language))
                return
            
            await state.update_data(age=age)
            await state.set_state(JobseekerStates.PROVIDING_PHONE)
            
            text = get_text("phone_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"Yosh xatoligi: {e}")
    
    async def handle_phone(self, message: Message, state: FSMContext):
        """Telefon raqamini qayta ishlash"""
        try:
            phone = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Telefon raqam validatsiyasi
            phone_clean = re.sub(r'[^\d+]', '', phone)
            if len(phone_clean) < 9 or len(phone_clean) > 15:
                await message.reply(get_text("invalid_phone", language))
                return
            
            await state.update_data(phone=phone_clean)
            await state.set_state(JobseekerStates.PROVIDING_EMAIL)
            
            text = get_text("email_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"Telefon raqam xatoligi: {e}")
    
    async def handle_email(self, message: Message, state: FSMContext):
        """Email ni qayta ishlash"""
        try:
            email = message.text.strip().lower()
            language = self.get_user_language(message.from_user.id)
            
            # Email validatsiyasi
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, email):
                await message.reply(get_text("invalid_email", language))
                return
            
            await state.update_data(email=email)
            await state.set_state(JobseekerStates.PROVIDING_ADDRESS)
            
            text = get_text("address_prompt", language)
            await message.answer(text)
            
        except Exception as e:
            logger.error(f"Email xatoligi: {e}")
    
    async def handle_address(self, message: Message, state: FSMContext):
        """Manzil va arizani yakunlash"""
        try:
            address = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            user_id = message.from_user.id
            
            if len(address) < 5:
                await message.reply(get_text("address_too_short", language))
                return
            
            await state.update_data(address=address)
            
            # Arizani yakunlash
            await self._complete_application(message, state, language)
            
        except Exception as e:
            logger.error(f"Manzil va yakunlash xatoligi: {e}")
            await message.reply(get_text("error", language))
    
    async def _complete_application(self, message: Message, state: FSMContext, language: str):
        """Arizani yakunlash va saqlash"""
        try:
            user_id = message.from_user.id
            data = await state.get_data()
            
            # Foydalanuvchini olish
            user = self.get_user_by_telegram_id(user_id)
            if not user:
                await message.reply(get_text("user_not_found", language))
                return
            
            # Arizani yaratish
            application_id = self.crud['application'].create_application(
                vacancy_id=data['vacancy_id'],
                user_id=user['user_id'],
                resume_file_path=data['resume_file_path'],
                parsed_data=data['parsed_resume_data']
            )
            
            # AI tahlil natijasini yangilash
            self.crud['application'].update_ai_analysis(
                application_id=application_id,
                ai_analysis=data['ai_analysis'],
                compatibility_score=data['compatibility_score']
            )
            
            # Interview natijalarini saqlash (agar bo'lsa)
            if data.get('interview_passed'):
                interview_session_id = self.crud['interview'].create_session(
                    application_id=application_id,
                    questions=data.get('questions', []),
                    answers=data.get('answers', []),
                    evaluation=data.get('interview_evaluation', {})
                )
            
            # Foydalanuvchi profilini yangilash
            self.crud['user'].update_profile(
                user_id=user['user_id'],
                profile_data={
                    'full_name': data['full_name'],
                    'age': data['age'],
                    'phone': data['phone'],
                    'email': data['email'],
                    'address': data['address']
                }
            )
            
            # Muvaffaqiyat xabari
            text = get_text("application_completed", language).format(
                vacancy_title=self.crud['vacancy'].get_vacancy_by_id(data['vacancy_id'])['title']
            )
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("my_applications", language),
                        callback_data="jobseeker_applications"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=get_text("find_more_jobs", language),
                        callback_data="jobseeker_find_jobs"
                    )
                ]
            ])
            
            await message.answer(text, reply_markup=keyboard)
            
            # Ish beruvchiga xabar yuborish
            await self._notify_employer(data, user)
            
            # Analytics
            self.crud['analytics'].log_user_action(
                user_id=user['user_id'],
                action='application_completed',
                data={
                    'application_id': application_id,
                    'vacancy_id': data['vacancy_id'],
                    'compatibility_score': data['compatibility_score'],
                    'interview_score': data.get('interview_score', 0)
                }
            )
            
            # State ni tozalash
            await state.clear()
            
            logger.info(f"Ariza yakunlandi: {user_id} - {application_id}")
            
        except Exception as e:
            logger.error(f"Ariza yakunlash xatoligi: {e}")
            await message.reply(get_text("completion_error", language))
    
    async def _save_rejected_application(self, user_id: int, state: FSMContext, rejection_reason: str):
        """Rad etilgan arizani saqlash"""
        try:
            data = await state.get_data()
            user = self.get_user_by_telegram_id(user_id)
            
            if not user:
                return
            
            # Rad etilgan arizani yaratish
            application_id = self.crud['application'].create_application(
                vacancy_id=data['vacancy_id'],
                user_id=user['user_id'],
                resume_file_path=data.get('resume_file_path', ''),
                parsed_data=data.get('parsed_resume_data', {})
            )
            
            # Rad etish ma'lumotlarini yangilash
            self.crud['application'].update_ai_analysis(
                application_id=application_id,
                ai_analysis=data.get('ai_analysis', {}),
                compatibility_score=data.get('compatibility_score', 0)
            )
            
            # Status ni rejected ga o'rnatish
            self.crud['application'].update_status(
                application_id=application_id,
                status='rejected',
                rejection_reason=rejection_reason
            )
            
            # Analytics
            self.crud['analytics'].log_user_action(
                user_id=user['user_id'],
                action='application_rejected',
                data={
                    'application_id': application_id,
                    'vacancy_id': data['vacancy_id'],
                    'rejection_reason': rejection_reason,
                    'compatibility_score': data.get('compatibility_score', 0)
                }
            )
            
        except Exception as e:
            logger.error(f"Rad etilgan arizani saqlash xatoligi: {e}")
    
    async def _notify_employer(self, application_data: Dict[str, Any], applicant_user: Dict[str, Any]):
        """Ish beruvchiga nomzod haqida xabar yuborish"""
        try:
            vacancy_id = application_data['vacancy_id']
            vacancy = self.crud['vacancy'].get_vacancy_by_id(vacancy_id)
            
            if not vacancy:
                return
            
            # Ish beruvchini topish
            company = self.crud['company'].get_company_by_id(vacancy['company_id'])
            if not company:
                return
            
            employer = self.crud['user'].get_user_by_id(company['employer_id'])
            if not employer:
                return
            
            # Ish beruvchi tilini olish
            language = employer.get('language_code', Config.DEFAULT_LANGUAGE)
            
            # Xabar yaratish
            text = get_text("new_application_notification", language) + "\n\n"
            text += f"🏢 **{get_text('company', language)}:** {company['name']}\n"
            text += f"💼 **{get_text('vacancy', language)}:** {vacancy['title']}\n"
            text += f"👤 **{get_text('applicant', language)}:** {application_data['full_name']}\n"
            text += f"📊 **{get_text('compatibility', language)}:** {application_data['compatibility_score']}%\n"
            text += f"📞 **{get_text('phone', language)}:** {application_data['phone']}\n"
            text += f"📧 **{get_text('email', language)}:** {application_data['email']}\n"
            text += f"📍 **{get_text('address', language)}:** {application_data['address']}\n"
            text += f"🎂 **{get_text('age', language)}:** {application_data['age']}\n"
            
            if application_data.get('interview_score'):
                text += f"💬 **{get_text('interview_score', language)}:** {application_data['interview_score']}%\n"
            
            text += f"\n📅 **{get_text('applied_at', language)}:** {datetime.now().strftime('%d.%m.%Y %H:%M')}\n\n"
            text += get_text("view_full_details_in_panel", language)
            
            # Ish beruvchiga yuborish
            await self.bot.send_message(
                chat_id=employer['telegram_id'],
                text=text,
                parse_mode='Markdown'
            )
            
            logger.info(f"Ish beruvchiga xabar yuborildi: {employer['telegram_id']}")
            
        except Exception as e:
            logger.error(f"Ish beruvchiga xabar yuborish xatoligi: {e}")
    
    # ===========================================
    # APPLICATION MANAGEMENT
    # ===========================================
    
    async def show_my_applications(self, chat_id: int, user_id: int, language: str):
        """Mening arizalarimni ko'rsatish"""
        try:
            user = self.db.get_user_by_telegram_id(user_id)
            if not user:
                await self.bot.send_message(chat_id, "Foydalanuvchi topilmadi")
                return
            
            # Foydalanuvchi arizalarini olish (database methodiga qarab o'zgartiring)
            try:
                # Agar get_applications_by_user metodi bo'lsa
                applications = self.db.get_applications_by_user(user['id'])
            except AttributeError:
                # Agar bunday metod bo'lmasa, boshqa usul ishlatamiz
                applications = []
            
            if not applications:
                text = "Sizda hali arizalar yo'q"
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="🔍 Ish izlash",
                            callback_data="jobseeker_find_jobs"
                        )
                    ]
                ])
                await self.bot.send_message(chat_id, text, reply_markup=keyboard)
                return
            
            # Arizalar ro'yxatini yaratish
            text = "📨 Mening arizalarim:\n\n"
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
            for app in applications:
                # Status emoji
                status_emoji = {
                    'pending': '🟡',
                    'ai_screening': '🔄',
                    'interview': '💬',
                    'accepted': '✅',
                    'rejected': '❌'
                }.get(app.get('status', 'pending'), '❓')
                
                # Status text
                status_text = {
                    'pending': 'Kutilmoqda',
                    'ai_screening': 'Tahlil qilinmoqda',
                    'interview': 'Suhbat',
                    'accepted': 'Qabul qilindi',
                    'rejected': 'Rad etildi'
                }.get(app.get('status', 'pending'), 'Noma\'lum')
                
                button_text = f"{status_emoji} {app.get('vacancy_title', 'Vakansiya')} - {status_text}"
                
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(
                        text=button_text,
                        callback_data=f"view_my_application_{app.get('id', 0)}"
                    )
                ])
            
            text += f"Jami: {len(applications)} ta ariza"
            
            keyboard.inline_keyboard.append([
                InlineKeyboardButton(
                    text="🔙 Orqaga",
                    callback_data="back_main"
                )
            ])
            
            await self.bot.send_message(chat_id, text, reply_markup=keyboard)
            
            # Analytics (agar analytics metodi bo'lsa)
            try:
                self.db.add_analytics_event('applications_viewed', user['id'], {
                    'applications_count': len(applications)
                })
            except:
                pass  # Analytics xatolik bersa ham davom etamiz
            
        except Exception as e:
            print(f"Arizalar ro'yxati xatoligi: {e}")
            await self.bot.send_message(chat_id, "❌ Xatolik yuz berdi")

    async def handle_view_my_application_callback(self, callback):
        """Mening arizamni ko'rish callback"""
        try:
            application_id = int(callback.data.split('_')[3])
            language = self.get_user_language(callback.from_user.id)
            user_id = callback.from_user.id
            
            # Ariza ma'lumotlarini olish
            try:
                application = self.db.get_application_by_id(application_id)
            except AttributeError:
                await callback.answer("Funksiya hali ishlab chiqilmagan")
                return
                
            if not application:
                await callback.answer("Ariza topilmadi")
                return
            
            # Foydalanuvchi tekshirish
            user = self.db.get_user_by_telegram_id(user_id)
            if not user or application.get('user_id') != user['id']:
                await callback.answer("Ruxsat berilmagan")
                return
            
            # Ariza tafsilotlarini ko'rsatish
            text = "📋 Ariza tafsilotlari:\n\n"
            text += f"💼 Vakansiya: {application.get('vacancy_title', 'N/A')}\n"
            text += f"🏢 Kompaniya: {application.get('company_name', 'N/A')}\n"
            text += f"📊 Moslik: {application.get('compatibility_score', 0)}%\n"
            text += f"📅 Sana: {application.get('applied_at', 'N/A')}\n"
            text += f"📋 Status: {application.get('status', 'N/A')}\n"
            
            if application.get('interview_score'):
                text += f"💬 Suhbat bali: {application['interview_score']}%\n"
            
            if application.get('rejection_reason'):
                text += f"\n❌ Rad etilish sababi: {application['rejection_reason']}"
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🔙 Orqaga",
                        callback_data="jobseeker_applications"
                    )
                ]
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard)
            await callback.answer()
            
        except Exception as e:
            print(f"Arizani ko'rish callback xatoligi: {e}")
            await callback.answer("❌ Xatolik yuz berdi")

    async def handle_cancel_application(self, callback, state):
        """Arizani bekor qilish"""
        try:
            await state.clear()
            
            text = "❌ Ariza bekor qilindi"
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🔍 Ish izlash",
                        callback_data="jobseeker_find_jobs"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="🔙 Asosiy menyu",
                        callback_data="back_main"
                    )
                ]
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard)
            await callback.answer()
            
            print(f"Ariza bekor qilindi: {callback.from_user.id}")
            
        except Exception as e:
            print(f"Ariza bekor qilish xatoligi: {e}")