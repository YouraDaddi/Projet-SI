from django.shortcuts import render, redirect
from .models import (
    Centre,
    Produit,
    Client,
    Fournisseur,
    Employe,
    Achat,
    Reglement,
    Vente,
    Transfert,
    paiementcredit,
    Stock,
    Matiere_premiere,
)
from .forms import (
    FournisseurForm,
    CentreForm,
    ClientForm,
    EmployeForm,
    ProduitForm,
    AchatForm,
    ReglementForm,
    PaiementForm,
    VenteForm,
    PaiementCreditForm,
    TransfertForm,
    PaiementClientForm,
    StockForm,
    MatierePremiereForm,
)
from django.db import models
from django.contrib import messages

# ------------------------------------ Fonction de MAJ sur toutes les tables ------------------------------------

# --------------Fournisseur


def fournisseur_list(request):
    # List of dictionaries representing instance data
    fournisseurs_data = [
        {
            "nom": "Fournisseur 1",
            "prenom": "Prenom 1",
            "adresse": "Adresse 1",
            "telephone": "123456789",
            "solde": 1000.00,
        },
        {
            "nom": "Fournisseur 2",
            "prenom": "Prenom 2",
            "adresse": "Adresse 2",
            "telephone": "987654321",
            "solde": 1500.00,
        },
        {
            "nom": "Fournisseur 3",
            "prenom": "Prenom 3",
            "adresse": "Adresse 3",
            "telephone": "555555555",
            "solde": 2000.00,
        },
        # Add more fournisseurs as needed
    ]

    # Create or get instances for each dictionary in fournisseurs_data
    for data in fournisseurs_data:
        fournisseur, created = Fournisseur.objects.get_or_create(
            nom=data["nom"],
            defaults={
                "prenom": data["prenom"],
                "adresse": data["adresse"],
                "telephone": data["telephone"],
                "solde": data["solde"],
            },
        )

    # Retrieve all fournisseurs
    fournisseurs = Fournisseur.objects.all()

    # Pass fournisseurs to the template
    return render(request, "fournisseur_list.html", {"fournisseurs": fournisseurs})


def fournisseur_create(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("fournisseur_list")
    else:
        form = FournisseurForm()
    return render(request, "fournisseur_form.html", {"form": form})


def fournisseur_update(request, pk):
    fournisseur = Fournisseur.objects.get(pk=pk)
    if request.method == "POST":
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect("fournisseur_list")
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, "fournisseur_form.html", {"form": form})


def fournisseur_delete(request, pk):
    Fournisseur.objects.get(pk=pk).delete()
    return redirect("fournisseur_list")


def fournisseur_create_achat(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("acheter_matiere")
    else:
        form = FournisseurForm()
    return render(request, "fournisseur_form.html", {"form": form})


# --------------Matiere premiere


def matiere_premiere_list(request):
    # List of dictionaries representing instance data
    matieres_premieres_data = [
        {"designation": "Matiere 1"},
        {"designation": "Matiere 2"},
        {"designation": "Matiere 3"},
        # Add more matieres_premieres as needed
    ]

    # Create or get instances for each dictionary in matieres_premieres_data
    for data in matieres_premieres_data:
        matiere_premiere, created = Matiere_premiere.objects.get_or_create(
            designation=data["designation"]
        )

    # Retrieve all matieres_premieres
    matieres_premieres = Matiere_premiere.objects.all()

    # Pass matieres_premieres to the template
    return render(
        request,
        "matiere_premiere_list.html",
        {"matieres_premieres": matieres_premieres},
    )


def matiere_premiere_create(request):
    if request.method == "POST":
        form = MatierePremiereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("matiere_premiere_list")
    else:
        form = MatierePremiereForm()
    return render(request, "matiere_premiere_form.html", {"form": form})


def matiere_premiere_update(request, pk):
    matiere_premiere = get_object_or_404(Matiere_premiere, pk=pk)
    if request.method == "POST":
        form = MatierePremiereForm(request.POST, instance=matiere_premiere)
        if form.is_valid():
            form.save()
            return redirect("matiere_premiere_list")
    else:
        form = MatierePremiereForm(instance=matiere_premiere)
    return render(request, "matiere_premiere_form.html", {"form": form})


def matiere_premiere_delete(request, pk):
    matiere_premiere = get_object_or_404(Matiere_premiere, pk=pk)
    matiere_premiere.delete()
    return redirect("matiere_premiere_list")


def matiere_premiere_create_achat(request):
    if request.method == "POST":
        form = MatierePremiereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("acheter_matiere")
    else:
        form = MatierePremiereForm()
    return render(request, "matiere_premiere_form.html", {"form": form})


# ---------------CLIENT


def liste_clients(request):
    clients = Client.objects.all()
    return render(request, "liste_clients.html", {"clients": clients})


def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("liste_clients")
    else:
        form = ClientForm()
    return render(request, "client_form.html", {"form": form})


def client_create_vente(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vendre_matiere")
    else:
        form = ClientForm()
    return render(request, "client_form.html", {"form": form})


def client_update(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("liste_clients")
    else:
        form = ClientForm(instance=client)
    return render(request, "client_form.html", {"form": form, "client": client})


def client_delete(request, pk):
    Client.objects.get(pk=pk).delete()
    return redirect("liste_clients")


# -------------- ACHAT

# def achat_update(request, pk):
#     achat = Achat.objects.get(pk=pk)
#     fournisseurs = Fournisseur.objects.all()
#     matieres = Matiere_premiere.objects.all()

#     if request.method == 'POST':
#         form = AchatForm(request.POST, instance=achat)
#         if form.is_valid():
#             updated_achat = form.save()

#             # Update Stock instance
#             stock = Stock.objects.get(matiere=updated_achat.matiere, fournisseur=updated_achat.fournisseur)
#             stock.quantite += (updated_achat.quantite-achat.quantite)
#             stock.prix = updated_achat.prix_unitaire_HT
#             stock.save()
#             return redirect('journal_achat')
#     else:
#         form = AchatForm(instance=achat)

#     return render(request, 'ajouter_achat.html', {'form': form, 'fournisseurs': fournisseurs, 'matieres': matieres})
from django.shortcuts import get_object_or_404


def achat_update(request, pk):
    achat = get_object_or_404(Achat, pk=pk)

    if request.method == "POST":
        form = AchatForm(request.POST, instance=achat)
        if form.is_valid():
            updated_achat = form.save()
            # Update Stock instance
            stock = Stock.objects.get(
                matiere=achat.matiere,
                fournisseur=achat.fournisseur,
                date_achat=achat.date_achat,
            )
            stock.quantite += updated_achat.quantite - achat.quantite
            stock.prix = updated_achat.prix_unitaire_HT
            stock.save()
            return redirect("journal_achat")
    else:
        form = AchatForm(instance=achat)

    return render(request, "update_achat.html", {"form": form, "achat": achat})


def delete_achat(request, pk):
    achat = Achat.objects.get(id=pk)

    # Subtract achat.montant_achat from fournisseur.solde
    achat.fournisseur.solde -= achat.montant_achat

    # Save the changes to the fournisseur object
    achat.fournisseur.save()

    # Delete related Reglement instances using the paiement_delete function
    paiements = Reglement.objects.filter(achat=achat)
    for paiement in paiements:
        paiement_fournisseur_delete(request, paiement.id)

    # Delete the achat instance
    achat.delete()

    return redirect("journal_achat")


# -------------- Paiement Fournisseur
def liste_paiement_fournisseur(request):
    paiement = Reglement.objects.all()
    return render(request, "liste_paiement_fournisseur.html", {"paiement": paiement})


def liste_paiement_achat(request, achat_id):
    achat_instance = Achat.objects.get(pk=achat_id)
    paiement = Reglement.objects.filter(achat=achat_instance)

    # Extract the 'montant' values and convert them to a list
    montant_list = paiement.values_list("montant", flat=True)

    # Calculate the sum of 'montant' values
    total_montant = sum(montant_list)

    # Calculate the remaining amount
    montant_restant = achat_instance.montant_achat - total_montant

    return render(
        request,
        "liste_paiement_fournisseur.html",
        {"paiement": paiement, "montant_restant": montant_restant},
    )


from decimal import Decimal


def paiement_fournisseur_update(request, pk):
    paiement = Reglement.objects.get(pk=pk)
    old_montant = paiement.montant
    achatId = paiement.achat.id
    if request.method == "POST":
        form = ReglementForm(request.POST, instance=paiement)
        if form.is_valid():
            form.save()

            # Calculate the difference between old and new montant
            new_montant = form.cleaned_data["montant"]
            montant_difference = new_montant - old_montant

            # Update the associated client's credit
            fournisseur = paiement.achat.fournisseur
            fournisseur.solde -= montant_difference
            fournisseur.save()

            return redirect("liste_paiement_achat", achat_id=achatId)
    else:
        form = ReglementForm(instance=paiement)

    return render(
        request,
        "complete_paiement_fournisseur.html",
        {"form": form, "paiement": paiement},
    )


def paiement_fournisseur_delete(request, pk):
    paiement = Reglement.objects.get(pk=pk)
    achatId = paiement.achat.id
    montant = paiement.montant
    fournisseur = paiement.achat.fournisseur
    fournisseur.solde += montant
    fournisseur.save()
    paiement.delete()
    return redirect("liste_paiement_achat", achat_id=achatId)


# -------------- VENTE


def vente_update(request, pk):
    vente = Vente.objects.get(pk=pk)
    clients = Client.objects.all()
    matieres = Matiere_premiere.objects.all()

    if request.method == "POST":
        form = VenteForm(request.POST, instance=vente)
        if form.is_valid():
            form.save()
            return redirect("journal_ventes")
    else:
        form = VenteForm(instance=vente)

    return render(
        request,
        "vendre_matiere.html",
        {"form": form, "clients": clients, "matieres": matieres},
    )


def delete_vente(request, pk):
    vente = Vente.objects.get(id=pk)

    # Subtract vente.montant_vente from client.credit
    vente.client.credit -= vente.montant_vente

    # Save the changes to the client object
    vente.client.save()

    # Delete related PaiementCredit instances using the paiement_delete function
    paiements = paiementcredit.objects.filter(vente=vente)
    for paiement in paiements:
        paiement_delete(request, paiement.id)

    # Delete the vente instance
    vente.delete()

    return redirect("journal_ventes")


# -------------- Paiement Client
def liste_paiement(request):
    paiement = paiementcredit.objects.all()
    return render(request, "liste_paiement.html", {"paiement": paiement})


def liste_paiement_vente(request, vente_id):
    vente_instance = Vente.objects.get(pk=vente_id)
    paiement = paiementcredit.objects.filter(vente=vente_instance)

    # Extract the 'montant' values and convert them to a list
    montant_list = paiement.values_list("montant", flat=True)

    # Calculate the sum of 'montant' values
    total_montant = sum(montant_list)

    # Calculate the remaining amount
    montant_restant = vente_instance.montant_vente - total_montant

    return render(
        request,
        "liste_paiement.html",
        {"paiement": paiement, "montant_restant": montant_restant},
    )


from decimal import Decimal


def paiement_update(request, pk):
    paiement = paiementcredit.objects.get(pk=pk)
    old_montant = paiement.montant
    if request.method == "POST":
        form = PaiementCreditForm(request.POST, instance=paiement)
        if form.is_valid():
            form.save()

            # Calculate the difference between old and new montant
            new_montant = form.cleaned_data["montant"]
            montant_difference = new_montant - old_montant

            # Update the associated client's credit
            client = paiement.vente.client
            client.credit -= montant_difference
            client.save()

            return redirect("liste_paiement")
    else:
        form = PaiementCreditForm(instance=paiement)

    return render(
        request, "complete_paiement.html", {"form": form, "paiement": paiement}
    )


def paiement_delete(request, pk):
    paiement = paiementcredit.objects.get(pk=pk)
    montant = paiement.montant
    client = paiement.vente.client
    client.credit += montant
    client.save()
    paiement.delete()
    return redirect("liste_paiement")


# ----------------------------------------------------- Achat de matiere premiere ------------------------------------
# --------------fonction pour saisir l'achat


def ajouter_achat(request):
    if request.method == "POST":
        form = AchatForm(request.POST)
        if form.is_valid():
            achat = form.save(commit=False)
            achat.montant_total = achat.quantite * achat.prix_unitaire_HT
            achat.save()
            fournisseurs = Fournisseur.objects.get(id=achat.fournisseur.id)
            fournisseurs.solde += achat.montant_total
            fournisseurs.save()

            regler = Reglement.objects.create(
                achat=achat, montant=0, date_reglement=achat.date_achat
            )
            regler.save()

            # Create Stock instance
            stock = Stock.objects.create(
                matiere=achat.matiere,
                quantite=achat.quantite,
                fournisseur=achat.fournisseur,
                date_achat=achat.date_achat,
                prix=achat.prix_unitaire_HT,
            )

            # Store the client information and Reglement ID in the session
            request.session["selected_fournisseur_id"] = achat.fournisseur.id
            request.session["Reglement_id"] = regler.id
            # redirect to paiement
            return redirect("paiement")
    else:
        form = AchatForm()

    return render(request, "ajouter_achat.html", {"form": form})


# --------------payer le fournisseur
def payer_fournisseur(request):
    k = 0
    if request.method == "POST":
        form = PaiementForm(request.POST)
        if form.is_valid():
            # Retrieve the supplier information from the session
            fournisseur_id = request.session.get("selected_fournisseur_id")

            if fournisseur_id:
                fournisseur = Fournisseur.objects.get(id=fournisseur_id)
                paiement = form.instance  # Access the form instance without saving
                fournisseur.solde -= paiement.solde
                fournisseur.save()

                # Clear the session variable after use
                del request.session["selected_fournisseur_id"]
            regler_id = request.session.get("regler_id")
            if regler_id:
                regler = Reglement.objects.get(id=regler_id)
                regler.montant = paiement.solde
                k = regler.achat.montant_achat
                regler.save()

                # Redirect after processing
            return redirect("journal_achat")

    else:
        form = PaiementForm()

    return render(request, "Paiement_fournisseur.html", {"form": form, "k": k})


from django.db.models import Sum, F


def journal_achat(request):
    # Get filter parameters from the request
    fournisseur = request.GET.get("fournisseur")
    matiere_name = request.GET.get("matiere_name")
    date_achat = request.GET.get("date_achat")

    # Construct the filter query based on the parameters
    filter_query = {}
    if fournisseur:
        filter_query["fournisseur__nom__icontains"] = fournisseur
    if matiere_name:
        filter_query["matiere__designation__icontains"] = matiere_name
    if date_achat:
        filter_query["date_achat"] = date_achat

    # Apply filters and calculate total purchase cost
    achats = Achat.objects.filter(**filter_query)
    # ventes = Vente.objects.all()
    total_achats = (
        achats.aggregate(total_achats=Sum(F("prix_unitaire_HT") * F("quantite")))[
            "total_achats"
        ]
        or 0
    )

    return render(
        request, "journal_achat.html", {"achats": achats, "total_achats": total_achats}
    )


def complete_paiement_fournisseur(request):
    if request.method == "POST":
        form = ReglementForm(request.POST)
        if form.is_valid():
            regler = form.save(commit=False)

            achat = Achat.objects.get(id=regler.achat.id)
            fournisseurs = achat.fournisseur
            fournisseurs.solde -= regler.montant
            fournisseurs.save()
            regler.save()

            return redirect("journal_achat")
    else:
        form = ReglementForm()

    fournisseurs = Fournisseur.objects.all()
    return render(
        request,
        "complete_paiement_fournisseur.html",
        {"form": form, "fournisseurs": fournisseurs},
    )


# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa  # pip install xhtml2pdf

# def generate_journal_achat_pdf(request):
#     # Your existing filter logic
#     supplier_name = request.GET.get('supplier_name')
#     product_name = request.GET.get('product_name')
#     date_achat = request.GET.get('date_achat')

#     filter_query = {}
#     if supplier_name:
#         filter_query['fournisseur__nom__icontains'] = supplier_name
#     if product_name:
#         filter_query['produit__designation__icontains'] = product_name
#     if date_achat:
#         filter_query['date_achat'] = date_achat

#     achats = Achat.objects.filter(**filter_query)
#     # total= achats.prix * achats.quantite

#     # Render the template
#     template = get_template('journal_achats.html')
#     context = {'achats': achats }
#     html = template.render(context)

#     # Create a PDF response
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="achat_report.pdf"'

#     # Create PDF
#     pisa_status = pisa.CreatePDF(html, dest=response)

#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')

#     return response


# --------------------------------------- VENDRE ----------------------------------------------------


def vendre_matiere(request):
    if request.method == "POST":
        form = VenteForm(request.POST)
        if form.is_valid():
            vente = form.save(commit=False)
            vente.montant_total = vente.quantite * vente.prix_unitaire
            vente.save()

            clients = Client.objects.get(id=vente.client.id)
            clients.credit += vente.montant_total

            # stocks=Stock.objects.get(produit=vente.produit)
            # if(stocks.quantite > vente.quantite):
            #     stocks.quantite -= vente.quantite
            clients.save()

            # Create a new PaiementCredit instance
            p = paiementcredit.objects.create(
                vente=vente, montant=0, date_paiement_credit=vente.date_vente
            )
            p.save()

            # Store the client information and PaiementCredit ID in the session
            request.session["selected_client_id"] = vente.client.id
            request.session["p_id"] = p.id

            return redirect("paiement_credit")
    else:
        form = VenteForm()

    clients = Client.objects.all()
    matieres = Matiere_premiere.objects.all()
    return render(
        request,
        "vendre_matiere.html",
        {"form": form, "clients": clients, "matieres": matieres},
    )


def paiement_credit(request):
    term_encour = None
    # Logique pour gérer le paiement crédit du client
    if request.method == "POST":
        form = PaiementClientForm(request.POST)
        if form.is_valid():
            # paiement_credit = form.save()

            # Retrieve the client information from the session
            client_id = request.session.get("selected_client_id")
            # paiement_credit_id = request.session.get('paiement_credit_id')

            if client_id:
                client = Client.objects.get(id=client_id)
                paiement_credit = form.instance
                client.credit -= paiement_credit.credit
                client.save()

            p_id = request.session.get("p_id")
            if p_id:
                p = paiementcredit.objects.get(id=p_id)
                p.montant = paiement_credit.credit
                p.save()
                term_encour = p.vente.montant_vente - p.montant
                # Clear the session variable after use
                del request.session["selected_client_id"]
                # del request.session['paiement_credit_id']
            # Calculate montant_total for the vente

            return redirect("journal_ventes")

    else:
        form = PaiementClientForm()

    return render(
        request, "paiement_credit.html", {"form": form, "term_encour": term_encour}
    )


def journal_ventes(request):
    # Get filter parameters from the request
    client = request.GET.get("client")
    matiere_name = request.GET.get("matiere_name")
    date_vente = request.GET.get("date_vente")

    # Construct the filter query based on the parameters
    filter_query = {}
    if client:
        filter_query["client__nom__icontains"] = client
    if matiere_name:
        filter_query["matiere__designation__icontains"] = matiere_name
    if date_vente:
        filter_query["date_vente"] = date_vente

    # Apply filters and calculate total purchase cost
    ventes = Vente.objects.filter(**filter_query)
    # ventes = Vente.objects.all()
    total_ventes = (
        ventes.aggregate(total_ventes=Sum(F("prix_unitaire") * F("quantite")))[
            "total_ventes"
        ]
        or 0
    )

    return render(
        request, "journal_ventes.html", {"ventes": ventes, "total_ventes": total_ventes}
    )


def complete_paiement(request):
    if request.method == "POST":
        form = PaiementCreditForm(request.POST)
        if form.is_valid():
            paiementCredit = form.save(commit=False)

            vente = Vente.objects.get(id=paiementCredit.vente.id)
            clients = vente.client
            clients.credit -= paiementCredit.montant
            clients.save()
            paiementCredit.save()

            return redirect("journal_ventes")
    else:
        form = PaiementCreditForm()

    clients = Client.objects.all()
    return render(request, "complete_paiement.html", {"form": form, "clients": clients})


# ---------------TRANSFERT


def transferer_matiere(request):
    if request.method == "POST":
        form = TransfertForm(request.POST)
        if form.is_valid():
            transfert = form.save(commit=False)
            # transfert.cout_transfert = transfert.produit.prix_unitaire_achat * transfert.quantite
            # hna lzm f stock ki ndir matiere w prix taeha njib mltm  nchof 3la hssab quantite w la date apres nchof  apres n9dr n3mr le coup
            transfert.cout_transfert = 0
            transfert.save()
            return redirect("journal_transferts")
    else:
        form = TransfertForm()

    return render(request, "transferer_matiere.html", {"form": form})


def journal_transferts(request):
    transferts = Transfert.objects.all()
    total_transferts = sum(transfert.cout_transfert for transfert in transferts)
    return render(
        request,
        "journal_transferts.html",
        {"transferts": transferts, "total_transferts": total_transferts},
    )


# ---------------------------------- STOCK --------------------------


def etat_stock(request):
    # Your existing filter logic
    supplier_name = request.GET.get("supplier_name")
    matiere_name = request.GET.get("matiere_name")
    date_achat = request.GET.get("date_achat")

    filter_query = {}
    if supplier_name:
        filter_query["fournisseur__nom__icontains"] = supplier_name
    if matiere_name:
        filter_query["matiere__designation__icontains"] = matiere_name
    if date_achat:
        filter_query["date_achat"] = date_achat

    # achats = Achat.objects.filter(**filter_query)

    # Implement the logic to retrieve the matieres and calculate total purchase cost
    stocks = Stock.objects.filter(
        **filter_query
    )  # You should customize this query based on your filtering logic

    total = sum(stock.prix * stock.quantite for stock in Stock.objects.all())
    # total_transfert = sum(transfert.cout_transfert for transfert in Transfert.objects.all())

    return render(request, "etat_stock.html", {"stocks": stocks, "total": total})


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  # pip install xhtml2pdf


def generate_stock_pdf(request):
    # Your existing filter logic
    supplier_name = request.GET.get("supplier_name")
    matiere_name = request.GET.get("matiere_name")
    date_achat = request.GET.get("date_achat")

    filter_query = {}
    if supplier_name:
        filter_query["fournisseur__nom__icontains"] = supplier_name
    if matiere_name:
        filter_query["matieret__designation__icontains"] = matiere_name
    if date_achat:
        filter_query["date_achat"] = date_achat

    stocks = Stock.objects.filter(**filter_query)
    # total= stocks.prix * stocks.quantite

    # Render the template
    template = get_template("stock_pdf_template.html")
    context = {"stocks": stocks}
    html = template.render(context)

    # Create a PDF response
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="stock_report.pdf"'

    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")

    return response


def delete_stock(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    stock.delete()
    return redirect("etat_stock")


# -----------------------------SECTION 05 ------------------------------

from django.db.models import Sum, F
from django.db.models.functions import TruncMonth
from django.utils import timezone
from dateutil.relativedelta import relativedelta  # installing
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # installing
import pandas as pd  # installing
from io import BytesIO
import base64

from .models import Achat, Fournisseur


def analyze_achats(request):
    # Get the total value of purchases for each month over the last 12 months
    achats_data = Achat.objects.filter(
        date_achat__gte=(timezone.now() - relativedelta(months=12))
    )
    monthly_total_achats = (
        achats_data.annotate(month=TruncMonth("date_achat"))
        .values("month")
        .annotate(total_achats=Sum(F("quantite") * F("prix_unitaire_HT")))
    )

    # Calculate the month-over-month percentage change
    total_achats_values = [entry["total_achats"] for entry in monthly_total_achats]
    monthly_percentage_change = [0] + [
        (current - previous) / previous * 100
        for previous, current in zip(total_achats_values[:-1], total_achats_values[1:])
    ]

    # Get the top suppliers based on the total value of purchases
    top_fournisseurs = Fournisseur.objects.annotate(
        total_achats=Sum(F("achat__quantite") * F("achat__prix_unitaire_HT"))
    ).order_by("-total_achats")[:5]

    # Create a bar chart for monthly purchases
    df = pd.DataFrame(list(monthly_total_achats))
    plt.bar(df["month"], df["total_achats"])
    plt.title("Monthly Total Achats Over the Last 12 Months")
    plt.xlabel("Month")
    plt.ylabel("Total Achats")

    # Save the plot to a BytesIO object
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    # Convert the BytesIO object to base64 for embedding in HTML
    img_data = base64.b64encode(img_buffer.getvalue()).decode("utf-8")

    # Render the data in the template
    context = {
        "monthly_total_achats": monthly_total_achats,
        "monthly_percentage_change": monthly_percentage_change,
        "top_fournisseurs": top_fournisseurs,
        "chart_image": img_data,
    }

    return render(request, "dashboard.html", context)


##-------------------------YOUSRAAA

from audioop import reverse
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Sum, Q
from django.http import Http404
from django.contrib import messages
from django.db.models import Sum, F, Q
from django.db.models.functions import TruncMonth
from django.utils import timezone
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
from django.db import transaction

from .models import (
    Centre,
    Produit,
    Client,
    Fournisseur,
    Employe,
    PaiementCreditCentre,
    Paiement_E,
    Vente_Produit,
    stock_Produit,
)
from .forms import (
    CalculSalaireForm,
    CalculVentesNettesForm,
    DateDetailForm,
    FournisseurForm,
    PaiementEForm,
    CentreForm,
    ClientForm,
    EmployeForm,
    ProduitForm,
    Vente_ProduitForm,
    PaiementCreditFormC,
    RechercheVenteProduitForm,
    Add_Produit_StockForm,
    RechercheStockProduitForm,
)
from django.db import models


def home(request):
    if Centre.objects.count() == 0:
        create_centre()

    return render(request, "home.html")


def create_centre():
    Centre.objects.create(code="Code1", designation="Centre1")
    Centre.objects.create(code="Code2", designation="Centre2")
    Centre.objects.create(code="Code3", designation="Centre3")


def afficher_BD(request):
    produits = Produit.objects.all()
    centres = Centre.objects.all()
    clients = Client.objects.all()
    fournisseurs = Fournisseur.objects.all()
    employes = Employe.objects.all()
    # return render(request,"magasin.html",{"products":produits})
    return render(
        request,
        "magasin.html",
        {
            "produits": produits,
            "centres": centres,
            "clients": clients,
            "fournisseurs": fournisseurs,
            "employes": employes,
        },
    )


#   --------------- CREATION DES TABLE---------
def create_model(
    request,
    model_form,
):
    if request.method == "POST":
        form = model_form(request.POST)
        if form.is_valid():
            form.save()
            form = model_form()
            mssg = "element creer avec sucees"
            return redirect("magasin")
    else:
        form = model_form()
        mssg = "veillez remplir tous les champs !"
    return render(request, "inserer.html", {"form": form})


def create_client(request):
    return create_model(request, ClientForm)


def create_fournisseur(request):
    return create_model(request, FournisseurForm)


def create_produit(request):
    return create_model(request, ProduitForm)


def create_employe(request):
    return create_model(request, EmployeForm)


# ------------- MODIFICATION DES TABLE -------------------
def edit_BD(request, pk, model_form, model_name):
    model = model_name.objects.get(
        id=pk
    )  # récupérer l'instance de "commande" correspondante
    if request.method == "POST":
        form = model_form(request.POST, instance=model)
        # create new order (commande) instance from post data. This instance will
        # replace an existing one in the database (the cmd instance).
        if form.is_valid():
            form.save()
            return redirect("magasin")  # rediriger vers l’url: CmdList.
    else:
        form = model_form(
            instance=model
        )  # fournir une instance pré-remplie de formulaire
        return render(request, "editer.html", {"form": form})


def editer_centre(request, pk):
    return edit_BD(request, pk, CentreForm, Centre)


def editer_produit(request, pk):
    return edit_BD(request, pk, ProduitForm, Produit)


def editer_client(request, pk):
    return edit_BD(request, pk, ClientForm, Client)


def editer_fournisseur(request, pk):
    return edit_BD(request, pk, FournisseurForm, Fournisseur)


def editer_employe(request, pk):
    return edit_BD(request, pk, EmployeForm, Employe)


# ------------- SUPPRIMER DES TABLE -------------------
def delete_BD(request, model_name, pk):
    item = get_object_or_404(model_name, id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("magasin")

    return render(request, "supprimer.html", {"item": item})


def delete_fournisseur(request, pk):
    return delete_BD(request, Fournisseur, pk)


def delete_centre(request, pk):
    return delete_BD(request, Centre, pk)


def delete_client(request, pk):
    return delete_BD(request, Client, pk)


def delete_employe(request, pk):
    return delete_BD(request, Employe, pk)


def delete_produit(request, pk):
    return delete_BD(request, Produit, pk)


# ------------- DETAIL DES TABLE -------------------


def detail_employe(request, employe_id):
    employe = Employe.objects.get(id=employe_id)
    paiement_today = Paiement_E.objects.filter(
        employe=employe, date_paiement=timezone.now().date()
    ).first()
    if request.method == "POST":
        form = DateDetailForm(request.POST)
        if form.is_valid():
            date_detail = form.cleaned_data["date_detail"]

            # Récupérez les paiements précédents jusqu'à la date spécifiée
            paiements_precedents = Paiement_E.objects.filter(
                employe=employe, date_paiement__lt=date_detail
            )

            return render(
                request,
                "employe/employe.html",
                {
                    "employe": employe,
                    "details_employe": paiements_precedents,
                    "form": form,
                    "paiement_today": paiement_today,
                },
            )
    else:
        form = DateDetailForm()

    paiements = Paiement_E.objects.filter(employe=employe)
    return render(
        request,
        "employe/employe.html",
        {
            "employe": employe,
            "paiements": paiements,
            "form": form,
            "paiement_today": paiement_today,
        },
    )


def detail_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    ventes = Vente_Produit.objects.filter(client=client)

    context = {
        "client": client,
        "ventes": ventes,
    }

    return render(request, "detail_client.html", context)


def detail_centre(request, centre_id):
    centre = get_object_or_404(Centre, id=centre_id)
    employes = Employe.objects.filter(centre=centre)
    ventes = Vente_Produit.objects.filter(centre=centre)

    # Recuperer les ventes d'aujourd'hui
    today_ventes = Vente_Produit.objects.filter(
        centre=centre, date_vente=timezone.now().date()
    )

    # Le code des ventes et code employe
    vente_codes = [vente.code for vente in today_ventes]

    # Recuperer les employés payés aujourd'hui
    today_paiements = Paiement_E.objects.filter(
        employe__centre=centre, date_paiement=timezone.now().date()
    )

    # Le code des employés payés
    employee_codes = [paiement.employe.id for paiement in today_paiements]

    return render(
        request,
        "centre.html",
        {
            "centre": centre,
            "employes": employes,
            "ventes": ventes,
            "today_ventes": today_ventes,
            "vente_codes": vente_codes,
            "today_paiements": today_paiements,
            "employee_codes": employee_codes,
        },
    )


# ------------- MONEY EMPLOYE -------------------


def saisir_paiement(request, employe_id):
    employe = Employe.objects.get(id=employe_id)

    if request.method == "POST":
        form = PaiementEForm(request.POST, initial={"employe": employe})
        if form.is_valid():
            paiement = form.save(commit=False)
            paiement.employe = employe

            # Ensure that the date_paiement is set to the specific date chosen in the form
            paiement.date_paiement = form.cleaned_data["date_paiement"]

            # Check if a payment already exists for the employee on the specific date
            existing_paiement = Paiement_E.objects.filter(
                employe=employe, date_paiement=paiement.date_paiement
            ).first()

            if existing_paiement:
                # If the payment exists, update the amount
                existing_paiement.montant = paiement.montant
                existing_paiement.avance = paiement.avance
                existing_paiement.save()
            else:
                # Otherwise, create a new payment
                paiement.save()

            paiements = Paiement_E.objects.filter(employe=employe)
            return render(
                request,
                "employe/employe.html",
                {"employe": employe, "paiements": paiements, "form": form},
            )
    else:
        form = PaiementEForm(initial={"employe": employe})

    return render(
        request, "employe/saisir_paiement.html", {"employe": employe, "form": form}
    )


def calculer_salaire_entre_dates(employe, date_debut, date_fin, salaire_absence):
    # Obtenir tous les paiements de l'employé entre les deux dates
    paiements_employe = Paiement_E.objects.filter(
        employe=employe, date_paiement__range=(date_debut, date_fin)
    )

    # Initialiser le salaire total
    salaire_total = 0
    jours_absence = 0

    # Parcourir chaque paiement entre date_debut et date_fin
    for paiement in paiements_employe:
        # Vérifier si l'employé est absent pour ce paiement
        if paiement.absence:
            # Retenir le salaire d'absence pour chaque jour absent
            jours_absence += 1
            # Mettre montant et avance à 0
            paiement.montant = 0
            paiement.avance = 0
            paiement.save()
        else:
            # Ajouter le montant ajusté en fonction de l'avance
            salaire_total += paiement.montant - paiement.avance

    # Soustraire le salaire d'absence pour chaque jour d'absence
    if jours_absence > 0:
        salaire_total -= jours_absence * salaire_absence

    return salaire_total


def calcul_salaire(request, employe_id):
    employe = Employe.objects.get(id=employe_id)

    if request.method == "POST":
        form = CalculSalaireForm(request.POST, initial={"employe": employe})

        if form.is_valid():
            date_debut = form.cleaned_data["date_debut"]
            date_fin = form.cleaned_data["date_fin"]
            salaire_absence = form.cleaned_data["pourcentage_absence"]

            salaire = calculer_salaire_entre_dates(
                employe, date_debut, date_fin, salaire_absence
            )

            return render(
                request,
                "employe/resultat_salaire.html",
                {"employe": employe, "salaire": salaire},
            )
    else:
        form = CalculSalaireForm(initial={"employe": employe})

    return render(
        request,
        "employe/calcul_salaire.html",
        {"form": form, "employe": employe},
    )


def modify_absence(request, employe_id):
    employe = get_object_or_404(Employe, id=employe_id)

    # Get the latest Paiement_E instance for the employee, if it exists
    latest_paiement = Paiement_E.objects.filter(
        employe=employe, date_paiement=timezone.now().date()
    ).first()

    # If there's a latest_paiement and its date is today, update it; otherwise, create a new one
    if latest_paiement and latest_paiement.date_paiement == timezone.now().date():
        latest_paiement.absence = not latest_paiement.absence
        latest_paiement.montant = 0
        latest_paiement.avance = 0
        latest_paiement.save()
    else:
        # Create a new Paiement_E instance for today and set employe_id
        new_paiement = Paiement_E.objects.create(
            date_paiement=timezone.now(),
            employe=employe,
            absence=True,
            avance=0,
            montant=0,
        )

    return redirect("centre", centre_id=employe.centre.id)


# ------------- VENTE PRODUIT -------------------


def vendre_produit(request, centre_id):
    centre = get_object_or_404(Centre, id=centre_id)

    if request.method == "POST":
        form = Vente_ProduitForm(request.POST, initial={"centre": centre_id})
        if form.is_valid():
            vente_produit_instance = form.save(commit=False)
            vente_produit_instance.centre = centre

            # Set the date_vente field to the current date and time
            vente_produit_instance.date_vente = form.cleaned_data.get("date")

            vente_produit_instance.save()

            stock_entry = stock_Produit.objects.get(
                produit=vente_produit_instance.produit, centre=centre
            )

            if vente_produit_instance.quantite > stock_entry.quantite:
                messages.error(
                    request,
                    "La quantité demandée dépasse la quantité disponible en stock.",
                )
                return redirect("centre", centre_id=vente_produit_instance.centre.id)

            vente_produit_instance.montant_total = (
                vente_produit_instance.quantite * vente_produit_instance.prix_unitaire
            )

            vente_produit_instance.credit = (
                vente_produit_instance.montant_total
                - vente_produit_instance.montant_verse
            )

            vente_produit_instance.save()

            stock_entry.quantite -= vente_produit_instance.quantite
            stock_entry.save()

            request.session["selected_client_id"] = vente_produit_instance.client.id

            return redirect("centre", centre_id=vente_produit_instance.centre.id)

        else:
            # Form is not valid, you might want to handle this case or provide additional feedback
            messages.error(
                request,
                "Le formulaire n'est pas valide. Veuillez vérifier les données.",
            )

    else:
        form = Vente_ProduitForm(initial={"centre": centre_id})

    ventes = Vente_Produit.objects.all()
    return render(request, "vente/vendre.html", {"ventes": ventes, "form": form})


def reglement_credit_client(request, vente_id):
    vente_produit = Vente_Produit.objects.get(id=vente_id)

    if request.method == "POST":
        form = PaiementCreditFormC(request.POST)
        if form.is_valid():
            montant_paiement = form.cleaned_data["montant"]

            # Check if payment amount is greater than credit
            if montant_paiement > vente_produit.credit:
                return render(
                    request,
                    "vente/paiement_credit.html",
                    {
                        "centre_id": vente_produit.centre.id,
                        "form": form,
                        "vente_produit": vente_produit,
                        "error_message": "Le montant du paiement est supérieur au crédit restant.",
                    },
                )

            # Create a PaiementCredit instance
            paiement_credit = PaiementCreditCentre.objects.create(
                vente=vente_produit,
                centre=vente_produit.centre,
                montant=montant_paiement,
            )

            # Update sale's credit
            vente_produit.credit -= montant_paiement
            vente_produit.save()

            return redirect("centre", centre_id=vente_produit.centre.id)
    else:
        form = PaiementCreditFormC()

    return render(
        request,
        "vente/paiement_credit.html",
        {
            "centre_id": vente_produit.centre.id,
            "form": form,
            "vente_produit": vente_produit,
        },
    )


def Journal_Vente_Produit(request, centre_id):
    centre = get_object_or_404(Centre, id=centre_id)
    form = RechercheVenteProduitForm(request.GET)

    ventes = Vente_Produit.objects.filter(centre=centre)

    montant_total = sum((vente.montant_total or 0) for vente in ventes) - sum(
        (vente.credit or 0) for vente in ventes
    )

    if request.method == "GET":  # Assuming the form is submitted via POST
        if form.is_valid():
            # récupérer les valeurs du formulaire
            Recherche_Nom_Code = form.cleaned_data.get("Recherche_Nom_Code")

            date = form.cleaned_data.get("date")

            # filtrer les ventes sur 2 conditions
    if request.method == "GET" and form.is_valid():
        # récupérer les valeurs du formulaire
        Recherche_Nom_Code = form.cleaned_data.get("Recherche_Nom_Code")
        date = form.cleaned_data.get("date")

        # filtrer les ventes sur 2 conditions

        if Recherche_Nom_Code:
            name_filter = ventes.filter(client__nom__icontains=Recherche_Nom_Code)
            code_filter = ventes.filter(code__icontains=Recherche_Nom_Code)
            ventes = name_filter.union(code_filter)

        if date:
            ventes = ventes.filter(date_vente=date)

    return render(
        request,
        "vente/Journal_Vente_Produit.html",
        {
            "centre": centre,
            "centre_id": centre_id,
            "ventes": ventes,
            "form": form,
            "montant_total": montant_total,
        },
    )


def supprimer_vente(request, vente_id):
    vente = get_object_or_404(Vente_Produit, id=vente_id)

    if request.method == "POST":
        vente.delete()
        return redirect(
            "magasin"
        )  # Remplacez 'liste_ventes' par le nom de votre vue de liste des ventes

    context = {
        "vente": vente,
    }

    return render(request, "vente/supprimer_vente.html", context)


def stock_state(request, centre_id):
    centre = get_object_or_404(Centre, pk=centre_id)
    stock_entries = stock_Produit.objects.filter(centre=centre)

    # Handling the search form
    form = RechercheStockProduitForm(request.GET)

    if form.is_valid():
        # Retrieve the values entered in the search form
        search_term = form.cleaned_data.get("Recherceh_Nom_Code")

        # If a search term is provided, filter stock_entries based on the product code or designation
        if search_term:
            stock_entries = stock_entries.filter(
                Q(produit__designation__icontains=search_term)
            )

    return render(
        request,
        "vente/stock_state.html",
        {"stock_entries": stock_entries, "centre": centre, "form": form},
    )


def add_produit_to_stock(request, centre_id):
    centre = Centre.objects.get(id=centre_id)

    if request.method == "POST":
        form = Add_Produit_StockForm(request.POST)
        if form.is_valid():
            produit = form.cleaned_data["produit"]
            quantite = form.cleaned_data["quantite"]

            # Try to get the existing stock entry, or create a new one if it doesn't exist
            stock_entry, created = stock_Produit.objects.get_or_create(
                produit=produit,
                centre=centre,
                defaults={"quantite": quantite},  # Set the default value for quantite
            )

            # If the stock entry already exists, update the quantite field
            if not created:
                stock_entry.quantite += quantite
                stock_entry.save()

            return redirect("stock_state", centre_id=centre.id)
    else:
        form = Add_Produit_StockForm()

    return render(request, "vente/Produit.html", {"centre": centre, "form": form})


def calculer_ventes_nettes_entre_dates(centre, date_debut, date_fin):
    # Obtenir toutes les ventes entre les deux dates
    ventes = Vente_Produit.objects.filter(
        centre=centre, date_vente__range=(date_debut, date_fin)
    )

    # Initialiser le montant total des ventes nettes
    montant_ventes_nettes = 0

    # Parcourir chaque vente entre date_debut et date_fin
    for vente in ventes:
        # Ajouter le montant total ajusté en fonction du crédit
        montant_ventes_nettes += vente.montant_total - vente.credit

    return montant_ventes_nettes


def calcul_ventes_nettes(request, centre_id):
    centre = Centre.objects.get(pk=centre_id)

    if request.method == "POST":
        form = CalculVentesNettesForm(request.POST)

        if form.is_valid():
            date_debut = form.cleaned_data["date_debut"]
            date_fin = form.cleaned_data["date_fin"]

            ventes_nettes = calculer_ventes_nettes_entre_dates(
                centre, date_debut, date_fin
            )

            return render(
                request,
                "vente/resultat_ventes_nettes.html",
                {"ventes_nettes": ventes_nettes, "centre": centre, "form": form},
            )

    else:
        form = CalculVentesNettesForm()

    return render(
        request, "vente/calcul_ventes_nettes.html", {"form": form, "centre": centre}
    )


# ---------------------------SECTION 5 CENTRE --------------------------


def analyze_ventes(request):
    # Récupérer toutes les ventes pour les 12 derniers mois
    ventes_data = Vente_Produit.objects.filter(
        date_vente__gte=(timezone.now() - relativedelta(months=12))
    )

    # Calculer le total des ventes pour chaque mois
    monthly_total_ventes = (
        ventes_data.annotate(month=TruncMonth("date_vente"))
        .values("month")
        .annotate(total_ventes=Sum(F("quantite") * F("prix_unitaire")))
    )

    # Calculer le taux d'évolution de la valeur des ventes
    total_ventes_values = [entry["total_ventes"] for entry in monthly_total_ventes]
    monthly_percentage_change = [0] + [
        (current - previous) / previous * 100
        for previous, current in zip(total_ventes_values[:-1], total_ventes_values[1:])
    ]

    # Calculer le taux d'évolution du bénéfice (montant total versé)
    total_montant_verse = ventes_data.aggregate(
        total_montant_verse=Sum("montant_verse")
    )["total_montant_verse"]

    # Top clients - Best customers
    top_clients = Client.objects.annotate(
        total_achats=Sum(F("vente_produits__montant_total"))
    ).order_by("-total_achats")[:5]

    # Les produits Best-seller (par quantité)
    best_sellers = (
        ventes_data.values("produit__designation")
        .annotate(total_quantite=Sum("quantite"))
        .order_by("-total_quantite")[:5]
    )

    # Créer un graphique à barres pour les ventes mensuelles
    df = pd.DataFrame(list(monthly_total_ventes))
    plt.bar(df["month"], df["total_ventes"])
    plt.title("Ventes mensuelles au cours des 12 derniers mois")
    plt.xlabel("Mois")
    plt.ylabel("Total des ventes")

    # Enregistrer le graphique dans un objet BytesIO
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    # Convertir l'objet BytesIO en base64 pour l'intégrer dans HTML
    img_data = base64.b64encode(img_buffer.getvalue()).decode("utf-8")

    # Rendre les données dans le modèle
    context = {
        "monthly_total_ventes": monthly_total_ventes,
        "monthly_percentage_change": monthly_percentage_change,
        "total_montant_verse": total_montant_verse,
        "top_clients": top_clients,
        "best_sellers": best_sellers,
        "chart_image": img_data,
    }

    return render(request, "dashboard_ventes.html", context)
