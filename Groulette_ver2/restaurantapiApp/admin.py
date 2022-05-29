from django.contrib import admin

# Register your models here.
from .models import Restaurant

admin.site.register(Restaurant)
# class RestaurantAdmin(admin.ModelAdmin):
#     pass