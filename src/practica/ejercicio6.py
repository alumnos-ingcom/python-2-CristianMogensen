################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. El Cifrado del Cesar
El cifrado César o cifrado de rotación usa una encriptación de
sustitución simple. Esto significa que cada caracter se sustituye
por otro caracter de acuerdo con un sistema especifico.

La codificación debe ser tal que la palabra codificada contenga
unicamente caracteres del tipo AZaz y 0 a 9, de manera que al
codificar las ultimas letras del abecedario se vuelva a las primeras
letras.

Por ejemplo, el método conocido y muy utilizado ROT13 rota el alfabeto
con 13 posiciones, resultando en A->N, B->O... Y->L y Z->M.

Implementar una funcion que codifique un texto rotandolo una cantidad
de posiciones ajustable.

Implementar la funcion que decodifique el texto rotado una cantidad
de posiciones ajustable.

Una buena forma para verificar este ejercicio es codificar y
decodificar un texto y compararlo con lo que fué ingresado
originalmente.

Tip: Implementar las funciones utilizando las funciones ord y chr.
"""


def ajustar_a_rango(numero: int, pasos: int, num1: int, num2: int):
    """
    Esta función verifica que un número (int) se encuentre dentro del
    rango ['num1', 'num2'] (ambos int's) y retorna un número entero
    dentro del rango. Para esto, se ubica al número sobre o debajo del
    extremo inferior, y si está debajo se le va a sumando al número
    una determinada cantidad de 'pasos' que le asigna un número
    adentro del rango mencionado.
    (FUNCIÓN AUXILIAR PARA EL CIFRADO)
    PRECONDICIONES: Recibe cuatro números enteros: (numero, pasos,
                    num1, num2).
    POSCONDICIONES: Devuelve un número entero (dentro del rango [num1,
                    num2].
    """

    # Verifico que 'numero' sea un entero (int).
    # Uso variable para cumplir con el formato de pycodestyle.
    error1: str = "El número debe ser un número entero (int)."
    assert (isinstance(numero, int)), error1

    # Verifico que 'pasos' (la cantidad de rotaciones) sea un entero
    # (int).
    # Uso variable para cumplir con el formato de pycodestyle.
    error2: str = "Los 'pasos' deben ser un número entero (int)."
    assert (isinstance(pasos, int)), error2

    # Verifico que 'num1' (extremo inferior) sea un entero (int).
    # Uso variable para cumplir con el formato de pycodestyle.
    error3: str = "'num1', extremo inferior, debe ser un número entero (int)."
    assert (isinstance(num1, int)), error3

    # Verifico que 'num2' (extremo superior) sea un entero (int).
    # Uso variable para cumplir con el formato de pycodestyle.
    error4: str = "'num2', extremo superior, debe ser un número entero (int)."
    assert (isinstance(num2, int)), error4

    # Verifico que 'num1' sea menor a 'num2'
    assert (num1 < num2), "Los extremos deben ser distintos y 'num1' < 'num2'."

    # Declaro y defino una variable en la que se verificará que ya
    # se haya sumado, al menos una vez, la cantidad de 'pasos' al
    # 'numero'.
    sumado = False

    # Mientras no se haya sumado la cantidad de pasos especificada
    # al menos una vez y el número no esté dentro del rango deseado
    # se ejecuta el bucle que intenta "meter" al número dentro de
    # ese rango, sumándole primero 'pasos'.
    while ((not sumado) or
           (numero < num1) or
           (num2 < numero)):

        # Verifico el caso en el que los pasos o rotaciones del
        # cifrado sea positivo (o cero también).
        if (pasos >= 0):

            # Si el número es menor al extremo superior, entonces se le
            # suma 'pasos' a 'numero'.
            if (numero <= num2):

                # Realizo la suma de los pasos.
                numero += pasos

                # Y confirmo que la suma ya fue hecha.
                sumado = True

            # Si el número es mayor al extremo superior, quiere decir que
            # hay que ajustarlo al rango (especificado por el usuario) sin
            # hacer antes una suma.
            # Por ejemplo: si se tiene un número fuera de rango como
            #              4 en [2, 3], entonces primero hay que asignarle
            #              el valor equivalente dentro del rango.
            #              En este ejemplo, el 4 es 1 unidad mayor al
            #              límite superior, por lo que debería volver a
            #              empezar desde el límite inferior y asignarle
            #              el equivalente de la diferencia entre el
            #              extremo superior y el número.
            #              Esto es, 4 = 3 + 1, entonces 1 sería el
            #              equivalente dentro del rango, y el 1 sería
            #              el primer elemento del rango (y este sería el
            #              2, que es el límite inferior).
            else:

                # Se calcula que tan fuera del rango está el número.
                distancia_a_extremo = numero - num2

                # Se le intenta asignar un equivalente dentro del
                # rango. (se verificará luego con el 'while')
                numero = num1 + distancia_a_extremo - 1

        # Si 'pasos' es negativo, entonces el comportamiento de la
        # función debería ser distinta.
        else:

            # Si el número es mayor al extremo inferior, entonces se le
            # suma 'pasos' a 'numero'.
            if (numero >= num1):

                # Realizo la suma de los pasos.
                numero += pasos

                # Y confirmo que la suma ya fue hecha.
                sumado = True

            # Si el número es menor al extremo inferior, quiere decir
            # que hay que ajustarlo al rango (especificado por el
            # usuario) sin hacer antes una suma.
            else:

                # Se calcula que tan fuera del rango está el número.
                distancia_a_extremo = abs(num1 - numero)

                # Se le intenta asignar un equivalente dentro del
                # rango. (se verificará luego con el 'while')
                numero = num2 - distancia_a_extremo + 1

    return numero


def codificar_cifrado(texto: str,
                      posiciones: int) -> str:
    """
    Esta función codifica un texto dado con una rotación en el cifrado
    especificada. Retorna el texto codificado.
    PRECONDICIONES: Recibe el texto (str) y las posiciones a rotar
                    (int). El texto sólo puede poseer caracteres de
                    la a-z, A-Z y 0-9.
    POSCONDICIONES: Devuelve el texto codificado (str).
    """

    # Verifico que el texto ingresado sea un string (str).
    # Uso variable para cumplir con el formato de pycodestyle.
    error1: str = "El 'texto' debe ser de tipo string (str)."
    assert (isinstance(texto, str)), error1

    # Verifico que el número de rotación del cifrado sea un número
    # entero (int).
    # Uso variable para cumplir con el formato de pycodestyle.
    error2: str = "La variable 'posiciones' debe ser de tipo entero (int)."
    assert (isinstance(posiciones, int)), error2

    # Declaro y defino la variable que almacenará el número
    # correspondiente al código ASCII de la letra 'A'.
    A: int = ord('A')

    # Declaro y defino la variable que almacenará el número
    # correspondiente al código ASCII de la letra 'Z'.
    Z: int = ord('Z')

    # Declaro y defino la variable que determina el tamaño del
    # alfabeto MAYÚSCULA.
    AZ: int = Z - A + 1

    # Declaro y defino la variable que almacenará el número
    # correspondiente al código ASCII de la letra 'a'.
    a: int = ord('a')

    # Declaro y defino la variable que almacenará el número
    # correspondiente al código ASCII de la letra 'z'.
    z: int = ord('z')

    # Declaro y defino la variable que determina el tamaño del
    # alfabeto MINÚSCULA.
    az: int = z - a + 1

    # Creo una lista para las letras MAYÚSCULAS.
    AZ_lista: list = []

    # Declaro y defino la variable que servirá como contador para los
    # elementos de la lista.
    elemento = 0

    # En el bucle se le agrega a la lista 'AZ_lista' cada letra
    # MAYÚSCULA del abecedario.
    while (elemento < AZ):

        AZ_lista.append(chr(A + elemento))

        elemento += 1

    # Creo una lista para las letras MINÚSCULAS.
    az_lista: list = []

    # Reinicio el contador a cero.
    elemento = 0

    # En el bucle se le agrega a la lista 'az_lista' cada letra
    # MINÚSCULA del abecedario.
    while (elemento < az):

        az_lista.append(chr(a + elemento))

        elemento += 1

    # Creo una lista para los números.
    numeros_lista: list = []

    # Reinicio el contador a cero.
    elemento = 0

    # En el bucle se le agrega a la lista 'numeros_lista' cada número.
    while (elemento <= 9):

        numeros_lista.append(chr(elemento + ord('0')))

        elemento += 1

    # De aquí en adelante comienza el cifrado.
    # Declaro y defino la variable en la que se guardará el resultado
    # del cifrado.
    resultado: str = ""

    # Para cada caracter en el texto se usa la lista adecuada para
    # luego cifrarlo.
    for caracter in texto:

        # Creo una variable que verifica si el caracter es "cifrable".
        # En otras palabras, que pertenezca a las listas definidas
        # anteriormente.
        cifrable: bool = False

        # Reinicio el contador utilizado anteriormente, para utilizarlo
        # para comparar con cada elemento de la lista correspondiente.
        elemento = 0

        # Verifico si el caracter es una letra y la cifro.
        while (elemento < len(AZ_lista)):

            # Comparo con las letras MAYÚSCULAS.
            if (caracter == AZ_lista[elemento]):

                resultado += AZ_lista[ajustar_a_rango(elemento,
                                                      posiciones,
                                                      0,
                                                      AZ - 1)]

                cifrable = True

                break

            # Comparo con las letras MINÚSCULAS.
            if (caracter == az_lista[elemento]):

                resultado += az_lista[ajustar_a_rango(elemento,
                                                      posiciones,
                                                      0,
                                                      az - 1)]

                cifrable = True

                break

            elemento += 1

        # Si no se pudo cifrar, verifico si se trata de un número y
        # lo cifro.
        if not cifrable:

            elemento = 0

            while (elemento < len(numeros_lista)):

                # Comparo con los números.
                if (caracter == numeros_lista[elemento]):

                    resultado += numeros_lista[ajustar_a_rango(elemento,
                                                               posiciones,
                                                               0, 9)]

                    cifrable = True

                    break

                elemento += 1

        # Si, finalmente, no se trata de un número ni una letra,
        # entonces dejo el caracter/símbolo así como está.
        if not cifrable:

            resultado += caracter

    return resultado


def decodificar_cifrado(texto_cifrado: str,
                        posiciones: int) -> str:
    """
    Esta función decodifica un texto dado con una rotación en el
    cifrado especificada. Retorna el texto decodificado.
    PRECONDICIONES: Recibe el texto (str) y las posiciones a rotar
                    (int). El texto sólo puede poseer caracteres de
                    la a-z, A-Z y 0-9.
    POSCONDICIONES: Devuelve el texto decodificado (str).
    """

    # Al tratarse de descifrar un texto anteriormente cifrado con el
    # mismo método, la función es análoga a la de codificar.

    # Verifico que el texto ingresado sea un string (str).
    # Uso variable para cumplir con el formato de pycodestyle.
    error1: str = "El 'texto' debe ser de tipo string (str)."
    assert (isinstance(texto_cifrado, str)), error1

    # Verifico que el número de rotación del cifrado sea un número
    # entero (int).
    # Uso variable para cumplir con el formato de pycodestyle.
    error2: str = "La variable 'posiciones' debe ser de tipo entero (int)."
    assert (isinstance(posiciones, int)), error2

    # Declaro y defino la variable que almacenará el número
    # correspondiente al código ASCII de la letra 'A'.
    A: int = ord('A')

    # Declaro y defino la variable que almacenará el número
    # correspondiente al código ASCII de la letra 'Z'.
    Z: int = ord('Z')

    # Declaro y defino la variable que determina el tamaño del
    # alfabeto MAYÚSCULA.
    AZ: int = Z - A + 1

    # Declaro y defino la variable que almacenará el número
    # correspondiente al código ASCII de la letra 'a'.
    a: int = ord('a')

    # Declaro y defino la variable que almacenará el número
    # correspondiente al código ASCII de la letra 'z'.
    z: int = ord('z')

    # Declaro y defino la variable que determina el tamaño del
    # alfabeto MINÚSCULA.
    az: int = z - a + 1

    # Creo una lista para las letras MAYÚSCULAS.
    AZ_lista: list = []

    # Declaro y defino la variable que servirá como contador para los
    # elementos de la lista.
    elemento = 0

    # En el bucle se le agrega a la lista 'AZ_lista' cada letra
    # MAYÚSCULA del abecedario.
    while (elemento < AZ):

        AZ_lista.append(chr(A + elemento))

        elemento += 1

    # Creo una lista para las letras MINÚSCULAS.
    az_lista: list = []

    # Reinicio el contador a cero.
    elemento = 0

    # En el bucle se le agrega a la lista 'az_lista' cada letra
    # MINÚSCULA del abecedario.
    while (elemento < az):

        az_lista.append(chr(a + elemento))

        elemento += 1

    # Creo una lista para los números.
    numeros_lista: list = []

    # Reinicio el contador a cero.
    elemento = 0

    # En el bucle se le agrega a la lista 'numeros_lista' cada número.
    while (elemento <= 9):

        numeros_lista.append(chr(elemento + ord('0')))

        elemento += 1

    # De aquí en adelante comienza el descifrado.
    # Declaro y defino la variable en la que se guardará el resultado
    # del descifrado.
    resultado: str = ""

    # Para cada caracter en el texto se usa la lista adecuada para
    # luego descifrarlo.
    for caracter in texto_cifrado:

        # Creo una variable que verifica si el caracter es
        # "descifrable". En otras palabras, que pertenezca a las
        # listas definidas anteriormente.
        descifrable: bool = False

        # Reinicio el contador utilizado anteriormente, para utilizarlo
        # para comparar con cada elemento de la lista correspondiente.
        elemento = 0

        # Verifico si el caracter es una letra y la descifro.
        while (elemento < len(AZ_lista)):

            # Comparo con las letras MAYÚSCULAS.
            if (caracter == AZ_lista[elemento]):

                resultado += AZ_lista[ajustar_a_rango(elemento,
                                                      -posiciones,
                                                      0,
                                                      AZ - 1)]

                descifrable = True

                break

            # Comparo con las letras MINÚSCULAS.
            if (caracter == az_lista[elemento]):

                resultado += az_lista[ajustar_a_rango(elemento,
                                                      -posiciones,
                                                      0,
                                                      az - 1)]

                descifrable = True

                break

            elemento += 1

        # Si no se pudo descifrar, verifico si se trata de un número y
        # lo descifro.
        if not descifrable:

            elemento = 0

            while (elemento < len(numeros_lista)):

                # Comparo con los números.
                if (caracter == numeros_lista[elemento]):

                    resultado += numeros_lista[ajustar_a_rango(elemento,
                                                               -posiciones,
                                                               0, 9)]

                    descifrable = True

                    break

                elemento += 1

        # Si, finalmente, no se trata de un número ni una letra,
        # entonces dejo el caracter/símbolo así como está.
        if not descifrable:

            resultado += caracter

    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Imprimo título:
    print("Ejercicio 5:\tEl Cifrado del Cesar")

    # Input:
    texto: str = str(input("Ingrese texto a codificar: "))
    codificado: str = codificar_cifrado(texto, 13)

    # Salida
    print(f"\nTexto ingresado: {texto}\n")
    print(f"Texto codificado: {codificado}\n")
    print(f"Texto decodificado: {decodificar_cifrado(codificado,13)}")


if __name__ == "__main__":
    principal()
