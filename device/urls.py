from django.urls import path

from device.views import DeviceListView, DeviceCategoryView

urlpatterns = [
    path("", DeviceListView.as_view(), name="device-list"),
    path("category/<int:pk>/", DeviceCategoryView.as_view(), name="device-category"),
]


app_name = "device"
