from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/agregar/', views.agregar_libro, name='agregar_libro'),
    path('libros/<int:pk>/editar/', views.editar_libro, name='editar_libro'),
    path('libros/<int:pk>/', views.detalle_libro, name='detalle_libro'),
]  
