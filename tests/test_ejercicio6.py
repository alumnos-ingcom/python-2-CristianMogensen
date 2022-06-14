################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio6 import ajustar_a_rango
from practica.ejercicio6 import codificar_cifrado
from practica.ejercicio6 import decodificar_cifrado


"""
Tests del Ejercicio 6: El Cifrado del Cesar.

Se buscan testear 3 casos de prueba para la función ajustar_a_rango,
1 para la función codificar_cifrado y 1 para la función
decodificar_cifrado:

ajustar_a_rango(numero: int, pasos: int, num1: int, num2: int):
1- Número > num2
2- Número < num1
3- Número dentro del rango [num1, num2] (intervalo cerrado)

codificar_cifrado(texto: str, posiciones: int):
1- texto = "abcdefghijklmnopqrstuvwxyz()0123456789[]"
   posiciones = 13
   Resultado esperado: "nopqrstuvwxyzabcdefghijklm()3456789012[]"

decodificar_cifrado(texto_cifrado: str, posiciones: int)
1- texto = "nopqrstuvwxyzabcdefghijklm()3456789012[]"
   posiciones = 13
   Resultado esperado: "abcdefghijklmnopqrstuvwxyz()0123456789[]"
"""


def test_ajustar_a_rango_numero_mayor_a_extremo_superior():
    """
    Test función ajustar_a_rango(numero, pasos, num1, num2)
    Caso de prueba 1:
    - Entrada: numero = 6
               pasos = 3
               num1 = 2
               num2 = 4
    - Resultado esperado: 3
    """

    numero: int = 6

    pasos: int = 3

    num1: int = 2

    num2: int = 4

    resultado: int = ajustar_a_rango(numero, pasos, num1, num2)

    assert (resultado == 3), "El resultado no es el esperado."


def test_ajustar_a_rango_numero_mayor_a_extremo_inferior():
    """
    Test función ajustar_a_rango(numero, pasos, num1, num2)
    Caso de prueba 2:
    - Entrada: numero = 1
               pasos = 3
               num1 = 2
               num2 = 4
    - Resultado esperado: 4
    """

    numero: int = 1

    pasos: int = 3

    num1: int = 2

    num2: int = 4

    resultado: int = ajustar_a_rango(numero, pasos, num1, num2)

    assert (resultado == 4), "El resultado no es el esperado."


def test_ajustar_a_rango_numero_dentro_de_rango():
    """
    Test función ajustar_a_rango(numero, pasos, num1, num2)
    Caso de prueba 3:
    - Entrada: numero = 2
               pasos = 1
               num1 = 2
               num2 = 4
    - Resultado esperado: 3
    """

    numero: int = 2

    pasos: int = 1

    num1: int = 2

    num2: int = 4

    resultado: int = ajustar_a_rango(numero, pasos, num1, num2)

    assert (resultado == 3), "El resultado no es el esperado."


def test_codificar_cifrado_13():
    """
    Test función codificar_cifrado(texto, posiciones)
    Caso de prueba 1:
    - Entrada: texto = "abcdefghijklmnopqrstuvwxyz()0123456789[]"
               posiciones = 13
    - Resultado esperado: "nopqrstuvwxyzabcdefghijklm()3456789012[]"
    """

    texto: str = "abcdefghijklmnopqrstuvwxyz()0123456789[]"

    posiciones: int = 13

    esperado: str = "nopqrstuvwxyzabcdefghijklm()3456789012[]"

    resultado: int = codificar_cifrado(texto, posiciones)

    assert (resultado == esperado), "El resultado no es el esperado."


def test_decodificar_cifrado_13():
    """
    Test función decodificar_cifrado(texto, posiciones)
    Caso de prueba 1:
    - Entrada: texto = "nopqrstuvwxyzabcdefghijklm()3456789012[]"
               posiciones = 13
    - Resultado esperado: "abcdefghijklmnopqrstuvwxyz()0123456789[]"
    """

    texto: str = "nopqrstuvwxyzabcdefghijklm()3456789012[]"

    posiciones: int = 13

    esperado: str = "abcdefghijklmnopqrstuvwxyz()0123456789[]"

    resultado: int = decodificar_cifrado(texto, posiciones)

    assert (resultado == esperado), "El resultado no es el esperado."
