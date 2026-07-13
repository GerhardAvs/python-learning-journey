import os

def Menu():
    print('\n//////////////////////////////////////')
    print('//////  Turnos para la farmacia  ///////')
    print('////////////////////////////////////////')
    print('1.Tomar turno')
    print('2.Mostrar turnos')
    print('3.Salir')
    return int(input('Ingrese el numero de su opcion: '))
    
def decorator(funcion):  
    gen = funcion()
    def Texto_turnos():
        print("\nBuenos dias, su turno es: ")
        print(next(gen))
        print("Favor de tomar asiento")
    return Texto_turnos

def Elegir_Modulo():
    os.system('cls')
    print('1.Medicina')
    print('2.Cosmeticos')
    print('3.Facial')
    
    return int(input('Escoge una opcion: '))

@decorator
def Medicina():
    m = 0
    while True:
        m += 1
        yield f'M-{m}'
@decorator   
def Cosmeticos():
    c = 0
    while True:
        c += 1
        yield f'C-{c}'
        
@decorator   
def Facial():
    f = 0
    while True:
        f += 1
        yield f'F-{f}'

            
def Mostrar_turnos():
    pass



"""def Turno(opcion):
    global m, c, f
    while True:
        if opcion == 1: #Lista Medicina
            m += 1
            yield f'M-{m}'
                
        elif opcion == 2:#Lista Cosmeticos
            c += 1
            yield f'C-{c}'
                
        else: #Lista Facial
            f += 1
            yield f'F-{f}'"""