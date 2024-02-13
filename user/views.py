from django.urls import reverse_lazy
from django.views import generic

from user.forms import UsersCreationForm
from user.models import User


class UserCreateView(generic.CreateView):
    model = User
    form_class = UsersCreationForm
    success_url = reverse_lazy("device:device-list")
    template_name = "shop/user_form.html"


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UsersCreationForm
    success_url = reverse_lazy("device:device-list")
    template_name = "shop/user_form.html"
