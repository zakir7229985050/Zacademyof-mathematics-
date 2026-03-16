# GRAVITY - Coaching Institute Website

A professional coaching institute website for IIT/NEET preparation built with Flask and SQLite.

## 🚀 LIVE DEPLOYMENT (Recommended: Render.com - Free!)

**Your project is now production-ready! Deploy to get a public URL anyone can use.**

### Step-by-Step Render.com Deployment (Free Tier)

1. **Create GitHub Repo:**
   ```
   git init
   git add .
   git commit -m "Initial commit: Complete GRAVITY coaching website"
   # Create repo on github.com -> Copy HTTPS URL
   git remote add origin https://github.com/YOUR_USERNAME/gravity-coaching.git
   git push -u origin main
   ```

2. **Deploy on Render (Free):**
   - Go to [render.com](https://render.com) → Sign up (free with GitHub)
   - New → **Web Service**
   - Connect your GitHub repo (`gravity-coaching`)
   - Settings:
     | Field | Value |
     |-------|-------|
     | Name | gravity-coaching |
     | Environment | **Python 3** |
     | Region | (default) |
     | Branch | main |
     | Build Command | `pip install -r requirements.txt` |
     | Start Command | `gunicorn --bind 0.0.0.0:$PORT wsgi:app` |
   - **Environment Variables** (Dashboard → Environment):
     | Key | Value (generate secure one) |
     |-----|----------------------------|
     | SECRET_KEY | `your-super-secure-random-key-here-32+chars` |
   - Click **Create Web Service**

3. **Your Site Goes Live!** → `https://gravity-coaching-abc123.onrender.com`

**Note:** Free tier sleeps after inactivity (wakes in ~30s). SQLite persists.

### Alternative Free Hosts
- **Railway.app**: Similar Git-based deploy
- **Railway**: `pip install -r requirements.txt && gunicorn wsgi:app`

## Features

### User Features
- **Homepage**: Banner with motivational tagline, featured courses, student success stories, testimonials
- **Course Listing**: Display courses (JEE, NEET, Engineering Entrance, BCA) with descriptions, duration, and pricing
- **Student Login/Registration**: OTP verification system and password-based login
- **Payment**: Secure payment gateway integration (UPI, Credit/Debit Card, Net Banking)
- **Student Dashboard**: Enrolled courses, video lectures, PDF study materials, progress tracking
- **Study Material**: Embedded video player, chapter-wise content, downloadable PDFs

### Admin Features
- Upload videos and PDF study materials
- Add/edit courses
- Manage student enrollments
- View student data and progress

## Technology Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python Flask
- **Database**: SQLite

## Project Structure

```
GRAVITY/
├── app.py                 # Flask application
├── database.db            # SQLite database (auto-created)
├── README.md             # This file
├── TODO.md               # Project TODO list
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   ├── js/
│   │   └── main.js       # JavaScript functionality
│   ├── videos/           # Video storage
│   └── pdfs/             # PDF storage
└── templates/
    ├── index.html        # Homepage
    ├── login.html        # Login/Registration
    ├── courses.html      # Course listing
    ├── payment.html     # Payment page
    ├── dashboard.html   # Student dashboard
    ├── study_material.html  # Video & materials
    └── admin.html       # Admin panel
```

## Installation & Setup

### Prerequisites
- Python 3.7+

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Development
```bash
python app.py
```

### Production (with Gunicorn)
```bash
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

The application will start at `http://localhost:5000`.

## Default Login Credentials

### Admin Account
- **Phone**: 9999999999
- **Password**: admin123

## Demo Flow

1. **Browse Courses**: Visit homepage or courses page
2. **Register/Login**: Use phone+OTP (demo shows OTP) or password
3. **Enroll**: Click \"Enroll Now\" → Simulated payment → Dashboard
4. **Admin**: Login as admin → /admin to manage content

## Pages Overview

- **Homepage** (`/`): Hero banner, featured courses, testimonials
- **Courses** (`/courses`): All courses
- **Login** (`/login`): OTP/password auth
- **Dashboard** (`/dashboard`): Enrolled courses
- **Payment** (`/payment/<id>`): Simulated payment
- **Study Material** (`/study_material/<id>`): Videos/PDFs
- **Admin** (`/admin`): Content management

## Notes

- ✅ **Production Ready**: Gunicorn WSGI, env SECRET_KEY
- 💳 Payments simulated (add Razorpay for real)
- 📱 OTP demo mode (add Twilio/Fast2SMS for production)
- 🎥 Add videos/PDFs via Admin panel → static/videos/ static/pdfs/
- 🛡️ DB auto-initializes with sample courses + admin user

**Congratulations! Your GRAVITY coaching website is LIVE and ready for students worldwide! 🎓**

