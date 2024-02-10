from django.shortcuts import render
from django.views import generic

from device.models import Device, Category


class DeviceListView(generic.ListView):
    model = Device
    template_name = "shop/device_list.html"


def get_category_list():          # TODO тег 16 відео seldefu також мейт
    return Category.objects.all()

