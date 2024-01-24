# Generated by Django 5.0.1 on 2024-01-24 11:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('telephone', models.CharField(max_length=15)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('telephone', models.CharField(max_length=15)),
                ('solde', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere_premiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('telephone', models.CharField(max_length=15)),
                ('salaire_jour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.centre')),
            ],
        ),
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('prix_unitaire_HT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_achat', models.DateField()),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.fournisseur')),
                ('matiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.matiere_premiere')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement_E',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_paiement', models.DateField(default=django.utils.timezone.now)),
                ('montant', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('avance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('absence', models.BooleanField(default=False)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('quantite', models.PositiveIntegerField()),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.matiere_premiere')),
            ],
        ),
        migrations.CreateModel(
            name='Reglement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_reglement', models.DateField()),
                ('achat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.achat')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('date_achat', models.DateField(null=True)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.fournisseur')),
                ('matiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.matiere_premiere')),
            ],
        ),
        migrations.CreateModel(
            name='stock_Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.DecimalField(decimal_places=2, max_digits=15)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.centre')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Transfert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_transfert', models.DateField()),
                ('quantite', models.PositiveIntegerField()),
                ('cout_transfert', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('centre_dest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.centre')),
                ('matiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.matiere_premiere')),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('prix_unitaire', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_vente', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.client')),
                ('matiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.matiere_premiere')),
            ],
        ),
        migrations.CreateModel(
            name='paiementcredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paiement_credit', models.DateField()),
                ('vente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.vente')),
            ],
        ),
        migrations.CreateModel(
            name='Vente_Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_vente', models.DateField()),
                ('code', models.CharField(max_length=10, unique=True)),
                ('quantite', models.PositiveIntegerField()),
                ('prix_unitaire', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montant_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('montant_verse', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('credit', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.centre')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vente_produits', to='app1.client')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.produit')),
            ],
        ),
        migrations.CreateModel(
            name='PaiementCreditCentre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paiement_credit', models.DateField(auto_now_add=True)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.centre')),
                ('vente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.vente_produit')),
            ],
        ),
    ]
