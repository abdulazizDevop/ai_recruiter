import sqlite3
from datetime import datetime
from enum import Enum
import json

class UserRole(Enum):
    EMPLOYER = "employer"
    JOBSEEKER = "jobseeker"
    ADMIN = "admin"

class VacancyStatus(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"

class ApplicationStatus(Enum):
    PENDING = "pending"
    INTERVIEW = "interview"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

class DatabaseManager:
    def __init__(self, db_path="job_bot.db"):
        self.db_path = db_path
        self.init_db()
    
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Users jadvali - asosiy foydalanuvchilar
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE NOT NULL,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                phone TEXT,
                language TEXT DEFAULT 'uz',
                role TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Companies jadvali - kompaniyalar
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS companies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                employer_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (employer_id) REFERENCES users(id)
            )
        """)
        
        # Vacancies jadvali - vakansiyalar
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vacancies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_id INTEGER,
                employer_id INTEGER,
                title TEXT NOT NULL,
                description TEXT,
                requirements TEXT,
                responsibilities TEXT,
                salary_from INTEGER,
                salary_to INTEGER,
                work_hours TEXT,
                work_days TEXT,
                location TEXT,
                criteria TEXT, -- AI uchun kriteriyalar (JSON)
                questions TEXT, -- Savol-javoblar (JSON)
                status TEXT DEFAULT 'active',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (company_id) REFERENCES companies(id),
                FOREIGN KEY (employer_id) REFERENCES users(id)
            )
        """)
        
        # Job applications jadvali - ishga topshirish arizalari
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS job_applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vacancy_id INTEGER,
                jobseeker_id INTEGER,
                resume_path TEXT,
                ai_analysis TEXT, -- AI tahlili (JSON)
                match_percentage REAL,
                status TEXT DEFAULT 'pending',
                interview_questions TEXT, -- Savol-javoblar (JSON)
                interview_answers TEXT, -- Javoblar (JSON)
                final_score REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (vacancy_id) REFERENCES vacancies(id),
                FOREIGN KEY (jobseeker_id) REFERENCES users(id),
                UNIQUE(vacancy_id, jobseeker_id) -- bir vakansiyaga faqat 1 marta
            )
        """)
        
        # User profiles jadvali - to'liq profil ma'lumotlari
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                full_name TEXT,
                age INTEGER,
                phone TEXT,
                email TEXT,
                address TEXT,
                additional_info TEXT, -- Qo'shimcha ma'lumotlar (JSON)
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        # User sessions jadvali - foydalanuvchi holatlari
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                session_type TEXT, -- 'create_vacancy', 'apply_job', etc.
                session_data TEXT, -- JSON format
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        # Analytics jadvali - statistikalar
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analytics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT, -- 'start', 'vacancy_created', 'application_sent', etc.
                user_id INTEGER,
                event_data TEXT, -- JSON format
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    # Users CRUD
    def create_user(self, telegram_id, username=None, first_name=None, last_name=None, language='uz'):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO users (telegram_id, username, first_name, last_name, language)
                VALUES (?, ?, ?, ?, ?)
            """, (telegram_id, username, first_name, last_name, language))
            
            user_id = cursor.lastrowid
            conn.commit()
            
            # Analytics ga yozish
            self.add_analytics_event('user_start', user_id, {'telegram_id': telegram_id})
            
            return user_id
        finally:
            conn.close()
    
    def get_user_by_telegram_id(self, telegram_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
            return cursor.fetchone()
        finally:
            conn.close()
    
    def update_user_role(self, telegram_id, role):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                UPDATE users SET role = ?, updated_at = CURRENT_TIMESTAMP 
                WHERE telegram_id = ?
            """, (role, telegram_id))
            conn.commit()
        finally:
            conn.close()
    
    # Companies CRUD
    def create_company(self, name, description, employer_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO companies (name, description, employer_id)
                VALUES (?, ?, ?)
            """, (name, description, employer_id))
            
            company_id = cursor.lastrowid
            conn.commit()
            return company_id
        finally:
            conn.close()
    
    def get_companies_by_employer(self, employer_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT * FROM companies WHERE employer_id = ?", (employer_id,))
            return cursor.fetchall()
        finally:
            conn.close()
    
    def get_all_companies(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT * FROM companies")
            return cursor.fetchall()
        finally:
            conn.close()
    
    # Vacancies CRUD
    def create_vacancy(self, vacancy_data):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO vacancies 
                (company_id, employer_id, title, description, requirements, 
                 responsibilities, salary_from, salary_to, work_hours, work_days, 
                 location, criteria, questions)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                vacancy_data['company_id'], vacancy_data['employer_id'],
                vacancy_data['title'], vacancy_data['description'],
                vacancy_data['requirements'], vacancy_data['responsibilities'],
                vacancy_data.get('salary_from'), vacancy_data.get('salary_to'),
                vacancy_data.get('work_hours'), vacancy_data.get('work_days'),
                vacancy_data.get('location'), 
                json.dumps(vacancy_data.get('criteria', [])),
                json.dumps(vacancy_data.get('questions', []))
            ))
            
            vacancy_id = cursor.lastrowid
            conn.commit()
            
            # Analytics
            self.add_analytics_event('vacancy_created', vacancy_data['employer_id'], 
                                   {'vacancy_id': vacancy_id})
            
            return vacancy_id
        finally:
            conn.close()
    
    def get_vacancies_by_company(self, company_id, status='active'):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                SELECT * FROM vacancies 
                WHERE company_id = ? AND status = ?
                ORDER BY created_at DESC
            """, (company_id, status))
            return cursor.fetchall()
        finally:
            conn.close()
    
    def get_vacancy_by_id(self, vacancy_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT * FROM vacancies WHERE id = ?", (vacancy_id,))
            return cursor.fetchone()
        finally:
            conn.close()
    
    def update_vacancy_status(self, vacancy_id, status):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                UPDATE vacancies SET status = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (status, vacancy_id))
            conn.commit()
        finally:
            conn.close()
    
    # Job Applications CRUD
    def create_job_application(self, application_data):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO job_applications 
                (vacancy_id, jobseeker_id, resume_path, ai_analysis, match_percentage)
                VALUES (?, ?, ?, ?, ?)
            """, (
                application_data['vacancy_id'], application_data['jobseeker_id'],
                application_data['resume_path'], 
                json.dumps(application_data.get('ai_analysis', {})),
                application_data.get('match_percentage', 0)
            ))
            
            application_id = cursor.lastrowid
            conn.commit()
            
            # Analytics
            self.add_analytics_event('application_sent', application_data['jobseeker_id'], 
                                   {'vacancy_id': application_data['vacancy_id']})
            
            return application_id
        finally:
            conn.close()
    
    def update_application_status(self, application_id, status, additional_data=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            if additional_data:
                cursor.execute("""
                    UPDATE job_applications 
                    SET status = ?, interview_answers = ?, final_score = ?, 
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (status, json.dumps(additional_data.get('answers', [])), 
                         additional_data.get('score', 0), application_id))
            else:
                cursor.execute("""
                    UPDATE job_applications 
                    SET status = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (status, application_id))
            
            conn.commit()
        finally:
            conn.close()
    
    def check_existing_application(self, vacancy_id, jobseeker_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                SELECT id FROM job_applications 
                WHERE vacancy_id = ? AND jobseeker_id = ?
            """, (vacancy_id, jobseeker_id))
            return cursor.fetchone() is not None
        finally:
            conn.close()
    
    def get_applications_for_employer(self, employer_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                SELECT ja.*, v.title as vacancy_title, u.first_name, u.username
                FROM job_applications ja
                JOIN vacancies v ON ja.vacancy_id = v.id
                JOIN users u ON ja.jobseeker_id = u.id
                WHERE v.employer_id = ?
                ORDER BY ja.created_at DESC
            """, (employer_id,))
            return cursor.fetchall()
        finally:
            conn.close()
    
    # User Sessions
    def create_session(self, user_id, session_type, session_data=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Avvalgi sessiyalarni o'chirish
            cursor.execute("""
                UPDATE user_sessions SET is_active = 0 
                WHERE user_id = ? AND session_type = ?
            """, (user_id, session_type))
            
            # Yangi sessiya yaratish
            cursor.execute("""
                INSERT INTO user_sessions (user_id, session_type, session_data)
                VALUES (?, ?, ?)
            """, (user_id, session_type, json.dumps(session_data or {})))
            
            session_id = cursor.lastrowid
            conn.commit()
            return session_id
        finally:
            conn.close()
    
    def get_active_session(self, user_id, session_type):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                SELECT * FROM user_sessions 
                WHERE user_id = ? AND session_type = ? AND is_active = 1
                ORDER BY created_at DESC LIMIT 1
            """, (user_id, session_type))
            return cursor.fetchone()
        finally:
            conn.close()
    
    def update_session_data(self, session_id, session_data):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                UPDATE user_sessions 
                SET session_data = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (json.dumps(session_data), session_id))
            conn.commit()
        finally:
            conn.close()
    
    def close_session(self, user_id, session_type):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                UPDATE user_sessions SET is_active = 0 
                WHERE user_id = ? AND session_type = ?
            """, (user_id, session_type))
            conn.commit()
        finally:
            conn.close()
    
    # Analytics
    def add_analytics_event(self, event_type, user_id, event_data=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO analytics (event_type, user_id, event_data)
                VALUES (?, ?, ?)
            """, (event_type, user_id, json.dumps(event_data or {})))
            conn.commit()
        finally:
            conn.close()
    
    def get_analytics_summary(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Umumiy statistikalar
            stats = {}
            
            # Foydalanuvchilar soni
            cursor.execute("SELECT COUNT(*) as count FROM users")
            stats['total_users'] = cursor.fetchone()['count']
            
            # Ish beruvchilar soni
            cursor.execute("SELECT COUNT(*) as count FROM users WHERE role = 'employer'")
            stats['employers'] = cursor.fetchone()['count']
            
            # Ishga topshiruvchilar soni
            cursor.execute("SELECT COUNT(*) as count FROM users WHERE role = 'jobseeker'")
            stats['jobseekers'] = cursor.fetchone()['count']
            
            # Vakansiyalar soni
            cursor.execute("SELECT COUNT(*) as count FROM vacancies")
            stats['total_vacancies'] = cursor.fetchone()['count']
            
            # Aktiv vakansiyalar
            cursor.execute("SELECT COUNT(*) as count FROM vacancies WHERE status = 'active'")
            stats['active_vacancies'] = cursor.fetchone()['count']
            
            # Arxivlangan vakansiyalar
            cursor.execute("SELECT COUNT(*) as count FROM vacancies WHERE status = 'archived'")
            stats['archived_vacancies'] = cursor.fetchone()['count']
            
            # Arizalar soni
            cursor.execute("SELECT COUNT(*) as count FROM job_applications")
            stats['total_applications'] = cursor.fetchone()['count']
            
            # Qabul qilinganlar
            cursor.execute("SELECT COUNT(*) as count FROM job_applications WHERE status = 'accepted'")
            stats['accepted_applications'] = cursor.fetchone()['count']
            
            return stats
        finally:
            conn.close()