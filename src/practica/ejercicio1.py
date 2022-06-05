################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Pares e impares
Escribir una función que retorne True cuando un número entero es par
y False cuando no lo sea, sin utilizar módulo. (%)
"""



def es_par(numero:int):
    """
    Verifica que un numero (int) sea par (devuelve True) o impar (devuelve False),
    sin utilizar el operador %.
    PRECONDICIONES: Número entero.
    POSCONDICIONES: Bool (True o False).
    """
    
    #Verifico que el número ingresado sea de tipo entero.
    assert type(numero)==int, "No es un numero entero (int)."
    
    #Declaro (y también defino momentáneamente) el resultado a devolver.
    resultado = False
    
    #'aux' es igual al módulo de 'numero' para no tener que hacer el caso especial
    #en el que el 'numero' ingresado sea un número negativo.
    aux = abs(numero)
    
    #En este bucle se le restan dos unidades (-2) a la variable 'aux' para que
    #en algún momento llegue al -2 (de esta forma incluye al caso en el que
    #sea 'numero'==0). Si es impar en algún momento llegaría al -1 (de esta
    #manera se incluyen a todos los casos de números positivos impares).
    while (True):
        
        aux -= 2
        
        if (aux == -1):
            
            resultado = False
            break
        
        elif (aux == -2):
            
            resultado = True
            break
        
    return resultado



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    
    #Imprimo título:
    print("Ejercicio 1:\tPares e impares")
    
    #Input:
    num = int(input("Ingrese número: "))
    
    #Algoritmo y salida:
    if (es_par(num)):
        print(f"Su número {num} es par.")
    else:
        print(f"Su número {num} es impar.")



if __name__ == "__main__":
    principal()
