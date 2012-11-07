'''
Created on 01/nov/2012

@author: titty
'''
from models import *
from django.contrib import admin

admin.site.register(Apparecchio)
admin.site.register(Operatore)

class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    search_fields = ('cognome','nome','citta')
    list_display = ('cognome','nome','email','telefono','cellulare','citta')
    fieldsets = (
               (None, {
                       'fields' : ('cognome', 'nome', 'email')
                       }),
               ('Recapito', {
                'fields' : ('citta', 'indirizzo', 'telefono', 'cellulare')
                })
               )


admin.site.register(Cliente, ClienteAdmin)

class SchedaRitiroAdmin(admin.ModelAdmin):
    class Media:
        js=['/js/toggle_filter.js','/js/scheda_ritiro.js']
        
    model = SchedaRitiro
    search_fields = ('utente__cognome', '=progressivo')
    list_filter = ('ritirato_da__nome','apparecchio__tipo','apparecchio__marca','apparecchio__modello','apparecchio',)
    list_display = ('progressivo','apparecchio', 'utente', 'data_ritiro', 'ritirato_da')
    raw_id_fields = ('apparecchio','utente')
    
    
        
admin.site.register(SchedaRitiro, SchedaRitiroAdmin)
