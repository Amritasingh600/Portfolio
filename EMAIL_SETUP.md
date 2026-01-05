# Email Notification Setup Guide

## Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 2: Generate Gmail App Password

1. Go to your Google Account: https://myaccount.google.com/
2. Click on "Security" in the left sidebar
3. Enable "2-Step Verification" if not already enabled
4. After enabling 2FA, go back to Security
5. Click on "App passwords" (you'll see this option after enabling 2FA)
6. Select "Mail" as the app and "Windows Computer" as the device
7. Click "Generate"
8. Copy the 16-character password (it will look like: xxxx xxxx xxxx xxxx)

## Step 3: Configure .env File

Open the `.env` file and update it with your credentials:

```env
MAIL_USERNAME=singhamrita2904@gmail.com
MAIL_PASSWORD=your_16_character_app_password_here
```

**IMPORTANT:** 
- Use the App Password (16 characters), NOT your regular Gmail password
- Remove any spaces from the app password
- Keep the .env file secure and never commit it to GitHub

## Step 4: Run the Application

```bash
python app.py
```

## Step 5: Test the Contact Form

1. Open http://localhost:5000 in your browser
2. Navigate to the Contact section
3. Fill out the form and submit
4. You should receive an email at singhamrita2904@gmail.com

## Troubleshooting

### If emails aren't sending:

1. **Check App Password**: Make sure you're using the App Password, not your regular password
2. **Enable 2FA**: App Passwords only work with 2-Step Verification enabled
3. **Check Console**: Look for error messages in the terminal where Flask is running
4. **Gmail Security**: Make sure "Less secure app access" is OFF (we're using App Passwords which is more secure)

### Common Errors:

- **"535-5.7.8 Username and Password not accepted"**: Wrong credentials or using regular password instead of App Password
- **"SMTPAuthenticationError"**: 2FA not enabled or incorrect App Password
- **"Connection refused"**: Check your internet connection or firewall settings

## How It Works

1. User fills out the contact form on your portfolio
2. Form data is sent to Flask backend via AJAX
3. Flask creates an email using Flask-Mail
4. Email is sent via Gmail's SMTP server
5. You receive a formatted email notification at singhamrita2904@gmail.com
6. User sees success/error message

## Email Format

You'll receive emails with:
- Subject: "Portfolio Contact: [their subject]"
- Sender name and email (with clickable reply-to)
- Their message
- Nicely formatted HTML email

## Security Notes

- The .env file is in .gitignore - it won't be committed to GitHub
- App Passwords are more secure than regular passwords
- Never share your .env file or App Password
- Consider rotating your App Password periodically
