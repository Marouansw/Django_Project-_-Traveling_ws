from django.urls import path
from . import views

urlpatterns = [
    path('index.html/', views.home, name='home'),
    path('about.html/', views.about, name='about'),
    path('service.html/', views.service, name='service'),
    path('destination.html/', views.destination, name='destination'),
    path('package.html/', views.package, name='package'),
]