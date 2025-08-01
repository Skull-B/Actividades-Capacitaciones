from django.contrib import admin
from .models import Libro
# Register your models here.

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('Autor', 'titulo', 'editorial', 'fecha_publicacion', 'estado')
    search_fields = ('titulo', 'Autor')
    list_filter = ('estado', 'fecha_publicacion')


