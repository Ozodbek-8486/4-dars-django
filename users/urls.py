from django.urls import path
from .views import LoginView, RegisterView, ProfileView ,landing_page , profile_update
from django.contrib.auth.views import LogoutView
app_name = 'users'

urlpatterns = [
    path("", landing_page, name="landing"),  
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/',ProfileView.as_view(), name='profile' ),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('update/', profile_update, name='profile_update')
]
