from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message
from django.contrib.auth.decorators import login_required


def newChat(request):
    print(request.POST)
    form = MessageForm(request.POST or None)
    if form.is_valid():
        texte = form.cleaned_data['texte']
        user = request.user
        message = Message(texte = texte, user = user)
        message.save()
        envoi = True
    return render(request, 'chat/chat.html', locals())


def chatFrame(request):
    liste = Message.objects.all().order_by('date').reverse()
    return render(request, 'chat/chatFrame.html', locals())


@login_required()
def chat(request):
    return render(request, 'chat/pageChat.html')


@login_required()
def resetChat(request):
    if request.user.is_superuser:
        tab = Message.objects.all()
        for message in tab:
            message.delete()
    return redirect(newChat)
