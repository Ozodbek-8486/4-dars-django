from django.urls import path
from .views import LoginView, RegisterView, LogoutView , AboutWiev , landing_page 

app_name = 'users'

urlpatterns = [
   
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('about/',AboutWiev.as_view(), name='about' ),
    path('landing/',landing_page, name='landing_page'),








path('logout/', LogoutView.as_view(), name='logout'),

]
