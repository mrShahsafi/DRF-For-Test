from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as UA

from .forms import *
from .models import *


class UserAdmin(UA):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['email', 'username']


admin.site.register(User, UserAdmin)
