"""
Práctica Generadores 3
Crea un generador que reste una a una las vidas de un personaje de videojuego,
y devuelva un mensaje cada vez que sea llamado:

"Te quedan 3 vidas"

"Te quedan 2 vidas"

"Te queda 1 vida"

"Game Over"

Almacena el generador en la variable perder_vida
"""

def restar_vida():
    i = 3
    while i > 0:
        yield f"Te quedan {i} vidas" if i > 1 else "Te queda 1 vida"
        i-=1
  
    yield "Game Over"
    
perder_vida = restar_vida()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
