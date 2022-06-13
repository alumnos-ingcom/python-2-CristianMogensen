################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Súper-puestos
Desarrollar una función que indique el grado de superposición entre dos listas.
Siendo 0 sin superposición y uno para cada elemento superpuesto.

['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']

y

['H', 'o', 'l', 'a']

Tienen una superposición de cuatro elementos.

Extra #1
Indicar en lugar de la cantidad de caracteres superpuestos, la posicion de
inicio de la superposición.
"""


# Importo función para encontrar el menor número de una secuencia, para
# utilizarla en la funcion de contar_superposiciones (también en la función
# extra encontrar_inicio_superposicion). Se utiliza de manera
# tal que ayuda a indicar cuál es el tamaño más chico de las dos listas.
from ejercicio2 import encontrar_menor


def contar_superposiciones(lista1: list, lista2: list) -> int:
    """
    Busca las coincidencias simultáneas entre 2 listas ('lista1' y 'lista2')
    y retorna un número entero que indica el grado de superposición (0: no hay
    ninguna superposición).
    PRECONDICIONES: Recibe 2 listas para comparar.
    POSCONDICIONES: Devuelve un número entero.
    """

    # Declaro y defino la variable en la que se cuenten la cantidad de
    # elementos superpuestos en ambas listas.
    superposiciones: int = 0

    # Declaro y defino la variable con la que se recorrerá cada elemento de
    # cada lista.
    posicion: int = 0

    # Declaro y defino la variable que indicará el límite del bucle que
    # recorrerá ambas listas. Estará determinado por el tamaño más pequeño
    # de ambas listas (el menor len(lista)).
    menor_tam: int = encontrar_menor([len(lista1), len(lista2)])

    # Se buscan las superposiciones.
    while (posicion < menor_tam):

        if (lista1[posicion] == lista2[posicion]):

            superposiciones += 1

        posicion += 1

    return superposiciones


def encontrar_inicio_superposicion(lista1: list, lista2: list) -> int:
    """
    Busca la primer coincidencia simultáneas entre 2 listas ('lista1' y
    'lista2') y retorna un número entero que indica el la posición en las
    listas en donde comienza la superposición.
    PRECONDICIONES: Recibe 2 listas para comparar.
    POSCONDICIONES: Devuelve un número entero.
    """

    # Declaro y defino la variable que indicará la posición final, en donde
    # comienza la superposición entre las dos listas.
    resultado: int = None

    # Declaro y defino la variable con la que se recorrerá cada elemento de
    # cada lista.
    posicion: int = 0

    # Declaro y defino la variable que indicará el límite del bucle que
    # recorrerá ambas listas. Estará determinado por el tamaño más pequeño
    # de ambas listas (el menor len(lista)).
    menor_tam: int = encontrar_menor([len(lista1), len(lista2)])

    # Se buscan las superposiciones.
    while (posicion < menor_tam):

        if (lista1[posicion] == lista2[posicion]):

            resultado = posicion
            break

        posicion += 1

    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Imprimo título:
    print("Ejercicio 3:\tSúper-puestos")

    # Input:
    print("Ingrese primera lista:")
    print("Cada elemento debe tener 1 caracter.")
    print("(presione Enter para terminarla)")

    # Declaro las listas a comparar
    lista1: list = []
    lista2: list = []

    # Declaro la variable en la que se guardará el input.
    entrada: str = None

    # Se realiza el input hasta que el usuario presione enter sin ingresar
    # ningún caracter.
    while (entrada != ''):

        entrada = input()

        # Verifico que sea de 1 caracter.
        if (len(entrada) == 1):

            # Agrego la entrada a la lista correspondiente.
            lista1.append(entrada)

        elif (len(entrada) > 1):

            print("Debe ingresar 1 solo caracter.")

    print("Ingrese segunda lista:")
    print("Cada elemento debe tener 1 caracter.")
    print("(presione Enter para terminarla)")

    entrada = None

    while (entrada != ''):

        entrada = input()

        # Verifico que sea de 1 caracter.
        if (len(entrada) == 1):

            # Agrego la entrada a la lista correspondiente.
            lista2.append(entrada)

        elif (len(entrada) > 1):

            print("Debe ingresar 1 solo caracter.")

    # Salida:
    print("Las listas ingresadas son:")
    print(lista1)
    print(lista2)

    # Uso variables para cumplir con "pycodestyle".
    output1: str = "La cantidad de superposiciones es: "
    output1 += f"{contar_superposiciones(lista1,lista2)}"

    output2: str = "La superposición comienza en el elemento: "
    output2 += f"{encontrar_inicio_superposicion(lista1,lista2)}"

    print(output1)
    print(output2)


if __name__ == "__main__":
    principal()
