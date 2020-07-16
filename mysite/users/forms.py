from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    First_name = forms.CharField(max_length=80)
    Last_name = forms.CharField(max_length=80)

    class Meta:
        model = User
        fields = ['username', 'email', 'First_name', 'Last_name', 'password1', 'password2']
