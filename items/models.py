from django.db import models
from django.contrib.auth.models import User

# Create your models here

def custom_upload_to(instance, filename):
    old_instance = Item.objects.filter(pk=instance.pk)
    if old_instance:
        old_instance[0].image.delete()
    return 'item_images/' + filename

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class Item(models.Model):
    name  = models.CharField(max_length=255, verbose_name='Nombre')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    price = models.FloatField(verbose_name='Precio')
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True, verbose_name='Imágen')
    availability = models.BooleanField(default=True, verbose_name='Disponibilidad')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE, verbose_name='Usuario')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ítem'
        verbose_name_plural = 'Ítems'
        ordering = ('-created_at',)

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name='items')