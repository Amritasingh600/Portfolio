from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    """Main profile information - only one instance should exist"""
    name = models.CharField(max_length=100, default='Amrita')
    tagline = models.CharField(max_length=200, default='ML Enthusiast | AIML Specialist | Problem Solver')
    description = models.TextField(help_text="Short description shown in home section")
    about_text_1 = models.TextField(help_text="First paragraph of about section")
    about_text_2 = models.TextField(help_text="Second paragraph of about section")
    about_text_3 = models.TextField(help_text="Third paragraph of about section")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    
    # Social Links
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    leetcode_url = models.URLField(blank=True)
    hackerrank_url = models.URLField(blank=True)
    
    # Stats
    cups_of_coffee = models.IntegerField(default=1000)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Ensure only one profile exists
        if not self.pk and Profile.objects.exists():
            existing = Profile.objects.first()
            self.pk = existing.pk
        super().save(*args, **kwargs)


class Education(models.Model):
    """Education entries"""
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year_range = models.CharField(max_length=50, help_text="e.g., 2024 - 2028")
    grade = models.CharField(max_length=50, help_text="CGPA or Percentage")
    order = models.IntegerField(default=0, help_text="Display order (lower = first)")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class SkillCategory(models.Model):
    """Skill categories like Programming Languages, ML & AI, etc."""
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, help_text="FontAwesome icon class, e.g., 'fas fa-laptop-code'")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"
        ordering = ['order']

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Individual skills"""
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, help_text="FontAwesome icon class")
    proficiency = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Proficiency percentage (0-100)"
    )
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Project(models.Model):
    """Portfolio projects"""
    title = models.CharField(max_length=200)
    emoji = models.CharField(max_length=10, blank=True, help_text="Emoji for the title, e.g., ✈️")
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ProjectTag(models.Model):
    """Tags for projects like Flask, Python, etc."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.project.title})"


class Achievement(models.Model):
    """Achievements and awards"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.CharField(max_length=50, help_text="e.g., 2025 or 2024-2025")
    icon_class = models.CharField(max_length=100, default='fas fa-trophy', help_text="FontAwesome icon class")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class CertificateCategory(models.Model):
    """Certificate categories like Microsoft, Coursera, etc."""
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Certificate Category"
        verbose_name_plural = "Certificate Categories"
        ordering = ['order']

    def __str__(self):
        return self.name


class Certificate(models.Model):
    """Certifications"""
    category = models.ForeignKey(CertificateCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='certificates')
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, help_text="e.g., AI-900 or Machine Learning")
    icon_class = models.CharField(max_length=100, default='fas fa-certificate', help_text="FontAwesome icon class")
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_url = models.URLField(blank=True, help_text="External URL if no file uploaded")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.issuer}"
    
    def get_certificate_link(self):
        if self.certificate_file:
            # Handle both FileField and direct URL strings (Cloudinary)
            str_value = str(self.certificate_file)
            if str_value.startswith('http://') or str_value.startswith('https://'):
                return str_value
            if hasattr(self.certificate_file, 'url'):
                return self.certificate_file.url
            return str_value
        return self.certificate_url


class GalleryImage(models.Model):
    """Gallery photos"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"


class TypingText(models.Model):
    """Typing animation texts"""
    text = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Typing Text"
        verbose_name_plural = "Typing Texts"

    def __str__(self):
        return self.text
