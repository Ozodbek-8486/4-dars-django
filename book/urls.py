from django.urls import path
from .views import BooksView,BookDetailView

app_name = "books"


urlpatterns = [
    path('list/', BooksView.as_view(), name='list'),
    path("<int:id>/",BookDetailView.as_view(),name="detail"),
]