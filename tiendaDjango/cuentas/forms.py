from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import producto


class CumstomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2',]
        

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombreproducto', 'descripcionproducto', 'precio', 'cantidad', 'especificaciones', 'imagenP','imagen1','imagen2']
        

    
