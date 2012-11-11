'''
Created on 01/nov/2012

@author: titty
'''
from models import *
from django.contrib import admin

class ReadonlyTabularInline(admin.TabularInline):
    can_delete = False
    extra = 0
    editable_fields = []
    
    def get_readonly_fields(self, request, obj=None):
        fields = []
        for field in self.model._meta.get_all_field_names():
            if (not field == 'id'):
                if (field not in self.editable_fields):
                    fields.append(field)
        return fields
    
    def has_add_permission(self, request):
        return False
    
admin.site.register(Apparecchio)
admin.site.register(Operatore)

class SchedaRitiroAdmin(admin.ModelAdmin):
    class Media:
        js=['/js/scheda_ritiro.js']
        
    model = SchedaRitiro
    search_fields = ('utente__cognome', '=progressivo')
    list_filter = ('ritirato_da__nome','apparecchio__tipo','apparecchio__marca','apparecchio__modello','apparecchio',)
    list_display = ('progressivo','apparecchio', 'utente', 'data_ritiro', 'ritirato_da')
    raw_id_fields = ('apparecchio','utente')
    
class SchedaRitiroInline(ReadonlyTabularInline):    
    model=SchedaRitiro
    fieldsets = (
            (None, {
                'fields' : ('progressivo','apparecchio', 'utente', 'data_ritiro', 'garanzia', 'ritirato_da')
            }),
            )
        
admin.site.register(SchedaRitiro, SchedaRitiroAdmin)
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
    inlines = [SchedaRitiroInline]


admin.site.register(Cliente, ClienteAdmin)


