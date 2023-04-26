from django import template


register = template.Library()


# Filters go here
@register.filter
def truncate(text: str, length: int):
    """
    A function for truncating the parts of the given text after the given length.
    """

    return text[:length] if len(text) <= length else f'{text[:length]}...'


@register.filter
def translate_dc(string: str, language_code: str):
    """
    A filter that retrieves the appropriate translation of dynamic content from the given string.

    The given string should have all the translations that are needed else the English version of a translation
    is going to be returned.
    """

    translations = string.split('|||')
    for translation in translations:
        if translation.lstrip().startswith('--' + language_code):
            return translation.replace('--' + language_code, '').strip()
    
    return translations[0].replace('--' + language_code).strip()


# Tags go here
@register.simple_tag
def replacechars(text: str, _from: str, _to: str):
    """
    A function for replacing the _from character from a text into the _to character.
    """

    return text.replace(_from, _to)
