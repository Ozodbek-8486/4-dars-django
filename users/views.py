from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            messages.success(request, "Tizimdam muvvafaqiyatli chiqdingiz")
            return redirect('home')  
        else:
            messages.error(request, "Login yoki parol noto‘g‘ri!")
            return render(request, 'users/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, "users/register.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Bunday foydalanuvchi allaqachon mavjud!")
            return render(request, "users/register.html")

        
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        messages.success(request, "Ro‘yxatdan muvaffaqiyatli o‘tdingiz! Endi login qilishingiz mumkin.")
        return redirect("users:login")


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Tizimga kirish qismidasiz!")
        return redirect("home")  
    






class HomeWiev(View):
    def get(self,request):
        return render(request, 'users/home.html')
    

def landing_page(request):
    return render(request, 'landing_page.html')


class BlogView(View):
    def get(self,request):
        return render(request, 'users/blog.html')
    
def landing_page(request):
    return render(request, 'landing_page.html')


class AboutView(View):
       def get(self,request):
        return render(request, 'users/about.html')
       

def landing_page(request):
    return render(request, 'landing_page.html')



class ContactView(View):
        def get(self,request):
            return render(request, 'users/contact.html')
        
def landing_page(request):
    return render(request, 'landing_page.html')
