from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ConnexionForm, InscriptionForm, ProfilForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .models import Profil
from django.contrib.auth.decorators import login_required
from personnages.models import Perso



def connexion(request):
	next = request.GET.get('next', False)
	if next != False:
		url = reverse(connexion) + "?next="+next
	else:
		url = reverse(connexion)
	error = False
	if request.method == "POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)

			if user:
				login(request, user)  # nous connectons l'utilisateur
				if next != False:
					return redirect(next)
				else:
				    return redirect('rpicHomep')
			else:
				error = True
	else:
		form = ConnexionForm()
	return render(request, 'user/connexion.html', locals())


def inscription(request):
	form = InscriptionForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		email = form.cleaned_data['email']
		nom = form.cleaned_data['nom']
		prenom = form.cleaned_data['prenom']
		inscrit = True
		user = User.objects.create_user(username = username, password = password)
		profil = Profil(email = email, nom = nom, prenom = prenom, user = user)
		profil.save()
	return render(request, 'user/inscription.html', locals())


def deconnexion(request):
	logout(request)
	return redirect('rpicHomep')


@login_required()
def afficherProfil(request):
    user = request.user
    profil = user.profil
    return render(request, 'user/afficherProfil.html', locals())

@login_required()
def modifierProfil(request):
    user = request.user
    profil = user.profil

    if request.method == 'GET':
        form = ProfilForm(instance = profil)

    elif request.method == 'POST':
        form = ProfilForm(request.POST, instance = profil)
        id_perso = request.POST.get('perso', False)
        if form.is_valid():
            profil = form.save(commit=False)
            if id_perso != 'None':
                profil.personnagePrincipal = Perso.objects.get(id = id_perso)
            profil.save()
            return redirect(afficherProfil)

    listePerso = user.perso_set.all()
    perso = profil.personnagePrincipal

    return render(request, 'user/modifierProfil.html', locals())


