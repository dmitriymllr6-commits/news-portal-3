from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import News


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        )


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'summary', 'content']