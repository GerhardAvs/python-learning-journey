""" 
 
Práctica Generadores 1
Crea un generador (almacenado en la variable generador) que sea 
capaz de devolver una secuencia infinita de números, iniciando desde el 1, 
y entregando un número consecutivo superior cada vez que sea llamada mediante next.

Pista: Utiliza un loop while para realizar este ejercicio.

"""

def Inf_Secuence():
    i = 0
    while True:
        i += 1
        yield i
        
        
generador = Inf_Secuence()
print(next(generador))
print(next(generador))
