from django.shortcuts import render, redirect
from .forms import QueteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .models import Quete
from home.views import hasNotPerm


@permission_required('quetes.add_quete', login_url='/hasNotPerm')
def creationQuete(request):
    form = QueteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(voirQuetes)
    return render(request, 'quetes/creationQuete.html', locals())


@permission_required('quetes.change_quete', login_url='/hasNotPerm')
def modifierQuete(request, id_quete):
    quete = Quete.objects.get(id = id_quete)
    print(quete.participants.all())
    if request.method == "GET":
        form = QueteForm(instance = quete)
    elif request.method == "POST":
        form = QueteForm(request.POST, instance = quete)
        if form.is_valid():
            form.save()
            return redirect(voirQuetes)
    return render(request, 'quetes/modifierQuete.html', locals())


@login_required()
def modifierParticipation(request, id_quete):
    user = request.user
    quete = Quete.objects.get(id = id_quete)
    if (user in quete.participants.all()):
        quete.participants.remove(user)
    else:
        quete.participants.add(user)
    return redirect(voirQuetes)


@login_required()
def voirQuetes(request):
    user = request.user
    if user.has_perm("quetes.voirQuetes"):
        listeQuetesFutures = Quete.objects.filter(etat = "future")
        listeQuetesEnCours = Quete.objects.filter(etat = "enCours")
        listeQuetesPassees = Quete.objects.filter(etat = "terminee")
    else:
        listeQuetesFutures = Quete.objects.filter(etat = "future", visible = True)
        listeQuetesEnCours = Quete.objects.filter(etat = "enCours", visible = True)
        listeQuetesPassees = Quete.objects.filter(etat = "terminee", visible = True)
    if user.has_perm("quetes.change_quete"):
        peutModifier = True
    if user.has_perm("quetes.add_quete"):
        peutCreer = True
    return render(request, 'quetes/voirQuetes.html', locals())


@login_required()
def afficherQuete(request, id_quete):
    user = request.user
    quete = Quete.objects.get(id = id_quete)
    if quete.visible:
        return render(request, 'quetes/afficherQuete.html', locals())
    else:
        if user.has_perm("quetes.voirQuetes"):
            return render(request, 'quetes/afficherQuete.html', locals())
        else:
            return redirect(hasNotPerm)


















