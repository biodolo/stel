'''
Created on 29/ott/2012

@author: titty


'''
import os
import StringIO

from xhtml2pdf import pisa

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template.context import Context
from django.utils.html import escape
from django.template import Context, loader
from django.http import HttpResponse

def home(request):
    t = loader.get_template('anagrafica/home.html')
    c = Context({
                 'lista': [0,1,2,3,4,5,6,7,8,9],
    })
    return HttpResponse(t.render(c))

def guarda(request,dato):
    t = loader.get_template('anagrafica/home.html')
    c = Context({
                 'lista': [0,1,2,3,4,5,6,7,8,9],
                 'dato':dato
    })
    return HttpResponse(t.render(c))


def fetch_resources(uri, rel):
    """
    Callback to allow xhtml2pdf/reportlab to retrieve Images,Stylesheets, etc.
    `uri` is the href attribute from the html link element.
    `rel` gives a relative path, but it's not used here.

    """
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT,
                            uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT,
                            uri.replace(settings.STATIC_URL, ""))
    else:
        path = os.path.join(settings.STATIC_ROOT,
                            uri.replace(settings.STATIC_URL, ""))

        if not os.path.isfile(path):
            path = os.path.join(settings.MEDIA_ROOT,
                                uri.replace(settings.MEDIA_URL, ""))

            #if not os.path.isfile(path):
            #    raise UnsupportedMediaPathException(
            #                        'media urls must start with %s or %s' % (
            #                        settings.MEDIA_ROOT, settings.STATIC_ROOT))

    return path


def generate_pdf(template_src, context_dict):
    """Function to render html template into a pdf file"""
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")),
                                            dest=result,
                                            encoding='UTF-8',
                                            link_callback=fetch_resources)
    if not pdf.err:
        response = HttpResponse(result.getvalue(),
                                                    mimetype='application/pdf')

        return response

    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


def download_pdf(request):
    """Build briefing packages format and export as HTML and PDF."""
    response = HttpResponse(content_type='application/pdf')
    return generate_pdf('xhtml2pdf.html', {'file_object':response})
