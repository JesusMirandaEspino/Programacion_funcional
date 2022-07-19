
def sumar(num1, num2):
    try:
        suma = num1 + num2
        return "el resultado de la suma es: ", suma
    except TypeError as error:
        return 'No se puede sumar un tipo entero con un tipo string', error

def restar(num1, num2):
    try:
        resta = num1 - num2
        return "el resultado de la resta es: ", resta
    except TypeError as error:
        return 'No se puede restar un tipo entero con un tipo string', error


def multiplicar(num1, num2):
    try:
        multiplicacion = num1 * num2
        return "el resultado de la multiplicación es: ", multiplicacion
    except TypeError as error:
        return 'No se puede multlipicar un tipo entero con un tipo string, puede existir algun error, favor de verificar', error
            

def dividir(num1, num2):
    try:
        division = num1 / num2
        return "el resultado de la división es: ", division
    except (ZeroDivisionError, TypeError) as error:
        return 'No se puede dividir entre cero, o  hacer una division con un string incluido, o Intenta dividir entre un numero mayor a cero', error

def residuo(num1, num2):
    try:
        residuo_r = int(num1) % int(num2)
        return "el resultado del Residuo es: ", residuo_r
    except (ZeroDivisionError, TypeError) as error:
        return 'Ha ocurrido un error, favor de validar', error


def potencia(num1, num2):
    try:
        potencia_r = num1 ** num2
        return "el resultado de la potencia es: ", potencia_r
    except  TypeError as error:
        return 'Ha ocurrido un error, favor de validar', error


def ingresar_numero_1():

    try:
        return float(input("ingrese el primer numero: "))
    except ValueError as error:
        return 'No se puede usar un tipo string. para realizar una operacion', error


def ingresar_numero_2():

    try:
        return float(input("ingrese el segundo numero: "))
    except ValueError as error:
        return 'No se puede usar un tipo string. para realizar una operacion, Si devuelve un resultado con string, favor de verificar, puede existir un error', error

def operacion(func, num1, num2):
    return func(num1, num2)


def menu():
    init = True
    select = None

    while init:
        print("====================================")
        print('Elige que operacion deseas realizar')
        print('1.- Suma')
        print('2.- Resta')
        print('3.- Division')
        print('4.- Multiplicacion')
        print('5.- Residuo')
        print('6.- Potencia')
        print('7.- Salir')

        select = input()
        print("====================================")

        if select == '1':
            num1 = ingresar_numero_1()
            num2 = ingresar_numero_2()
            print(operacion(sumar, num1, num2))
        elif select == '2':
            num1 = ingresar_numero_1()
            num2 = ingresar_numero_2()
            print(operacion(restar, num1, num2))
        elif select == '3':
            num1 = ingresar_numero_1()
            num2 = ingresar_numero_2()
            print(operacion(dividir, num1, num2))
        elif select == '4':
            num1 = ingresar_numero_1()
            num2 = ingresar_numero_2()
            print(operacion(multiplicar, num1, num2))
        elif select == '5':
            num1 = ingresar_numero_1()
            num2 = ingresar_numero_2()
            print(operacion(residuo, num1, num2))
        elif select == '6':
            num1 = ingresar_numero_1()
            num2 = ingresar_numero_2()
            print(operacion(potencia, num1, num2))
        elif select == '7':
            init = False
            print('Programa Terminado. Ten Un buen dia')
        else:
            print('Hubo un error, Por favor elige nuevamente')
    
        


menu()