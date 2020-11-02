from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def monitoring(request):
    return render(request, 'main/monitoring.html')


def administrator(request):
    return render(request, 'main/administrator.html')
