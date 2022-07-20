unir = lambda texto: ''.join(map(str, texto))

def verify_number(num):
    try:
        return int(num)
    except ValueError:
        return False


def verify_rfc(rfc):

    if len(rfc) < 13:
        return False

    rfc_list = list(rfc)
    month = unir(rfc_list[6:8])
    day = unir(rfc_list[8:10])

    # verificar iniciales nombre
    for i in rfc_list[0:4]:
        if verify_number(i):
            return False

    # Verificar la fecha de nacimiento
    if not verify_number(unir(rfc_list[4:6])):
        return False

    elif not verify_number(month):
        return False

    elif verify_number(month) > 12 or  verify_number(month) < 1:
        return False

    elif not verify_number(day):
        return False

    elif verify_number(day) > 31 or verify_number(day) < 1:
        return False

    else:
        return True

def into_rfc():
    print('Ingresa tu RFC')
    rfc = input()

    if verify_rfc(rfc):
        print('RFC valido: ', rfc.upper())
    else:
        print('RFC Invalido')

into_rfc()