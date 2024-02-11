from django.shortcuts import render, get_object_or_404
# Create your views here.
""" vistas para catalogo de productos
"""

from  .models import Categoria,Producto

def index(request):
    listaProductos = Producto.objects.all()
    listaCategorias = Categoria.objects.all()
    # print(listaProductos)
    context = {
        'productos': listaProductos,
        'categorias':listaCategorias
    }
    # Enviando un diccionario 'context' cuyo primer valor sera el listado 
    # de todos los productos de la base de datos
    return  render(request, 'index.html',context)



def productosPorCategoria(request,categoria_id):
    """Vista para filtrar productos por categoria   """
    objCategoria = Categoria.objects.get(pk=categoria_id)
    # Esto me traera en el listado de productos, todos los productos que pertenecen a esta Categoria
    listaProductos = objCategoria.producto_set.all()
    listaCategorias = Categoria.objects.all()
    context = {
        'productos': listaProductos,
        'categorias':listaCategorias
    }
    return render(request,'index.html',context)


def productosPorNombre(request):
    """ VISTA PARA FILTRADO DE PRODUCTOS POR NOMBRE """
    nombre = request.POST['nombre']
    # listando todos los productos cuyo nombre sea igual al parametro guardado en el formulario nombre
    listaProductos = Producto.objects.filter(nombre__contains = nombre)
    listaCategorias = Categoria.objects.all()
    
    context = {
        'productos': listaProductos,
        'categorias':listaCategorias
    }
    return render(request, 'index.html', context)



def productoDetalle(request,producto_id):
    """ VISTA PARA EL DETALLE DEL PRODUCTO """
    # objProducto = Producto.objects.get(pk = producto_id)
    objProducto = get_object_or_404(Producto,pk=producto_id)
    context = {
        'producto':objProducto
    }
    return render(request,'producto.html',context)