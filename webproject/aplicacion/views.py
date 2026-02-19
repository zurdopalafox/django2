from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Creamos metodos para dibujar las vistas
def index(request):
    return render(request, "paginas/index.html")

def prueba(request):
    return render(request, "paginas/prueba.html")

def peliculas(request):
    return render(request, "paginas/peliculas.html")

def futbol(request):
    informacion = {
        "varequipo" : "Real Madrid"
    }
    return render(request, "paginas/futbol.html", informacion)

def nombres(request):
    listadonombres = ["Carlos","Ricardo","Boni","Adrian","Rubén"]

    listapersonas = [
        {"nombre": "Julio", "edad": 26},
        {"nombre": "Lucia", "edad": 33},
        {"nombre": "Jessica", "edad": 50}
    ]
    # Debemos enviarlo siempre como diccionario
    informacion = {
        "listanombres":  listadonombres,
        "listapersonas": listapersonas
    }
    return render(request, "paginas/nombres.html", informacion)

def mascotas(request):
    listamascotas = [
        {"nombre": "Candy", "raza": "Pastor", "edad": 10},
        {"nombre": "Rosco", "raza": "Cocker Spaniel", "edad": 11},
        {"nombre": "Piplo", "raza": "Rotweiller", "edad": 12}
    ]
    # Debemos enviarlo siempre como diccionario
    informacion = {
        "listamascotas": listamascotas
    }
    return render(request, "paginas/mascotas.html", informacion)

def colores(request):
    #Comprobamos si recibimos el parametro micolor o no
    if ('micolor' in request.GET):
    # La información viene en la URL mediante GET
       colorRecibido = request.GET["micolor"]
    # Ya tenemos un color, que hacemos ahora con el ??
    #Devolvemos el color para dibujarlo
    else:
        colorRecibido = "No recibí parametro de Color !!!"
    
    informacion = {
           "color": colorRecibido
       }
    return render(request, "paginas/colores.html", informacion)
