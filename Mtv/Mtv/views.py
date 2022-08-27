from django.http import HttpResponse
from django.template import Template, Context

def probar_template(request):
    with open (r'C:\Users\Francisco\Desktop\Python\Trabajos\Django\MVT-Lima\MTV\Templates\templates.html') as archivo:
        
        plantilla = Template(archivo.read())
    
    contexto = Context()

    documento_html  = plantilla.render(contexto)

    return HttpResponse(documento_html)