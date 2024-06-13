# Generated by Django 5.0.6 on 2024-06-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_alter_profile_options_alter_profile_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(choices=[('', 'Estado'), ('AN', 'Anzoátegui'), ('AP', 'Apure'), ('AR', 'Aragua'), ('BA', 'Barinas'), ('BO', 'Bolívar'), ('CA', 'Carabobo'), ('CO', 'Cojedes'), ('DA', 'Delta Amacuro'), ('DC', 'Distrito Capital'), ('FA', 'Falcón'), ('GU', 'Guárico'), ('LA', 'Lara'), ('ME', 'Mérida'), ('MI', 'Miranda'), ('MO', 'Monagas'), ('NE', 'Nueva Esparta'), ('PO', 'Portuguesa'), ('SU', 'Sucre'), ('TA', 'Táchira'), ('TR', 'Trujillo'), ('VA', 'Vargas'), ('YA', 'Yaracuy'), ('ZU', 'Zulia')], default='', max_length=2),
        ),
    ]
