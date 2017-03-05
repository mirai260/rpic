from django.shortcuts import render, redirect
from .forms import BackgroundForm
from .models import Background
from django.contrib.auth.decorators import login_required



@login_required()
def creationLore(request):
    form = BackgroundForm(request.POST or None)
    creation = False
    if form.is_valid():
        creation = True
        form.save()
    return render(request, 'background/creationLore.html', locals())


def stories(request):
    liste = Background.objects.all
    return render(request, 'background/stories.html', locals())

def consulterLore(request,id):
    lore = Background.objects.get(id=id)
    return render(request, 'background/consulterLore.html', locals())
