# Generated by Django 5.0.6 on 2024-05-30 14:13

import items.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=items.models.custom_upload_to),
        ),
    ]
