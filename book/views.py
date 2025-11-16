from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from book.models import Book
from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator
from .models import Book, Comment
from .forms import CommentForm



class BookDetailView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        comments = book.comments.all().order_by('-created_at')
        form = CommentForm()
        return render(request, 'books/detail.html', {
            'book': book,
            'comments': comments,
            'form': form
            
        })

    def post(self, request, id):
        book = get_object_or_404(Book, id=id)
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            if request.user.is_authenticated:
                comment.name = request.user.username

            else:
                comment.name = "Anonim foydalanuvchi"
            comment.save()
            return redirect('books:book_detail', id=book.id)

        comments = book.comments.all().order_by('-created_at')
        return render(request, 'books/detail.html', {
            'book': book,
            'comments': comments,
            'form': form
        })
    
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # ❗ Faqat comment yozgan odam yoki admin o‘chira oladi
    if request.user.is_authenticated and (request.user.username == comment.name or request.user.is_superuser):
        book_id = comment.book.id
        comment.delete()
        messages.success(request, "Izoh o‘chirildi!")
        return redirect('books:book_detail', id=book_id)
    else:
        messages.error(request, "Siz bu izohni o‘chira olmaysiz!")
        return redirect('books:book_detail', id=comment.book.id)

class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by("id")

        search_query = request.GET.get("search")
        if search_query:
            books = books.filter(title__icontains=search_query)

        paginator = Paginator(books, 3) 
        page_num = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_num)

        context = {
            "page_obj": page_obj,
            "search_query": search_query, 
        }

        return render(request, "books/list.html", context)


