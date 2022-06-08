################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Corchetes balanceados
Implementar una función que determine si una cadena con corchetes
está balanceada.

Es decir, si cada corchete que abre, tiene su par que cierra. El
resultado debe ser un valor lógico indicando si esta o no balanceado.

Ejemplos

   (vacio)      True
   []           True
   [][]         True
   [[][]]       True
   ][           False
   ][][         False
   []][[]       False

La funcion deberia de ignorar todo lo que no sean corchetes.

Extra #1
Hacer que la funcion reciba que par de simbolos buscar si esta
balanceado. (como para pasar parentesis, llaves o cualquier otro)

Extra #2
Hacer que la función verifique el balanceo simultaneo de parentesis,
llaves y corchetes.
"""


def hay_balanceo_corchetes(texto: str) -> bool:
    """
    Esta función verifica si los niveles de corchetes están balanceados
    en un 'texto' (str). Retorna True si para cada corchete que se
    abre existe un corchete que lo cierre. False para el caso
    contrario. (Ignora todo lo que no sean corchetes).
    PRECONDICIONES: Recibe un texto (string).
    POSCONDICIONES: Devuelve un bool (True o False).
    """
    
    # Verifico que el texto (variable 'texto') de entrada sea de tipo
    # string (str).
    assert (isinstance(texto, str)), "El 'texto' ingresado no es un string."
    
    # Declaro y defino una variable en la que se contará en qué "nivel"
    # se encuentra de los corchetes. Por ejemplo [nivel1[nivel2]].
    nivel: int = 0
    
    # Recorro todo el texto ingresado en el argumento de la función.
    for elemento in texto:
        
        # Si el elemento es el corchete que "abre", entonces el nivel
        # aumentará en 1.
        if (elemento == '['):
            
            nivel += 1
            
        # Sino, si es el corchete que "cierra", entonces el nivel
        # decrecerá en 1, sólo si ya hubo un símbolo de 'inicio'.
        elif (elemento == ']'):
            
            if (nivel > 0):
                
                nivel -= 1
            
    # Finalmente, se verifica que el nivel sea el mismo con el que
    # se comenzó (cero). Si se cumple, entonces retornará True, y
    # sino False.
    return (nivel == 0)


def hay_balanceo_especifico(texto: str,
                            inicio: str,
                            cierre: str) -> bool:
    """
    Esta función verifica si los niveles de un par de símbolos dados
    (sean corchetes, paréntesis o lo que se elija) están balanceados
    en un 'texto' (str). Retorna True si para cada símbolo que se
    "abre" existe otro que lo "cierre". False para el caso
    contrario. (Ignora todo lo que sea distinto a los símbolos o
    caracteres especificados en los argumentos 'inicio' y 'cierre').
    PRECONDICIONES: Recibe tres strings ('texto', 'inicio',
                    'cierre').
    POSCONDICIONES: Devuelve un bool (True o False).
    """
    
    # Verifico que el texto (variable 'texto') de entrada sea de tipo
    # string (str).
    assert (isinstance(texto, str)), "El 'texto' ingresado no es un string."
    
    # Verifico que el símbolo de "apertura" (variable 'inicio'),
    # ingresado en la entrada o argumento de la función, sea de tipo
    # string (str).
    assert (isinstance(inicio, str)), "El 'inicio' ingresado no es un string."
    
    # Verifico que el símbolo de "cierre" (variable 'cierre'),
    # ingresado en la entrada o argumento de la función, sea de tipo
    # string (str).
    assert (isinstance(cierre, str)), "El 'cierre' ingresado no es un string."
    
    # Verifico que los símbolos ingresados para el 'inicio' y 'cierre'
    # sean distintos. De esta manera, se puede distinguir si se "abre"
    # o se "cierra".
    assert (inicio != cierre), "Los símbolos de apertura y cierre no pueden ser iguales."
    
    # Verifico que la longitud del string 'inicio' sea 1.
    assert (len(inicio) == 1), "El símbolo de 'inicio' posee más de un caracter."
    
    # Verifico que la longitud del string 'cierre' sea 1.
    assert (len(cierre) == 1), "El símbolo de 'cierre' posee más de un caracter."
    
    # Declaro y defino una variable en la que se contará en qué "nivel"
    # se encuentra de los corchetes, paréntesis, o símbolo
    # especificado. Por ejemplo (nivel1(nivel2)).
    nivel: int = 0
    
    # Recorro todo el texto ingresado en el argumento de la función.
    for elemento in texto:
        
        # Si el elemento es el corchete que "abre", entonces el nivel
        # aumentará en 1.
        if (elemento == inicio):
            
            nivel += 1
            
        # Sino, si es el corchete que "cierra", entonces el nivel
        # decrecerá en 1, sólo si ya hubo un símbolo de 'inicio'.
        elif (elemento == cierre):
            
            if (nivel > 0):
                
                nivel -= 1
            
    # Finalmente, se verifica que el nivel sea el mismo con el que
    # se comenzó (cero). Si se cumple, entonces retornará True, y
    # sino False.
    return (nivel == 0)


def hay_balanceo_simultaneo(texto: str) -> bool:
    """
    Esta función verifica simultáneamente si los niveles de corchetes,
    paréntesis y llaves están balanceados en un 'texto' (str). Retorna
    True si para cada corchete, paréntesis y llave que se abre existe
    el caracter correspondiennte que lo cierre. False para el caso
    contrario. (Ignora todo lo que no sean corchetes, paréntesis
    o llaves).
    PRECONDICIONES: Recibe un texto (string).
    POSCONDICIONES: Devuelve un bool (True o False).
    """

    # Verifico que el texto (variable 'texto') de entrada sea de tipo
    # string (str).
    assert (isinstance(texto, str)), "El 'texto' ingresado no es un string."

    # Reutilizo la función en la que se puede especificar el
    # caracter de inicio y cierre, para verificar que esté
    # balanceado.
    return (hay_balanceo_especifico(texto, '[', ']') and
            hay_balanceo_especifico(texto, '(', ')') and
            hay_balanceo_especifico(texto, '{', '}'))


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    
    # Imprimo título:
    print("Ejercicio 5:\tCorchetes balanceados")
    
    # Input:
    print("Ingrese texto para verificar que los corchetes estén balanceados:")
    
    entrada: str = input()
    
    print(f"¿Está balanceado? {hay_balanceo_corchetes(entrada)}")


if __name__ == "__main__":
    principal()
