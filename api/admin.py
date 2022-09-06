from django.contrib import admin

# Register your models here.

from .models import Reservation,Pricelist

admin.site.register(Reservation)
admin.site.register(Pricelist)