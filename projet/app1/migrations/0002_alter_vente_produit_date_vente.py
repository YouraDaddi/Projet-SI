# Generated by Django 5.0.1 on 2024-01-23 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vente_produit',
            name='date_vente',
            field=models.DateField(),
        ),
    ]
