from django.urls import path
from .views import LoginView, RegisterView, LogoutView , HomeWiev , landing_page , BlogView , AboutView , ContactView

app_name = 'users'

urlpatterns = [
   
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/',HomeWiev.as_view(), name='home' ),
    path('blog/',BlogView.as_view(), name='blog' ),
    path('about/',AboutView.as_view(), name='about'),
    path('contact/' ,ContactView.as_view(), name='contact'),




path('landing/',landing_page, name='landing_page'),

path('logout/', LogoutView.as_view(), name='logout'),

]
