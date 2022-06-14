################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio3 import contar_superposiciones
from practica.ejercicio3 import encontrar_inicio_superposicion

"""
Tests del Ejercicio 3: Súper-puestos.

Se buscan testear 2 casos de prueba para la función contar_superposiciones y
3 para la función encontrar_inicio_superposicion:

contar_superposiciones(lista1: list, lista2: list):
1- Listas iguales.
2- Listas con 3 superposiciones.

encontrar_inicio_superposicion(lista1: list, lista2: list)
1- Listas iguales.
2- Listas con superposición al final.
3- Listas con superposición en alguna parte de la mitad.
"""


def test_contar_superposiciones_listas_iguales():
    """
    Test función contar_superposiciones(lista1, lista2)
    Caso de prueba 1:
    - Entrada: lista1, lista2, con 5 elementos iguales
    - Resultado esperado: 5
    """

    lista1: list = ['M', 'u', 'n', 'd', 'o']

    lista2: list = lista1

    resultado: int = contar_superposiciones(lista1, lista2)

    assert (resultado == 5), "El resultado es distinto de 5."


def test_contar_superposiciones_listas_con_3_superposiciones():
    """
    Test función contar_superposiciones(lista1, lista2)
    Caso de prueba 2:
    - Entrada: lista1, lista2, con 5 elementos
    - Resultado esperado: 3
    """

    lista1: list = ['M', 'u', 'n', 'd', 'o']

    lista2: list = ['u', 'u', 'd', 'd', 'o']

    resultado: int = contar_superposiciones(lista1, lista2)

    assert (resultado == 3), "El resultado es distinto de 3."


def test_encontrar_inicio_superposicion_listas_iguales():
    """
    Test función encontrar_inicio_superposicion(lista1, lista2)
    Caso de prueba 1:
    - Entrada: lista1, lista2, con 5 elementos iguales
    - Resultado esperado: 0
    """

    lista1: list = ['M', 'u', 'n', 'd', 'o']

    lista2: list = lista1

    resultado: int = encontrar_inicio_superposicion(lista1, lista2)

    assert (resultado == 0), "El resultado es distinto de 0."


def test_encontrar_inicio_superposicion_al_final():
    """
    Test función encontrar_inicio_superposicion(lista1, lista2)
    Caso de prueba 2:
    - Entrada: lista1, lista2, con 5 elementos iguales
    - Resultado esperado: 0
    """

    lista1: list = ['M', 'u', 'n', 'd', 'o']

    lista2: list = ['a', 'b', 'c', 'a', 'o']

    resultado: int = encontrar_inicio_superposicion(lista1, lista2)

    assert (resultado == 4), "El resultado es distinto de 4."


def test_encontrar_inicio_superposicion_al_azar():
    """
    Test función encontrar_inicio_superposicion(lista1, lista2)
    Caso de prueba 3:
    - Entrada: lista1, lista2, con 5 elementos iguales
    - Resultado esperado: 0
    """

    lista1: list = ['M', 'u', 'n', 'd', 'o']

    lista2: list = ['a', 'b', 'c', 'd', 'w']

    resultado: int = encontrar_inicio_superposicion(lista1, lista2)

    assert (resultado == 3), "El resultado es distinto de 3."
