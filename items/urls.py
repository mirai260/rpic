from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^creationItem$', views.creationItem, name = "creationItem"),
	url(r'^voirItems$', views.voirItems, name = "voirItems"),
	url(r'^magasin$', views.magasin, name = 'magasin'),
]
