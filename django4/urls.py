from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', TemplateView.as_view(template_name='landing_page.html'), name='landing'), 
    path('header/', TemplateView.as_view(), name='header'),
    path("books/",include("book.urls")),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)