from django import forms
from django import forms
from django.contrib.auth.models import AbstractUser
from .models import Profile  
from django.contrib.auth.models import AbstractUser
from .models import CustomUser



class UserCreateForm(forms.ModelForm):
    email = forms.EmailField(required=True)  

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "password")

    def save(self, commit=True):
        user = super().save(commit=False) 
        user.set_password(self.cleaned_data["password"])  
        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)








class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username',"last_name", 'email',"first_name","profile_pictures"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username',"last_name", 'email',"first_name","profile_pictures"]