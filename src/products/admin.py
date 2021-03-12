from django.contrib import admin

# Register your models here.
from .models import Product, Employee, Anime
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Anime)
