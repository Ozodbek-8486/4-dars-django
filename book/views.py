from django.shortcuts import render
from django.views import View
from book.models import Book
from django.core.paginator import Paginator

# class BooksView(View):
#     def get(self, request):
#         books = Book.objects.all()
#         return render(request, 'books/list.html',{"books": books})
    


class BookDetailView(View):
    template_name = 'books/detail.html'
    pk_url_kwarg = "id"
    model = Book



class BooksView(View):
    def get(self,request):
        books = Book.objects.all().order_by("id")

        search_query = request.GET.get("search")
        if search_query:
            books = books.filter(title__icontains=search_query)

        peginator = Paginator(books, 3)
        page_num = request.GET.get('page',1)
        page_obj = peginator.get_page(page_num)


        context = {
            "page_obj": page_obj,
            "search_query": search_query, 
        }


        return render(request, 'books/list.html', {"page_obj": page_obj})