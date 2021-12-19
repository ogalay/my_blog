from django.contrib.auth.forms import UserCreationForm
from .models import models
from django.contrib.auth.models import User


class register_form(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]



