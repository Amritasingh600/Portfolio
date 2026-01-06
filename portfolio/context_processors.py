from .models import Profile, Project, Achievement, Certificate


def portfolio_context(request):
    """
    Context processor to add common portfolio data to all templates.
    This makes profile data available in all templates without explicitly passing it.
    """
    profile = Profile.objects.first()
    
    # Count active items for stats
    project_count = Project.objects.filter(is_active=True).count()
    achievement_count = Achievement.objects.filter(is_active=True).count()
    certificate_count = Certificate.objects.filter(is_active=True).count()
    
    return {
        'site_profile': profile,
        'stats': {
            'projects': project_count,
            'achievements': achievement_count,
            'certificates': certificate_count,
            'coffee': profile.cups_of_coffee if profile else 1000,
        }
    }
