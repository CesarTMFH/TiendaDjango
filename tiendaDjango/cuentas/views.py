from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CumstomUserCreationForm , ProductoForm
from django.contrib.auth import authenticate , login
from .models import producto

# Create your views here.
def home (request):
        return render(request, 'aplicacion/home.html', {})

# Login obligatorio para visitar los productos 
@login_required
def productos (request):
        if request.method == 'POST':
                form = ProductoForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                return redirect('mostrar_productos')
        else:
                form = ProductoForm()
                return render(request, 'aplicacion/productos.html', {'form': form})
# Peticion para cerrar secion  
def salir(request):
        logout(request)
        return redirect('home')
#registrar un nuevo usuario
def registro (request):
        data = {
                'form' : CumstomUserCreationForm()
        }
        if request.method == 'POST':
                user_creation_form = CumstomUserCreationForm(data=request.POST)
                
                if user_creation_form.is_valid():
                        user_creation_form.save()
                        
                        user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
                        login(request, user)
                return redirect('home')
        return render (request, 'registration/registro.html', data)


# muestra en una lista los objetos de la base de datos del libro Productos 
def mostrar_productos(request):
        productos = producto.objects.all()
        return render(request, 'list/mostrar_productos.html', {'productos': productos})



# Elimina un registro de la base de productos 
def borrar (request, id ):
        productos = producto.objects.get(id=id)
        productos.delete()
        return redirect('mostrar_productos')


# edita un registro de la base de productos 
def editar (request, id):
        productos = producto.objects.get(id=id)
        form = ProductoForm(request.POST or None, request.FILES or None, instance=productos)
        if form.is_valid()and request.method == 'POST':
                form.save()
                return redirect('mostrar_productos')
        return render (request, 'list/editar.html', {'form': form})
    
def catalogo(request):
        productos = producto.objects.all()
        return render(request, 'aplicacion/catalogo.html', {'productos': productos})



