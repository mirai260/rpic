from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ConnexionForm, InscriptionForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


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
				error = True		
	else:
		form = ConnexionForm()
	return render(request, 'user/connexion.html', locals())
	
	
def inscription(request):
	form = InscriptionForm(request.POST or None)
	if form.is_valid(): 
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		inscrit = True
		User.objects.create_user(username, email, password)
	return render(request, 'user/inscription.html', locals())

	
def deconnexion(request):
	logout(request)
	return redirect('rpicHomep')

