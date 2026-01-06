from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count
from .models import (
    Profile, Education, SkillCategory, Skill, Project, ProjectTag,
    Achievement, CertificateCategory, Certificate, GalleryImage,
    ContactMessage, TypingText
)


# Inline classes for related models
class EducationInline(admin.TabularInline):
    model = Education
    extra = 0


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('name', 'icon_class', 'proficiency', 'order', 'is_active')


class ProjectTagInline(admin.TabularInline):
    model = ProjectTag
    extra = 2


class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 0
    fields = ('title', 'issuer', 'icon_class', 'certificate_file', 'order', 'is_active')


# Main Admin Classes
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tagline', 'description', 'profile_image', 'resume')
        }),
        ('About Section', {
            'fields': ('about_text_1', 'about_text_2', 'about_text_3'),
            'classes': ('collapse',)
        }),
        ('Contact Information', {
            'fields': ('email', 'location')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'leetcode_url', 'hackerrank_url'),
            'classes': ('collapse',)
        }),
        ('Fun Stats', {
            'fields': ('cups_of_coffee',),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        # Only allow one profile
        if Profile.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year_range', 'grade', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('degree', 'institution')
    ordering = ('order',)


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview', 'skill_count', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    inlines = [SkillInline]
    ordering = ('order',)

    def icon_preview(self, obj):
        return format_html('<i class="{}"></i> {}', obj.icon_class, obj.icon_class)
    icon_preview.short_description = 'Icon'

    def skill_count(self, obj):
        return obj.skills.filter(is_active=True).count()
    skill_count.short_description = 'Active Skills'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency_bar', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name',)
    ordering = ('category', 'order')

    def proficiency_bar(self, obj):
        return format_html(
            '<div style="width:100px;background:#ddd;border-radius:5px;">'
            '<div style="width:{}px;background:#6c5ce7;height:20px;border-radius:5px;text-align:center;color:white;font-size:12px;">{}</div>'
            '</div>',
            obj.proficiency, f'{obj.proficiency}%'
        )
    proficiency_bar.short_description = 'Proficiency'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'github_link', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    inlines = [ProjectTagInline]
    ordering = ('order',)

    fieldsets = (
        ('Project Details', {
            'fields': ('title', 'emoji', 'description', 'image')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:50px;max-width:80px;border-radius:5px;"/>', obj.image.url)
        return "No image"
    image_preview.short_description = 'Preview'

    def github_link(self, obj):
        if obj.github_url:
            return format_html('<a href="{}" target="_blank">GitHub</a>', obj.github_url)
        return "-"
    github_link.short_description = 'GitHub'


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'icon_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    ordering = ('order',)

    def icon_preview(self, obj):
        return format_html('<i class="{}"></i>', obj.icon_class)
    icon_preview.short_description = 'Icon'


@admin.register(CertificateCategory)
class CertificateCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'certificate_count', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    inlines = [CertificateInline]
    ordering = ('order',)

    def certificate_count(self, obj):
        return obj.certificates.filter(is_active=True).count()
    certificate_count.short_description = 'Certificates'


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'category', 'has_file', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'issuer')
    ordering = ('order',)

    def has_file(self, obj):
        if obj.certificate_file:
            return format_html('<span style="color:green;">✓</span>')
        elif obj.certificate_url:
            return format_html('<span style="color:blue;">URL</span>')
        return format_html('<span style="color:red;">✗</span>')
    has_file.short_description = 'File'


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'subtitle', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
    ordering = ('order',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:60px;max-width:60px;border-radius:50%;object-fit:cover;"/>', obj.image.url)
        return "No image"
    image_preview.short_description = 'Preview'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_editable = ('is_read',)
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    fieldsets = (
        ('Sender Information', {
            'fields': ('name', 'email')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )


@admin.register(TypingText)
class TypingTextAdmin(admin.ModelAdmin):
    list_display = ('text', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)
