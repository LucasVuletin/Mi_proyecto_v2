from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenidos a mi pagina django</h1>')

def plantilla(request):

    template = loader.get_template('plantilla.html')

    datos = {
        'lista': ['primero', 'segundo', 'tercero'],
        'nombre': 'Lucas' 
    }

    plantilla_generada=template.render(datos)

    return HttpResponse(plantilla_generada)    