################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Fibonacci
La sucesión de Fibonacci es una sucesión infinita donde cada elemento
es la suma de los dos anteriores. En la misma, los dos primeros
términos son 1.
(En algunos lugares se toma el primer término en 0 y el segundo en 1)
Implementar una función que permita obtener el n-esimo termino de la
sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.
"""


def fibonacci(termino: int):
    """
    Calcula la sucesión de fibonacci hasta el termino indicado de
    tipo entero positivo (int > 0). Retorna el número entero con la
    suma hecha.
    PRECONDICIONES: Recibe un número entero ('termino').
    POSCONDICIONES: Devuelve un número entero.
    """
    # Verifico que el número ingresado sea mayor que cero.
    assert (termino > 0), "El argumento debe ser mayor a cero."
    
    # Verifico que el número ingresado sea de tipo entero.
    assert (isinstance(termino, int)), "El argumento debe ser de tipo int."
    
    # Defino los términos primeros.
    if (termino == 1 or termino == 2):

        return 1

    # Defino el caso general.
    else:
        # La sucesión evaluada en un termino N, resulta en la suma
        # de sus dos términos anteriores (N-1 y N-2).
        return fibonacci(termino - 1) + fibonacci(termino - 2)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print(fibonacci(int(input())))


if __name__ == "__main__":
    principal()
