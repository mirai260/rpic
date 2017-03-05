from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^chat$', views.chat, name = "chat"),
    url(r'^chatFrame$', views.chatFrame, name = "chatFrame"),
    url(r'^newChat$', views.newChat, name="newChat"),
    url(r'^resetChat$', views.resetChat, name="resetChat"),
]