from django.shortcuts import render, redirect

from .forms import AdemcoCodeForm
from .models import (
    AdemcoCode
)


def index(request):
    codes = AdemcoCode.objects.order_by('id')
    return render(
        request, 'main/index.html',
        {'title': 'Главная страница сайта',
         'codes': codes}
    )


def monitoring(request):
    return render(
        request,
        'main/monitoring.html'
    )


def administrator(request):
    error: str = ''
    if request.method == "POST":
        form = AdemcoCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Form isn't correct"
    form: AdemcoCodeForm = AdemcoCodeForm()
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
