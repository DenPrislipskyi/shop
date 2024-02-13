from django.urls import reverse_lazy
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


class DeviceDetailView(generic.DetailView):
    model = Device
    template_name = "shop/device_detail.html"


class DeviceCreateView(generic.CreateView):
    model = Device
    fields = "__all__"
    template_name = "shop/device_form.html"
    success_url = reverse_lazy("device:device-list")


class DeviceUpdateView(generic.UpdateView):
    model = Device
    fields = "__all__"
    template_name = "shop/device_form.html"
    success_url = reverse_lazy("device:device-list")


class DeviceDeleteView(generic.DeleteView):
    model = Device
    success_url = reverse_lazy("device:device-list")
    template_name = "shop/device_confirm_delete.html"


class Index(generic.ListView):
    pass