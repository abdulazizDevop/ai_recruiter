# -*- coding: utf-8 -*-

import json
import os
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from utils.language import get_text
from services.ai_service import validate_file_format, get_file_size_mb
from config import Config

# Jobseeker holatlari
class JobseekerStates(StatesGroup):
    UPLOADING_RESUME = State()
    ANSWERING_QUESTIONS = State()
    PROVIDING_INFO_NAME = State()
    PROVIDING_INFO_AGE = State()
    PROVIDING_INFO_PHONE = State()
    PROVIDING_INFO_EMAIL = State()
    PROVIDING_INFO_ADDRESS = State()

class JobseekerHandlers:
    def __init__(self, bot, db, ai_service, file_service):
        self.bot = bot
        self.db = db
        self.ai_service = ai_service
        self.file_service = file_service
        self.router = Router()
        
        # Handlerlarni ro'yxatga olish
        self.register_handlers()
    
    def get_user_language(self, user_id: int) -> str:
        """Foydalanuvchi tilini olish"""
        user = self.db.get_user_by_telegram_id(user_id)
        return user['language'] if user else 'uz'
    
    def register_handlers(self):
        """Jobseeker handlerlarini ro'yxatga olish"""
        
        # Jobseeker callback handlerni ro'yxatga olish
        @self.router.callback_query(F.data.startswith('jobseeker_'))
        async def jobseeker_callbacks(callback: CallbackQuery, state: FSMContext):
            """Jobseeker callback handleri"""
            try:
                action = callback.data.replace('jobseeker_', '')
                user_id = callback.from_user.id
                language = self.get_user_language(user_id)
                
                if action == 'find_jobs':
                    await self.show_companies(callback.message.chat.id, language)
                elif action == 'applications':
                    await self.show_my_applications(callback.message.chat.id, user_id, language)
                
                await callback.answer()
                
            except Exception as e:
                print(f"Jobseeker callback xatoligi: {e}")
                await callback.answer(get_text("error", "uz"))
        
        # Kompaniya tanlash
        @self.router.callback_query(F.data.startswith('select_company_'))
        async def select_company_callback(callback: CallbackQuery):
            await self.select_company_callback(callback)
        
        # Vakansiya tanlash
        @self.router.callback_query(F.data.startswith('select_vacancy_'))
        async def select_vacancy_callback(callback: CallbackQuery):
            await self.select_vacancy_callback(callback)
        
        # Vakansiyaga ariza berish
        @self.router.callback_query(F.data.startswith('apply_vacancy_'))
        async def apply_vacancy_callback(callback: CallbackQuery, state: FSMContext):
            await self.apply_vacancy_callback(callback, state)
        
        # Resume yuklash
        @self.router.message(StateFilter(JobseekerStates.UPLOADING_RESUME), F.document)
        async def handle_resume_upload(message: Message, state: FSMContext):
            await self.handle_resume_upload(message, state)
        
        # Suhbat savollari
        @self.router.callback_query(F.data == 'start_interview')
        async def start_interview_callback(callback: CallbackQuery, state: FSMContext):
            await self.start_interview_callback(callback, state)
        
        @self.router.message(StateFilter(JobseekerStates.ANSWERING_QUESTIONS))
        async def handle_interview_answer(message: Message, state: FSMContext):
            await self.handle_interview_answer(message, state)
        
        # Qo'shimcha ma'lumotlar
        @self.router.message(StateFilter(JobseekerStates.PROVIDING_INFO_NAME))
        async def handle_full_name(message: Message, state: FSMContext):
            await self.handle_full_name(message, state)
        
        @self.router.message(StateFilter(JobseekerStates.PROVIDING_INFO_AGE))
        async def handle_age(message: Message, state: FSMContext):
            await self.handle_age(message, state)
        
        @self.router.message(StateFilter(JobseekerStates.PROVIDING_INFO_PHONE))
        async def handle_phone(message: Message, state: FSMContext):
            await self.handle_phone(message, state)
        
        @self.router.message(StateFilter(JobseekerStates.PROVIDING_INFO_EMAIL))
        async def handle_email(message: Message, state: FSMContext):
            await self.handle_email(message, state)
        
        @self.router.message(StateFilter(JobseekerStates.PROVIDING_INFO_ADDRESS))
        async def handle_address(message: Message, state: FSMContext):
            await self.handle_address(message, state)
        
        # Noto'g'ri fayl formati
        @self.router.message(StateFilter(JobseekerStates.UPLOADING_RESUME))
        async def handle_invalid_resume(message: Message):
            language = self.get_user_language(message.from_user.id)
            await message.reply(get_text("invalid_file", language))
    
    async def show_companies(self, chat_id: int, language: str):
        """Kompaniyalar ro'yxatini ko'rsatish"""
        try:
            companies = self.db.get_all_companies()
            
            if not companies:
                text = get_text("no_companies", language)
                await self.bot.send_message(chat_id, text)
                return
            
            text = get_text("select_company", language)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
            for company in companies:
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(
                        text=f"🏢 {company['name']}",
                        callback_data=f"select_company_{company['id']}"
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
            print(f"Kompaniyalar ro'yxati xatoligi: {e}")
    
    async def select_company_callback(self, callback: CallbackQuery):
        """Kompaniya tanlash callback"""
        try:
            company_id = int(callback.data.split('_')[2])  # select_company_123 -> 123
            language = self.get_user_language(callback.from_user.id)
            
            # Kompaniya vakansiyalarini olish
            vacancies = self.db.get_vacancies_by_company(company_id, 'active')
            
            if not vacancies:
                text = get_text("no_active_vacancies", language)
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
            
            text = get_text("select_vacancy", language)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
            for vacancy in vacancies:
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(
                        text=f"📌 {vacancy['title']}",
                        callback_data=f"select_vacancy_{vacancy['id']}"
                    )
                ])
            
            keyboard.inline_keyboard.append([
                InlineKeyboardButton(
                    text=get_text("btn_back", language),
                    callback_data="jobseeker_find_jobs"
                )
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard)
            await callback.answer()
            
        except Exception as e:
            print(f"Kompaniya tanlash xatoligi: {e}")
            await callback.answer("Xatolik yuz berdi!")
    
    async def select_vacancy_callback(self, callback: CallbackQuery):
        """Vakansiya tanlash callback"""
        try:
            vacancy_id = int(callback.data.split('_')[2])  # select_vacancy_123 -> 123
            language = self.get_user_language(callback.from_user.id)
            user_id = callback.from_user.id
            
            # Vakansiya ma'lumotlarini olish
            vacancy = self.db.get_vacancy_by_id(vacancy_id)
            if not vacancy:
                await callback.answer("Vakansiya topilmadi!")
                return
            
            # Allaqachon ariza berganligini tekshirish
            user = self.db.get_user_by_telegram_id(user_id)
            if self.db.check_existing_application(vacancy_id, user['id']):
                text = get_text("already_applied", language)
                await callback.message.edit_text(text)
                await callback.answer()
                return
            
            # Vakansiya tafsilotlarini ko'rsatish
            company = self.db.get_companies_by_employer(vacancy['employer_id'])[0]  # Simplified
            
            text = get_text("vacancy_details", language).format(
                vacancy['title'],
                company['name'],
                vacancy['description'],
                vacancy['requirements'],
                vacancy['responsibilities'],
                "Ko'rsatilmagan",  # salary - keyinchalik format qilamiz
                vacancy.get('work_hours', 'Ko\'rsatilmagan'),
                vacancy.get('work_days', 'Ko\'rsatilmagan'),
                vacancy.get('location', 'Ko\'rsatilmagan')
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
            
            await callback.message.edit_text(text, reply_markup=keyboard)
            await callback.answer()
            
        except Exception as e:
            print(f"Vakansiya tanlash xatoligi: {e}")
            await callback.answer("Xatolik yuz berdi!")
    
    async def apply_vacancy_callback(self, callback: CallbackQuery, state: FSMContext):
        """Vakansiyaga ariza berish"""
        try:
            vacancy_id = int(callback.data.split('_')[2])
            language = self.get_user_language(callback.from_user.id)
            
            # State ga vakansiya ID ni saqlash
            await state.update_data(vacancy_id=vacancy_id)
            await state.set_state(JobseekerStates.UPLOADING_RESUME)
            
            # Resume yuklashni so'rash
            text = get_text("upload_resume", language)
            
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
            
        except Exception as e:
            print(f"Ariza berish xatoligi: {e}")
            await callback.answer("Xatolik yuz berdi!")
    
    async def handle_resume_upload(self, message: Message, state: FSMContext):
        """Resume fayl yuklashni qayta ishlash"""
        try:
            language = self.get_user_language(message.from_user.id)
            
            # Fayl ma'lumotlarini olish
            document = message.document
            file_name = document.file_name
            file_size = document.file_size
            
            # Fayl formatini tekshirish
            if not validate_file_format(file_name):
                await message.reply(get_text("invalid_file", language))
                return
            
            # Fayl hajmini tekshirish
            if file_size > Config.MAX_FILE_SIZE_MB * 1024 * 1024:  # MB to bytes
                await message.reply(get_text("file_too_large", language))
                return
            
            # Faylni yuklab olish
            processing_msg = await message.reply(get_text("processing", language))
            
            file_info = await self.bot.get_file(document.file_id)
            file_content = await self.bot.download_file(file_info.file_path)
            
            # Faylni saqlash
            file_path = self.file_service.save_resume_file(
                document, message.from_user.id, file_content.read()
            )
            
            if not file_path:
                await processing_msg.edit_text(get_text("error", language))
                return
            
            # Resume ni tahlil qilish
            await processing_msg.edit_text(get_text("ai_analyzing", language))
            
            # State dan vakansiya ma'lumotlarini olish
            data = await state.get_data()
            vacancy_id = data['vacancy_id']
            vacancy = self.db.get_vacancy_by_id(vacancy_id)
            
            # Resume matnini chiqarish
            resume_text = self.ai_service.extract_text_from_file(file_path)
            
            if not resume_text:
                await processing_msg.edit_text("❌ Resume matnini o'qib bo'lmadi!")
                return
            
            # AI tahlili
            criteria = json.loads(vacancy['criteria']) if vacancy['criteria'] else {}
            vacancy_info = {
                'title': vacancy['title'],
                'description': vacancy['description'],
                'requirements': vacancy['requirements']
            }
            
            analysis = self.ai_service.analyze_resume(resume_text, criteria, vacancy_info)
            match_percentage = analysis.get('match_percentage', 0)
            
            # State ga ma'lumotlarni saqlash
            await state.update_data(
                resume_path=file_path,
                ai_analysis=analysis,
                match_percentage=match_percentage
            )
            
            # Natijani ko'rsatish
            await processing_msg.delete()
            
            if match_percentage < Config.MIN_MATCH_PERCENTAGE:
                # Moslik darajasi past
                text = get_text("match_too_low", language).format(match_percentage)
                
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=get_text("find_jobs", language),
                            callback_data="jobseeker_find_jobs"
                        )
                    ]
                ])
                
                await message.answer(text, reply_markup=keyboard)
                await state.clear()
            else:
                # Moslik darajasi yaxshi - suhbatga o'tish
                text = get_text("match_good", language).format(match_percentage)
                
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=get_text("continue", language),
                            callback_data="start_interview"
                        )
                    ]
                ])
                
                await message.answer(text, reply_markup=keyboard)
            
        except Exception as e:
            print(f"Resume yuklash xatoligi: {e}")
            await message.reply(get_text("error", language))
    
    async def start_interview_callback(self, callback: CallbackQuery, state: FSMContext):
        """Suhbatni boshlash"""
        try:
            language = self.get_user_language(callback.from_user.id)
            
            # State dan ma'lumotlarni olish
            data = await state.get_data()
            vacancy_id = data['vacancy_id']
            vacancy = self.db.get_vacancy_by_id(vacancy_id)
            
            # Savollarni olish
            questions = json.loads(vacancy['questions']) if vacancy['questions'] else []
            
            if not questions:
                await callback.answer("Savollar topilmadi!")
                return
            
            # State ga suhbat ma'lumotlarini saqlash
            await state.update_data(
                questions=questions,
                answers=[],
                current_question=0
            )
            await state.set_state(JobseekerStates.ANSWERING_QUESTIONS)
            
            # Birinchi savolni ko'rsatish
            text = get_text("interview_started", language).format(1, len(questions))
            text += "\n\n" + get_text("question", language).format(questions[0])
            
            await callback.message.edit_text(text)
            await callback.answer()
            
        except Exception as e:
            print(f"Suhbat boshlash xatoligi: {e}")
            await callback.answer("Xatolik yuz berdi!")
    
    async def handle_interview_answer(self, message: Message, state: FSMContext):
        """Suhbat javobini qayta ishlash"""
        try:
            language = self.get_user_language(message.from_user.id)
            answer = message.text.strip()
            
            if len(answer) < 10:
                await message.reply("❌ Javob juda qisqa! Iltimos, batafsil javob bering.")
                return
            
            # State dan ma'lumotlarni olish
            data = await state.get_data()
            questions = data['questions']
            answers = data['answers']
            current_question = data['current_question']
            
            # Javobni saqlash
            answers.append(answer)
            current_question += 1
            
            if current_question < len(questions):
                # Keyingi savol
                await state.update_data(
                    answers=answers,
                    current_question=current_question
                )
                
                text = get_text("interview_started", language).format(current_question + 1, len(questions))
                text += "\n\n" + get_text("question", language).format(questions[current_question])
                
                await message.answer(text)
            else:
                # Barcha savollar tugadi - baholash
                await state.update_data(answers=answers)
                await self.evaluate_interview(message, state, language)
            
        except Exception as e:
            print(f"Suhbat javobi xatoligi: {e}")
            await message.reply(get_text("error", language))
    
    async def evaluate_interview(self, message: Message, state: FSMContext, language: str):
        """Suhbat javoblarini baholash"""
        try:
            # Baholash jarayoni
            processing_msg = await message.answer(get_text("evaluating_answers", language))
            
            # State dan ma'lumotlarni olish
            data = await state.get_data()
            vacancy_id = data['vacancy_id']
            questions = data['questions']
            answers = data['answers']
            
            # Vakansiya ma'lumotlarini olish
            vacancy = self.db.get_vacancy_by_id(vacancy_id)
            criteria = json.loads(vacancy['criteria']) if vacancy['criteria'] else {}
            vacancy_info = {
                'title': vacancy['title'],
                'requirements': vacancy['requirements']
            }
            
            # AI baholash
            evaluation = self.ai_service.evaluate_interview_answers(
                questions, answers, vacancy_info, criteria
            )
            
            total_score = evaluation.get('total_score', 0)
            passed = evaluation.get('passed', False)
            
            await processing_msg.delete()
            
            if passed:
                # Muvaffaqiyatli
                text = get_text("interview_success", language).format(total_score)
                
                # Qo'shimcha ma'lumotlar so'rash
                await state.update_data(
                    interview_evaluation=evaluation,
                    interview_passed=True
                )
                await self.request_additional_info(message, state, language)
            else:
                # Muvaffaqiyatsiz
                text = get_text("interview_failed", language).format(total_score)
                
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=get_text("find_jobs", language),
                            callback_data="jobseeker_find_jobs"
                        )
                    ]
                ])
                
                await message.answer(text, reply_markup=keyboard)
                
                # Application ni rad etilgan deb belgilash
                user = self.db.get_user_by_telegram_id(message.from_user.id)
                application_data = {
                    'vacancy_id': vacancy_id,
                    'jobseeker_id': user['id'],
                    'resume_path': data['resume_path'],
                    'ai_analysis': data['ai_analysis'],
                    'match_percentage': data['match_percentage']
                }
                
                app_id = self.db.create_job_application(application_data)
                self.db.update_application_status(app_id, 'rejected', {
                    'answers': answers,
                    'score': total_score
                })
                
                await state.clear()
            
        except Exception as e:
            print(f"Suhbat baholash xatoligi: {e}")
            await message.answer(get_text("error", language))
    
    async def request_additional_info(self, message: Message, state: FSMContext, language: str):
        """Qo'shimcha ma'lumotlar so'rash"""
        try:
            text = get_text("additional_info", language) + "\n\n"
            text += get_text("full_name", language)
            
            await state.set_state(JobseekerStates.PROVIDING_INFO_NAME)
            await message.answer(text)
            
        except Exception as e:
            print(f"Qo'shimcha ma'lumotlar so'rash xatoligi: {e}")
    
    async def handle_full_name(self, message: Message, state: FSMContext):
        """To'liq ismni qayta ishlash"""
        try:
            full_name = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            if len(full_name) < 3:
                await message.reply("❌ Ism juda qisqa!")
                return
            
            await state.update_data(full_name=full_name)
            await state.set_state(JobseekerStates.PROVIDING_INFO_AGE)
            
            text = get_text("age", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"To'liq ism xatoligi: {e}")
    
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
                await message.reply("❌ Yoshni to'g'ri kiriting (16-80 oralig'ida)!")
                return
            
            await state.update_data(age=age)
            await state.set_state(JobseekerStates.PROVIDING_INFO_PHONE)
            
            text = get_text("phone_number", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Yosh xatoligi: {e}")
    
    async def handle_phone(self, message: Message, state: FSMContext):
        """Telefon raqamini qayta ishlash"""
        try:
            phone = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Telefon raqam validatsiyasi (oddiy)
            if len(phone) < 9:
                await message.reply("❌ Telefon raqamini to'g'ri kiriting!")
                return
            
            await state.update_data(phone=phone)
            await state.set_state(JobseekerStates.PROVIDING_INFO_EMAIL)
            
            text = get_text("email", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Telefon raqam xatoligi: {e}")
    
    async def handle_email(self, message: Message, state: FSMContext):
        """Email ni qayta ishlash"""
        try:
            email = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Email validatsiyasi (oddiy)
            if '@' not in email or '.' not in email:
                await message.reply("❌ Email manzilini to'g'ri kiriting!")
                return
            
            await state.update_data(email=email)
            await state.set_state(JobseekerStates.PROVIDING_INFO_ADDRESS)
            
            text = get_text("address", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Email xatoligi: {e}")
    
    async def handle_address(self, message: Message, state: FSMContext):
        """Manzilni qayta ishlash va arizani yakunlash"""
        try:
            address = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            user_id = message.from_user.id
            
            # Ma'lumotni saqlash
            await state.update_data(address=address)
            
            # Barcha ma'lumotlarni olish
            data = await state.get_data()
            
            # Job application yaratish
            user = self.db.get_user_by_telegram_id(user_id)
            
            application_data = {
                'vacancy_id': data['vacancy_id'],
                'jobseeker_id': user['id'],
                'resume_path': data['resume_path'],
                'ai_analysis': data['ai_analysis'],
                'match_percentage': data['match_percentage']
            }
            
            app_id = self.db.create_job_application(application_data)
            
            # Suhbat natijalarini saqlash
            self.db.update_application_status(app_id, 'accepted', {
                'answers': data['answers'],
                'score': data['interview_evaluation']['total_score']
            })
            
            # User profile yaratish yoki yangilash
            profile_data = {
                'full_name': data['full_name'],
                'age': data['age'],
                'phone': data['phone'],
                'email': data['email'],
                'address': address
            }
            
            # Profile ma'lumotlarini saqlash (simplified)
            # Bu yerda user_profiles jadvaliga yozish logikasi bo'lishi kerak
            
            # Muvaffaqiyat xabari
            text = get_text("info_saved", language)
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("find_jobs", language),
                        callback_data="jobseeker_find_jobs"
                    )
                ]
            ])
            
            await message.answer(text, reply_markup=keyboard)
            
            # Ish beruvchiga xabar yuborish
            await self.notify_employer(data, profile_data)
            
            # State ni tozalash
            await state.clear()
            
        except Exception as e:
            print(f"Manzil xatoligi: {e}")
            await message.reply(get_text("error", language))
    
    async def notify_employer(self, application_data: dict, profile_data: dict):
        """Ish beruvchiga nomzod haqida xabar yuborish"""
        try:
            vacancy_id = application_data['vacancy_id']
            vacancy = self.db.get_vacancy_by_id(vacancy_id)
            
            # Ish beruvchi telegram ID sini olish
            employer = self.db.get_user_by_telegram_id(vacancy['employer_id'])
            
            if employer:
                language = employer.get('language', 'uz')
                
                # Xabar matni
                text = f"""🎉 Yangi nomzod!
                
📌 Vakansiya: {vacancy['title']}
👤 Nomzod: {profile_data['full_name']}
📊 Moslik: {application_data['match_percentage']}%
📞 Telefon: {profile_data['phone']}
📧 Email: {profile_data['email']}
📍 Manzil: {profile_data['address']}
🎂 Yosh: {profile_data['age']}

Resume fayli va batafsil ma'lumotlar admin paneldan ko'rish mumkin."""
                
                await self.bot.send_message(employer['telegram_id'], text)
                
        except Exception as e:
            print(f"Ish beruvchiga xabar yuborish xatoligi: {e}")
    
    async def show_my_applications(self, chat_id: int, user_id: int, language: str):
        """Mening arizalarimni ko'rsatish"""
        try:
            # Bu funksiya keyinchalik implement qilinadi
            text = "Bu funksiya hali ishlab chiqilmoqda!"
            await self.bot.send_message(chat_id, text)
            
        except Exception as e:
            print(f"Arizalar ro'yxati xatoligi: {e}")