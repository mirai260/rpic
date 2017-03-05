from django.shortcuts import render, HttpResponse
#from django.contrib.auth.decorators import login_required
from personnages.models import Perso
from django.contrib.auth.models import User, Group


def univers1(request):
	return render (request, 'home/Univers-1.html')


def rpicHomep(request):
	user = request.user
	news = ["voirQuetes"]
	return render (request, 'home/RPIC homep.html', locals())


def membres(request):
    listeMJ = []
    liste = []
    for user in User.objects.all():
        test = False
        for g in user.groups.all():
            if g.name == "MJ":
                test = True
        if test:
            listeMJ.append(user)
        else:
            liste.append(user)
    return render(request, 'home/Membres.html', locals())


def contact(request):
	return render(request, 'home/Contact.html')


def index(request):
    tab = ["rpicHomep", "afficherProfil", "afficherPerso", "voirQuetes", "stories", "resumeSeance1", "resumeSeance2"]
    return render(request, 'home/index.html', locals())

def hasNotPerm(request):
    return render(request, 'home/hasNotPerm.html')


def test(request):
    liste = User.objects.all()
    texte = ""
    for user in liste:
        texte += str(user.id) + " : " + str(user.username) + "<br>"
    return HttpResponse(texte)

def idees(request):
    return render(request, 'home/idees.html')

# Create your views here.
