""" 
Generadores vs Funciones

Las funciones normales en Python utilizan return para devolver un resultado 
y terminan su ejecución inmediatamente. El valor retornado se guarda en memoria
y la función no puede continuar desde donde se quedó.

Los generadores, en cambio, utilizan yield para devolver valores uno por uno. 
En lugar de terminar la función, yield pausa su ejecución y guarda su estado 
para continuar después cuando se solicite el siguiente valor mediante next() 
o un ciclo for.

Los generadores son útiles cuando se trabajan con grandes cantidades de datos, 
ya que generan los valores bajo demanda y consumen menos memoria que una función 
que devuelve una lista completa.
"""

def mi_funcion():
    list = [x*10 for x in range(4)]
    return list

def mi_generador():
    for x in range(5):
        yield x*10
    
print(mi_funcion()) 
print(mi_generador())

g = mi_generador()
for _ in range(5):
    print(next(g))

# print(next(g)) 
# StopIteration Error al pedir un valor al generador cuando ya termino
