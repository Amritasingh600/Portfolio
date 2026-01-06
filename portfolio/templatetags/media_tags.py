from django import template

register = template.Library()


@register.filter
def media_url(value):
    """
    Returns the URL for a media field.
    Handles both FileField objects and direct URL strings (Cloudinary).
    """
    if not value:
        return ''
    
    # Convert to string first
    str_value = str(value)
    
    # If it's already a full URL (Cloudinary), return it directly
    if str_value.startswith('http://') or str_value.startswith('https://'):
        return str_value
    
    # If it has a .url attribute (FileField), use that
    if hasattr(value, 'url'):
        return value.url
    
    # Fallback: return the string (likely a relative path)
    return str_value
