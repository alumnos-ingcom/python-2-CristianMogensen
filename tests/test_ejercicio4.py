################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio4 import fibonacci

"""
Tests del Ejercicio 4: Fibonacci.

Se buscan testear 5 casos de prueba para la función fibonacci:

fibonacci(termino: int):
1- termino = 1. Resultado esperado: 1
2- termino = 2. Resultado esperado: 1
3- termino = 3. Resultado esperado: 2
4- termino = 4. Resultado esperado: 3
5- termino = 10. Resultado esperado: 55
"""


def test_fibonacci_primer_termino():
    """
    Test función fibonacci(termino)
    Caso de prueba 1:
    - Entrada: termino = 1
    - Resultado esperado: 1
    """

    termino: int = 1

    resultado: int = fibonacci(termino)

    assert (isinstance(resultado, int)), "El resultado debe ser de tipo int."
    assert (resultado == 1), "El resultado es distinto del esperado."


def test_fibonacci_segundo_termino():
    """
    Test función fibonacci(termino)
    Caso de prueba 2:
    - Entrada: termino = 2
    - Resultado esperado: 1
    """

    termino: int = 2

    resultado: int = fibonacci(termino)

    assert (isinstance(resultado, int)), "El resultado debe ser de tipo int."
    assert (resultado == 1), "El resultado es distinto del esperado."


def test_fibonacci_tercer_termino():
    """
    Test función fibonacci(termino)
    Caso de prueba 3:
    - Entrada: termino = 3
    - Resultado esperado: 2
    """

    termino: int = 3

    resultado: int = fibonacci(termino)

    assert (isinstance(resultado, int)), "El resultado debe ser de tipo int."
    assert (resultado == 2), "El resultado es distinto del esperado."


def test_fibonacci_cuarto_termino():
    """
    Test función fibonacci(termino)
    Caso de prueba 4:
    - Entrada: termino = 4
    - Resultado esperado: 3
    """

    termino: int = 4

    resultado: int = fibonacci(termino)

    assert (isinstance(resultado, int)), "El resultado debe ser de tipo int."
    assert (resultado == 3), "El resultado es distinto del esperado."


def test_fibonacci_decimo_termino():
    """
    Test función fibonacci(termino)
    Caso de prueba 5:
    - Entrada: termino = 10
    - Resultado esperado: 55
    """

    termino: int = 10

    resultado: int = fibonacci(termino)

    assert (isinstance(resultado, int)), "El resultado debe ser de tipo int."
    assert (resultado == 55), "El resultado es distinto del esperado."
