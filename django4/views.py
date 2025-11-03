from django.shortcuts import render

def landing_page(request):

    return render(request, 'landing_page.html')



from django.shortcuts import render

def offline_page(request):
    return render(request, 'offline.html')

from django.http import JsonResponse
def heartbeat(request):
    return JsonResponse({'status': 'ok'})