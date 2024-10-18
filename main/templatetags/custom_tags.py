# custom_tags.py
from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def is_active(context, url_name):
    request = context['request']
    current_url = request.path
    url = reverse(url_name)

    return 'active' if current_url == url else ''
