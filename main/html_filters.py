from django import template


register = template.Library()

@register.filter
def truncate(text, length):
    """
    A function for truncating the parts of the given text after the given length.
    """

    return text[:length] if len(text) <= length else f'{text[:length]}...'
