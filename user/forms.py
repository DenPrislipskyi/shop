from django.contrib.auth.forms import UserCreationForm

from user.models import User


class UsersCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
