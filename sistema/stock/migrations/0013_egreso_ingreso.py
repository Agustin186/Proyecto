# Generated by Django 5.1.1 on 2024-10-08 03:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0012_arqueocaja_alter_compras_id_caja_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id_egreso', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_egreso', models.DateTimeField(auto_now_add=True)),
                ('id_caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='egresos', to='stock.arqueocaja')),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id_ingreso', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('id_caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingresos', to='stock.arqueocaja')),
            ],
        ),
    ]
