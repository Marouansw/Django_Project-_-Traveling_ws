from django.urls import path, re_path
from django.contrib.auth.models import User

from travel_agency import settings
from . import views


urlpatterns =[
    path('dashboard/', views.dashboard, name='dash'),
    path('profil/', views.update_user, name='update'),
    path('password/', views.update_pwd, name='update'),
    path('checkout/', views.checkout, name='check'),
    path('Users/', views.users, name='check'),
    path('delete_user/<str:usk>/', views.delete_user, name='delete_user'),
    path('add_flight/', views.add_flight, name='check'),
    path('add_pack/', views.add_pack, name='pack'),
    path('delete_pack_from_check/<str:id>/', views.delete_pack_from_check, name='pack'),
    path('paiment/', views.paiment, name='paiment'),
    # path('delete_user/', views.users, name='delete'),



]