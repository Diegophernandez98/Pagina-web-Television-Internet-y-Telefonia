# Generated by Django 4.2.4 on 2023-11-17 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_boleta_cliente_alter_boleta_descuento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='rol_id',
            new_name='rol',
        ),
    ]
