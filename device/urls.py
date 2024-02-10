from django.urls import path

from device.views import DeviceListView

urlpatterns = [
    path("", DeviceListView.as_view(), name="device-list"),
    # path("category/", CategoryListView.as_view(), name="category-list"),
]


app_name = "device"
