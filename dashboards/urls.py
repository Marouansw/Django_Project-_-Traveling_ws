from django.urls import path, re_path
from django.contrib.auth.models import User

from travel_agency import settings
from . import views


urlpatterns =[
    path('dashboard/', views.dashboard, name='dash'),
    path('profil/', views.update_user, name='update'),
    path('password/', views.update_pwd, name='update'),


]