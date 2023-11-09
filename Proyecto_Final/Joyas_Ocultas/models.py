from django.db import models


class Usuarios(models.Model):
    ID_Usuario = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=50)
    Tipo = models.CharField(max_length=50)
    Fecha_Registro = models.DateField()
    Fecha_Actualización = models.DateField()

    def __str__(self):
        return self.Nombre
    

class Categorias(models.Model):
    ID_Categoria = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre
    
class Articulos(models.Model):
    ID_Articulo = models.AutoField(primary_key=True)
    ID_Categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    ID_Vendedor = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
    Precio = models.IntegerField()
    Fecha_Publicacion = models.DateField()
    Imagen = models.ImageField()
    Estado = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre
    

class Verificaciones(models.Model):
    ID_Verificacion = models.AutoField(primary_key=True)
    ID_Articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    Estado = models.CharField(max_length=50)

    def __str__(self):
        return self.Estado  
    

class Mensajes(models.Model):
    ID_Mensaje = models.AutoField(primary_key=True)
    ID_Usuario_Emisor = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    ID_Usuario_Receptor = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Contenido = models.CharField(max_length=50)

    def __str__(self):
        return self.Contenido
    

class Valoraciones (models.Model):
    ID_Valoracion = models.AutoField(primary_key=True)
    ID_Usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    ID_Articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    Puntuacion = models.IntegerField()
    Comentario = models.CharField(max_length=200)
    Fecha_Valoracion = models.DateField("Fecha de Valoracion")
    def __str__(self):
        return self.ID_Valoracion


class Carrito (models.Model):   
    ID_Carrito = models.AutoField(primary_key=True)
    ID_Usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    ID_Articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ID_Carrito
    

class Detalles_Carrito (models.Model):
    ID_Detalle_Carrito = models.AutoField(primary_key=True)
    ID_Carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    ID_Articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    Precio = models.IntegerField()
    Subtotal = models.IntegerField()
    
    def __str__(self):
        return self.ID_Detalle_Carrito

class Pagos (models.Model):
    ID_Pago = models.AutoField(primary_key=True)
    ID_Usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    ID_Carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    Monto = models.IntegerField()
    Metodo_Pago = models.CharField(max_length=50)
    Estado = models.CharField(max_length=50)
    Fecha_Pago = models.DateField("Fecha de Pago")
    
    def __str__(self):
        return self.ID_Pago

