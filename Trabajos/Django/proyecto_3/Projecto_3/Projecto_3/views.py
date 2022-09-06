from importlib.resources import open_binary
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def probar_template(request):
    with open(r"C:\Users\Francisco\Desktop\Python\Trabajos\Django\proyecto_3\Projecto_3\Projecto_3\plantillas\plantilla1.html") as archivo:
        plantilla = Template(archivo.read())

    contexto = Context() 

    documento_html = plantilla.render(contexto)


    return HttpResponse(documento_html)