from django.shortcuts import redirect, render ,get_object_or_404
from .models import Libro
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
# Create your views here.

# Listado de libros

def lista_libros(request):

    query = request.GET.get('q', '')
    if query:
        libros = Libro.objects.filter(
            Q(titulo__icontains=query) |
            Q(Autor__icontains=query) |
            Q(editorial__icontains=query) |
            Q(fecha_publicacion__icontains=query) |
            Q(estado__icontains=query)
        ).order_by('Autor', 'titulo', 'editorial', 'fecha_publicacion', 'estado')
    else:
        libros = Libro.objects.all().order_by('Autor', 'titulo', 'editorial', 'fecha_publicacion', 'estado')
    
    paginator = Paginator(libros, 5)  #
    page_number = request.GET.get('page')
    libros = paginator.get_page(page_number)

    return render(request, 'lista_libros.html', {'libros': libros, 'query': query})

# Detalle libro

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)

    q = request.GET.get('q', '')
    page = request.GET.get('page', '')

    return render(request, 'detalle_libro.html', {
        'libro': libro,
        'q': q,
        'page': page
    })

def agregar_libro(request):
    if request.method == 'POST':
        Autor = request.POST.get('Autor')
        titulo = request.POST.get('titulo') 
        editorial = request.POST.get('editorial')
        fecha_publicacion = request.POST.get('fecha_publicacion')
        estado = request.POST.get('estado')

        if not Autor or not titulo or not editorial or not fecha_publicacion or not estado:
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'agregar_libro.html')
        
        libro = Libro(
            Autor=Autor,
            titulo=titulo,
            editorial=editorial,
            fecha_publicacion=fecha_publicacion,
            estado=estado
        )
        libro.save()
        messages.success(request, 'Libro agregado exitosamente.')
        return redirect('lista_libros')
    return render(request, 'agregar_libro.html')

def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.Autor = request.POST.get('Autor', libro.Autor)
        libro.titulo = request.POST.get('titulo', libro.titulo)
        libro.editorial = request.POST.get('editorial', libro.editorial)
        libro.fecha_publicacion = request.POST.get('fecha_publicacion', libro.fecha_publicacion)
        libro.estado = request.POST.get('estado', libro.estado)

        if not libro.Autor or not libro.titulo or not libro.editorial or not libro.fecha_publicacion or not libro.estado:
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'editar_libro.html', {'libro': libro})
        
        libro.save()
        messages.success(request, 'Libro editado exitosamente.')
        return redirect('lista_libros')

    return render(request, 'editar_libro.html', {'libro': libro})
