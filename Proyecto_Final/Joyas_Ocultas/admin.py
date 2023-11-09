from django.contrib import admin

# Register your models here.
from .models import Usuarios, Categorias,Articulos, Verificaciones, Mensajes, Valoraciones, Carrito, Detalles_Carrito, Pagos

admin.site.register(Usuarios)
admin.site.register(Categorias)
admin.site.register(Articulos)
admin.site.register(Verificaciones)
admin.site.register(Mensajes)
admin.site.register(Valoraciones)
admin.site.register(Carrito)
admin.site.register(Detalles_Carrito)
admin.site.register(Pagos)