from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.decorators.http import require_POST
from django.views.generic import View
from django.urls import reverse_lazy

from cart.models import Cart
from device.models import Device


class CartListView(generic.ListView):
    model = Cart
    template_name = "shop/cart_list.html"
    context_object_name = "cart_list"

    def get_queryset(self):
        user = self.request.user
        # Перевірка, чи існує корзина для поточного користувача
        if hasattr(user, "cart"):
            return user.cart.devices.all()
        return Device.objects.none()


class AddToCartView(View):
    def post(self, request):
        device_id = request.POST.get("device_id")
        if device_id:
            device = Device.objects.get(pk=device_id)
            # Отримання або створення корзини для поточного користувача
            cart, created = Cart.objects.get_or_create(user=request.user)
            # Додавання товару до корзини
            cart.devices.add(device)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CartDeleteView(View):
    def post(self, request, pk):
        cart = get_object_or_404(Cart, user=request.user)
        device = get_object_or_404(Device, pk=pk)
        cart.devices.remove(device)
        return redirect("cart:cart-list")
