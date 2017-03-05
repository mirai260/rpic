from django.contrib import admin
from .models import Item, Vendeur, Offre




class ItemAdmin(admin.ModelAdmin):
   list_display   = ('nom', 'description')


admin.site.register(Item, ItemAdmin)
admin.site.register(Vendeur)
admin.site.register(Offre)