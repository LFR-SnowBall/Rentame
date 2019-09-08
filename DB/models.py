from django.db import models

class Inmobiliaria(models.Model):
    idI=models.AutoField(primary_key=True,verbose_name="Clave")
    Nombre=models.CharField(max_length=50,verbose_name="Nombre")
    Correo=models.CharField(max_length=50,verbose_name="Correo")
    Telefono=models.CharField(max_length=11,verbose_name="Telefono")
    Servicios=models.TextField(verbose_name="Servicios")
    Informacion=models.TextField(verbose_name="Información")
    Logo=models.ImageField(null=True,upload_to="fotos",verbose_name="Logo")

    class Meta:
        verbose_name="Inmobiliaria"
        verbose_name_plural="Inmobiliarias"
        ordering=["-Nombre"]

    def __str__(self):
        return self.Nombre

class VentaRenta(models.Model):
    idVR=models.AutoField(primary_key=True,verbose_name="Clave Venta Renta")
    Categoria=models.CharField(max_length=7,verbose_name="Categoria")
    Precio=models.IntegerField(verbose_name="Precio")
    FechaP=models.DateField(auto_now_add=True,verbose_name="Fecha Publicación")
    FechaM=models.DateField(auto_now_add=True,verbose_name="Fecha Actualización")
    
    class Meta:
        verbose_name="Venta Renta"
        verbose_name_plural="Ventas Rentas"
        ordering=["-FechaP"]

    def __str__(self):
        return self.Categoria

class Hotel(models.Model):
    idH=models.AutoField(primary_key=True,verbose_name="Clave Hotel")
    idVR=models.ForeignKey(VentaRenta,on_delete=models.CASCADE,verbose_name="Clave Venta Renta")
    Categoria=models.CharField(max_length=15,verbose_name="Categoria")
    Nombre=models.CharField(max_length=50,verbose_name="Nombre")
    NoHabitacion=models.CharField(max_length=5,verbose_name="Numero de Habitación")
    NoCuartos=models.CharField(max_length=5,verbose_name="Numero de Cuartos")
    Telefono=models.CharField(max_length=11,verbose_name="Telefono")
    Correo=models.CharField(max_length=50,verbose_name="Correo")
    Banios=models.CharField(max_length=3,verbose_name="Baños")
    Estado=models.CharField(max_length=20,verbose_name="Estado")
    Ciudad=models.CharField(max_length=40,verbose_name="Ciudad")
    Calle=models.CharField(max_length=60,verbose_name="Calle")
    Colonia=models.CharField(max_length=60,verbose_name="Colonia")
    No=models.CharField(max_length=5,verbose_name="Numero")
    Descripcion=models.TextField(verbose_name="Descripción")
    FotoUno=models.ImageField(null=True,upload_to="fotos",verbose_name="Imagen")
    FotoDos=models.ImageField(null=True,upload_to="fotos",verbose_name="Imagen")
    FotoTres=models.ImageField(null=True,upload_to="fotos",verbose_name="Imagen")
    FotoCuatro=models.ImageField(null=True,upload_to="fotos",verbose_name="Imagen")

    class Meta:
        verbose_name="Hotel"
        verbose_name_plural="Hoteles"
        ordering=["-Nombre"]

    def __str__(self):
        return self.Nombre

class Propiedad(models.Model):
    idP=models.AutoField(primary_key=True,verbose_name="Clave Propiedad")
    idI=models.ForeignKey(Inmobiliaria,on_delete=models.CASCADE,verbose_name="Clave Inmobiliaria")
    idVR=models.ForeignKey(VentaRenta,on_delete=models.CASCADE,verbose_name="Clave Venta Renta")
    Tipo=models.CharField(max_length=15,verbose_name="Tipo")
    Titulo=models.CharField(max_length=100,verbose_name="Titulo")
    NoCuartos=models.CharField(max_length=5,verbose_name="Numero de Cuartos")
    Telefono=models.CharField(max_length=11,verbose_name="Telefono")
    Correo=models.CharField(max_length=50,verbose_name="Correo")
    Banios=models.CharField(max_length=3,verbose_name="Baños")
    Estado=models.CharField(max_length=20,verbose_name="Estado")
    Ciudad=models.CharField(max_length=40,verbose_name="Ciudad")
    Calle=models.CharField(max_length=60,verbose_name="Calle")
    Colonia=models.CharField(max_length=60,verbose_name="Colonia")
    No=models.CharField(max_length=5,verbose_name="Numero")
    Descripcion=models.TextField(verbose_name="Descripción")
    FotoUno=models.ImageField(null=True,upload_to="fotos",verbose_name="Imagen")
    FotoDos=models.ImageField(null=True,upload_to="fotos",verbose_name="Imagen")
    FotoTres=models.ImageField(null=True,upload_to="fotos",verbose_name="Imagen")
    FotoCuatro=models.ImageField(null=True,upload_to="fotos",verbose_name="Imagen")

    class Meta:
        verbose_name="Propiedad"
        verbose_name_plural="Propiedades"
        ordering=["-Titulo"]

    def __str__(self):
        return self.Titulo

class Contacto(models.Model):
    idP=models.ForeignKey(Propiedad,on_delete=models.CASCADE,blank=True,null=True,verbose_name="Clave Propiedad")
    idH=models.ForeignKey(Hotel,on_delete=models.CASCADE,blank=True,null=True,verbose_name="Clave Hotel")
    Persona=models.CharField(max_length=50,verbose_name="Correo")
    Comentario=models.TextField(verbose_name="Comentario")

    class Meta:
        verbose_name="Comentario"
        verbose_name_plural="Comentarios"
        ordering=["-Comentario"]

    def __str__(self):
        return self.Persona
# Create your models here.
