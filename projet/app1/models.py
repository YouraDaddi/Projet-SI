from django.db import models

class Centre(models.Model):
    code=models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    # def __str__(self):

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    solde = models.DecimalField(max_digits=10, decimal_places=2)

class Employe(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    salaire_jour = models.DecimalField(max_digits=10, decimal_places=2)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)

class Matiere_premiere(models.Model):
    designation = models.CharField(max_length=100)

class Produit(models.Model):
    designation = models.CharField(max_length=100)
    


class Achat(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere_premiere, on_delete=models.CASCADE, null=True)
    quantite = models.PositiveIntegerField()
    prix_unitaire_HT = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    @property
    def montant_achat(self):
        return self.quantite * self.prix_unitaire_HT



class Reglement(models.Model):
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE,null=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_reglement = models.DateField()


class Vente(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere_premiere, on_delete=models.CASCADE, null=True)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_vente = models.DateField()

    @property
    def montant_vente(self):
        return self.quantite * self.prix_unitaire

class paiementcredit(models.Model):
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, null=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement_credit = models.DateField()


class Transfert(models.Model):
    date_transfert = models.DateField()
    centre_dest = models.ForeignKey(Centre, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere_premiere, on_delete=models.CASCADE,null=True)
    quantite = models.PositiveIntegerField()
    cout_transfert = models.DecimalField(max_digits=10, decimal_places=2, editable=False)


class Stock(models.Model):
    matiere = models.ForeignKey(Matiere_premiere, on_delete=models.CASCADE, null=True)
    quantite = models.PositiveIntegerField()
    fournisseur  = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    date_achat = models.DateField(null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)







class stock_Produit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    quantite = models.DecimalField(max_digits=15, decimal_places=2)

class Vente_Produit(models.Model):
    date_vente = models.DateField()
    code = models.CharField(max_length=10, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,related_name='vente_produits')
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    montant_total = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    montant_verse = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, blank=True, null=True
    )
    credit = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, blank=True, null=True
    )
 
class PaiementCreditCentre(models.Model):
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    vente = models.ForeignKey(Vente_Produit, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement_credit = models.DateField(auto_now_add=True)

from django.utils import timezone

class Paiement_E(models.Model):
    date_paiement = models.DateField(default=timezone.now)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2, default=0) #salir_jour
    avance = models.DecimalField(max_digits=10, decimal_places=2, default=0) #Massrouf
    absence = models.BooleanField(default=False)   