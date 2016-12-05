from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^creationPerso$', views.creationPerso, name = "creationPerso"),
	url(r'^creationFichePerso$', views.creationFichePerso, name = "creationFichePerso")
]