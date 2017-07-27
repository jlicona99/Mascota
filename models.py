from django.db import models

# Create your models here.
class partner(models.Model):
    name=models.CharField(max_lenght=50,help_text='Escriba el nombre del proveedor')
    tel = models.CharField(max_lenght=12,help_text='Escriba el numero del proveedor')
    email = models.EmailField(help_text='Ingrese el email de contacto del proveedor')
    startre= models.DateField(help_text='Seleccione la fecha de inicio de relación con el proveedor')

class product(models.Model):
    categories =(
        ('F', 'Food'),
        ('A', 'Accesories'),
        ('D','Drugs'),
        ('T','Toys')
    )
    Product = models.CharField(max_lenght=40,help_text='Escriba el nombre del producto')
    Parner = models.ForeignKey(partner)
    Clasificacition = models.CharField(max_lenght=40,help_text='Escriba la Clasificacicion')
    Date = models.DateField(auto_now=True)
    Price = models.DecimalField()
    category = models.CharField(max_lenght=1, help_text="Seleccione la categoria",choices=categories)

class stock (models.Model):
    product=models.ForeignKey(product)
    stock=models.Integerfield(help_text="Ingrese la cantidad de productos existentes")
