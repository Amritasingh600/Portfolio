# Amrita's Portfolio

![GitHub Actions](https://github.com/Amritasingh600/Portfolio/actions/workflows/deploy.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)

An interactive and modern portfolio website showcasing projects, skills, achievements, and certifications.

## 🌐 Live Demo
- **Render:** [amrita-portfolio.onrender.com](https://amrita-portfolio.onrender.com)

## Features

- 🎨 **Modern Design** - Clean and professional UI with purple wave theme
- ✨ **Dynamic Animations** - Smooth transitions and interactive elements
- 📱 **Fully Responsive** - Works perfectly on all devices
- 📧 **Contact Form** - Email notifications via Flask-Mail
- 🔒 **Secure** - Environment variables for sensitive data
- 🚀 **CI/CD** - GitHub Actions for automated testing
- 🎯 **Interactive Sections**:
  - Home with animated typing effect
  - About Me with education timeline
  - Skills with progress bars
  - Projects showcase with GitHub links
  - Achievements timeline
  - Certifications gallery (13 certificates)
  - Gallery with marquee effect
  - Contact form with email notifications
- 🔗 **Social Links** - GitHub, LinkedIn, LeetCode, HackerRank, Email
- 📄 **Resume Download** - Easy access to downloadable resume

## 🛠️ Tech Stack

- **Backend:** Python, Flask 3.0.0
- **Frontend:** HTML5, CSS3, JavaScript
- **Email:** Flask-Mail with Gmail SMTP
- **Deployment:** Render.com / GitHub Actions
- **Server:** Gunicorn (production)

## 📦 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Amritasingh600/Portfolio.git
cd Portfolio
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
cp .env.example .env
# Edit .env with your Gmail credentials
```

### 5. Run Locally
```bash
python app.py
# Visit http://localhost:5000
```

## 🔐 GitHub Secrets Setup

For GitHub Actions to work, add these secrets to your repository:

1. Go to **Repository → Settings → Secrets and variables → Actions**
2. Click **"New repository secret"**
3. Add the following secrets:

| Secret Name | Description |
|------------|-------------|
| `MAIL_USERNAME` | Your Gmail address (e.g., singhamrita2904@gmail.com) |
| `MAIL_PASSWORD` | Your Gmail App Password (16 characters) |
| `RENDER_DEPLOY_HOOK_URL` | (Optional) Render deploy hook URL |

### How to Get Gmail App Password:
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Enable **2-Step Verification**
3. Go to **App Passwords**
4. Generate a new app password for "Mail"

## 🚀 Deployment Options

### Option 1: Render.com (Recommended)
1. Connect your GitHub repo to Render
2. Set environment variables in Render dashboard
3. Render auto-deploys on every push to main

### Option 2: Railway.app
1. Connect GitHub repo
2. Add environment variables
3. Deploy automatically

### Option 3: Manual Deploy
```bash
gunicorn app:app
```

## 📁 Project Structure

```
Portfolio/
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions CI/CD
├── static/
│   ├── styles.css          # Main stylesheet
│   ├── script.js           # JavaScript functionality
│   ├── pic.jpeg            # Profile image
│   ├── resume.pdf          # Downloadable resume
│   ├── *.png               # Project screenshots
│   ├── *.jpeg              # Gallery images
│   └── *.pdf               # Certificate files
├── templates/
│   └── index.html          # Main HTML template
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Procfile                # Deployment configuration
├── .env.example            # Environment template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🔧 GitHub Actions Workflow

The workflow (`.github/workflows/deploy.yml`) automatically:

1. ✅ Checks out the code
2. ✅ Sets up Python 3.11
3. ✅ Installs dependencies
4. ✅ Runs syntax checks
5. ✅ Tests Flask app
6. ✅ Creates deployment artifact
7. ✅ Triggers Render deployment (optional)

### Workflow Triggers:
- **Push to main:** Full build + deploy
- **Pull requests:** Build + test only

## 🎨 Customization

### Colors
Edit CSS variables in `static/styles.css`:
```css
:root {
    --primary-color: #6c5ce7;
    --secondary-color: #00b894;
    --accent-color: #fd79a8;
}
```

### Typing Animation
Edit phrases in `static/script.js`:
```javascript
const phrases = [
    'ML Enthusiast',
    'AIML Specialist',
    'Problem Solver'
];
```

## 📧 Contact Form

The contact form sends email notifications using:
- **Flask-Mail** for email handling
- **Gmail SMTP** for delivery
- **App Passwords** for security

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

## 📄 License

This project is open source. Feel free to use it for your own portfolio!

## 👩‍💻 Author

**Amrita Singh**
- GitHub: [@Amritasingh600](https://github.com/Amritasingh600)
- LinkedIn: [Amrita Singh](https://www.linkedin.com/in/amrita-singh-308333326/)
- Email: singhamrita2904@gmail.com

---

⭐ Star this repo if you found it helpful!
