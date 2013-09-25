from django.contrib import admin
from models import Avocat, Assistant, Client, Adversaire, PartieAdverse, Dossier

class DossierAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('client', 'partie_adverse', 'adversaire', 'date_ouverture', 'echeance')
    search_fields = ['client__name', 'client__first_name', 'adversaire__name']

admin.site.register(Avocat)
admin.site.register(Assistant)
admin.site.register(Client)
admin.site.register(Adversaire)
admin.site.register(PartieAdverse)
admin.site.register(Dossier, DossierAdmin)
