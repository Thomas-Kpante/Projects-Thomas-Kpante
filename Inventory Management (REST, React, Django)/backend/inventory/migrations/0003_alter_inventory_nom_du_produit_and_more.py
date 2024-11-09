# Generated by Django 5.1.1 on 2024-10-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_inventory_delete_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='Nom_du_produit',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='Quantité_actuelle_en_stock',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='Seuil_minimum_en_stock',
            field=models.IntegerField(),
        ),
    ]
