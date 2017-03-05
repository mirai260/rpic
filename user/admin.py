from django.contrib import admin
from .models import Profil



class ProfilAdmin(admin.ModelAdmin):
   list_display   = ('user', 'personnagePrincipal', 'prenom', 'nom', 'email')
   list_filter    = ('user', 'personnagePrincipal', 'prenom', 'nom', 'email')
   ordering       = ('user', 'personnagePrincipal', 'prenom', 'nom', 'email')
   search_fields  = ('user', 'personnagePrincipal', 'prenom', 'nom', 'email')

admin.site.register(Profil, ProfilAdmin)



