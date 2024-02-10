from django.contrib import admin

from device.models import Device, Category, Tag

admin.site.register(Device)
admin.site.register(Category)
admin.site.register(Tag)
