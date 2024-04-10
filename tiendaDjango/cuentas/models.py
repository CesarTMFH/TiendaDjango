from django.db import models

class producto (models.Model):
    nombreproducto = models.CharField(max_length=100)
    descripcionproducto = models.TextField()
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    cantidad = models.IntegerField()
    especificaciones = models.TextField()
    imagenP = models.ImageField(upload_to='img_producto/')
    imagen1 = models.ImageField(upload_to='img_producto/', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='img_producto/', blank=True, null=True)
    
    
    def precio_formateado(self):
        return '{:,.2f}'.format(self.precio)

    def __str__(self):
        return self.nombreproducto
