from django.contrib import admin

# Register your models here.
# 1ero Importando de el archivo models.py  las 2 clases
from .models import Categoria,Producto

# 2do Regisrando las clases
# admin.site.register(Categoria)
# admin.site.register(Producto)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha_registro')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','categoria','fecha_registro')
    list_editable = ('precio',)

