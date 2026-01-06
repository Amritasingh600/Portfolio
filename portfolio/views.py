from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json

from .models import (
    Profile, Education, SkillCategory, Project, Achievement,
    Certificate, GalleryImage, ContactMessage, TypingText
)


def home(request):
    """Main portfolio page"""
    context = get_portfolio_context()
    return render(request, 'index.html', context)


def get_portfolio_context():
    """Get all portfolio data for template context"""
    profile = Profile.objects.first()
    
    # Count active items for stats
    project_count = Project.objects.filter(is_active=True).count()
    achievement_count = Achievement.objects.filter(is_active=True).count()
    certificate_count = Certificate.objects.filter(is_active=True).count()
    
    context = {
        'profile': profile,
        'education_list': Education.objects.filter(is_active=True),
        'skill_categories': SkillCategory.objects.filter(is_active=True).prefetch_related('skills'),
        'projects': Project.objects.filter(is_active=True).prefetch_related('tags'),
        'achievements': Achievement.objects.filter(is_active=True),
        'certificates': Certificate.objects.filter(is_active=True).select_related('category'),
        'gallery_images': GalleryImage.objects.filter(is_active=True),
        'typing_texts': list(TypingText.objects.filter(is_active=True).values_list('text', flat=True)),
        
        # Stats
        'project_count': project_count,
        'achievement_count': achievement_count,
        'certificate_count': certificate_count,
    }
    return context


@csrf_exempt
def send_message(request):
    """Handle contact form submission"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', '')
            email = data.get('email', '')
            subject = data.get('subject', '')
            message = data.get('message', '')

            # Save to database
            contact = ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            # Try to send email notification
            try:
                profile = Profile.objects.first()
                recipient_email = profile.email if profile else settings.EMAIL_HOST_USER
                
                email_body = f"""
New message from your portfolio website!

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
Sent from your portfolio contact form
"""
                
                send_mail(
                    subject=f'Portfolio Contact: {subject}',
                    message=email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[recipient_email],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")
                # Still return success as message was saved

            return JsonResponse({
                'success': True,
                'message': 'Message sent successfully!'
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


def api_portfolio_data(request):
    """API endpoint to get all portfolio data as JSON"""
    profile = Profile.objects.first()
    
    data = {
        'profile': {
            'name': profile.name if profile else '',
            'tagline': profile.tagline if profile else '',
            'description': profile.description if profile else '',
            'email': profile.email if profile else '',
            'location': profile.location if profile else '',
            'github_url': profile.github_url if profile else '',
            'linkedin_url': profile.linkedin_url if profile else '',
            'leetcode_url': profile.leetcode_url if profile else '',
            'hackerrank_url': profile.hackerrank_url if profile else '',
        } if profile else None,
        'skills': [
            {
                'category': cat.name,
                'icon': cat.icon_class,
                'skills': [
                    {'name': s.name, 'icon': s.icon_class, 'proficiency': s.proficiency}
                    for s in cat.skills.filter(is_active=True)
                ]
            }
            for cat in SkillCategory.objects.filter(is_active=True)
        ],
        'projects': [
            {
                'title': p.title,
                'emoji': p.emoji,
                'description': p.description,
                'image': p.image.url if p.image else '',
                'github_url': p.github_url,
                'live_url': p.live_url,
                'tags': list(p.tags.values_list('name', flat=True))
            }
            for p in Project.objects.filter(is_active=True)
        ],
        'achievements': [
            {
                'title': a.title,
                'description': a.description,
                'date': a.date,
                'icon': a.icon_class
            }
            for a in Achievement.objects.filter(is_active=True)
        ],
        'certificates': [
            {
                'title': c.title,
                'issuer': c.issuer,
                'description': c.description,
                'icon': c.icon_class,
                'link': c.get_certificate_link()
            }
            for c in Certificate.objects.filter(is_active=True)
        ],
        'gallery': [
            {
                'title': g.title,
                'subtitle': g.subtitle,
                'image': g.image.url if g.image else ''
            }
            for g in GalleryImage.objects.filter(is_active=True)
        ]
    }
    
    return JsonResponse(data)
