"""
Iker Martínez Rodríguez
Modulo que define funciones con números primos


>>> esPrimo(4)
False


>>> esPrimo(-2)
True
"""




def esPrimo(numero):
    """
    Devuelve True si el número dado es primo
    o False en caso contrario


    >>> esPrimo(1023)
    False


    >>> esPrimo(1021)
    True
    """
   
    for prova in range(2, numero):
        if numero % prova == 0:
            return False
    return True

def primos(numero):
    """
     Devuelve una tupla con todos los números primos 
     menores que su argumento.

     >>> primos(50)
     (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """

    if numero <= 1:
        return False
    
    return tuple([i for i in range (2, numero) if esPrimo(i)])


if __name__=="__main__":
    import doctest
    doctest.testmod()
