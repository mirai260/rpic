from django.shortcuts import render
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
	return render(request, 'personnages/creationPerso.html', locals())

@login_required()
def creationFichePerso(request):
	form = FichePersoForm(request.POST or None)
	user = request.user
	listePerso = user.perso_set.all()
	id_perso = request.POST.get('perso',True)
	if form.is_valid() and id_perso != True:
	
		nom = form.cleaned_data['nom']
		hp = form.cleaned_data['hp']
		mana = form.cleaned_data['mana']
		po = form.cleaned_data['po']
		traits = form.cleaned_data['traits']
		competences = form.cleaned_data['competences']
		sorts = form.cleaned_data['sorts']
		items = form.cleaned_data['items']
		descriptif = form.cleaned_data['descriptif']
		perso = Perso.objects.get(id = id_perso)
		
		fichePerso = FichePerso(nom = nom, hp = hp, mana = mana, po = po, traits = traits, competences = competences, sorts = sorts, items = items, descriptif = descriptif, perso = perso)
		fichePerso.save()
		creation = True
	return render(request, 'personnages/creationFichePerso.html', locals())
		
