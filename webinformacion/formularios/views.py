from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "paginas/index.html")

def ejemplo(request):
    return render(request, "paginas/ejemplo.html")

def saludo(request):
    # Cuando tenemos un Post es obligatorio preguntar si traemos parametros
    if ('cajanombre' in request.POST):
        dato = request.POST["cajanombre"]
        informacion = {
                "nombre": dato
        }
        return render(request, "paginas/saludo.html", informacion)
    else:
        return render(request, "paginas/saludo.html")

def sumarnumeros(request):
    # Cuando tenemos un Post es obligatorio preguntar si traemos parametros
    if (('cajanum1' in request.POST) and ('cajanum2' in request.POST)):
        suma = int(request.POST["cajanum1"]) + int(request.POST["cajanum2"])
        informacion = {
                "resultado": suma
        }
        return render(request, "paginas/sumarnumeros.html", informacion)
    else:
        return render(request, "paginas/sumarnumeros.html")
    
def parimpar(request):
    # Cuando tenemos un Post es obligatorio preguntar si traemos parametros
    if ('cajanum' in request.POST):
        if ((int(request.POST["cajanum"])%2) != 0):
            resultado = "IMPAR"
        else:
            resultado = "PAR" 
        numero = int(request.POST["cajanum"])           
        informacion = {
                "resultado": resultado,
                "numero"   : numero 
        }
        return render(request, "paginas/parimpar.html", informacion)
    else:
        return render(request, "paginas/parimpar.html")
    
def collatz(request):
    if ('cajanumero' in request.POST):
        listanumeros = []
        numero = int(request.POST["cajanumero"])
        while (numero != 1):
            if (numero % 2 == 0):
                numero = numero / 2
            else:
                numero = numero * 3 + 1
            listanumeros.append(numero)
            
        informacion = {
            "numeros" : listanumeros
            }
        return render(request, "paginas/collatz.html", informacion)        
    else:    
        return render(request, "paginas/collatz.html")
        