from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
'''
una categoria tiene muchos productos

on_delete=models.RESTRICT  Para mantener la Integridad Referencial entre tablas: 
                    Es para cuando alguien intente borrar una categoria, no se lo 
                    permita si tiene productos existentes asignados a dicha categoria
ChartField() tiene una cantidad equivalente a un Varchar con 255 caracteres como maximo para almacenar
TextField(null=True)  Campo que me permite mas de 255 caracteres
DecimalField() campo que me permite decimales
    max_digits=9  máxima cantidad de digitos
    decimal_places=2 numero de decimales
ImageField(upload_to='productos',blank=True) Para colocar una Imagen principal
    blank = True  Para que si deseo no colocaré imagen
    
'''    
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos',blank=True)

    def __str__(self):
        return self.nombre
    