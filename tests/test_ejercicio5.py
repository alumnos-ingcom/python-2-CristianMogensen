################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio5 import hay_balanceo_corchetes
from practica.ejercicio5 import hay_balanceo_especifico
from practica.ejercicio5 import hay_balanceo_simultaneo

"""
Tests del Ejercicio 5: Corchetes balanceados.

Se buscan testear 7 casos de prueba para la función hay_balanceo_corchetes,
7 para la función hay_balanceo_especifico y N para la función
hay_balanceo_simultaneo:

hay_balanceo_corchetes(texto: str):
1- texto = "". Resultado esperado: True
2- texto = "[]". Resultado esperado: True
3- texto = "[][]". Resultado esperado: True
4- texto = "[[][]]". Resultado esperado: True
5- texto = "][". Resultado esperado: False
6- texto = "][][". Resultado esperado: False
7- texto = "[]][[]". Resultado esperado: False

hay_balanceo_especifico(texto: str, inicio: str, cierre: str)
1- texto = "", inicio = 'a', cierre = 'b'. Resultado esperado: True
2- texto = "ac", inicio = 'a', cierre = 'c'. Resultado esperado: True
3- texto = "dcdc", inicio = 'd', cierre = 'c'. Resultado esperado: True
4- texto = "ppopoo", inicio = 'p', cierre = 'o'. Resultado esperado: True
5- texto = "21", inicio = '1', cierre = '2'. Resultado esperado: False
6- texto = "2121", inicio = '1', cierre = '2'. Resultado esperado: False
7- texto = "122112", inicio = '1', cierre = '2'. Resultado esperado: False

hay_balanceo_simultaneo(texto: str)
1- texto = "({[]})". Resultado esperado: True
2- texto = "}{)([]". Resultado esperado: False
"""


def test_hay_balanceo_corchetes_caso_1():
    """
    Test función hay_balanceo_corchetes(texto)
    Caso de prueba 1:
    - Entrada: texto = ""
    - Resultado esperado: True
    """

    texto: str = ""

    resultado: bool = hay_balanceo_corchetes(texto)

    assert resultado, "El resultado no es el esperado."


def test_hay_balanceo_corchetes_caso_2():
    """
    Test función hay_balanceo_corchetes(texto)
    Caso de prueba 2:
    - Entrada: texto = "[]"
    - Resultado esperado: True
    """

    texto: str = "[]"

    resultado: bool = hay_balanceo_corchetes(texto)

    assert resultado, "El resultado no es el esperado."


def test_hay_balanceo_corchetes_caso_3():
    """
    Test función hay_balanceo_corchetes(texto)
    Caso de prueba 3:
    - Entrada: texto = "[][]"
    - Resultado esperado: True
    """

    texto: str = "[][]"

    resultado: bool = hay_balanceo_corchetes(texto)

    assert resultado, "El resultado no es el esperado."


def test_hay_balanceo_corchetes_caso_4():
    """
    Test función hay_balanceo_corchetes(texto)
    Caso de prueba 4:
    - Entrada: texto = "[[][]]"
    - Resultado esperado: True
    """

    texto: str = "[[][]]"

    resultado: bool = hay_balanceo_corchetes(texto)

    assert resultado, "El resultado no es el esperado."


def test_hay_balanceo_corchetes_caso_5():
    """
    Test función hay_balanceo_corchetes(texto)
    Caso de prueba 5:
    - Entrada: texto = "]["
    - Resultado esperado: False
    """

    texto: str = "]["

    resultado: bool = hay_balanceo_corchetes(texto)

    assert not resultado, "El resultado no es el esperado."


def test_hay_balanceo_corchetes_caso_6():
    """
    Test función hay_balanceo_corchetes(texto)
    Caso de prueba 6:
    - Entrada: texto = "][]["
    - Resultado esperado: False
    """

    texto: str = "][]["

    resultado: bool = hay_balanceo_corchetes(texto)

    assert not resultado, "El resultado no es el esperado."


def test_hay_balanceo_corchetes_caso_7():
    """
    Test función hay_balanceo_corchetes(texto)
    Caso de prueba 7:
    - Entrada: texto = "[]][[]"
    - Resultado esperado: False
    """

    texto: str = "[]][[]"

    resultado: bool = hay_balanceo_corchetes(texto)

    assert not resultado, "El resultado no es el esperado."


def test_hay_balanceo_especifico_caso_1():
    """
    Test función hay_balanceo_especifico(texto, inicio, cierre)
    Caso de prueba 1:
    - Entrada: texto = "", inicio = 'a', cierre = 'b'
    - Resultado esperado: True
    """

    texto: str = ""

    inicio: str = 'a'

    cierre: str = 'b'

    resultado: bool = hay_balanceo_especifico(texto, inicio, cierre)

    assert resultado, "El resultado no es el esperado."


def test_hay_balanceo_especifico_caso_2():
    """
    Test función hay_balanceo_especifico(texto, inicio, cierre)
    Caso de prueba 2:
    - Entrada: texto = "ac", inicio = 'a', cierre = 'c'
    - Resultado esperado: True
    """

    texto: str = "ac"

    inicio: str = 'a'

    cierre: str = 'c'

    resultado: bool = hay_balanceo_especifico(texto, inicio, cierre)

    assert resultado, "El resultado no es el esperado."


def test_hay_balanceo_especifico_caso_3():
    """
    Test función hay_balanceo_especifico(texto, inicio, cierre)
    Caso de prueba 3:
    - Entrada: texto = "dcdc", inicio = 'd', cierre = 'c'
    - Resultado esperado: True
    """

    texto: str = "dcdc"

    inicio: str = 'd'

    cierre: str = 'c'

    resultado: bool = hay_balanceo_especifico(texto, inicio, cierre)

    assert resultado, "El resultado no es el esperado."


def test_hay_balanceo_especifico_caso_4():
    """
    Test función hay_balanceo_especifico(texto, inicio, cierre)
    Caso de prueba 4:
    - Entrada: texto = "ppopoo", inicio = 'p', cierre = 'o'
    - Resultado esperado: True
    """

    texto: str = "ppopoo"

    inicio: str = 'p'

    cierre: str = 'o'

    resultado: bool = hay_balanceo_especifico(texto, inicio, cierre)

    assert resultado, "El resultado no es el esperado."


def test_hay_balanceo_especifico_caso_5():
    """
    Test función hay_balanceo_especifico(texto, inicio, cierre)
    Caso de prueba 5:
    - Entrada: texto = "21", inicio = '1', cierre = '2'
    - Resultado esperado: False
    """

    texto: str = "21"

    inicio: str = '1'

    cierre: str = '2'

    resultado: bool = hay_balanceo_especifico(texto, inicio, cierre)

    assert not resultado, "El resultado no es el esperado."


def test_hay_balanceo_especifico_caso_6():
    """
    Test función hay_balanceo_especifico(texto, inicio, cierre)
    Caso de prueba 6:
    - Entrada: texto = "2121", inicio = '1', cierre = '2'
    - Resultado esperado: False
    """

    texto: str = "2121"

    inicio: str = '1'

    cierre: str = '2'

    resultado: bool = hay_balanceo_especifico(texto, inicio, cierre)

    assert not resultado, "El resultado no es el esperado."


def test_hay_balanceo_especifico_caso_7():
    """
    Test función hay_balanceo_especifico(texto, inicio, cierre)
    Caso de prueba 7:
    - Entrada: texto = "122112", inicio = '1', cierre = '2'
    - Resultado esperado: False
    """

    texto: str = "122112"

    inicio: str = '1'

    cierre: str = '2'

    resultado: bool = hay_balanceo_especifico(texto, inicio, cierre)

    assert not resultado, "El resultado no es el esperado."


def test_hay_balanceo_simultaneo_caso_1():
    """
    Test función hay_balanceo_simultaneo(texto)
    Caso de prueba 1:
    - Entrada: texto = "({[]})"
    - Resultado esperado: True
    """

    texto: str = "({[]})"

    resultado: bool = hay_balanceo_simultaneo(texto)

    assert resultado, "El resultado no es el esperado."


def test_hay_balanceo_simultaneo_caso_2():
    """
    Test función hay_balanceo_simultaneo(texto)
    Caso de prueba 2:
    - Entrada: texto = "}{)([]"
    - Resultado esperado: False
    """

    texto: str = "}{)([]"

    resultado: bool = hay_balanceo_simultaneo(texto)

    assert not resultado, "El resultado no es el esperado."
