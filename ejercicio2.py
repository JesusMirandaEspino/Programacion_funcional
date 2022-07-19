
sumando = lambda num1, num2 : num1 + num2
restando = lambda num1, num2 : num1 - num2
multiplicando = lambda num1, num2 : num1 * num2
dividiendo = lambda num1, num2 : num1 / num2
residual = lambda num1, num2 : int(num1) % int(num2)
potencia_r = lambda num1, num2 : num1 ** num2


def try_simple( func, num1, num2, tipo):
    try:
        return "el resultado de la ", tipo , " es: ", func(num1, num2)
    except TypeError as error:
        return 'No se puede realizar la operacion con un tipo entero con un tipo string', error

def try_div(func, num1, num2, tipo):
    try:
        return "el resultado " , tipo , " es: ", func(num1, num2)
    except (ZeroDivisionError, TypeError) as error:
        return 'No se puede dividir entre cero, o  hacer una division con un string incluido, o Intenta dividir entre un numero mayor a cero', error


def sumar(sumando, num1, num2):
    return try_simple( sumando, num1, num2, 'Suma')


def restar(num1, num2):
    return try_simple( restando, num1, num2, 'Resta')


def potencia(num1, num2):
    return try_simple( potencia_r, num1, num2, 'Potencia')    


def multiplicar(num1, num2):
    return try_simple( multiplicando, num1, num2, 'Multiplicacion')    
            

def dividir(num1, num2):
    return try_div( dividiendo, num1, num2, 'de la DIvision')    

def residuo(num1, num2):
    return try_div( residual, num1, num2, 'del residuo')    


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

operacion = lambda  func, num1, num2 :  func(num1, num2)


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