""" 
generadores

Los generadores son tipos especiales de funciones que
devuelven un iterador que no almacena su contenido
completo en memoria, sino que "demora" la ejecución de una
expresión hasta que su valor se solicita
"""

def gen():
    x = 1
    yield x
    
    x += 1
    yield x
    
    x += 1
    yield x
    
g = gen()
print(next(g))
print(next(g))
print(next(g))
