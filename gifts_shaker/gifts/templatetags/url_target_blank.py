from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import urlize as urlize_impl

register = template.Library()

#
# @register.filter(is_safe=True, needs_autoescape=True)
# @stringfilter
# def url_target_blank(value, autoescape=None):
#     return mark_safe(urlize_impl(value,  nofollow=True, autoescape=autoescape).replace('<a', '<a target="_blank"'))


@register.filter(name="url_target", is_safe=True)
def url_target_blank(text):
    print(text)
    return text.replace('<a ', '<a target="_blank" ')


register.filter(url_target_blank, is_safe = True)
