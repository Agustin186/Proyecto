# Generated by Django 5.1 on 2024-09-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_empleados_delete_empleado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
