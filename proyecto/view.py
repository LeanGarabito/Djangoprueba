from django.http import HttpResponse 
from datetime import datetime
from django.template import Template, Context



def Inicio(request):
    return HttpResponse("Hola mundo")


def saludo2(request):
    return HttpResponse("<br> <br> Esta es la segunda vista ")

#Dia de hoy con datetime.now()
def Dia(request):
    dia = datetime.now()
    
    archivoTexto = f"el dia de hoy es: {dia}"
    
    return HttpResponse(archivoTexto)




def probandoTemplate(self):
    
    miHtml = open("C:/Users/jigwo/Desktop/Estudios/DjandoPrueba/proyecto/plantillas/template1.html")
    
    plantilla = Template(miHtml.read())
    
    miHtml.close()
    
    miContexto = Context()
    
    documento = plantilla.render(miContexto)
    
    return HttpResponse(documento)
    
    
    