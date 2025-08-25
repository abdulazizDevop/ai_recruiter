import openai
import json
import os
from typing import Dict, List
import PyPDF2
import docx
import re

class AIService:
    def __init__(self, api_key: str):
        """OpenAI API bilan ishlash uchun servis"""
        openai.api_key = api_key
        self.model = "gpt-4"  # yoki "gpt-4-turbo"
        
    def extract_text_from_pdf(self, file_path: str) -> str:
        """PDF dan matn chiqarish"""
        try:
            text = ""
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            print(f"PDF o'qishda xatolik: {e}")
            return ""
    
    def extract_text_from_docx(self, file_path: str) -> str:
        """DOCX dan matn chiqarish"""
        try:
            doc = docx.Document(file_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text.strip()
        except Exception as e:
            print(f"DOCX o'qishda xatolik: {e}")
            return ""
    
    def extract_text_from_file(self, file_path: str) -> str:
        """Fayl formatiga qarab matn chiqarish"""
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension == '.pdf':
            return self.extract_text_from_pdf(file_path)
        elif file_extension in ['.docx', '.doc']:
            return self.extract_text_from_docx(file_path)
        else:
            return ""
    
    def analyze_resume(self, resume_text: str, criteria: Dict, vacancy_info: Dict) -> Dict:
        """Resume ni tahlil qilish"""
        
        # AI uchun prompt tayyorlash
        prompt = self._create_analysis_prompt(resume_text, criteria, vacancy_info)
        
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Siz professional HR mutaxassisigiz. Resume ni tahlil qilib, vakansiya talablariga mosligini baholaysiz."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=1500
            )
            
            analysis_text = response.choices[0].message.content
            
            # JSON formatga o'girish
            analysis_data = self._parse_analysis_result(analysis_text)
            
            return analysis_data
            
        except Exception as e:
            print(f"AI tahlilida xatolik: {e}")
            return {
                "match_percentage": 0,
                "analysis": "Tahlil qilishda xatolik yuz berdi",
                "strengths": [],
                "weaknesses": [],
                "recommendations": []
            }
    
    def _create_analysis_prompt(self, resume_text: str, criteria: Dict, vacancy_info: Dict) -> str:
        """AI uchun prompt yaratish"""
        
        prompt = f"""
RESUME TAHLILI UCHUN VAZIFA:

VAKANSIYA MA'LUMOTLARI:
- Nomi: {vacancy_info.get('title', 'N/A')}
- Tavsif: {vacancy_info.get('description', 'N/A')}
- Talablar: {vacancy_info.get('requirements', 'N/A')}

AI TAHLIL KRITERIYLARI:
- Ko'nikmalar: {criteria.get('skills', 'N/A')}
- Tajriba: {criteria.get('experience', 'N/A')} yil
- Ta'lim: {criteria.get('education', 'N/A')}
- Tillar: {criteria.get('languages', 'N/A')}
- Qo'shimcha: {criteria.get('additional', 'N/A')}

RESUME MATNI:
{resume_text}

TAHLIL QILING VA QUYIDAGI JSON FORMATDA JAVOB BERING:
{{
    "match_percentage": 75,
    "analysis": "Umumiy tahlil matni",
    "strengths": ["Kuchli tomonlar ro'yxati"],
    "weaknesses": ["Zaif tomonlar ro'yxati"],
    "recommendations": ["Tavsiyalar ro'yxati"],
    "skills_match": {{"python": true, "javascript": false}},
    "experience_match": true,
    "education_match": true,
    "languages_match": true
}}

ESLATMA: 
- match_percentage 0 dan 100 gacha bo'lishi kerak
- Har bir kriteriyani alohida baholang
- 60% dan past bo'lsa, rad etish sabablari aniq ko'rsating
"""
        
        return prompt
    
    def _parse_analysis_result(self, analysis_text: str) -> Dict:
        """AI javobini parse qilish"""
        try:
            # JSON qismini topish
            json_start = analysis_text.find('{')
            json_end = analysis_text.rfind('}') + 1
            
            if json_start != -1 and json_end != -1:
                json_str = analysis_text[json_start:json_end]
                return json.loads(json_str)
            else:
                # Agar JSON topilmasa, oddiy tahlil
                return {
                    "match_percentage": 50,
                    "analysis": analysis_text,
                    "strengths": [],
                    "weaknesses": [],
                    "recommendations": []
                }
                
        except json.JSONDecodeError:
            return {
                "match_percentage": 50,
                "analysis": analysis_text,
                "strengths": [],
                "weaknesses": [],
                "recommendations": []
            }
    
    def evaluate_interview_answers(self, questions: List[str], answers: List[str], 
                                 vacancy_info: Dict, criteria: Dict) -> Dict:
        """Suhbat javoblarini baholash"""
        
        # Savol-javoblarni birlashtirish
        qa_pairs = []
        for i, (q, a) in enumerate(zip(questions, answers), 1):
            qa_pairs.append(f"Savol {i}: {q}\nJavob {i}: {a}")
        
        qa_text = "\n\n".join(qa_pairs)
        
        prompt = f"""
SUHBAT JAVOBLARINI BAHOLASH:

VAKANSIYA MA'LUMOTLARI:
- Nomi: {vacancy_info.get('title', 'N/A')}
- Talablar: {vacancy_info.get('requirements', 'N/A')}

KRITERILAR:
- Ko'nikmalar: {criteria.get('skills', 'N/A')}
- Tajriba: {criteria.get('experience', 'N/A')} yil

SAVOL-JAVOBLAR:
{qa_text}

JAVOBLARNI BAHOLANG VA QUYIDAGI JSON FORMATDA NATIJA BERING:
{{
    "total_score": 85,
    "individual_scores": [80, 90, 85],
    "evaluation": "Umumiy baholash matni",
    "strengths": ["Kuchli javoblar"],
    "improvements": ["Yaxshilanishi kerak bo'lgan tomonlar"],
    "recommendation": "Qabul qilish yoki rad etish tavsiyasi",
    "passed": true
}}

ESLATMA:
- total_score 0 dan 100 gacha
- individual_scores har bir savol uchun ball
- passed: 70 ball va undan yuqori bo'lsa true
- Javoblarning sifati, aniqlik va professionalligini baholang
"""
        
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Siz professional HR suhbat o'tkazuvchisigiz. Nomzod javoblarini baholaysiz."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=1000
            )
            
            result_text = response.choices[0].message.content
            
            # JSON parse qilish
            try:
                json_start = result_text.find('{')
                json_end = result_text.rfind('}') + 1
                json_str = result_text[json_start:json_end]
                result = json.loads(json_str)
                
                # Natijani tekshirish
                if result.get('total_score', 0) >= 70:
                    result['passed'] = True
                else:
                    result['passed'] = False
                    
                return result
                
            except json.JSONDecodeError:
                return {
                    "total_score": 60,
                    "evaluation": result_text,
                    "passed": False,
                    "individual_scores": [60] * len(questions),
                    "strengths": [],
                    "improvements": [],
                    "recommendation": "Baholashda xatolik"
                }
                
        except Exception as e:
            print(f"Suhbat baholashda xatolik: {e}")
            return {
                "total_score": 0,
                "evaluation": "Baholashda xatolik yuz berdi",
                "passed": False,
                "individual_scores": [0] * len(questions),
                "strengths": [],
                "improvements": [],
                "recommendation": "Qayta urinib ko'ring"
            }
    
    def generate_interview_questions(self, criteria: Dict, vacancy_info: Dict, count: int = 3) -> List[str]:
        """Suhbat savollarini avtomatik yaratish (ixtiyoriy)"""
        
        prompt = f"""
SUHBAT SAVOLLARI YARATISH:

VAKANSIYA: {vacancy_info.get('title', 'N/A')}
TALABLAR: {vacancy_info.get('requirements', 'N/A')}
KRITERILAR: Ko'nikmalar: {criteria.get('skills', 'N/A')}, 
Tajriba: {criteria.get('experience', 'N/A')} yil

{count} ta professional suhbat savolini yarating.
Savollar vakansiya talablariga mos va nomzod qobiliyatini baholashga yo'naltirilgan bo'lsin.

Javobni quyidagi formatda bering:
1. Savol matni
2. Savol matni
3. Savol matni
"""
        
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Siz professional HR mutaxassisigiz. Suhbat savollarini yaratasiz."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=800
            )
            
            questions_text = response.choices[0].message.content
            
            # Savollarni ajratish
            questions = []
            lines = questions_text.split('\n')
            
            for line in lines:
                line = line.strip()
                # Raqam bilan boshlanuvchi satrlarni topish
                if re.match(r'^\d+\.', line):
                    question = re.sub(r'^\d+\.\s*', '', line)
                    if question:
                        questions.append(question)
            
            # Agar kerakli miqdorda savol topilamsa
            if len(questions) >= count:
                return questions[:count]
            else:
                # Fallback: standart savollar
                return [
                    "O'zingiz haqingizda qisqacha gapiring.",
                    "Nega aynan bu vakansiyani tanladingiz?",
                    "Kelajakdagi rejalaringiz qanday?"
                ][:count]
                
        except Exception as e:
            print(f"Savollar yaratishda xatolik: {e}")
            return [
                "O'zingiz haqingizda qisqacha gapiring.",
                "Nega aynan bu vakansiyani tanladingiz?",
                "Kelajakdagi rejalaringiz qanday?"
            ][:count]

# Yordamchi funksiyalar
def validate_file_format(filename: str) -> bool:
    """Fayl formatini tekshirish"""
    allowed_extensions = ['.pdf', '.doc', '.docx']
    file_extension = os.path.splitext(filename)[1].lower()
    return file_extension in allowed_extensions

def get_file_size_mb(file_path: str) -> float:
    """Fayl hajmini MB da qaytarish"""
    try:
        size_bytes = os.path.getsize(file_path)
        size_mb = size_bytes / (1024 * 1024)
        return round(size_mb, 2)
    except:
        return 0

def create_safe_filename(original_filename: str, user_id: int) -> str:
    """Xavfsiz fayl nomi yaratish"""
    import time
    import re
    
    # Faqat harflar, raqamlar va nuqtalarni qoldirish
    safe_name = re.sub(r'[^a-zA-Z0-9.]', '_', original_filename)
    
    # Vaqt va user_id qo'shish
    timestamp = int(time.time())
    name, extension = os.path.splitext(safe_name)
    
    return f"{user_id}_{timestamp}_{name}{extension}"