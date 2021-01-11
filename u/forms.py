from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm as UCM
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')


class UserChangeForm(UCM):

    class Meta:
        model = User
        fields = ('username', 'email')


class LoginForm(AuthenticationForm):
    pass
