from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def resumeSeance1(request):
	tab = []
	nombreImage = 8
	for k in range(1, nombreImage+1):
		tab.append("resume/seance1/" + str(k) + ".jpg")
	return render(request, 'resume/seance1.html', {"tab": tab})


@login_required()
def resumeSeance2(request):
	tab = []
	nombreImage = 9
	for k in range(1,nombreImage+1):
		tab.append("resume/seance2/" + str(k) + ".jpg")
	return render(request, 'resume/seance1.html', {"tab": tab})


