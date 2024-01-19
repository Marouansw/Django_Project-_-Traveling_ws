from django.urls import path
from . import views

urlpatterns = [
    path('index.html/', views.home, name='home'),
    path('about.html/', views.about, name='about'),
    path('service.html/', views.service, name='service'),
    path('destination.html/', views.destination, name='destination'),
    path('package.html/', views.package, name='package'),
    path('contact.html/', views.contact, name='contact'),
    path('Flight_result/', views.flight, name='flight'),
    path('checkout_package/<str:cntr>/', views.checkout_package, name='checkout_package'),
    path('checkout_flight/<str:fid>/', views.checkout_flight, name='checkout_flight'),

    # path('register.html/', views.register, name='contact'),
]