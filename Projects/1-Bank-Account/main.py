import sys
import Bank_Functions

while True:
    monto = 0
    
    match Bank_Functions.Menu():
        case 1:
            cuenta = Bank_Functions.crear_cliente(False)
        case 2:
            cuenta = Bank_Functions.crear_cliente(True)
        case 3:
            monto = float(input('Monto a depositar: '))
            cuenta.depositar(monto)
        case 4:
            monto = float(input('Monto a retirar: '))
            cuenta.retirar(monto)
        case 5:
            print(cuenta)
        case 6:
            sys.exit()