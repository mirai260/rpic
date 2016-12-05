from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def univers1(request):
	return render (request, 'home/Univers-1.html')
	
def rpicHomep(request):
	user = request.user
	return render (request, 'home/RPIC homep.html', {"user": user})

@login_required()
def membres(request):
	return render(request, 'home/Membres.html')
	
def contact(request):
	return render(request, 'home/Contact.html')

# Create your views here.
