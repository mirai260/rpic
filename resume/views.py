from django.shortcuts import render

def resumeSeance1(request):
	tab = []
	nombreImage = 8
	for k in range(nombreImage):
		tab.append("resume/seance1/" + str(k) + ".jpg")
	return render(request, 'resume/seance1.html', {"tab": tab})

def resumeSeance2(request):
	tab = []
	nombreImage = 9
	for k in range(nombreImage):
		tab.append("resume/seance2/" + str(k) + ".jpg")
	return render(request, 'resume/seance1.html', {"tab": tab})

# Create your views here.
