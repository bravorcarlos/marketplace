# Generated by Django 5.0.6 on 2024-05-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
