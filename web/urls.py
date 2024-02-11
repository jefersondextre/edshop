from django.urls import path
from . import views
# Dentro de la carpeta web importamos todas las vistas de nuestra app web.

app_name = 'web'
# app_name Para ubicar los enlaces e identificar en que aplicacion esta en la 
# vista que referenciará

# urlpatterns = [
#    path('admin/', admin.site.urls),
# ]
# Establesclo la Url de la aplicacion. Todavia tengo que agregarlos a mi urls 
# principal
urlpatterns = [
    path('', views.index, name='index'),
    path('productosPorCategoria/<int:categoria_id>',
         views.productosPorCategoria,
         name='productosPorCategoria'),
    path('productosPorNombre',views.productosPorNombre,name="productosPorNombre"),
    path('producto/<int:producto_id>',views.productoDetalle,name="producto")
]
# path()
# ''  ruta principal
# views.index   el archivo que ejecutareos
# name='index'   para el alias de la urls