from django.db.models import fields
from django import forms
from .models import Centre, Client, Fournisseur, Employe, Produit , Achat, Reglement,Vente,  paiementcredit , Transfert ,Stock ,Matiere_premiere

class CentreForm(forms.ModelForm):
    class Meta:
        model = Centre
        fields ="__all__"

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = "__all__"

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = "__all__"

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"

class MatierePremiereForm(forms.ModelForm):
    class Meta:
        model = Matiere_premiere
        fields = "__all__"


class AchatForm(forms.ModelForm):
    class Meta:
        model = Achat
        fields =  "__all__"

class ReglementForm(forms.ModelForm):
    class Meta:
        model = Reglement
        fields = "__all__"
        

class PaiementForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = [ 'solde']
    

class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields =  "__all__"
        

class PaiementClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [ 'credit']
        exclude = ['id']

class PaiementCreditForm(forms.ModelForm):
    class Meta:
        model =  paiementcredit
        fields = "__all__"

class TransfertForm(forms.ModelForm):
    class Meta:
        model = Transfert
        fields ="__all__"

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields ="__all__"




#-----------YOUSRAAAA

from django.db.models import fields
from django import forms
from .models import (
    Centre,
    Client,
    Fournisseur,
    Employe,
    Produit,
    PaiementCreditCentre,
    Vente_Produit,
    Paiement_E,
)

class RechercheVenteProduitForm(forms.Form):
    Recherceh_Nom_Code = forms.CharField(required=False)
    date= forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

class RechercheStockProduitForm(forms.Form):
    Recherceh_Nom_Code = forms.CharField(required=False)

class CalculVentesNettesForm(forms.Form):
    date_debut = forms.DateField(label='Date de début')
    date_fin = forms.DateField(label='Date de fin')

        
class Vente_ProduitForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Vente_Produit
        exclude = ['date_vente']  # Exclude the non-editable field
        fields = ["date", "code", "centre", "client", "produit", "quantite", "prix_unitaire", "montant_verse"] 

class PaiementCreditFormC(forms.ModelForm):
    class Meta:
        model = PaiementCreditCentre
        fields = ["montant"]

class PaiementEForm(forms.ModelForm):
    date_paiement = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Paiement_E
        fields = ['date_paiement', 'employe', 'montant','avance']
 
class DateInput(forms.DateInput):
    input_type = 'date'

class CalculSalaireForm(forms.Form):
    employe = forms.ModelChoiceField(queryset=Employe.objects.all(), label="Employé")
    date_debut = forms.DateField(label="Date de début", widget=DateInput)
    date_fin = forms.DateField(label="Date de fin", widget=DateInput)
    pourcentage_absence = forms.DecimalField(max_digits=5, decimal_places=2, initial=0, label="montant d'absence à relever")

class DateDetailForm(forms.Form):
    employe = forms.ModelChoiceField(queryset=Employe.objects.all(), label="Employé")
    date_detail = forms.DateField(label="Date pour afficher les détails", widget=forms.DateInput(attrs={'type': 'date'}))

class Add_Produit_StockForm(forms.Form):
    produit = forms.ModelChoiceField(queryset=Produit.objects.all(), label='Produit')
    centre = forms.ModelChoiceField(queryset=Centre.objects.all(), label='Centre')
    quantite = forms.DecimalField(label='Quantité')