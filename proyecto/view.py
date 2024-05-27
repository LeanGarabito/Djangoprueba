from django.http import HttpResponse 
from datetime import datetime




def Inicio(request):
    return HttpResponse("Hola mundo")


def saludo2(request):
    return HttpResponse("<br> <br> Esta es la segunda vista ")

#Dia de hoy con datetime.now()
def Dia(request):
    dia = datetime.now()
    
    archivoTexto = f"el dia de hoy es:<br> {dia}"
    
    return HttpResponse(archivoTexto)