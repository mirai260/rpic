from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.rpicHomep, name = 'rpicHomep'),
	url(r'^univers1$', views.univers1, name = 'univers1'),
	url(r'^contact$', views.contact, name = 'contact'),
	url(r'^membres$', views.membres, name = 'membres')
]