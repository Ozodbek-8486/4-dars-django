from django.shortcuts import render

def landing_page(request):

    return render(request, 'landing_page.html')



def header(request):
     return render(request, 'header.html')