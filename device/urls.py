from django.urls import path

from device.views import DeviceListView, DeviceCategoryView, DeviceDetailView

urlpatterns = [
    path("", DeviceListView.as_view(), name="device-list"),
    path("category/<int:pk>/", DeviceCategoryView.as_view(), name="device-category"),
    path("device/<int:pk>/", DeviceDetailView.as_view(), name="device-detail"),
]


app_name = "device"
