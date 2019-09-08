from django.shortcuts import render

def Carga(request):
    return render(request,"inicio/Carga.html")

def Inicio(request):
    return render(request,"inicio/Inicio.html")

def Muestrario(request):
    return render(request,"inicio/Muestrario.html")    

def Informacion(request):
    return render(request,"inicio/Informacion.html")

def ejemplo(request):
    return render(request,"inicio/ejemplo.html")

# Create your views here.
