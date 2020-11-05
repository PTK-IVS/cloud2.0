from django.shortcuts import render, redirect

from .forms import MessageETHContactIDForm
from .models import (
    MessageETHContactID
)


def index(request):
    messages = MessageETHContactID.objects.order_by('id')
    context = {
        'title': 'Главная страница сайта',
        'messages': messages
    }
    return render(
        request, 'main/index.html',
        context
    )


def monitoring(request):
    return render(
        request,
        'main/monitoring.html'
    )


def administrator(request):
    error: str = ''
    if request.method == "POST":
        form = MessageETHContactIDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Form isn't correct"
    form = MessageETHContactIDForm()
    context = {
        'form': form,
        'title': 'Страница администратора',
        'error': error
    }
    return render(
        request,
        'main/administrator.html',
        context
    )
