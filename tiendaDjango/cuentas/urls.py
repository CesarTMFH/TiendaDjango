from django.urls import path , include
from .views import *
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', home, name='home'),
    path('Productos/', productos, name='productos'), 
    path('salir/', salir, name='salir'),
    path('registro/', registro, name='registro'), 
    path('borrar/<int:id>', borrar, name='borrar'),
    path('editar/<int:id>', editar, name='editar'),
    path('mostrar-productos/', mostrar_productos, name='mostrar_productos'),
    path('catalogo/', catalogo, name='catalogo'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
