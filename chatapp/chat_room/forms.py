from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import PasswordInput

class RegisterForm(UserCreationForm):

    usable_password = None

    class Meta:
        model = get_user_model()
        fields = ["username", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(widget=PasswordInput())