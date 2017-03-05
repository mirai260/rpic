from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^creationPerso$', views.creationPerso, name = "creationPerso"),
	url(r'^creationFichePerso$', views.creationFichePerso, name = "creationFichePerso"),
	url(r'^afficherPerso$', views.afficherPerso, name = "afficherPerso"),
	url(r'^modifierFichePerso/(\d+)$', views.modifierFichePerso, name='modifierFichePerso'),
	url(r'^modifierPerso/(\d+)$', views.modifierPerso, name='modifierPerso'),
]