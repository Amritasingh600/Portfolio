# Amrita's Portfolio - Django Backend

A professional portfolio website with Django admin panel for content management.

## Features

- ✅ Full Admin Portal for content management
- ✅ Cloudinary integration for media storage
- ✅ Contact form with email notifications
- ✅ Dynamic content (Skills, Projects, Certificates, Gallery)
- ✅ Responsive design

## Local Development

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Create .env file with your credentials
cp .env.example .env
# Edit .env with your values

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## Environment Variables

Create a `.env` file with:

```env
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True

EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

## Deployment on Render

1. Push to GitHub
2. Create new Web Service on Render
3. Connect your repository
4. Set environment variables:
   - `DJANGO_SECRET_KEY`
   - `DEBUG=False`
   - `EMAIL_HOST_USER`
   - `EMAIL_HOST_PASSWORD`
   - `CLOUDINARY_CLOUD_NAME`
   - `CLOUDINARY_API_KEY`
   - `CLOUDINARY_API_SECRET`

5. Build Command:
   ```
   pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
   ```

6. Start Command:
   ```
   gunicorn portfolio_backend.wsgi:application
   ```

## Admin Panel

Access at `/admin/` to manage:
- Profile (name, bio, resume, social links)
- Skills & Categories
- Projects with tags
- Certificates
- Gallery images
- Contact messages

## Tech Stack

- Django 5.0+
- Cloudinary (media storage)
- WhiteNoise (static files)
- Gunicorn (production server)
