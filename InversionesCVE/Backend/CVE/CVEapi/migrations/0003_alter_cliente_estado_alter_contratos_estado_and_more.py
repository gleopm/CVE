# Generated by Django 4.2.6 on 2023-10-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVEapi', '0002_alter_cliente_estado_alter_contratos_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.CharField(choices=[('P', 'Pendiente'), ('A', 'Activo')], max_length=1),
        ),
        migrations.AlterField(
            model_name='contratos',
            name='estado',
            field=models.CharField(choices=[('Ve', 'Vencido'), ('Vi', 'Vigente')], max_length=2),
        ),
        migrations.AlterField(
            model_name='facturas',
            name='estado',
            field=models.CharField(choices=[('P', 'Pendiente'), ('A', 'Activo')], max_length=1),
        ),
    ]
