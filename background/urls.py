from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^creationLore$', views.creationLore, name = "creationLore"),
	url(r'^stories$', views.stories, name = "stories"),
	url(r'^consulterLore/(\d+)$', views.consulterLore, name = "consulterLore"),
]