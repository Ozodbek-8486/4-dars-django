from django.urls import path , include
from .views import BooksView,BookDetailView 

app_name = 'books'


urlpatterns = [
    path('list/', BooksView.as_view(), name='book_list'),
    path("/<int:id>/",BookDetailView.as_view(),name="book_detail"),


]