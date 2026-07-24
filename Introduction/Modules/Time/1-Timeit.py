""" 
Módulo timeit

El módulo timeit está diseñado para medir con precisión el tiempo
que tarda en ejecutarse un fragmento de código. A diferencia del módulo time,
timeit ejecuta el código varias veces y calcula el tiempo de forma más confiable,
reduciendo la influencia de otros procesos del sistema. Es una herramienta muy
utilizada para comparar el rendimiento de algoritmos, funciones o diferentes
formas de resolver un mismo problema. Sus funciones más importantes son timeit(),
que mide el tiempo de ejecución de un bloque de código repetido varias veces, y
repeat(), que realiza varias mediciones para obtener resultados más consistentes.
"""

import timeit

declaracion_for = """
prueba_for(10)
"""
mi_setup_for = """
def prueba_for(numero):

    lista = []
    
    for num in range(numero + 1):
        lista.append(num)
        
    return lista
"""
declaracion_while = """
prueba_while(10)
"""
mi_setup_while = """
def prueba_while(numero):
    lista = []
    contador = 1
    
    while contador <= numero:
        lista.append(contador)
        contador += 1
        
    return lista
"""
duracion_for = timeit.timeit(declaracion_for, mi_setup_for, number = 10000)
duracion_while = timeit.timeit(declaracion_while, mi_setup_while, number = 10000)

print(f"duracion de la prueba for: {duracion_for}")
print(f"duracion de la prueba while: {duracion_while}")



