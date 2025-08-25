# 🤖 Job Bot - Ish Topish Boti

Telegram orqali ish beruvchilar va ishga topshiruvchilarni bog'lovchi AI-powered bot.

## 🏗️ Loyiha Strukturasi

```
job_bot/
├── bot.py                    # Asosiy bot fayli
├── run.py
├── setup.py
├── config.py                 # Konfiguratsiya
├── requirements.txt          # Python kutubxonalar
├── .env                      # Environment variables
├── README.md                 # Bu fayl
├── job_bot.db
├── database/
│   ├── __init__.py
│   └── models.py            # Database modellari va CRUD
├──
├── services/
│   ├── __init__.py
│   ├── ai_service.py        # OpenAI integratsiyasi
│   └── file_service.py      # Fayl boshqaruvi
├──
├── handlers/
│   ├── __init__.py
│   ├── employer.py          # Ish beruvchi handlerlari
│   └── jobseeker.py         # Ishga topshiruvchi handlerlari
├──
├── utils/
│   ├── __init__.py
│   └── languages.py         # Ikki til qo'llab-quvvatlash
├──
└── files/
    └── resumes/             # Resume fayllar saqlanadigan papka
```

## 🚀 O'rnatish

### 1. Repository ni clone qiling
```bash
git clone https://github.com/abdulazizDevop/ai_recruiter.git
cd ai_recruiter
```

### 2. Virtual environment yarating
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# yoki
venv\Scripts\activate     # Windows
```

### 3. Kutubxonalarni o'rnating
```bash
pip install -r requirements.txt
```

### 4. Environment variables o'rnating
```bash
# .env fayl yaratish
python config.py
```

`.env` faylni to'ldiring:
```env
# Bot Token - @BotFather dan oling
TELEGRAM_BOT_TOKEN=your_bot_token_here

# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Database
DATABASE_URL=job_bot.db

# Admin users (telegram ID)
ADMIN_USERS=123456789

# Files storage
FILES_PATH=files
MAX_FILE_SIZE_MB=10

# AI Settings
MIN_MATCH_PERCENTAGE=60
MIN_INTERVIEW_SCORE=70
```

### 5. Botni ishga tushiring
```bash
python setup.py
```
```bash
python run.py
```
```bash
python bot.py
```

## 📋 Xususiyatlar

### 🏢 Ish Beruvchilar uchun:
- ✅ `/ad_vacancy` - Maxfiy vakansiya yaratish komandasi
- ✅ Kompaniya va vakansiya ma'lumotlari kiritish (16 bosqich)
- ✅ AI uchun kriteriyalar o'rnatish
- ✅ Suhbat savollarini kiritish (3-7 ta)
- ✅ Vakansiyalar boshqaruvi (faollashtirish/arxivlash)
- ✅ Kelgan arizalarni ko'rish
- ✅ Nomzod ma'lumotlarini olish

### 👤 Ishga Topshiruvchilar uchun:
- ✅ Kompaniyalar ro'yxatini ko'rish
- ✅ Vakansiyalarni tanlash
- ✅ Resume yuklash (PDF, DOC, DOCX)
- ✅ AI tahlili (60% dan yuqori moslik kerak)
- ✅ Avtomatik suhbat (AI savollari)
- ✅ Qo'shimcha ma'lumotlar kiritish
- ✅ Ish beruvchiga avtomatik yuborish

### 🤖 AI Xususiyatlari:
- ✅ Resume tahlili (GPT-4)
- ✅ Ko'nikmalar, tajriba, ta'lim baholash
- ✅ Suhbat javoblarini baholash
- ✅ Avtomatik savol yaratish (ixtiyoriy)
- ✅ Har xil til qo'llab-quvvatlash

### ⚙️ Admin Panel:
- ✅ Tizim statistikasi
- ✅ Foydalanuvchilar soni
- ✅ Vakansiyalar statistikasi
- ✅ Arizalar analitikasi

## 🌐 Tillar

- 🇺🇿 O'zbek tili
- 🇷🇺 Rus tili

## 📊 Database Schema

### Users
- Telegram ma'lumotlari
- Til va rol
- Yaratilish sanasi
- Yangilanish sanasi

### Companies
- Kompaniya nomi va tavsifi
- Ish beruvchi bog'lanishi

### Vacancies
- To'liq vakansiya ma'lumotlari
- AI kriteriylari
- Suhbat savollari
- Status (active/archived)

### Job Applications
- Resume fayl yo'li
- AI tahlili natijalari
- Suhbat javoblari
- Status va ballari

### Analytics
- Barcha hodisalar
- Statistika uchun ma'lumotlar

## 🔧 Ishlatilgan Texnologiyalar

- **aiogram 3.2.0** - Telegram Bot API
- **OpenAI GPT-4** - AI tahlil va baholash
- **SQLite3** - Ma'lumotlar bazasi (test)
- **PostgreSQL** - Production database (keyinchalik)
- **PyPDF2** - PDF fayllarni o'qish
- **python-docx** - Word fayllarni o'qish

## 📝 Foydalanish

### Ish beruvchi sifatida:
1. `/start` - Botni boshlash
2. Til tanlash
3. "Ish beruvchi" ni tanlash yoki `/ad_vacancy` komandasi
4. Vakansiya yaratish (16 bosqich)
5. Kelgan arizalarni ko'rish

### Ishga topshiruvchi sifatida:
1. `/start` - Botni boshlash
2. Til tanlash
3. "Ishga topshiruvchi" ni tanlash
4. Kompaniya va vakansiya tanlash
5. Resume yuklash
6. AI tahlilidan o'tish
7. Suhbat savollarga javob berish
8. Qo'shimcha ma'lumotlar kiritish

## 🔒 Xavfsizlik

- Fayl hajmi cheklangan (10MB)
- Faqat PDF, DOC, DOCX fayllar qabul qilinadi
- Admin paneli himoyalangan
- Ma'lumotlar bazasi xavfsiz

## 🚀 Production uchun

1. PostgreSQL ga o'tish

## 📞 Yordam

- [https:/t.me/AbdulazizAlimov](https:/t.me/AbdulazizAlimov)
- [https:/www.linkedin.com/in/abdulazizolimov](https:/www.linkedin.com/in/abdulazizolimov)

## 📄 License

MIT License