""" 

Práctica Generadores 2
Crea un generador (almacenado en la variable generador) 
que sea capaz de devolver de manera indefinida múltiplos de 7, 
iniciando desde el mismo 7, y que cada vez que sea llamado devuelva 
el siguiente múltiplo (7, 14, 21, 28...).

"""

def multiplo_siete():
    i = 0
    while True:
        i += 7
        yield i

generador = multiplo_siete()