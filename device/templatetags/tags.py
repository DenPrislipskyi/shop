from django import template
from device.views import get_category_list

register = template.Library()


@register.simple_tag
def get_category():
    return get_category_list()

