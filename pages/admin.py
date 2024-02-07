from django.contrib import admin
from .models import Flight, Package,Notification
admin.site.register(Package)
admin.site.register(Flight)
admin.site.register(Notification)
# Register your models here.
