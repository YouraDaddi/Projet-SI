from django.urls import path 

from app1.models import Produit, Fournisseur, Client, Employe, Centre
from . import views

urlpatterns = [ 
        # achat
# path('acheter_matiere/create_fournisseur/', views.fournisseur_create_achat, name='fournisseur_create_achat'),
# path('acheter_matiere/create_mp/', views.matiere_premiere_create_achat, name='matiere_premiere_create_achat'),
# path('delete_achat/<int:achat_id>/', views.delete_achat, name='delete_achat'),
# path('generate_journal_achat_pdf/', views.generate_journal_achat_pdf, name='generate_journal_achat_pdf'),
path('ajouter_achat/', views.ajouter_achat, name='ajouter_achat'),
path('journal_achat/', views.journal_achat, name='journal_achat'),
path('paiement/', views.payer_fournisseur, name='paiement'),
path('complete_paiement_fournisseur/', views.complete_paiement_fournisseur, name='complete_paiement_fournisseur'),
path('ajouter_achat/paiement/<int:achat_id>/', views.liste_paiement_achat, name='liste_paiement_achat'),
path('ajouter_achat/paiement/update/<int:pk>/', views.paiement_fournisseur_update, name='paiement_fournisseur_update'),
path('ajouter_achat/paiement/delete/<int:pk>/', views.paiement_fournisseur_delete, name='paiement_fournisseur_delete'),
        # Vente 
path('vendre/', views.vendre_matiere, name='vendre_matiere'),
path('vendre/create_client', views.client_create_vente, name='client_create_vente'),
path('paiement_credit/', views.paiement_credit, name='paiement_credit'),
path('journal_ventes/', views.journal_ventes, name='journal_ventes'),
path('vendre/paiement/<int:vente_id>/', views.liste_paiement_vente, name='liste_paiement_vente'),
# path('delete_vente/<int:vente_id>/', views.delete_vente, name='delete_vente'),
# path('journal_ventes/editer_vente/<int:pk>',views.update_vente,name='editer_vente'),
path('complete_paiement/', views.complete_paiement, name='complete_paiement'),
        #Transfert 
path('transfert/', views.transferer_matiere, name='transfert_matiere'),
path('journal_transferts/', views.journal_transferts, name='journal_transferts'),
                # MAJ models 
        #Fournisseur
path('fournisseurs/', views.fournisseur_list, name='fournisseur_list'),
path('fournisseurs/create/', views.fournisseur_create, name='fournisseur_create'),
path('fournisseurs/update/<int:pk>/', views.fournisseur_update, name='fournisseur_update'),
path('fournisseurs/delete/<int:pk>/', views.fournisseur_delete, name='fournisseur_delete'),
        #STOCK 
path('etat_stock/', views.etat_stock, name='etat_stock'),
path('generate_stock_pdf/', views.generate_stock_pdf, name='generate_stock_pdf'),
path('etat_stock/delete_stock/<int:stock_id>/', views.delete_stock, name='delete_stock'),
        #matiere premiere
path('matiere_premiere_list/', views.matiere_premiere_list, name='matiere_premiere_list'),
path('matieres_premieres/create/', views.matiere_premiere_create, name='matiere_premiere_create'),
path('matieres_premieres/update/<int:pk>/', views.matiere_premiere_update, name='matiere_premiere_update'),
path('matieres_premieres/delete/<int:pk>/', views.matiere_premiere_delete, name='matiere_premiere_delete'),
        #Client
path('clients/', views.liste_clients, name='liste_clients'),
path('clients/create/', views.client_create, name='client_create'),
path('clients/update/<int:pk>/', views.client_update, name='client_update'),
path('clients/delete/<int:pk>/', views.client_delete, name='client_delete'),
        #Achat
path('update_achat/<int:pk>/', views.achat_update, name='achat_update'),
        #Vente
path('update/<int:pk>/', views.vente_update, name='vente_update'),
path('delete_vente/<int:pk>/', views.delete_vente, name='delete_vente'),
        #Paiement client
path('paiement/', views.liste_paiement, name='liste_paiement'),
path('paiement/create/', views.complete_paiement, name='complete_paiement'),
path('paiement/update/<int:pk>/', views.paiement_update, name='paiement_update'),
path('paiement/delete/<int:pk>/', views.paiement_delete, name='paiement_delete'),

#---------------Section 2-3-4----



#-----------Affichage home ----------------------
    path("", views.home, name="home"),
    path("mag/", views.afficher_BD, name="magasin"),
    path("mag/editer/<int:pk>", views.edit_BD, name="editer"),
  #-----------creation / modif / supppression ----------------------
    path("editer_client/<int:pk>/", views.editer_client, name="inserer_Client"),
    path("editer_employe/<int:pk>/", views.editer_employe, name="create_employe"),
    path("editer_produit/<int:pk>/", views.editer_produit, name="create_produit"),
    path("editer_Fournisseur/<int:pk>/", views.editer_fournisseur, name="inserer"),
    path("mag/create_employe/", views.create_employe, name="create_employe"),
    path("mag/create_produit/", views.create_produit, name="create_produit"),
    path("mag/insertFournisseur/", views.create_fournisseur, name="inserer"),
    path("mag/insertClient/", views.create_client, name="inserer_Client"),
    path("supprimer_client/<int:pk>/",views.delete_BD,{"model_name": Client},name="supprimer_client",),
    path("supprimer_produit/<int:pk>/",views.delete_BD,{"model_name": Produit},name="supprimer_produit",),
    path("supprimer_centre/<int:pk>/",views.delete_BD,{"model_name": Centre,},name="supprimer_centre",),
    path("supprimer_employe/<int:pk>/",views.delete_BD,{"model_name": Employe},name="supprimer_employe",),
    path("supprimer_fournisseur/<int:pk>/",views.delete_BD,{"model_name": Fournisseur},name="supprimer_fournisseur",),
   
    path('reglement_credit_client/<int:vente_id>/', views.reglement_credit_client, name='reglement_credit_client'),
    path("vendre_produit/<int:centre_id>/", views.vendre_produit, name="vendre_produit"),
    path("centre/<int:centre_id>/", views.detail_centre, name="centre"),
    path("employe/<int:employe_id>/", views.detail_employe, name="detail_employe"),
    path("paiement-employe/<int:employe_id>/",views.saisir_paiement,name="paiement_employe"),
    path("paiement-calcule/<int:employe_id>/", views.calcul_salaire, name="calcul_salaire"),
    path('journal_vente_produit/<int:centre_id>/', views.Journal_Vente_Produit, name='Journal_Vente_Produit'),
    path('modify_absence/<int:employe_id>/', views.modify_absence, name='modify_absence'),
    path('client/<int:client_id>/', views.detail_client, name='client_detail'),
    path('vente/<int:vente_id>/supprimer/', views.supprimer_vente, name='supprimer_vente'),
    path('stock_state/<int:centre_id>/', views.stock_state, name='stock_state'),
    path('add_produit_to_stock/<int:centre_id>/', views.add_produit_to_stock, name='Produit'),
    path('calcul_ventes_nettes/<int:centre_id>/', views.calcul_ventes_nettes, name='calcul_ventes_nettes'),
    path('calculer_benefice/<int:centre_id>/', views.calculer_benefice, name='calculer_benefice'),
   
    path('detail_produit/<int:pk>/', views.detail_produit, name='detail_produit'),
    path('journal_transferts-centre/<int:centre_id>/', views.journal_transfert_c, name='journal_transferts'),


#-------------SECTION  5----
path('analyze-achats/', views.analyze_achats, name='analyze_achats'),
path('dashboard_ventes/', views.analyze_ventes, name='dashboard_ventes'),
]

