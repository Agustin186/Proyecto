# Generated by Django 5.1 on 2024-09-07 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_articulos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_prod', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_prod', models.CharField(max_length=100, verbose_name='Nombre del Articulo')),
                ('precio_prod', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('stock_min', models.IntegerField(blank=True, null=True)),
                ('stock_max', models.IntegerField(blank=True, null=True)),
                ('stock_actual', models.IntegerField(blank=True, null=True)),
                ('punto_reposicion', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id_prov', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_prov', models.CharField(blank=True, max_length=100, verbose_name='nombre del proveedor')),
                ('cuit_prov', models.IntegerField(blank=True, null=True, verbose_name='cuit del proveedor')),
                ('tipo_prov', models.CharField(blank=True, max_length=100, null=True, verbose_name='tipo de proveedor')),
                ('direcc_prov', models.CharField(max_length=100, verbose_name='direccion del proveedor')),
                ('tel_prov', models.CharField(blank=True, max_length=50, null=True, verbose_name='telefono del proveedor')),
                ('correo_prov', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email del proveedor')),
            ],
        ),
        migrations.DeleteModel(
            name='Proveedor',
        ),
        migrations.AddField(
            model_name='productos',
            name='id_prov',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productos', to='stock.proveedores'),
        ),
    ]
