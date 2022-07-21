# Repositorio https://github.com/JesusMirandaEspino/Programacion_funcional

lista_productos = ( 'Huevo', 'frijol', 'Arroz', 'Leche', 'Tortilla', 'Pollo', 'Frutas', 'Verduras', 'Avena', 'Cereal')
lista_precio = ( 40.5, 20.5, 30.5, 20, 20, 32.5, 22.5 , 18.5, 15, 45.5 )

nuevo_precio = lambda precio : precio * 0.16

def agregar_iva(lista_precio):
    nuevos_precios = map(nuevo_precio, lista_precio)
    return list(nuevos_precios)


lista_nuevos_precio = agregar_iva(lista_precio)


def imprimir_productos(productos, precio):
    for index, producto in enumerate(productos):
        print("Producto #{} = {}, Precio: {}".format(index, producto, precio[index]))


imprimir_productos(lista_productos, lista_nuevos_precio)
