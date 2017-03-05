from django.shortcuts import render, redirect
from .models import Item, Offre
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


@login_required()
def voirItems(request):
    listeItems = Item.objects.all()
    return render(request, 'items/voirItems.html', locals())




@permission_required('items.add_items', login_url='/hasNotPerm')
def creationItem(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(voirItems)
    return render(request, 'items/creationItem.html', locals())


@login_required()
def magasin(request):
    listeOffres = Offre.objects.all()
    return render(request, 'items/magasin.html', locals())
