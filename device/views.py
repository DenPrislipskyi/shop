from django.shortcuts import render, get_object_or_404
from django.views import generic

from device.models import Device, Category


class DeviceListView(generic.ListView):
    model = Device
    template_name = "shop/device_list.html"


def get_category_list():          # TODO тег 16 відео seldefu також мейт
    return Category.objects.all()


class DeviceCategoryView(generic.ListView):
    model = Device
    template_name = "shop/category_detail.html"
    context_object_name = "devices"

    def get_queryset(self):
        category_id = self.kwargs["pk"]
        return Device.objects.filter(category_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(pk=self.kwargs["pk"])
        return context

# def categorydetail(request, category_id):
#     # Отримати об'єкт категорії за ідентифікатором
#     category = get_object_or_404(Category, id=category_id)
#     # Отримати всі товари, пов'язані з цією категорією
#     devices_in_category = Device.objects.filter(category=category)
#
#     return render(request, 'shop/category_detail.html', {'category': category, 'devices': devices_in_category})


# def show_category(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     devices_in_category = Device.objects.filter(category=category)
#     data = {
#         'devices': devices_in_category,
#         'category': category,
#     }
#     return render(request, 'shop/category_detail.html', context=data)
