from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^creationQuete$', views.creationQuete, name = "creationQuete"),
    url(r'^voirQuetes$', views.voirQuetes, name = "voirQuetes"),
    url(r'^modifierQuete/(\d+)$', views.modifierQuete, name = "modifierQuete"),
	url(r'^modifierParticipation/(\d+)$', views.modifierParticipation, name = "modifierParticipation"),
	url(r'^afficherQuete/(\d+)$', views.afficherQuete, name = "afficherQuete"),
]