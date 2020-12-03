from django.contrib import admin

# Register your models here.
from . models import Instrumento, Producto

admin.site.register(Instrumento)
admin.site.register(Producto)