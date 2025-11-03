from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 
from django.conf import settings
from django.conf.urls.static import static
from .views import landing_page
from . import views
app_name = "config"

urlpatterns = [
    path('', TemplateView.as_view(template_name='landing_page.html'), name='landing'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path("books/", include("book.urls"),name="books"),
    path('offline/', views.offline_page, name='offline'),
    path('heartbeat/', views.heartbeat, name='heartbeat'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)