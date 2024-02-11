from django import template

from device.models import Category
from device.views import get_category_list

register = template.Library()


@register.simple_tag
def get_category():
    return get_category_list()

# @register.inclusion_tag("shop/categories.html")
# def show_categories(cat_selected=0):
#     cats = Category.objects.all()
#     return {"cats": cats, "cat_selected": cat_selected}
