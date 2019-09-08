from django.shortcuts import render, redirect,get_object_or_404
from .models import Propiedad,Hotel,VentaRenta,Contacto
from django.urls import reverse
from .forms import ContactoForm

def Inicio(request):
    Propiedades=Propiedad.objects.all()
    return render(request,"db/Inicio.html",{'Propiedad':Propiedades})

def Muestrario(request):
    Propiedades=Propiedad.objects.all() #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    Hoteles=Hotel.objects.all()
    VentasRentas=VentaRenta.objects.all()
    #print("Tipo de petición:{}".format(request.method))
    return render(request, "db/Muestrario.html",{'Propiedad':Propiedades,'Hotel':Hoteles})

def MuestrarioR(request):
    Propiedades=Propiedad.objects.all() #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    Hoteles=Hotel.objects.all()
    VentasRentas=VentaRenta.objects.all()
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados    
    return render(request, "db/MuestrarioR.html",{'Propiedad':Propiedades,'Hotel':Hoteles})

def MuestrarioV(request):
    Propiedades=Propiedad.objects.all() #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    Hoteles=Hotel.objects.all()
    VentasRentas=VentaRenta.objects.all()
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados    
    return render(request, "db/MuestrarioV.html",{'Propiedad':Propiedades,'Hotel':Hoteles})

def Informacion(request,idP):
    clave=get_object_or_404(Propiedad,idP=idP)

    register_form=ContactoForm()
    if(request.method=="POST"):
        register_form=ContactoForm(data=request.POST)
        #Se verifica si los elementos del formulario cumplen con las 
        # carácterísticas descritas para los campos en el form
        if register_form.is_valid():
                try:
                         #Se recuperan los valores del formulario
                        claves=get_object_or_404(Propiedad,idP=idP)
                        persona=request.POST.get("persona",'')
                        comentario=request.POST.get("comentario",'')
                        #Se crea una instancia comentario que construira el nuevo registro
                        nuevoComentario=Contacto()
                        #Se busca el alumno al que pertenece la clave recuperada del
                        # formulario y se asigna como valor para la llave foránea alumno en
                        # el nuevo comentario
                        nuevoComentario.idP=claves
                        nuevoComentario.Persona=persona
                        #Se asigna como valor del comentario el valor recuperado del
                        # formulario
                        nuevoComentario.Comentario=comentario
                        #Se almacena el nuevo comentrio en la tabla de la base de datos
                        nuevoComentario.save()
                        #Si tido es correcto se redirecciona a la página de
                        # comentario y se indica que todo es correcto
                        #Contacto es el nombre de la url
                        return render(request,"db/Informacion.html",{'clave':clave,'form':register_form} )
                except:
                        #Si ocurre algun problema se redirecciona a la página de
                        # comentario y se indica que algo salio mal
                        return ('error')
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados    
    return render(request,"db/Informacion.html",{'clave':clave,'form':register_form} )

def InformacionH(request,idH):
        clave=get_object_or_404(Hotel,idH=idH)

        register_form=ContactoForm()
        if(request.method=="POST"):
                register_form=ContactoForm(data=request.POST)
                #Se verifica si los elementos del formulario cumplen con las 
                # carácterísticas descritas para los campos en el form
                if register_form.is_valid():
                        try:
                                #Se recuperan los valores del formulario
                                claves=get_object_or_404(Hotel,idH=idH)
                                persona=request.POST.get("persona",'')
                                comentario=request.POST.get("comentario",'')
                                #Se crea una instancia comentario que construira el nuevo registro
                                nuevoComentario=Contacto()
                                #Se busca el alumno al que pertenece la clave recuperada del
                                # formulario y se asigna como valor para la llave foránea alumno en
                                # el nuevo comentario
                                nuevoComentario.idH=claves
                                nuevoComentario.Persona=persona
                                #Se asigna como valor del comentario el valor recuperado del
                                # formulario
                                nuevoComentario.Comentario=comentario
                                #Se almacena el nuevo comentrio en la tabla de la base de datos
                                nuevoComentario.save()
                                #Si tido es correcto se redirecciona a la página de
                                # comentario y se indica que todo es correcto
                                #Contacto es el nombre de la url
                                return render(request,"db/Informacion.html",{'clave':clave,'form':register_form} )
                        except:
                                #Si ocurre algun problema se redirecciona a la página de
                                # comentario y se indica que algo salio mal
                                return ('error')
        #Indicamos el lugar donde se renderizará el resultado de esta vista
        # y enviamos la lista de alumnos recuparados    
        return render(request,"db/Informacion.html",{'clave':clave,'form':register_form} )