from django import template

from re import findall

register = template.Library()


@register.filter(name='function_short_url')
def function_short_url(url):
    regex = r"^(?:https?://)?(?:www\.)?([^:/?\n]+)"
    match = findall(regex, url)
    return "".join(match[0])
