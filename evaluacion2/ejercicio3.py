# Repositorio https://github.com/JesusMirandaEspino/Programacion_funcional

def determinar_edad(edad):

    if edad < 0:
        print( 'Edad incorrecta, numero negativo' )
    elif 0 <= edad < 18:
        print( 'Menor de edad' )
    elif 18 <= edad < 65:
        print( 'Mayor de edad' )
    else:
        print( '“Tercera edad”' )

def ingresa_edad():
    try:
        print('Ingresa Tu edad')
        edad = int(input())
        determinar_edad(edad)
    except ValueError:
        print( 'No se ingreso una edad correcta' )

ingresa_edad()
