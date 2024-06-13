# Generated by Django 5.0.6 on 2024-06-04 06:14

import django.db.models.deletion
import items.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_item_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-created_at',), 'verbose_name': 'Ítem', 'verbose_name_plural': 'Ítems'},
        ),
        migrations.AlterField(
            model_name='item',
            name='availability',
            field=models.BooleanField(default=True, verbose_name='Disponibilidad'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.category', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=items.models.custom_upload_to, verbose_name='Imágen'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(verbose_name='Precio'),
        ),
    ]