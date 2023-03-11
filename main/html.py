from django import template


register = template.Library()

@register.filter
def truncate(text: str, length: int):
    """
    A function for truncating the parts of the given text after the given length.
    """

    return text[:length] if len(text) <= length else f'{text[:length]}...'


@register.simple_tag
def replacechars(text: str, _from: str, _to: str):
    """
    A function for replacing the _from character from a text into the _to character.
    """

    return text.replace(_from, _to)