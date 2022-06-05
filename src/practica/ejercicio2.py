################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Estadísticas
Implementar una función que obtenga los máximos, mínimos y promedio de una
secuencia con números, retornando los valores como una tuple.

Sin utilizar lazos for o las funciones integradas del lenguaje que procesan
secuencias.
"""

from typing import Union, List, Tuple


def encontrar_mayor(secuencia:
                    Union[Union[List[int],
                                List[float]],
                          Union[Tuple[int],
                                Tuple[float]]]) -> Union[int, float]:
    """
    Encuentra el MAYOR número en una secuencia de números (int's o float's).
    Retorna un entero (int) o decimal (float).
    PRECONDICIONES: Recibe en la entrada una secuencia de números enteros (int)
                    o decimales (float). Esta secuencia puede ser una List o
                    una Tuple.
    POSCONDICIONES: Devuelve un número entero (int) o decimal (float).
    """

    # Verifico que la secuencia tenga al menos un elemento.
    assert (len(secuencia) > 0), "La secuencia de números no posee elementos."

    # Declaro y defino la variable en la que se guardará el mayor número de la
    # secuencia de números 'secuencia'. Fijo el primer elemento para comparar
    # de ahí en adelante, cuál es el mayor número.
    mayor: Union[int, float] = secuencia[0]

    # Declaro y defino la posición 0 (primer elemento) para utilizar con la
    # secuencia.
    posicion: int = 0

    # Verifico que en la secuencia haya más de un elemento. (De lo contrario,
    # no haría falta que entre en el bucle, pues el primer elemento será el
    # mayor número).
    if (len(secuencia) > 1):

        # Realizo la comparación iterativa que verifica si el elemento
        # siguiente es mayor al número mayor anteriormente guardado en la
        # variable 'mayor' y se queda con el que sea más grande.
        while (posicion + 1 < len(secuencia)):

            if (secuencia[posicion+1] > mayor):

                mayor = secuencia[posicion + 1]

            posicion += 1

    return mayor


def encontrar_menor(secuencia:
                    Union[Union[List[int],
                                List[float]],
                          Union[Tuple[int],
                                Tuple[float]]]) -> Union[int, float]:
    """
    Encuentra el MENOR número en una secuencia de números (int's o float's).
    Retorna un entero (int) o decimal (float).
    PRECONDICIONES: Recibe en la entrada una secuencia de números enteros (int)
                    o decimales (float). Esta secuencia puede ser una List o
                    una Tuple.
    POSCONDICIONES: Devuelve un número entero (int) o decimal (float).
    """

    # Verifico que la secuencia tenga al menos un elemento.
    assert (len(secuencia) > 0), "La secuencia de números no posee elementos."

    # Declaro y defino la variable en la que se guardará el menor número de la
    # secuencia de números 'secuencia'. Fijo el primer elemento para comparar
    # de ahí en adelante, cuál es el menor número.
    menor: Union[int, float] = secuencia[0]

    # Declaro y defino la posición 0 (primer elemento) para utilizar con la
    # secuencia.
    posicion: int = 0

    # Verifico que en la secuencia haya más de un elemento. (De lo contrario,
    # no haría falta que entre en el bucle, pues el primer elemento será el
    # menor número).
    if (len(secuencia) > 1):

        # Realizo la comparación iterativa que verifica si el elemento
        # siguiente es mayor al número mayor anteriormente guardado en la
        # variable 'mayor' y se queda con el que sea más grande.
        while (posicion + 1 < len(secuencia)):

            if (secuencia[posicion + 1] < menor):

                menor = secuencia[posicion + 1]

            posicion += 1

    return menor


def obtener_promedio(secuencia:
                     Union[Union[List[int],
                                 List[float]],
                           Union[Tuple[int],
                                 Tuple[float]]]) -> Union[int, float]:
    """
    Calcula el promedio de uns secuencia de números dada. Retorna un entero
    (int) o decimal (float).
    PRECONDICIONES: Recibe en la entrada una secuencia de números enteros
                    (int) o decimales (float). Esta secuencia puede ser una
                    List o una Tuple.
    POSCONDICIONES: Devuelve un número entero (int) o decimal (float).
    """

    # Verifico que la secuencia tenga al menos un elemento.
    assert (len(secuencia) > 0), "La secuencia de números no posee elementos."

    # Declaro y defino la variable en la que se sumarán todos los elementos
    # de la secuencia de números.
    suma: Union[int, float] = 0

    # Declaro y defino la variable en la que se calculará el promedio final.
    promedio: Union[int, float] = 0

    # Declaro y defino la posición 0 (primer elemento) para utilizar con la
    # secuencia.
    posicion: int = 0

    # Declaro y defino la cantidad de elementos de la secuencia 'secuencia'.
    cant_elementos: int = len(secuencia)

    # Sumo todos los elementos de 'secuencia' a la variable 'suma'.
    while (posicion < cant_elementos):

        suma += secuencia[posicion]

        posicion += 1

    # Finalmente, se calcula el promedio.
    promedio = suma / cant_elementos

    return promedio


def obtener_estadisticas(secuencia:
                         Union[Union[List[int],
                                     List[float]],
                               Union[Tuple[int],
                                     Tuple[float]]]) -> Union[Tuple[int],
                                                              Tuple[float]]:
    """
    Obtiene las estadísticas de una secuencia de números (int's o float's),
    retornando un tuple con (en orden) el máximo, el mínimo y el promedio de
    todos los números.
    PRECONDICIONES: Recibe en la entrada una secuencia de números enteros
                    (int) o decimales (float). Esta secuencia puede ser una
                    List o una Tuple.
    POSCONDICIONES: Devuelve tuple con (máximo, mínimo, promedio) [todos estos
                    enteros (int) o decimales (float)].
    """

    # Utilizando las funciones encontrar_mayor(...), encontrar_menor(...) y
    # obtener_promedio(...), calculo los valores buscados para retornarlos en
    # la tuple.
    return (encontrar_mayor(secuencia),
            encontrar_menor(secuencia),
            obtener_promedio(secuencia))


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Imprimo título:
    print("Ejercicio 2:\tEstadísticas")

    # Input:

    # Dejo que el usuario defina si quiere probar las funciones con lists
    # o tuples.
    print("¿Desea ingresar una List o un Tuple?")
    # Declaro y defino una variable 'decision' que determine, segun lo que
    # ingrese el usuario, si quiere una lista o tuple.
    decision: str = ''
    # Se hace el input de la decision hasta que ingrese el valor correcto.
    while (decision != 't' and
           decision != 'T' and
           decision != 'l' and
           decision != 'L'):
        decision = str(input("(l: list/ t: tuple): "))

    # Dejo que el usuario elija el tamaño de la lista o tuple correspondiente.
    print("¿Cuántos números desea ingresar?")
    # Declaro y defino la variable 'cant_numeros" para determinar el tamaño
    # que el usuario desea que la lista o tuple posea.
    cant_numeros: int = 0
    # Se hace el input de valores enteros, que forman parte de cada elemento
    # de la lista o tuple.
    while (cant_numeros <= 0):
        cant_numeros = int(input("(N > 0, entero): "))

    # Declaro y defino una variable 'contador' para indicar que elemento está
    # ingresando el usuario.
    contador: int = 0
    # Se bifurcan los caminos por si se trata de una lista o tuple, para
    # utilizar las funciones adecuadas a cada tipo de secuencia.
    # Si se verifica el 'if' se trata de un tuple:
    if (decision == 't' or decision == 'T'):
        # Declaro la variable en la que se guardará cada número que el
        # usuario ingrese.
        secuencia_numeros: Tuple[float] = ()
        print("Ingrese Tuple:\n")
        # Se pide cada número de cada elemento del tuple, guardándolos en
        # una variable auxiliar 'numero' de tipo float para luego asignárselo
        # al elemento correspondiente del tuple.
        while (contador < cant_numeros):
            # Se pide el número.
            numero: float = float(input(f"Elemento N{contador}= "))
            # Se lo asigna al elemento correspondiente.
            secuencia_numeros += (numero, )
            # Se suma 1 al contador, para indicar que se pasa el próximo
            # elemento.
            contador += 1
    # Si no se verifica el 'if' se trata de una list:
    else:
        # Declaro la variable en la que se guardará cada número que el
        # usuario ingrese.
        secuencia_numeros: List[float] = []
        print("Ingrese List:\n")
        # Se pide cada número de cada elemento del tuple, guardándolos en
        # una variable auxiliar 'numero' de tipo float para luego asignárselo
        # al elemento correspondiente de la list.
        while (contador < cant_numeros):
            # Se pide el número.
            numero: float = float(input(f"Elemento N{contador}= "))
            # Se lo asigna al elemento correspondiente.
            secuencia_numeros += [numero, ]
            # Se suma 1 al contador, para indicar que se pasa el próximo
            # elemento.
            contador += 1

    # Salida:
    print("Las estadísticas de la secuencia")
    print(secuencia_numeros)
    print("son (mayor, menor, promedio):")
    print(obtener_estadisticas(secuencia_numeros))


if __name__ == "__main__":
    principal()
