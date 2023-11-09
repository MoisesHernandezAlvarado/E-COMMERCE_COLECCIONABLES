from django.contrib import admin
from django.contrib import Usuarios
from django.contrib import Categorias
from django.contrib import Articulos
from django.contrib import Verificaciones
from django.contrib import Mensajes
from django.contrib import Valoraciones
from django.contrib import Carrito
from django.contrib import Detalles_Carrito
from django.contrib import Pagos

# Register your models here.
from models import Admin, Usuarios, Categorias,Articulos, Verificaciones, Mensajes, Valoraciones, Carrito, Detalles_Carrito, Pagos
admin.site.register(Admin)
admin.site.register(Usuarios)
admin.site.register(Categorias)
admin.site.register(Articulos)
admin.site.register(Verificaciones)
admin.site.register(Mensajes)
admin.site.register(Valoraciones)
admin.site.register(Carrito)
admin.site.register(Detalles_Carrito)
admin.site.register(Pagos)