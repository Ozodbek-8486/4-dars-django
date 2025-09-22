from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreateForm, UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages



def landing_page(request):
    return render(request, "landing_page.html")


class RegisterView(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, "users/register.html", {"form": form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
        return render(request, "users/register.html", {"form": form})

class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm()
        return render(request, "users/login.html", {"login_form": login_form})
    
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("users:landing")
        else:
            return render(request, "users/login.html", {"login_form": login_form})
        
class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,"users/profile.html", {"users:request":"user"})
    




class Logoutview(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.info(request,"Tizimdan chiqildi!")
        return redirect ("landing_page")