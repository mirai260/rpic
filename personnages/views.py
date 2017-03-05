from django.shortcuts import render, redirect
from .forms import PersoForm, FichePersoForm
from .models import Perso, FichePerso
from django.contrib.auth.decorators import login_required



@login_required()
def creationPerso(request):
	form = PersoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		nom = form.cleaned_data['nom']
		image = form.cleaned_data['image']
		user = request.user
		perso = Perso(nom = nom, image = image, user = user)
		perso.save()
		creation = True
		return redirect(afficherPerso)
	return render(request, 'personnages/creationPerso.html', locals())



@login_required()
def creationFichePerso(request):
    form = FichePersoForm(request.POST or None)
    user = request.user
    listePerso = user.perso_set.all()
    id_perso = request.POST.get('perso',False)
    if (form.is_valid() and id_perso != False):
        fichePerso = form.save(commit=False)
        fichePerso.perso = Perso.objects.get(id = id_perso)
        fichePerso.save()
        return redirect(afficherPerso)
    return render(request, 'personnages/creationFichePerso.html', locals())


@login_required()
def modifierPerso(request, id_perso):
    perso = Perso.objects.get(id = id_perso)
    if request.method == "GET":
        form = PersoForm(instance = perso)
    elif request.method == "POST":
        form = PersoForm(request.POST, request.FILES, instance = perso)
        if form.is_valid():
            form.save()
            return redirect(afficherPerso)
    return render(request, 'personnages/modifierPerso.html', locals())


@login_required()
def modifierFichePerso(request, id_fichePerso):
    fichePerso = FichePerso.objects.get(id = id_fichePerso)
    if request.method == "GET":
        form = FichePersoForm(instance = fichePerso)
    elif request.method == "POST":
        form = FichePersoForm(request.POST, instance = fichePerso)
        if form.is_valid():
            form.save()
            return redirect(afficherPerso)
    return render(request, 'personnages/modifierFichePerso.html', locals())



@login_required()
def afficherPerso(request):
    user = request.user
    if user.has_perm("personnages.voirFichePerso"):
        listePerso = Perso.objects.all()
    else:
        listePerso = user.perso_set.all()
    id_perso = request.POST.get('perso', "None")
    id_fichePerso = request.POST.get('fichePerso', "None")
    if id_fichePerso != "None":
        fichePerso = FichePerso.objects.get(id = id_fichePerso)
        perso = fichePerso.perso
        listeFiche = perso.ficheperso_set.all()
        afficher = True
        listeItems = fichePerso.item.all()
        return render(request, 'personnages/afficherPerso.html', locals())
    elif id_perso != "None":
        perso = Perso.objects.get(id = id_perso)
        listeFiche = perso.ficheperso_set.all()
        choisirFiche = True
        return render(request, 'personnages/afficherPerso.html', locals())
    else:
        choisirPerso = True
        return render(request, 'personnages/afficherPerso.html', locals())









