from django.urls import path, include
from django.views.generic import RedirectView
from catalog import views

urlpatterns = [
    path('', views.index, name = 'index')
]
