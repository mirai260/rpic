from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^resumeSeance1$', views.resumeSeance1, name = 'resumeSeance1'),
	url(r'^resumeSeance2$', views.resumeSeance2, name = 'resumeSeance2'),
]

