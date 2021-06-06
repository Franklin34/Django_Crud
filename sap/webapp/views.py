from django.http import HttpResponse
from django.shortcuts import render
from personas.models import Persona

# Create your views here.
def bienvenido(request):
    no_personas =  Persona.objects.count() #Cantidad de Registros
    #personas = Persona.objects.all() #Devuelve todas las personas
    personas = Persona.objects.order_by('id') #Devuelve todas las personas

    return render(request,'bienvenido.html', {'no_personas':no_personas,'personas':personas})

