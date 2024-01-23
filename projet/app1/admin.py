from django.contrib import admin
from .models import Centre , Produit , Client , Fournisseur , Employe, Vente_Produit,stock_Produit

admin.site.register(Centre)
admin.site.register(Produit)
admin.site.register(Client)
admin.site.register(Fournisseur)
admin.site.register(Employe)
admin.site.register(Vente_Produit)
admin.site.register(stock_Produit)

# Register your models here.
