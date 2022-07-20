import math


def formula(n):
    respuesta = int((((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / (2 ** n * math.sqrt(5))))
    return respuesta

def imprimir_serie(n):
    if n < 0:
        return
    else:
        print(formula(n))
        return imprimir_serie(n-1)
        


def ingresar_longitud():

    try:
        print('Ingresa la longitud de la serie')
        long = int(input())
        imprimir_serie(long)
    except ValueError:
        print( 'No se ingreso un valor numerico' )


ingresar_longitud()