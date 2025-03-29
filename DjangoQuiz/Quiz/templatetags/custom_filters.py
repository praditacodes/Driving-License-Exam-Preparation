from django import template

register = template.Library()

@register.filter
def input_class(value):
    # Define your filter logic here, e.g., add a CSS class to the value
    return f'{value} custom-class'  # Example logic
