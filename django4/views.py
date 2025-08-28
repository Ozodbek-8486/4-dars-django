from django.shortcuts import render

def landing_page(request):
    # request.user avtomatik template ga uzatiladi, qo'shimcha shart shart emas
    return render(request, 'landing_page.html')
