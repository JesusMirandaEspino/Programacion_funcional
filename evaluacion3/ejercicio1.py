
import re

filtrador_com = lambda elemento : re.match("^com", elemento )
filtrador_arp = lambda elemento : re.match("^arp", elemento )

lista_palabras = [ 'comal', 'comba', 'combar', 'combi', 'combo', 'arpón', 'arpía',  'arpes', 'arpeo', 'arpen',  'arpas', 'arpar', 'arpan', 'arpad', ]


def separador_lista(lista):
    lista_com = list(filter(filtrador_com, lista))
    lista_arp = list(filter(filtrador_arp, lista))

    maximo = max(lista)
    minimo = min(lista)

    print('El minimo de la lista es: ', minimo)
    print('El maximo de la lista es: ', maximo)

    print(lista_arp)
    print(lista_com)


separador_lista(lista_palabras)
