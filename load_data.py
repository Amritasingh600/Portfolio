"""
Initial data loader for Amrita's Portfolio.
Run: python manage.py shell < load_data.py
Or: python manage.py shell -c "exec(open('load_data.py', encoding='utf-8').read())"
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_backend.settings')

import django
django.setup()

from portfolio.models import (
    Profile, Education, SkillCategory, Skill, Project, ProjectTag,
    Achievement, CertificateCategory, Certificate, GalleryImage, TypingText
)

def load_data():
    print("Loading portfolio data...")
    
    # ==============================
    # Profile
    # ==============================
    profile, _ = Profile.objects.update_or_create(
        pk=1,
        defaults={
            'name': 'Amrita',
            'tagline': 'ML Enthusiast | AIML Specialist | Problem Solver',
            'description': "Passionate student crafting innovative solutions through code. Exploring the endless possibilities of technology and design.",
            'about_text_1': "I'm a passionate Computer Science student specializing in Artificial Intelligence and Machine Learning at GLA University. My journey in AI/ML is driven by curiosity and a desire to create intelligent solutions that make a real-world impact.",
            'about_text_2': "With expertise in machine learning algorithms, deep learning, and data science, I've completed comprehensive courses from Stanford University and earned multiple Azure AI certifications. I specialize in developing AI-powered applications, predictive models, and intelligent systems.",
            'about_text_3': "My technical arsenal includes Python, TensorFlow, scikit-learn, and various ML frameworks. I'm constantly exploring cutting-edge AI technologies and applying them to solve complex problems through innovative projects.",
            'email': 'singhamrita2904@gmail.com',
            'location': 'Mathura, Uttar Pradesh',
            'github_url': 'https://github.com/Amritasingh600',
            'linkedin_url': 'https://www.linkedin.com/in/amrita-singh-308333326/',
            'leetcode_url': 'https://leetcode.com/u/Amrita_singh600/',
            'hackerrank_url': 'https://www.hackerrank.com/profile/_2415500063',
            'cups_of_coffee': 1000,
            'profile_image': 'https://res.cloudinary.com/dwh7ztpa9/image/upload/v1767712422/portfolio/profile/pic.jpg',
            'resume': 'https://res.cloudinary.com/dwh7ztpa9/raw/upload/v1767712423/portfolio/resume/resume.pdf',
        }
    )
    print(f"✅ Profile: {profile.name}")

    # ==============================
    # Typing Texts
    # ==============================
    typing_texts = ['Full Stack Developer', 'Problem Solver', 'ML Enthusiast', 'AIML Specialist', 'Tech Explorer']
    for i, text in enumerate(typing_texts):
        TypingText.objects.update_or_create(text=text, defaults={'order': i, 'is_active': True})
    print(f"✅ {len(typing_texts)} Typing texts")

    # ==============================
    # Education
    # ==============================
    Education.objects.update_or_create(
        degree='Bachelor of Technology in Computer Science with Specialization in AIML',
        defaults={'institution': 'GLA University', 'year_range': '2024 - 2028', 'grade': 'CGPA: 8.2', 'order': 1}
    )
    Education.objects.update_or_create(
        degree='Senior Secondary Education',
        defaults={'institution': 'Kanha Makhan Public School', 'year_range': '2022 - 2024', 'grade': 'Percentage: 87%', 'order': 2}
    )
    print("✅ 2 Education entries")

    # ==============================
    # Skill Categories and Skills
    # ==============================
    skill_data = {
        'Programming Languages': {
            'icon': 'fas fa-laptop-code', 'order': 1,
            'skills': [
                ('Python', 'fab fa-python', 90),
                ('Java', 'fab fa-java', 85),
                ('JavaScript', 'fab fa-js', 88),
            ]
        },
        'Frameworks & Technologies': {
            'icon': 'fas fa-tools', 'order': 2,
            'skills': [
                ('Flask', 'fas fa-flask', 85),
                ('Django', 'fab fa-python', 80),
                ('Next.js', 'fab fa-react', 75),
                ('React', 'fab fa-react', 78),
            ]
        },
        'Machine Learning & AI': {
            'icon': 'fas fa-brain', 'order': 3,
            'skills': [
                ('TensorFlow', 'fas fa-brain', 82),
                ('scikit-learn', 'fas fa-cogs', 88),
                ('YOLO', 'fas fa-eye', 75),
                ('NLP', 'fas fa-language', 70),
            ]
        },
        'Tools & Platforms': {
            'icon': 'fas fa-cloud', 'order': 4,
            'skills': [
                ('Git/GitHub', 'fab fa-github', 90),
                ('Azure', 'fab fa-microsoft', 78),
                ('Docker', 'fab fa-docker', 65),
                ('VS Code', 'fas fa-code', 95),
            ]
        },
    }
    
    for cat_name, cat_data in skill_data.items():
        category, _ = SkillCategory.objects.update_or_create(
            name=cat_name,
            defaults={'icon_class': cat_data['icon'], 'order': cat_data['order']}
        )
        for i, (skill_name, icon, prof) in enumerate(cat_data['skills']):
            Skill.objects.update_or_create(
                category=category, name=skill_name,
                defaults={'icon_class': icon, 'proficiency': prof, 'order': i}
            )
    print("✅ 4 Skill categories with skills")

    # ==============================
    # Projects (with Cloudinary images)
    # ==============================
    projects = [
        {
            'title': 'AI Travel Planner', 'emoji': '✈️',
            'description': 'Comprehensive travel planning app using Google Gemini AI to generate personalized itineraries with interactive maps, route planning, and detailed recommendations.',
            'github_url': 'https://github.com/Amritasingh600/travel_planner',
            'live_url': 'https://travel-planner-chi-flax.vercel.app/',
            'image': 'https://res.cloudinary.com/dwh7ztpa9/image/upload/v1767712425/portfolio/projects/travel%20planner.png',
            'order': 1, 'tags': ['Flask', 'Google Gemini AI', 'Leaflet.js'],
        },
        {
            'title': 'Chest X-Ray Pneumonia Detection', 'emoji': '🏥',
            'description': 'AI-powered medical diagnosis system combining YOLO deep learning models with Gemini AI for pneumonia detection and comprehensive medical analysis.',
            'github_url': 'https://github.com/Amritasingh600/x_ray_detect',
            'live_url': 'https://github.com/Amritasingh600/x_ray_detect',
            'image': 'https://res.cloudinary.com/dwh7ztpa9/image/upload/v1767712426/portfolio/projects/pneo_detect.png',
            'order': 2, 'tags': ['Streamlit', 'YOLO', 'Gemini AI'],
        },
        {
            'title': 'AI Educational Platform', 'emoji': '📚',
            'description': 'Dual-portal educational system with AI Tutor using Socratic method, offline search engine, and faculty knowledge base management.',
            'github_url': 'https://github.com/Amritasingh600/aitutor',
            'live_url': 'https://github.com/Amritasingh600/aitutor',
            'image': 'https://res.cloudinary.com/dwh7ztpa9/image/upload/v1767712427/portfolio/projects/ai%20tutor.png',
            'order': 3, 'tags': ['Next.js 14', 'TypeScript', 'Google AI'],
        },
        {
            'title': 'Climate Data Visual Explorer', 'emoji': '🌍',
            'description': 'Modern web app to visualize and analyze climate data with AI insights, anomaly detection, interactive charts, and air quality monitoring.',
            'github_url': 'https://github.com/Amritasingh600/weather-app',
            'live_url': 'https://github.com/Amritasingh600/weather-app',
            'image': 'https://res.cloudinary.com/dwh7ztpa9/image/upload/v1767712428/portfolio/projects/climate_pred.png',
            'order': 4, 'tags': ['Flask', 'Chart.js', 'Open-Meteo API'],
        },
        {
            'title': 'Diabetes Prediction System', 'emoji': '💉',
            'description': 'Machine learning-based healthcare application for diabetes risk prediction with trained model pipelines and user-friendly interface.',
            'github_url': 'https://github.com/Amritasingh600/diabetes_prediction',
            'live_url': 'https://github.com/Amritasingh600/diabetes_prediction',
            'image': 'https://res.cloudinary.com/dwh7ztpa9/image/upload/v1767712429/portfolio/projects/diabetes_pred.png',
            'order': 5, 'tags': ['Python', 'Machine Learning', 'Flask'],
        },
        {
            'title': 'Real vs Fake Image Detection', 'emoji': '🔍',
            'description': 'Deep learning application to detect fake or manipulated images using advanced computer vision techniques and neural networks.',
            'github_url': 'https://github.com/Amritasingh600/Real_vs_Fake',
            'live_url': 'https://github.com/Amritasingh600/Real_vs_Fake',
            'image': 'https://res.cloudinary.com/dwh7ztpa9/image/upload/v1767712430/portfolio/projects/real%20vs%20ai.png',
            'order': 6, 'tags': ['Python', 'Deep Learning', 'Flask'],
        },
    ]
    
    for proj in projects:
        tags = proj.pop('tags')
        project, _ = Project.objects.update_or_create(title=proj['title'], defaults=proj)
        project.tags.all().delete()
        for tag_name in tags:
            ProjectTag.objects.create(project=project, name=tag_name)
    print(f"✅ {len(projects)} Projects")

    # ==============================
    # Achievements
    # ==============================
    achievements = [
        {'title': 'Ventureathon Winner - 2nd Position', 'description': 'Secured 2nd position in Ventureathon, demonstrating innovative entrepreneurial skills and technical excellence in developing venture solutions.', 'date': '2025', 'icon_class': 'fas fa-trophy', 'order': 1},
        {'title': 'IIT Bombay Techfest Participant', 'description': "Participated in IIT Bombay Techfest, one of Asia's largest science and technology festivals, showcasing technical projects and innovations.", 'date': '2025', 'icon_class': 'fas fa-university', 'order': 2},
        {'title': 'Machine Learning Course Completion', 'description': 'Successfully completed comprehensive Machine Learning course from Stanford University, mastering supervised, unsupervised learning, and advanced algorithms.', 'date': '2025-2026', 'icon_class': 'fas fa-graduation-cap', 'order': 3},
        {'title': 'Microsoft Azure Certifications', 'description': 'Earned multiple Microsoft Azure certifications including Azure Fundamentals and AI Fundamentals (AI-900), demonstrating cloud computing expertise.', 'date': '2025', 'icon_class': 'fas fa-certificate', 'order': 4},
        {'title': 'HackerRank Programming Excellence', 'description': 'Achieved multiple HackerRank certifications in C programming, demonstrating strong problem-solving abilities and programming proficiency.', 'date': '2024-2025', 'icon_class': 'fas fa-code', 'order': 5},
    ]
    for ach in achievements:
        Achievement.objects.update_or_create(title=ach['title'], defaults=ach)
    print(f"✅ {len(achievements)} Achievements")

    # ==============================
    # Certificates (with Cloudinary PDFs)
    # ==============================
    cert_categories = {'Microsoft': 1, 'Coursera - Stanford': 2, 'Data Science': 3, 'Web Development': 4, 'Programming': 5}
    for name, order in cert_categories.items():
        CertificateCategory.objects.update_or_create(name=name, defaults={'order': order})
    
    certificates = [
        {'title': 'MS Azure Fundamentals', 'issuer': 'Microsoft', 'description': 'Azure Certification', 'icon_class': 'fab fa-microsoft', 'category': 'Microsoft', 'certificate_file': 'https://res.cloudinary.com/dwh7ztpa9/raw/upload/v1767712432/portfolio/certificates/ms%20azure%20fundamentals%20certificate.pdf'},
        {'title': 'Azure AI Fundamentals', 'issuer': 'Microsoft', 'description': 'AI-900', 'icon_class': 'fab fa-microsoft', 'category': 'Microsoft', 'certificate_file': 'https://learn.microsoft.com/api/credentials/share/en-us/AmritaSingh-0442/A71F2BE053E0FD5E?sharingId=3D17A3C2FAFEBDCA'},
        {'title': 'Machine Learning Specialization', 'issuer': 'Coursera - Stanford University', 'description': 'Machine Learning', 'icon_class': 'fas fa-brain', 'category': 'Coursera - Stanford', 'certificate_file': 'https://res.cloudinary.com/dwh7ztpa9/raw/upload/v1767712434/portfolio/certificates/machine_learning_stanford.pdf'},
        {'title': 'Supervised Machine Learning', 'issuer': 'Coursera - Stanford University', 'description': 'Machine Learning', 'icon_class': 'fas fa-chart-line', 'category': 'Coursera - Stanford', 'certificate_file': 'https://res.cloudinary.com/dwh7ztpa9/raw/upload/v1767712436/portfolio/certificates/supervised%20learning%20certificate.pdf'},
        {'title': 'Unsupervised Learning', 'issuer': 'Coursera - Stanford University', 'description': 'Machine Learning', 'icon_class': 'fas fa-project-diagram', 'category': 'Coursera - Stanford', 'certificate_file': 'https://res.cloudinary.com/dwh7ztpa9/raw/upload/v1767712437/portfolio/certificates/unsupervised_certificate.pdf'},
        {'title': 'Advanced Learning Algorithms', 'issuer': 'Coursera - Stanford University', 'description': 'Machine Learning', 'icon_class': 'fas fa-robot', 'category': 'Coursera - Stanford', 'certificate_file': 'https://res.cloudinary.com/dwh7ztpa9/raw/upload/v1767712438/portfolio/certificates/advanced_learning_algorithm.pdf'},
        {'title': 'HTML5 Certification', 'issuer': 'Infosys Springboard', 'description': 'Web Development', 'icon_class': 'fab fa-html5', 'category': 'Web Development', 'certificate_file': 'https://res.cloudinary.com/dwh7ztpa9/raw/upload/v1767712449/portfolio/certificates/infosys%20html.pdf'},
        {'title': 'CSS3 Certification', 'issuer': 'Infosys Springboard', 'description': 'Web Development', 'icon_class': 'fab fa-css3-alt', 'category': 'Web Development', 'certificate_file': 'https://res.cloudinary.com/dwh7ztpa9/raw/upload/v1767712450/portfolio/certificates/css%20infosys.pdf'},
        {'title': 'JavaScript Certification', 'issuer': 'Infosys Springboard', 'description': 'Web Development', 'icon_class': 'fab fa-js', 'category': 'Web Development', 'certificate_file': 'https://res.cloudinary.com/dwh7ztpa9/raw/upload/v1767712451/portfolio/certificates/js%20infosys%20%281%29.pdf'},
        {'title': 'C Programming (Basic)', 'issuer': 'HackerRank', 'description': 'Programming Certification', 'icon_class': 'fas fa-code', 'category': 'Programming', 'certificate_file': 'https://res.cloudinary.com/dwh7ztpa9/raw/upload/v1767712457/portfolio/certificates/c%20basic%20hackerrank.pdf'},
        {'title': 'C Programming (Intermediate)', 'issuer': 'HackerRank', 'description': 'Programming Certification', 'icon_class': 'fas fa-code', 'category': 'Programming', 'certificate_file': 'https://res.cloudinary.com/dwh7ztpa9/raw/upload/v1767712464/portfolio/certificates/intermediate%20c%20hackkerank.pdf'},
    ]
    
    for i, cert in enumerate(certificates):
        cat_name = cert.pop('category')
        category = CertificateCategory.objects.get(name=cat_name)
        Certificate.objects.update_or_create(
            title=cert['title'],
            defaults={**cert, 'category': category, 'order': i+1}
        )
    print(f"✅ {len(certificates)} Certificates")

    # ==============================
    # Gallery Images (Cloudinary)
    # ==============================
    gallery = [
        {'title': 'Ventureathon 2025', 'subtitle': '2nd Position Winner', 'image': 'https://res.cloudinary.com/dwh7ztpa9/image/upload/v1767712466/portfolio/gallery/venture.jpg', 'order': 1},
        {'title': 'IIT Bombay', 'subtitle': 'Techfest Participant', 'image': 'https://res.cloudinary.com/dwh7ztpa9/image/upload/v1767712466/portfolio/gallery/iitbombay%20techfest.jpg', 'order': 2},
    ]
    for img in gallery:
        GalleryImage.objects.update_or_create(title=img['title'], defaults=img)
    print(f"✅ {len(gallery)} Gallery images")

    print("\n🎉 All data loaded successfully!")
    print("Visit http://localhost:8000/ to see your portfolio")
    print("Admin panel: http://localhost:8000/admin/")

if __name__ == '__main__':
    load_data()
else:
    load_data()
