from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class MyPetsLoginForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=24)
    password = forms.CharField(min_length=8, max_length=99)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password



class MyPetsRegisterForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=24)
    email = forms.EmailField()
    password1 = forms.CharField(min_length=8, max_length=99)
    password2 = forms.CharField(min_length=8, max_length=99)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password2')
        )
        return user