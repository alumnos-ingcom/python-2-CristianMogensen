################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio1 import es_par

"""
Tests del Ejercicio 1: Pares e impares.

Casos de prueba:
-> Función es_par(numero: int) -> bool:
    - numero < 0, par
    - numero > 0, par
    - numero < 0, impar
    - numero > 0, impar
    - numero = 0, par
"""


def test_es_par_positivo_par():
    """
    Caso de prueba:
    - Entrada: numero > 0, par
    - Salida esperada: True
    """

    # Entrada.
    numero: int = 232

    # Salida.
    resultado: bool = es_par(numero)

    # Uso variable para cumplir con el formato de pycodestyle.
    error1: str = "El resultado debe ser de tipo 'bool'."
    assert (isinstance(resultado, bool)), error1

    # Uso variable para cumplir con el formato de pycodestyle.
    error2: str = "El resultado de es_par de un número par debe ser True."
    assert (resultado is True), error2


def test_es_par_negativo_par():
    """
    Caso de prueba:
    - Entrada: numero < 0, par
    - Salida esperada: True
    """

    # Entrada.
    numero: int = -232

    # Salida.
    resultado: bool = es_par(numero)

    # Uso variable para cumplir con el formato de pycodestyle.
    error1: str = "El resultado debe ser de tipo 'bool'."
    assert (isinstance(resultado, bool)), error1

    # Uso variable para cumplir con el formato de pycodestyle.
    error2: str = "El resultado de es_par de un número par debe ser True."
    assert (resultado is True), error2


def test_es_par_positivo_impar():
    """
    Caso de prueba:
    - Entrada: numero > 0, impar
    - Salida esperada: False
    """

    # Entrada.
    numero: int = 111

    # Salida.
    resultado: bool = es_par(numero)

    # Uso variable para cumplir con el formato de pycodestyle.
    error1: str = "El resultado debe ser de tipo 'bool'."
    assert (isinstance(resultado, bool)), error1

    # Uso variable para cumplir con el formato de pycodestyle.
    error2: str = "El resultado de es_par de un número impar debe ser False."
    assert (resultado is False), error2


def test_es_par_negativo_impar():
    """
    Caso de prueba:
    - Entrada: numero < 0, impar
    - Salida esperada: False
    """

    # Entrada.
    numero: int = -111

    # Salida.
    resultado: bool = es_par(numero)

    # Uso variable para cumplir con el formato de pycodestyle.
    error1: str = "El resultado debe ser de tipo 'bool'."
    assert (isinstance(resultado, bool)), error1

    # Uso variable para cumplir con el formato de pycodestyle.
    error2: str = "El resultado de es_par de un número impar debe ser False."
    assert (resultado is False), error2


def test_es_par_cero():
    """
    Caso de prueba:
    - Entrada: numero = 0
    - Salida esperada: True
    """

    # Entrada.
    numero: int = 0

    # Salida.
    resultado: bool = es_par(numero)

    # Uso variable para cumplir con el formato de pycodestyle.
    error1: str = "El resultado debe ser de tipo 'bool'."
    assert (isinstance(resultado, bool)), error1

    # Uso variable para cumplir con el formato de pycodestyle.
    error2: str = "El resultado de es_par de un número nulo debe ser True."
    assert (resultado is True), error2
