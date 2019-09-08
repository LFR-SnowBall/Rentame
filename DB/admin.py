from django.contrib import admin
from .models import Propiedad,VentaRenta,Inmobiliaria,Hotel,Contacto



class LinesHotel(admin.StackedInline):
    model=Hotel
    extra=0
class LinesPr(admin.StackedInline):
    model=Propiedad
    extra=0

class AdminVentaRenta(admin.ModelAdmin):
    list_display=('Categoria','FechaP','FechaM')
    list_filter='Categoria','FechaP'
    search_fields=('Categoria','Categoria')
    date_hierarchy = 'FechaP'
    readonly_fields = ('FechaP','FechaM')
    inlines=[LinesHotel,LinesPr]

class AdminInmobiliaria(admin.ModelAdmin):
    list_display=('idI','Nombre','Correo','Telefono','Logo')
    search_fields=('Nombre','Correo')
    inlines=[LinesPr]

class AdminPropiedad(admin.ModelAdmin):
    list_display=('idP','idI','idVR','Tipo','Titulo','FotoUno')
    list_filter='Tipo','Estado','Ciudad','Calle','Colonia','idVR'
    search_fields=('Titulo','Estado','Ciudad','Calle','Colonia')

class AdminHotel(admin.ModelAdmin):
    list_display=('idH','idVR','Nombre','Categoria','Correo','FotoUno')
    list_filter='Categoria','Estado','Ciudad','Colonia','Calle'
    search_fields=('Nombre','Estado','Ciudad','Colonia','Calle',)
    
class Comentario(admin.ModelAdmin):
    list_display=('idP','idH','Persona','Comentario')

admin.site.register(Contacto,Comentario)    
admin.site.register(Inmobiliaria,AdminInmobiliaria)
admin.site.register(Propiedad,AdminPropiedad)
admin.site.register(Hotel,AdminHotel)
admin.site.register(VentaRenta,AdminVentaRenta)
# Register your models here.
