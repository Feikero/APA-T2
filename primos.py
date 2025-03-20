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


if __name__=="__main__":
    import doctest
    doctest.testmod()
