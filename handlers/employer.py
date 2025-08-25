# -*- coding: utf-8 -*-

import json
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from utils.language import get_text

# Employer holatlari
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

class EmployerHandlers:
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
        """Employer handlerlarini ro'yxatga olish"""
        
        # Employer callback handlerni ro'yxatga olish
        @self.router.callback_query(F.data.startswith('employer_'))
        async def employer_callbacks(callback: CallbackQuery, state: FSMContext):
            """Employer callback handleri"""
            try:
                action = callback.data.replace('employer_', '')
                user_id = callback.from_user.id
                language = self.get_user_language(user_id)
                
                if action == 'create_vacancy':
                    await self.start_vacancy_creation(callback, state, language)
                elif action == 'vacancies':
                    await self.show_my_vacancies(callback.message.chat.id, user_id, language)
                elif action == 'applications':
                    await self.show_applications(callback.message.chat.id, user_id, language)
                
                await callback.answer()
                
            except Exception as e:
                print(f"Employer callback xatoligi: {e}")
                await callback.answer(get_text("error", "uz"))
        
        # Vakansiya yaratish bo'yicha message handlerlar
        @self.router.message(StateFilter(EmployerStates.CREATING_COMPANY_NAME))
        async def handle_company_name(message: Message, state: FSMContext):
            await self.handle_company_name(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_COMPANY_DESC))
        async def handle_company_description(message: Message, state: FSMContext):
            await self.handle_company_description(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_VACANCY_TITLE))
        async def handle_vacancy_title(message: Message, state: FSMContext):
            await self.handle_vacancy_title(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_VACANCY_DESC))
        async def handle_vacancy_description(message: Message, state: FSMContext):
            await self.handle_vacancy_description(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_VACANCY_REQ))
        async def handle_vacancy_requirements(message: Message, state: FSMContext):
            await self.handle_vacancy_requirements(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_VACANCY_RESP))
        async def handle_vacancy_responsibilities(message: Message, state: FSMContext):
            await self.handle_vacancy_responsibilities(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_SALARY))
        async def handle_salary_range(message: Message, state: FSMContext):
            await self.handle_salary_range(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_WORK_HOURS))
        async def handle_work_hours(message: Message, state: FSMContext):
            await self.handle_work_hours(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_WORK_DAYS))
        async def handle_work_days(message: Message, state: FSMContext):
            await self.handle_work_days(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_WORK_LOCATION))
        async def handle_work_location(message: Message, state: FSMContext):
            await self.handle_work_location(message, state)
        
        # Kriteriya handlerlar
        @self.router.message(StateFilter(EmployerStates.CREATING_CRITERIA_SKILLS))
        async def handle_criteria_skills(message: Message, state: FSMContext):
            await self.handle_criteria_skills(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_CRITERIA_EXP))
        async def handle_criteria_experience(message: Message, state: FSMContext):
            await self.handle_criteria_experience(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_CRITERIA_EDU))
        async def handle_criteria_education(message: Message, state: FSMContext):
            await self.handle_criteria_education(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_CRITERIA_LANG))
        async def handle_criteria_languages(message: Message, state: FSMContext):
            await self.handle_criteria_languages(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_CRITERIA_ADD))
        async def handle_criteria_additional(message: Message, state: FSMContext):
            await self.handle_criteria_additional(message, state)
        
        @self.router.message(StateFilter(EmployerStates.CREATING_QUESTIONS))
        async def handle_question_input(message: Message, state: FSMContext):
            await self.handle_question_input(message, state)
        
        # Savollar soni tanlash
        @self.router.callback_query(F.data.startswith('questions_count_'))
        async def questions_count_callback(callback: CallbackQuery, state: FSMContext):
            await self.handle_questions_count_callback(callback, state)
        
        # Vakansiya ko'rish va boshqarish
        @self.router.callback_query(F.data.startswith('view_vacancy_'))
        async def view_vacancy_callback(callback: CallbackQuery):
            await self.view_vacancy_callback(callback)
        
        # Vakansiya arxivlash/faollashtirish
        @self.router.callback_query(F.data.startswith('archive_vacancy_'))
        async def archive_vacancy_callback(callback: CallbackQuery):
            await self.archive_vacancy_callback(callback)
        
        @self.router.callback_query(F.data.startswith('activate_vacancy_'))
        async def activate_vacancy_callback(callback: CallbackQuery):
            await self.activate_vacancy_callback(callback)
        
        # Arizalarni ko'rish
        @self.router.callback_query(F.data.startswith('view_application_'))
        async def view_application_callback(callback: CallbackQuery):
            await self.view_application_callback(callback)
        
        # Bekor qilish
        @self.router.callback_query(F.data == 'cancel_vacancy')
        async def cancel_vacancy(callback: CallbackQuery, state: FSMContext):
            await state.clear()
            language = self.get_user_language(callback.from_user.id)
            await self.show_employer_menu(callback.message.chat.id, language)
            await callback.answer()
    
    async def start_vacancy_creation(self, callback: CallbackQuery, state: FSMContext, language: str):
        """Vakansiya yaratishni boshlash"""
        try:
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
            
        except Exception as e:
            print(f"Vakansiya yaratishni boshlash xatoligi: {e}")
    
    async def handle_company_name(self, message: Message, state: FSMContext):
        """Kompaniya nomini qayta ishlash"""
        try:
            company_name = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
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
            print(f"Kompaniya nomi xatoligi: {e}")
    
    async def handle_company_description(self, message: Message, state: FSMContext):
        """Kompaniya tavsifini qayta ishlash"""
        try:
            company_description = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(company_description=company_description)
            await state.set_state(EmployerStates.CREATING_VACANCY_TITLE)
            
            # Keyingi savol
            text = get_text("vacancy_title", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Kompaniya tavsifi xatoligi: {e}")
    
    async def handle_vacancy_title(self, message: Message, state: FSMContext):
        """Vakansiya nomini qayta ishlash"""
        try:
            vacancy_title = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
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
            print(f"Vakansiya nomi xatoligi: {e}")
    
    async def handle_vacancy_description(self, message: Message, state: FSMContext):
        """Vakansiya tavsifini qayta ishlash"""
        try:
            vacancy_description = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(vacancy_description=vacancy_description)
            await state.set_state(EmployerStates.CREATING_VACANCY_REQ)
            
            # Keyingi savol
            text = get_text("vacancy_requirements", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Vakansiya tavsifi xatoligi: {e}")
    
    async def handle_vacancy_requirements(self, message: Message, state: FSMContext):
        """Vakansiya talablarini qayta ishlash"""
        try:
            requirements = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(requirements=requirements)
            await state.set_state(EmployerStates.CREATING_VACANCY_RESP)
            
            # Keyingi savol
            text = get_text("vacancy_responsibilities", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Vakansiya talablari xatoligi: {e}")
    
    async def handle_vacancy_responsibilities(self, message: Message, state: FSMContext):
        """Vakansiya majburiyatlarini qayta ishlash"""
        try:
            responsibilities = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(responsibilities=responsibilities)
            await state.set_state(EmployerStates.CREATING_SALARY)
            
            # Keyingi savol
            text = get_text("salary_range", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Vakansiya majburiyatlari xatoligi: {e}")
    
    async def handle_salary_range(self, message: Message, state: FSMContext):
        """Ish haqqi oralig'ini qayta ishlash"""
        try:
            salary_text = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(salary_range=salary_text)
            await state.set_state(EmployerStates.CREATING_WORK_HOURS)
            
            # Keyingi savol
            text = get_text("work_hours", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Ish haqqi xatoligi: {e}")
    
    async def handle_work_hours(self, message: Message, state: FSMContext):
        """Ish soatlarini qayta ishlash"""
        try:
            work_hours = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(work_hours=work_hours)
            await state.set_state(EmployerStates.CREATING_WORK_DAYS)
            
            # Keyingi savol
            text = get_text("work_days", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Ish soatlari xatoligi: {e}")
    
    async def handle_work_days(self, message: Message, state: FSMContext):
        """Ish kunlarini qayta ishlash"""
        try:
            work_days = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(work_days=work_days)
            await state.set_state(EmployerStates.CREATING_WORK_LOCATION)
            
            # Keyingi savol
            text = get_text("work_location", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Ish kunlari xatoligi: {e}")
    
    async def handle_work_location(self, message: Message, state: FSMContext):
        """Ish joyini qayta ishlash"""
        try:
            work_location = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(work_location=work_location)
            await state.set_state(EmployerStates.CREATING_CRITERIA_SKILLS)
            
            # AI kriteriylarga o'tish
            text = get_text("ai_criteria", language) + "\n\n"
            text += get_text("criteria_skills", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Ish joyi xatoligi: {e}")
    
    async def handle_criteria_skills(self, message: Message, state: FSMContext):
        """Ko'nikmalar kriteriyasini qayta ishlash"""
        try:
            skills = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(criteria_skills=skills)
            await state.set_state(EmployerStates.CREATING_CRITERIA_EXP)
            
            # Keyingi savol
            text = get_text("criteria_experience", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Ko'nikmalar kriteriyas xatoligi: {e}")
    
    async def handle_criteria_experience(self, message: Message, state: FSMContext):
        """Tajriba kriteriyasini qayta ishlash"""
        try:
            experience = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(criteria_experience=experience)
            await state.set_state(EmployerStates.CREATING_CRITERIA_EDU)
            
            # Keyingi savol
            text = get_text("criteria_education", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Tajriba kriteriyasi xatoligi: {e}")
    
    async def handle_criteria_education(self, message: Message, state: FSMContext):
        """Ta'lim kriteriyasini qayta ishlash"""
        try:
            education = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(criteria_education=education)
            await state.set_state(EmployerStates.CREATING_CRITERIA_LANG)
            
            # Keyingi savol
            text = get_text("criteria_languages", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Ta'lim kriteriyasi xatoligi: {e}")
    
    async def handle_criteria_languages(self, message: Message, state: FSMContext):
        """Tillar kriteriyasini qayta ishlash"""
        try:
            languages_req = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(criteria_languages=languages_req)
            await state.set_state(EmployerStates.CREATING_CRITERIA_ADD)
            
            # Keyingi savol
            text = get_text("criteria_additional", language)
            await message.answer(text)
            
        except Exception as e:
            print(f"Tillar kriteriyasi xatoligi: {e}")
    
    async def handle_criteria_additional(self, message: Message, state: FSMContext):
        """Qo'shimcha kriteriyalarni qayta ishlash"""
        try:
            additional = message.text.strip()
            language = self.get_user_language(message.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(criteria_additional=additional)
            
            # Savollar sonini so'rash
            text = get_text("interview_questions", language)
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            for i in range(1, 6):  # 1-5 gacha savollar
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(
                        text=f"{i} ta savol", 
                        callback_data=f"questions_count_{i}"
                    )
                ])
            
            await message.answer(text, reply_markup=keyboard)
            
        except Exception as e:
            print(f"Qo'shimcha kriteriyalar xatoligi: {e}")
    
    async def handle_questions_count_callback(self, callback: CallbackQuery, state: FSMContext):
        """Savollar sonini callback orqali qayta ishlash"""
        try:
            questions_count = int(callback.data.split('_')[2])  # questions_count_3 -> 3
            language = self.get_user_language(callback.from_user.id)
            
            # Ma'lumotni saqlash
            await state.update_data(
                questions_count=questions_count,
                questions=[],
                current_question=1
            )
            await state.set_state(EmployerStates.CREATING_QUESTIONS)
            
            # Birinchi savolni so'rash
            text = get_text("question_prompt", language).format(1)
            await callback.message.edit_text(text)
            await callback.answer()
            
        except Exception as e:
            print(f"Savollar soni callback xatoligi: {e}")
    
    async def handle_question_input(self, message: Message, state: FSMContext):
        """Savol matnini qayta ishlash"""
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
                # Barcha savollar tugadi - vakansiyani saqlash
                await state.update_data(questions=questions)
                await self.complete_vacancy_creation(message, state, language)
            
        except Exception as e:
            print(f"Savol kiritish xatoligi: {e}")
    
    async def complete_vacancy_creation(self, message: Message, state: FSMContext, language: str):
        """Vakansiya yaratishni yakunlash"""
        try:
            data = await state.get_data()
            user_id = message.from_user.id
            
            # Avval kompaniyani yaratish yoki topish
            user = self.db.get_user_by_telegram_id(user_id)
            company_id = self.db.create_company(
                data['company_name'],
                data['company_description'],
                user['id']
            )
            
            # Kriteriyalarni formatlash
            criteria = {
                'skills': data.get('criteria_skills', ''),
                'experience': data.get('criteria_experience', ''),
                'education': data.get('criteria_education', ''),
                'languages': data.get('criteria_languages', ''),
                'additional': data.get('criteria_additional', '')
            }
            
            # Vakansiyani yaratish
            vacancy_data = {
                'company_id': company_id,
                'employer_id': user['id'],
                'title': data['vacancy_title'],
                'description': data['vacancy_description'],
                'requirements': data['requirements'],
                'responsibilities': data['responsibilities'],
                'salary_from': None,  # Keyinchalik parse qilish
                'salary_to': None,
                'work_hours': data['work_hours'],
                'work_days': data['work_days'],
                'location': data['work_location'],
                'criteria': criteria,
                'questions': data['questions']
            }
            
            vacancy_id = self.db.create_vacancy(vacancy_data)
            
            # State ni tozalash
            await state.clear()
            
            # Muvaffaqiyat xabari
            from datetime import datetime
            text = get_text("vacancy_created", language).format(
                data['vacancy_title'],
                data['company_name'],
                datetime.now().strftime("%d.%m.%Y")
            )
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("my_vacancies", language),
                        callback_data="employer_vacancies"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=get_text("btn_back", language),
                        callback_data="back_main"
                    )
                ]
            ])
            
            await message.answer(text, reply_markup=keyboard)
            
        except Exception as e:
            print(f"Vakansiya yaratishni yakunlash xatoligi: {e}")
            await message.answer(get_text("error", language))
    
    async def show_my_vacancies(self, chat_id: int, user_id: int, language: str):
        """Mening vakansiyalarimni ko'rsatish"""
        try:
            user = self.db.get_user_by_telegram_id(user_id)
            companies = self.db.get_companies_by_employer(user['id'])
            
            if not companies:
                text = get_text("no_vacancies", language)
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
            
            text = get_text("vacancy_list", language) + "\n\n"
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
            for company in companies:
                vacancies = self.db.get_vacancies_by_company(company['id'])
                if vacancies:
                    for vacancy in vacancies:
                        status_text = get_text("vacancy_status_active", language) if vacancy['status'] == 'active' else get_text("vacancy_status_archived", language)
                        button_text = f"{vacancy['title']} ({status_text})"
                        keyboard.inline_keyboard.append([
                            InlineKeyboardButton(
                                text=button_text,
                                callback_data=f"view_vacancy_{vacancy['id']}"
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
            print(f"Vakansiyalar ro'yxati xatoligi: {e}")
    
    async def show_applications(self, chat_id: int, user_id: int, language: str):
        """Kelgan arizalarni ko'rsatish"""
        try:
            user = self.db.get_user_by_telegram_id(user_id)
            applications = self.db.get_applications_for_employer(user['id'])
            
            if not applications:
                text = get_text("no_applications", language)
                await self.bot.send_message(chat_id, text)
                return
            
            text = get_text("applications_list", language) + "\n\n"
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
            for app in applications:
                button_text = f"{app['vacancy_title']} - {app['first_name'] or app['username']}"
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(
                        text=button_text,
                        callback_data=f"view_application_{app['id']}"
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
            print(f"Arizalar ro'yxati xatoligi: {e}")
    
    async def view_vacancy_callback(self, callback: CallbackQuery):
        """Vakansiyani ko'rish callback"""
        try:
            vacancy_id = int(callback.data.split('_')[2])  # view_vacancy_123 -> 123
            language = self.get_user_language(callback.from_user.id)
            
            vacancy = self.db.get_vacancy_by_id(vacancy_id)
            if not vacancy:
                await callback.answer("Vakansiya topilmadi!")
                return
            
            # Vakansiya ma'lumotlarini ko'rsatish
            text = get_text("vacancy_details", language).format(
                vacancy['title'],
                vacancy.get('company_name', 'N/A'),  # Kompaniya nomini qo'shish kerak
                vacancy['description'],
                vacancy['requirements'],
                vacancy['responsibilities'],
                vacancy.get('salary_range', 'N/A'),
                vacancy.get('work_hours', 'N/A'),
                vacancy.get('work_days', 'N/A'),
                vacancy.get('location', 'N/A')
            )
            
            # Boshqaruv tugmalari
            keyboard = InlineKeyboardMarkup(inline_keyboard=[])
            
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
            
            keyboard.inline_keyboard.append([
                InlineKeyboardButton(
                    text=get_text("btn_back", language),
                    callback_data="employer_vacancies"
                )
            ])
            
            await callback.message.edit_text(text, reply_markup=keyboard)
            await callback.answer()
            
        except Exception as e:
            print(f"Vakansiyani ko'rish xatoligi: {e}")
            await callback.answer("Xatolik yuz berdi!")
    
    async def archive_vacancy_callback(self, callback: CallbackQuery):
        """Vakansiyani arxivlash"""
        try:
            vacancy_id = int(callback.data.split('_')[2])
            language = self.get_user_language(callback.from_user.id)
            
            self.db.update_vacancy_status(vacancy_id, 'archived')
            
            await callback.answer("✅ Vakansiya arxivlandi!")
            # Vakansiyani qaytadan ko'rsatish
            await self.view_vacancy_callback(callback)
            
        except Exception as e:
            print(f"Vakansiyani arxivlash xatoligi: {e}")
            await callback.answer("Xatolik yuz berdi!")
    
    async def activate_vacancy_callback(self, callback: CallbackQuery):
        """Vakansiyani faollashtirish"""
        try:
            vacancy_id = int(callback.data.split('_')[2])
            language = self.get_user_language(callback.from_user.id)
            
            self.db.update_vacancy_status(vacancy_id, 'active')
            
            await callback.answer("✅ Vakansiya faollashtirildi!")
            # Vakansiyani qaytadan ko'rsatish
            await self.view_vacancy_callback(callback)
            
        except Exception as e:
            print(f"Vakansiyani faollashtirish xatoligi: {e}")
            await callback.answer("Xatolik yuz berdi!")
    
    async def view_application_callback(self, callback: CallbackQuery):
        """Arizani ko'rish"""
        try:
            application_id = int(callback.data.split('_')[2])
            language = self.get_user_language(callback.from_user.id)
            
            # Application ma'lumotlarini olish (keyinchalik implement qilamiz)
            await callback.answer("Bu funksiya hali ishlab chiqilmoqda!")
            
        except Exception as e:
            print(f"Arizani ko'rish xatoligi: {e}")
            await callback.answer("Xatolik yuz berdi!")
    
    async def show_employer_menu(self, chat_id: int, language: str):
        """Employer menyusini ko'rsatish"""
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
            
            await self.bot.send_message(chat_id, text, reply_markup=keyboard)
            
        except Exception as e:
            print(f"Employer menyu xatoligi: {e}")