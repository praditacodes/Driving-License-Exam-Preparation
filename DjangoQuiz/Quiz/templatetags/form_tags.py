# quiz/templatetags/form_tags.py
from django import template

register = template.Library()

@register.simple_tag
def my_custom_tag():
    return "Custom tag content"
