from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('monitoring/', views.monitoring, name='monitoring'),
    path('administrator/', views.administrator, name='administrator')
]
