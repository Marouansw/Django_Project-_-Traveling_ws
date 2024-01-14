from django.urls import path

from travel_agency import settings
from . import views

urlpatterns =[
    path('dashboard/', views.dashboard, name='dash'),
    path('profil/', views.profil, name='dash'),




]