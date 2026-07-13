import os
import Client_Class
from random import randint

def Menu():
    print('\n//////////////////////////////////////')
    print('//////  Turnos para la farmacia  ///////')
    print('////////////////////////////////////////')
    print('1.Crear cuenta')
    print('2.Iniciar sesion')
    print('3.Depositar')
    print('4.Retirar')
    print('5.Mostar datos')
    print('6.Salir')
    return int(input('Ingrese el numero de su opcion: '))

def crear_cliente(flag):
    os.system('cls')
    if flag == False:
        nombre = str(input('Deme su nombre: '))
        apellido = str(input('Deme su apellido: '))
        balance = 0
        cuenta = randint(100,1000)
        print(f'Cuenta creada con exito, numero de cuenta {cuenta}')
        
        return Client_Class.cliente(nombre,apellido, cuenta, balance)
    
    else:
        print('La cuenta inicio con exito')
        return Client_Class.cliente('Ger', 'Avs', 90107, 20450)
    
