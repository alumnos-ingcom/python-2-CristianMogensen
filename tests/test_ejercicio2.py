################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from typing import Union, List, Tuple

from practica.ejercicio2 import encontrar_mayor, encontrar_menor
from practica.ejercicio2 import obtener_promedio, obtener_estadisticas


"""
Tests del Ejercicio 2: Estadísticas.

Se buscan testear 32 casos de prueba para la función encontrar_mayor, 32 para
la función encontrar_menor, 10 para función obtener_promedio y 4 para la
función obtener_estadisticas.

encontrar_mayor(secuencia:
                    Union[Union[List[int],
                                List[float]],
                          Union[Tuple[int],
                                Tuple[float]]]) -> Union[int, float]:
1-  Lista de enteros, con 1 elemento
2-  Lista de enteros, con 2 elementos (primero distinto)
3-  Lista de enteros, con 2 elementos (segundo distinto)
4-  Lista de enteros, con 2 elementos iguales
5-  Lista de enteros, con 3 elementos (primero distinto)
6-  Lista de enteros, con 3 elementos (segundo distinto)
7-  Lista de enteros, con 3 elementos (tercero distinto)
8-  Lista de enteros, con 3 elementos y dos iguales (primero distinto)
9-  Lista de enteros, con 3 elementos y dos iguales (segundo distinto)
10- Lista de enteros, con 3 elementos y dos iguales (tercero distinto)
11- Lista de enteros, con 3 elementos y dos mayores iguales (1ero y 3ero)
12- Lista de enteros, con 3 elementos y dos mayores iguales (1er y 2do)
13- Lista de enteros, con 3 elementos y dos mayores iguales (2do y 3ero)
14- Lista de enteros, con 3 elementos iguales
15- Lista de enteros, con N elementos
16- Lista de enteros, con N elementos y algunos repetidos (incluyendo mayor)
17- Lista de decimales, con 1 elemento
18- Lista de decimales, con 2 elementos (primero distinto)
19- Lista de decimales, con 2 elementos (segundo distinto)
20- Lista de decimales, con 2 elementos iguales
21- Lista de decimales, con 3 elementos (primero distinto)
22- Lista de decimales, con 3 elementos (segundo distinto)
23- Lista de decimales, con 3 elementos (tercero distinto)
24- Lista de decimales, con 3 elementos y dos iguales (primero distinto)
25- Lista de decimales, con 3 elementos y dos iguales (segundo distinto)
26- Lista de decimales, con 3 elementos y dos iguales (tercero distinto)
27- Lista de decimales, con 3 elementos y dos mayores iguales (1ero y 3ero)
28- Lista de decimales, con 3 elementos y dos mayores iguales (1er y 2do)
29- Lista de decimales, con 3 elementos y dos mayores iguales (2do y 3ero)
30- Lista de decimales, con 3 elementos iguales
31- Lista de decimales, con N elementos
32- Lista de decimales, con N elementos y algunos repetidos (incluyendo mayor)

encontrar_menor(secuencia:
                    Union[Union[List[int],
                                List[float]],
                          Union[Tuple[int],
                                Tuple[float]]]) -> Union[int, float]:
1-  Lista de enteros, con 1 elemento
2-  Lista de enteros, con 2 elementos (primero distinto)
3-  Lista de enteros, con 2 elementos (segundo distinto)
4-  Lista de enteros, con 2 elementos iguales
5-  Lista de enteros, con 3 elementos (primero distinto)
6-  Lista de enteros, con 3 elementos (segundo distinto)
7-  Lista de enteros, con 3 elementos (tercero distinto)
8-  Lista de enteros, con 3 elementos y dos iguales (primero distinto)
9-  Lista de enteros, con 3 elementos y dos iguales (segundo distinto)
10- Lista de enteros, con 3 elementos y dos iguales (tercero distinto)
11- Lista de enteros, con 3 elementos y dos menores iguales (1ero y 3ero)
12- Lista de enteros, con 3 elementos y dos menores iguales (1er y 2do)
13- Lista de enteros, con 3 elementos y dos menores iguales (2do y 3ero)
14- Lista de enteros, con 3 elementos iguales
15- Lista de enteros, con N elementos
16- Lista de enteros, con N elementos y algunos repetidos (incluyendo mayor)
17- Lista de decimales, con 1 elemento
18- Lista de decimales, con 2 elementos (primero distinto)
19- Lista de decimales, con 2 elementos (segundo distinto)
20- Lista de decimales, con 2 elementos iguales
21- Lista de decimales, con 3 elementos (primero distinto)
22- Lista de decimales, con 3 elementos (segundo distinto)
23- Lista de decimales, con 3 elementos (tercero distinto)
24- Lista de decimales, con 3 elementos y dos iguales (primero distinto)
25- Lista de decimales, con 3 elementos y dos iguales (segundo distinto)
26- Lista de decimales, con 3 elementos y dos iguales (tercero distinto)
27- Lista de decimales, con 3 elementos y dos menores iguales (1ero y 3ero)
28- Lista de decimales, con 3 elementos y dos menores iguales (1er y 2do)
29- Lista de decimales, con 3 elementos y dos menores iguales (2do y 3ero)
30- Lista de decimales, con 3 elementos iguales
31- Lista de decimales, con N elementos
32- Lista de decimales, con N elementos y algunos repetidos (incluyendo menor)


obtener_promedio(secuencia:
                     Union[Union[List[int],
                                 List[float]],
                           Union[Tuple[int],
                                 Tuple[float]]]) -> Union[int, float]:
1-    Lista de enteros positivos, con 1 elemento
2-    Lista de enteros positivos, con más de 1 elemento
3-    Lista de enteros negativos, con 1 elemento
4-    Lista de enteros negativos, con más de 1 elemento
5-    Lista de decimales positivos, con 1 elemento
6-    Lista de decimales positivos, con más de 1 elemento
7-    Lista de decimales negativos, con 1 elemento
8-    Lista de decimales negativos, con más de 1 elemento
9-    Lista de enteros intercalados, con más de 1 elemento
10-   Lista de decimales intercalados, con más de 1 elemento

obtener_estadisticas(secuencia:
                         Union[Union[List[int],
                                     List[float]],
                               Union[Tuple[int],
                                     Tuple[float]]]) -> Union[Tuple[int],
                                                              Tuple[float]]:
1-    Lista de enteros, con 1 elemento
2-    Lista de decimales, con 1 elemento
3-    Lista de enteros, con más de 1 elemento
4-    Lista de decimales, con más de 1 elemento

"""


def test_encontrar_mayor_caso_1():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 1:
    - Entrada: secuencia: List[int] = [mayor: int]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 4

    secuencia: list = [mayor]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_2():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 2:
    - Entrada: secuencia: List[int] = [mayor: int, numero: int]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 4

    secuencia: list = [mayor, mayor - 2]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_3():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 3:
    - Entrada: secuencia: List[int] = [numero: int, mayor: int]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 4

    secuencia: list = [mayor - 2, mayor]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_4():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 4:
    - Entrada: secuencia: List[int] = [mayor: int, mayor: int]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 4

    secuencia: list = [mayor, mayor]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_5():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 5:
    - Entrada: secuencia: List[int] = [mayor, n1, n2]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 8

    secuencia: list = [mayor, mayor - 1, mayor - 2]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_6():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 6:
    - Entrada: secuencia: List[int] = [n1, mayor, n2]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 8

    secuencia: list = [mayor - 1, mayor, mayor - 2]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_7():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 7:
    - Entrada: secuencia: List[int] = [n1, n2, mayor]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 8

    secuencia: list = [mayor - 1, mayor - 2, mayor]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_8():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 8:
    - Entrada: secuencia: List[int] = [mayor, n, n]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 8

    secuencia: list = [mayor, mayor - 2, mayor - 2]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_9():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 9:
    - Entrada: secuencia: List[int] = [n, mayor, n]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 8

    secuencia: list = [mayor - 2, mayor, mayor - 2]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_10():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 10:
    - Entrada: secuencia: List[int] = [n, n, mayor]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 8

    secuencia: list = [mayor - 2, mayor - 2, mayor]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_11():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 11:
    - Entrada: secuencia: List[int] = [mayor, n, mayor]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 8

    secuencia: list = [mayor, mayor - 2, mayor]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_12():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 12:
    - Entrada: secuencia: List[int] = [mayor, mayor, n]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 8

    secuencia: list = [mayor, mayor, mayor - 2]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_13():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 13:
    - Entrada: secuencia: List[int] = [n, mayor, mayor]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 8

    secuencia: list = [mayor - 2, mayor, mayor]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_14():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 14:
    - Entrada: secuencia: List[int] = [mayor, mayor, mayor]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 8

    secuencia: list = [mayor, mayor, mayor]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_15():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 15:
    - Entrada: secuencia: List[int] = [n_1, n_2, ..., mayor, ..., n_N-1, n_N]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 8

    secuencia: list = [mayor - 1, mayor - 5, mayor, mayor - 7, mayor - 2]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_16():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 16:
    - Entrada: secuencia: List[int] = [n_1, n_2, ..., mayor, ..., n_N-1, n_N]
    - Resultado esperado esperado: mayor: int
    """

    mayor: int = 8

    secuencia: list = [mayor - 1, mayor - 1, mayor, mayor, mayor - 1]

    resultado: int = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_17():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 17:
    - Entrada: secuencia: List[float] = [mayor: float]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_18():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 18:
    - Entrada: secuencia: List[float] = [mayor: float, numero: float]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor, mayor - 2.3]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_19():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 19:
    - Entrada: secuencia: List[float] = [numero: float, mayor: float]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor - 3.1, mayor]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_20():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 20:
    - Entrada: secuencia: List[float] = [mayor: float, mayor: float]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor, mayor]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_21():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 21:
    - Entrada: secuencia: List[float] = [mayor, n1, n2]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor, mayor - 3.1, mayor - 5.2]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_22():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 22:
    - Entrada: secuencia: List[float] = [n1, mayor, n2]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor - 3.1, mayor, mayor - 5.2]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_23():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 23:
    - Entrada: secuencia: List[float] = [n1, n2, mayor]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor - 3.1, mayor - 2.2, mayor]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_24():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 24:
    - Entrada: secuencia: List[float] = [mayor, n, n]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor, mayor - 2.2, mayor - 2.2]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_25():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 25:
    - Entrada: secuencia: List[float] = [n, mayor, n]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor - 2.2, mayor, mayor - 2.2]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_26():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 26:
    - Entrada: secuencia: List[float] = [n, n, mayor]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor - 2.2, mayor - 2.2, mayor]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_27():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 27:
    - Entrada: secuencia: List[float] = [mayor, n, mayor]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor, mayor - 2.2, mayor]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_28():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 28:
    - Entrada: secuencia: List[float] = [mayor, mayor, n]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor, mayor, mayor - 1.1]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_29():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 29:
    - Entrada: secuencia: List[float] = [n, mayor, mayor]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor - 1.1, mayor, mayor]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_30():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 30:
    - Entrada: secuencia: List[float] = [mayor, mayor, mayor]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor, mayor, mayor]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_31():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 31:
    - Entrada: secuencia: List[float] = [n_1, n_2, ..., mayor, ..., n_N]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor - 1.2, mayor - 5.3, mayor - 2.8, mayor, mayor - 6]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_mayor_caso_32():
    """
    Test función encontrar_mayor(secuencia)
    Caso de prueba 32:
    - Entrada: secuencia: List[float] = [n_1, n_2, ..., mayor, ..., n_N]
    - Resultado esperado esperado: mayor: float
    """

    mayor: float = 8.5

    secuencia: list = [mayor - 5.3, mayor - 5.3, mayor - 2, mayor, mayor - 2]

    resultado: float = encontrar_mayor(secuencia)

    assert (resultado == mayor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_1():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 1:
    - Entrada: secuencia: List[int] = [menor: int]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 4

    secuencia: list = [menor]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_2():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 2:
    - Entrada: secuencia: List[int] = [menor: int, numero: int]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 4

    secuencia: list = [menor, menor + 2]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_3():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 3:
    - Entrada: secuencia: List[int] = [numero: int, menor: int]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 4

    secuencia: list = [menor + 2, menor]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_4():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 4:
    - Entrada: secuencia: List[int] = [menor: int, menor: int]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 4

    secuencia: list = [menor, menor]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_5():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 5:
    - Entrada: secuencia: List[int] = [menor, n1, n2]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 8

    secuencia: list = [menor, menor + 1, menor + 2]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_6():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 6:
    - Entrada: secuencia: List[int] = [n1, menor, n2]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 8

    secuencia: list = [menor + 1, menor, menor + 2]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_7():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 7:
    - Entrada: secuencia: List[int] = [n1, n2, menor]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 8

    secuencia: list = [menor + 1, menor + 2, menor]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_8():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 8:
    - Entrada: secuencia: List[int] = [menor, n, n]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 8

    secuencia: list = [menor, menor + 2, menor + 2]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_9():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 9:
    - Entrada: secuencia: List[int] = [n, menor, n]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 8

    secuencia: list = [menor + 2, menor, menor + 2]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_10():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 10:
    - Entrada: secuencia: List[int] = [n, n, menor]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 8

    secuencia: list = [menor + 2, menor + 2, menor]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_11():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 11:
    - Entrada: secuencia: List[int] = [menor, n, menor]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 8

    secuencia: list = [menor, menor + 2, menor]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_12():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 12:
    - Entrada: secuencia: List[int] = [menor, menor, n]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 8

    secuencia: list = [menor, menor, menor + 2]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_13():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 13:
    - Entrada: secuencia: List[int] = [n, menor, menor]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 8

    secuencia: list = [menor + 2, menor, menor]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_14():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 14:
    - Entrada: secuencia: List[int] = [menor, menor, menor]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 8

    secuencia: list = [menor, menor, menor]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_15():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 15:
    - Entrada: secuencia: List[int] = [n_1, n_2, ..., menor, ..., n_N-1, n_N]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 8

    secuencia: list = [menor + 1, menor + 5, menor, menor + 7, menor + 2]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_16():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 16:
    - Entrada: secuencia: List[int] = [n_1, n_2, ..., menor, ..., n_N-1, n_N]
    - Resultado esperado esperado: menor: int
    """

    menor: int = 8

    secuencia: list = [menor + 1, menor + 1, menor, menor, menor + 1]

    resultado: int = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_17():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 17:
    - Entrada: secuencia: List[float] = [menor: float]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_18():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 18:
    - Entrada: secuencia: List[float] = [menor: float, numero: float]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor, menor + 2.3]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_19():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 19:
    - Entrada: secuencia: List[float] = [numero: float, menor: float]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor + 3.1, menor]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_20():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 20:
    - Entrada: secuencia: List[float] = [menor: float, menor: float]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor, menor]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_21():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 21:
    - Entrada: secuencia: List[float] = [menor, n1, n2]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor, menor + 3.1, menor + 5.2]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_22():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 22:
    - Entrada: secuencia: List[float] = [n1, menor, n2]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor + 3.1, menor, menor + 5.2]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_23():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 23:
    - Entrada: secuencia: List[float] = [n1, n2, menor]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor + 3.1, menor + 2.2, menor]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_24():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 24:
    - Entrada: secuencia: List[float] = [menor, n, n]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor, menor + 2.2, menor + 2.2]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_25():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 25:
    - Entrada: secuencia: List[float] = [n, menor, n]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor + 2.2, menor, menor + 2.2]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_26():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 26:
    - Entrada: secuencia: List[float] = [n, n, menor]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor + 2.2, menor + 2.2, menor]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_27():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 27:
    - Entrada: secuencia: List[float] = [menor, n, menor]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor, menor + 2.2, menor]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_28():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 28:
    - Entrada: secuencia: List[float] = [menor, menor, n]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor, menor, menor + 1.1]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_29():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 29:
    - Entrada: secuencia: List[float] = [n, menor, menor]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor + 1.1, menor, menor]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_30():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 30:
    - Entrada: secuencia: List[float] = [menor, menor, menor]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor, menor, menor]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_31():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 31:
    - Entrada: secuencia: List[float] = [n_1, n_2, ..., menor, ..., n_N]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor + 1.2, menor + 5.3, menor + 2.8, menor, menor + 6]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_encontrar_menor_caso_32():
    """
    Test función encontrar_menor(secuencia)
    Caso de prueba 32:
    - Entrada: secuencia: List[float] = [n_1, n_2, ..., menor, ..., n_N]
    - Resultado esperado esperado: menor: float
    """

    menor: float = 8.5

    secuencia: list = [menor + 5.3, menor + 5.3, menor + 2, menor, menor + 2]

    resultado: float = encontrar_menor(secuencia)

    assert (resultado == menor), "El resultado es distinto al esperado."


def test_obtener_promedio_caso_1():
    """
    Test función obtener_promedio(secuencia)
    Caso de prueba 1:
    - Entrada: secuencia: List[int] = [numero: int]
    - Resultado esperado: numero: int
    """

    numero: int = 8

    secuencia: list = [numero]

    resultado: Union[float, int] = obtener_promedio(secuencia)

    assert (resultado == numero), "El resultado es distinto al esperado."


def test_obtener_promedio_caso_2():
    """
    Test función obtener_promedio(secuencia)
    Caso de prueba 2:
    - Entrada: secuencia: List[int]
    - Resultado esperado: promedio
    """

    numero: int = 8

    secuencia: list = [numero - 2, numero + 2, numero]

    resultado: Union[float, int] = obtener_promedio(secuencia)

    assert (resultado == numero), "El resultado es distinto al esperado."


def test_obtener_promedio_caso_3():
    """
    Test función obtener_promedio(secuencia)
    Caso de prueba 3:
    - Entrada: secuencia: List[int] = [numero: int]
    - Resultado esperado: numero: int
    """

    numero: int = -8

    secuencia: list = [numero]

    resultado: Union[float, int] = obtener_promedio(secuencia)

    assert (resultado == numero), "El resultado es distinto al esperado."


def test_obtener_promedio_caso_4():
    """
    Test función obtener_promedio(secuencia)
    Caso de prueba 4:
    - Entrada: secuencia: List[int]
    - Resultado esperado: promedio
    """

    numero: int = -8

    secuencia: list = [numero - 2, numero, numero + 2]

    resultado: Union[float, int] = obtener_promedio(secuencia)

    assert (resultado == numero), "El resultado es distinto al esperado."


def test_obtener_promedio_caso_5():
    """
    Test función obtener_promedio(secuencia)
    Caso de prueba 5:
    - Entrada: secuencia: List[float] = [numero: float]
    - Resultado esperado: numero: float
    """

    numero: float = 5.53

    secuencia: list = [numero]

    resultado: Union[float, int] = obtener_promedio(secuencia)

    assert (resultado == numero), "El resultado es distinto al esperado."


def test_obtener_promedio_caso_6():
    """
    Test función obtener_promedio(secuencia)
    Caso de prueba 6:
    - Entrada: secuencia: List[float]
    - Resultado esperado: numero: float
    """

    numero: float = 5.53

    secuencia: list = [numero + 2.25, numero, numero - 2.25]

    resultado: Union[float, int] = obtener_promedio(secuencia)

    assert (resultado == numero), "El resultado es distinto al esperado."


def test_obtener_promedio_caso_7():
    """
    Test función obtener_promedio(secuencia)
    Caso de prueba 7:
    - Entrada: secuencia: List[float] = [numero: float]
    - Resultado esperado: numero: float
    """

    numero: float = -5.53

    secuencia: list = [numero]

    resultado: Union[float, int] = obtener_promedio(secuencia)

    assert (resultado == numero), "El resultado es distinto al esperado."


def test_obtener_promedio_caso_8():
    """
    Test función obtener_promedio(secuencia)
    Caso de prueba 8:
    - Entrada: secuencia: List[float]
    - Resultado esperado: promedio
    """

    numero: float = -5.53

    secuencia: list = [numero, numero - 1.5, numero + 1.5]

    resultado: Union[float, int] = obtener_promedio(secuencia)

    assert (resultado == numero), "El resultado es distinto al esperado."


def test_obtener_promedio_caso_9():
    """
    Test función obtener_promedio(secuencia)
    Caso de prueba 9:
    - Entrada: secuencia: List[int]
    - Resultado esperado: promedio
    """

    numero: int = -5

    secuencia: list = [numero, numero - 12, numero + 12]

    resultado: Union[float, int] = obtener_promedio(secuencia)

    assert (resultado == numero), "El resultado es distinto al esperado."


def test_obtener_promedio_caso_10():
    """
    Test función obtener_promedio(secuencia)
    Caso de prueba 10:
    - Entrada: secuencia: List[float]
    - Resultado esperado: promedio
    """

    numero: float = -5.53

    secuencia: list = [numero, numero - 13.51, numero + 13.51]

    resultado: Union[float, int] = obtener_promedio(secuencia)

    assert (resultado == numero), "El resultado es distinto al esperado."


def test_obtener_estadisticas_caso_1():
    """
    Test función obtener_estadisticas(secuencia)
    Caso de prueba 1:
    - Entrada: secuencia: List[int] = [numero: int]
    - Resultado esperado: (numero,)*3 (float)
    """

    numero: int = 9

    secuencia: list = [numero]

    resultado: tuple = obtener_estadisticas(secuencia)

    assert (resultado == (numero,)*3), "El resultado es distinto al esperado."


def test_obtener_estadisticas_caso_2():
    """
    Test función obtener_estadisticas(secuencia)
    Caso de prueba 2:
    - Entrada: secuencia: List[float] = [numero: float]
    - Resultado esperado: (numero,)*3
    """

    numero: float = 3.53

    secuencia: list = [numero]

    resultado: tuple = obtener_estadisticas(secuencia)

    assert (resultado == (numero,)*3), "El resultado es distinto al esperado."


def test_obtener_estadisticas_caso_3():
    """
    Test función obtener_estadisticas(secuencia)
    Caso de prueba 3:
    - Entrada: secuencia: List[int]
    - Resultado esperado: (mayor, menor, promedio)
    """

    secuencia: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    resultado: tuple = obtener_estadisticas(secuencia)

    assertstring: str = "El resultado es distinto al esperado."
    assert (resultado == (9, 1, 5)), assertstring


def test_obtener_estadisticas_caso_4():
    """
    Test función obtener_estadisticas(secuencia)
    Caso de prueba 4:
    - Entrada: secuencia: List[int]
    - Resultado esperado: [mayor, menor, promedio]
    """

    secuencia: list = [1.1, 2.9, 10.5, 4.2, 1.8]

    promedio: float = (1.1 + 2.9 + 10.5 + 4.2 + 1.8)/5

    resultado: tuple = obtener_estadisticas(secuencia)

    assertstring: str = "El resultado es distinto al esperado."
    assert (resultado == (10.5, 1.1, promedio)), assertstring
