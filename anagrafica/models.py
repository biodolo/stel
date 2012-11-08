'''
Created on 29/ott/2012

@author: titty
'''

from django.db import models
from django.utils.datetime_safe import datetime
import random

TIPO_PROVA_ACQUISTO = (
        ('sc', 'Scontrino'),
        ('rf', 'Ricevuta Fiscale'),
        ('ft', 'Fattura'),
        ('dt', 'Documento di Trasporto'),
        ('ap', 'Autorizzazione del Produttore'),
        )

class Operatore(models.Model):
    nome = models.CharField( max_length = 100)
    utente = models.ForeignKey('auth.User', related_name='+') 
    
    
    def __unicode__(self):
        return self.nome
    
class Cliente(models.Model):
    cognome = models.CharField(max_length = 100)
    nome = models.CharField(max_length = 100)
    citta = models.CharField(max_length = 100)
    indirizzo = models.TextField(blank=True,null=True)
    telefono = models.CharField(max_length = 20)
    cellulare = models.CharField(max_length = 20,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    note = models.TextField(blank=True,null=True)
    
    def __unicode__(self):
        return '%s %s %s' % (self.cognome,self.nome,self.email)    
        
class Apparecchio(models.Model):
    tipo = models.CharField(max_length = 100)
    marca = models.CharField(max_length = 100)
    modello = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return '%s %s %s' % (self.tipo,self.marca,self.modello)    
    

random.seed()

def rnd():
    print 'random'
    return random.randint(1,1000000)



class SchedaRitiro(models.Model):
    progressivo = models.IntegerField(default = rnd)
    #progressivo = models.AutoField(primary_key=False)
    data_ritiro = models.DateTimeField(default = datetime.now)
    apparecchio = models.ForeignKey('Apparecchio', related_name='+') 
    seriale = models.CharField(max_length=100, blank=True,null=True)
    utente = models.ForeignKey('Cliente', related_name='+')
    garanzia = models.BooleanField()
    data_acquisto = models.DateField(blank=True,null=True)
    tipo_prova_acquisto = models.CharField(max_length = 2, choices = TIPO_PROVA_ACQUISTO,blank=True,null=True)
    difetto_dichiarato = models.TextField()
    accessori_corredo = models.CharField(max_length = 100,blank=True,null=True)
    acquisizione_garanzia = models.BooleanField()
    note = models.TextField(blank=True,null=True)
    ritirato_da = models.ForeignKey('Operatore', related_name='+') 
    preventivo_ok = models.BooleanField ()
    importo_preventivo = models.FloatField(blank=True,null=True)
    acconto = models.FloatField(blank=True,null=True)
    scontrino_acconto = models.CharField(max_length = 50, blank=True,null=True)
    riconsegnato_da = models.ForeignKey('Operatore',blank=True,null=True)
    data_riconsegna = models.DateField(blank=True,null=True)
    difetto_riscontrato = models.TextField(blank=True,null=True)
    costo_riparazione = models.FloatField(blank=True,null=True)
    
    def __unicode__(self):
        return '%s - %s' % (self.progressivo,self.data_ritiro)
    
    def save(self, force_insert=False, force_update=False, using=None):
        print 'save'
        super(SchedaRitiro,self).save(force_insert, force_update, using)
    
    