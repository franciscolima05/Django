from importlib.resources import open_binary
from django.http import HttpResponse
from django.template import Template, context
from datetime import datetime

def probar_template(request):
    with open("C:\Users\Francisco\Desktop\Python\Trabajos\Django\proyecto_3\Projecto_3\Projecto_3\plantillas\plantilla1.html") as archivo:
        plantilla = Template(archivo.read())

    contexto = context() 

    documento_html = plantilla.render(contexto)


    return HttpResponse(documento_html)