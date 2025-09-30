from django import forms
from django.contrib.auth.models import User


class UserCreateForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Emailingizni kiriting"
        })
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Username"
                
            }),
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ism"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Familiya"
            }),
            "password": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Parol"
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Username"
        })
    )
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Parol"
        })
    )














from django import forms
from django.contrib.auth.models import User
from .models import Profile  # Profil modeli ham kerak bo'ladi

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar',"first_name", "last_name",]