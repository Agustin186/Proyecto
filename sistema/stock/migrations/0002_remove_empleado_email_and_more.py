# Generated by Django 5.1 on 2024-09-03 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='email',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='fecha_contratacion',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='telefono',
        ),
    ]
