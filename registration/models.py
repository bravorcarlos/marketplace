from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles_images/' + filename

ESTADOS = (
    ('', 'Estado'),
    ('AN', 'Anzoátegui'),
    ('AP', 'Apure'),
    ('AR', 'Aragua'),
    ('BA', 'Barinas'),
    ('BO', 'Bolívar'),
    ('CA', 'Carabobo'),
    ('CO', 'Cojedes'),
    ('DA', 'Delta Amacuro'),
    ('DC', 'Distrito Capital'),
    ('FA', 'Falcón'),
    ('GU', 'Guárico'),
    ('LA', 'Lara'),
    ('ME', 'Mérida'),
    ('MI', 'Miranda'),
    ('MO', 'Monagas'),
    ('NE', 'Nueva Esparta'),
    ('PO', 'Portuguesa'),
    ('SU', 'Sucre'),
    ('TA', 'Táchira'),
    ('TR', 'Trujillo'),
    ('VA', 'Vargas'),
    ('YA', 'Yaracuy'),
    ('ZU', 'Zulia'),
)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=2, choices=ESTADOS, default='')
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
 

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)