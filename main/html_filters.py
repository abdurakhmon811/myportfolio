from django import template


register = template.Library()

@register.filter
def truncate_120(text):
    """
    A function for truncating the parts of the given text after 120 characters.
    """

    return f'{text[:120]}...'
