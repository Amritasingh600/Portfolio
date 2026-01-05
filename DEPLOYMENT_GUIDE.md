# Portfolio Deployment Guide

## 🔒 Security First

### ✅ Your .env file is SAFE because:
1. It's listed in `.gitignore` - won't be pushed to GitHub
2. Never share or commit `.env` to any repository
3. Use `.env.example` as a template for others (without real credentials)

---

## 🚀 Best Deployment Options for Flask Portfolio

### **RECOMMENDED: Render.com (Best for Flask)**

#### Why Render?
- ✅ **Free tier available** with decent limits
- ✅ **Easy Flask deployment** (built for Python)
- ✅ **Environment variables** (secure password storage)
- ✅ **Custom domain support**
- ✅ **Auto-deploy from GitHub**
- ✅ **HTTPS included**

#### Deployment Steps:

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio commit"
   git branch -M main
   git remote add origin https://github.com/Amritasingh600/portfolio.git
   git push -u origin main
   ```

2. **Sign up at Render.com:**
   - Go to https://render.com/
   - Sign up with GitHub

3. **Create New Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name:** amrita-portfolio
     - **Environment:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`
     - **Instance Type:** Free

4. **Add Environment Variables:**
   - In Render dashboard, go to "Environment"
   - Add:
     - `MAIL_USERNAME` = singhamrita2904@gmail.com
     - `MAIL_PASSWORD` = your_app_password

5. **Deploy!**
   - Click "Create Web Service"
   - Wait 2-3 minutes
   - Your site will be live at: `https://amrita-portfolio.onrender.com`

---

### **Alternative Option 1: PythonAnywhere**

#### Pros:
- ✅ Free tier (good for portfolios)
- ✅ Simple Flask setup
- ✅ Beginner-friendly

#### Cons:
- ❌ Limited outbound connections on free tier (email may not work)
- ❌ Custom domain requires paid plan

#### Best For: Static portfolios without email functionality

---

### **Alternative Option 2: Railway.app**

#### Pros:
- ✅ Modern platform
- ✅ Good free tier
- ✅ GitHub integration
- ✅ Easy environment variables

#### Cons:
- ❌ Free tier credits expire monthly

#### Deployment:
1. Sign up at https://railway.app/
2. Connect GitHub repo
3. Add environment variables
4. Deploy automatically

---

### **Alternative Option 3: Vercel (Requires Modifications)**

#### Note:
Vercel is primarily for serverless/static sites. Flask requires adaptation:
- Need to convert to serverless functions
- More complex setup
- Better for Next.js/React

#### Not Recommended for this Flask app

---

## 📦 Pre-Deployment Checklist

### 1. Add Gunicorn (for production)
Update `requirements.txt`:
```txt
Flask==3.0.0
Flask-Mail==0.9.1
python-dotenv==1.0.0
gunicorn==21.2.0
```

Then install:
```bash
pip install gunicorn
```

### 2. Create Procfile (for some platforms)
Create `Procfile` in root directory:
```
web: gunicorn app:app
```

### 3. Test locally with Gunicorn:
```bash
gunicorn app:app
```
Visit: http://localhost:8000

### 4. Update app.py for production:
```python
if __name__ == '__main__':
    # Use environment variable for port (important for deployment)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
```

### 5. Security Check:
```bash
# Verify .env is ignored
git status
# Should NOT show .env file
```

---

## 🎯 My Recommendation: Use Render.com

### Why?
1. **Free forever** (with sleep after inactivity)
2. **Email works** perfectly (no connection restrictions)
3. **Simple deployment** from GitHub
4. **Secure** environment variable storage
5. **Auto-deploys** when you push to GitHub
6. **Professional** (shows you're tech-savvy)

---

## 🔧 Quick Start with Render:

```bash
# 1. Install gunicorn
pip install gunicorn

# 2. Update requirements.txt
pip freeze > requirements.txt

# 3. Initialize git (if not already)
git init
git add .
git commit -m "Ready for deployment"

# 4. Push to GitHub
# Create repo at github.com/Amritasingh600/portfolio
git remote add origin https://github.com/Amritasingh600/portfolio.git
git push -u origin main

# 5. Go to render.com and connect your repo
# 6. Add environment variables in Render dashboard
# 7. Deploy!
```

---

## ⚡ After Deployment:

1. **Test contact form** - Send yourself a test email
2. **Check all links** - GitHub, LinkedIn, certificates
3. **Test on mobile** - Responsive design check
4. **Update resume** link if needed
5. **Share your portfolio URL!**

---

## 📱 Custom Domain (Optional)

After deploying to Render:
1. Buy domain from Namecheap/GoDaddy (~$10-15/year)
2. In Render: Settings → Custom Domains
3. Add your domain and update DNS records
4. Example: `amritasingh.tech`

---

## 💡 Pro Tips:

- Keep GitHub repo updated with latest changes
- Monitor Render dashboard for any errors
- Render free tier sleeps after 15 min inactivity (first load may be slow)
- Consider upgrading to paid plan ($7/month) if you want always-on
- Add Google Analytics to track visitors

---

## 🆘 Troubleshooting:

**Email not working?**
- Check environment variables in Render dashboard
- Verify app password is correct
- Check Render logs for errors

**Site not loading?**
- Check Render build logs
- Verify all dependencies in requirements.txt
- Ensure gunicorn is installed

**Images not showing?**
- Verify all paths use `url_for('static', filename='...')`
- Check static folder structure
