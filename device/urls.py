from django.urls import path

from device.views import DeviceListView, DeviceCategoryView, DeviceDetailView, DeviceCreateView, DeviceUpdateView, DeviceDeleteView, Index

urlpatterns = [
    path("", DeviceListView.as_view(), name="device-list"),
    path("category/<int:pk>/", DeviceCategoryView.as_view(), name="device-category"),
    path("<int:pk>/", DeviceDetailView.as_view(), name="device-detail"),
    path("create/", DeviceCreateView.as_view(), name="device-create"),
    path("update/<int:pk>/", DeviceUpdateView.as_view(), name="device-update"),
    path("delete/<int:pk>/", DeviceDeleteView.as_view(), name="device-delete"),
    path("index/", Index.as_view(), name="index"),
]


app_name = "device"
