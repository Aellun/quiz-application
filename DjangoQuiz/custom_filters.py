from django import template

register = template.Library()

@register.simple_tag
def static_img_url(path):
    return '{{% static "%s" %}}'.replace('"', '') % path
