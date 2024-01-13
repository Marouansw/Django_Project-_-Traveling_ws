from django.urls import path

from travel_agency import settings
from . import views

urlpatterns =[
    path('register.html/', views.register_user, name='register'),
    path('login.html/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('logout/', views.logout(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),


]





