from django.forms import ModelForm, forms
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

from users.models import CustomUserModel, Url


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'phone')


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['original_link']