from django.urls import path

from cart.views import CartListView, AddToCartView, CartDeleteView

urlpatterns = [
    path("", CartListView.as_view(), name="cart-list"),
    path("add-to-cart/", AddToCartView.as_view(), name='add-to-cart'),
    path("delete-from-cart/<int:pk>/", CartDeleteView.as_view(), name='delete-from-cart'),

]


app_name = "cart"
