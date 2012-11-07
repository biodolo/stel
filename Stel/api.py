'''
Created on 07/nov/2012

@author: titty
'''
import sys, traceback
from django.http import HttpResponse
from django.core import serializers
from anagrafica.models import *

def get_all(request,**params):
    if request.user.is_anonymous():
        return HttpResponse(status=403)
    try:
        qs = eval('%(classe)s.objects.all().filter(%(campo)s=\'%(valore)s\')' % params)
        return HttpResponse(serializers.serialize('json',qs),'application/javascript')
    except:
        traceback.print_exc()
        return HttpResponse(status=500)

def get_elem(request,**params):
    if request.user.is_anonymous():
        return HttpResponse(status=403)
    try:
        qs = eval('%(classe)s.objects.all().filter(pk=\'%(id)s\')' % params)[0]
        return HttpResponse(serializers.serialize('json',qs),'application/javascript')
    except:
        traceback.print_exc()
        return HttpResponse(status=500)

def get_str(request,**params):
    if request.user.is_anonymous():
        return HttpResponse(status=403)
    try:
        qs = eval('%(classe)s.objects.all().filter(pk=\'%(id)s\')' % params)[0]
        return HttpResponse('%s' % qs,'text/plain')
    except:
        traceback.print_exc()
        return HttpResponse(status=500)

