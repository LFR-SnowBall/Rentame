"""Rentame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from incio import views
from DB import views as views_DB

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Carga, name="Carga"),
    path('Inicio',views_DB.Inicio, name="Inicio"),
    path('Muestrario',views_DB.Muestrario, name='Muestrario'),
    path('MuestrarioR',views_DB.MuestrarioR, name='MuestrarioR'),
    path('MuestrarioV',views_DB.MuestrarioV, name='MuestrarioV'),
    path('Informacion/<int:idP>',views_DB.Informacion, name='Informacion'),
    path('InformacionH/<int:idH>',views_DB.InformacionH,name='InformacionH'),
    path('ejemplo',views.ejemplo, name="ejemplo"),
]
if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)