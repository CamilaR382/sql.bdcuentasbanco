import os 
import platform 
from desfin import (CuentaBancaria, CuentaBancariaCorriente, CuentaBancariaAhorro)

def limpiar_pantalla():
    ''' Limpiar la Pantalla segun el sistema operativo '''
    if platform.system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

sistema = CuentaBancaria ('C:\Users\Usuario\Documents\Analisis de Datos ETAPA 3 2024\nueva carpeta\datos.json')
print("Crear nueva Cuenta Bancaria:")
titular_de_la_cuenta = input("Ingrese el nombre del titular: ")
numero_de_cuenta = input("Ingrese el número de cuenta: ")
dni = int(input("Ingrese el DNI: "))
monto = float(input("Ingrese el saldo inicial: "))

cuenta_corriente = CuentaBancariaCorriente(titular_de_la_cuenta, numero_de_cuenta, dni, monto)

sistema.crear_cliente(cuenta_corriente)

print("Crear nueva Cuenta de Ahorro:")
titular_de_la_cuenta = input("Ingrese el nombre del titular: ")
numero_de_cuenta = input("Ingrese el número de cuenta: ")
dni = input("Ingrese el DNI: ")
monto = float(input("Ingrese el saldo inicial: "))

cuenta_ahorro = CuentaBancariaAhorro(titular_de_la_cuenta, numero_de_cuenta, dni, monto)
sistema.crear_cliente(cuenta_ahorro)

deposito = float(input("\nIngrese el monto a depositar en la Cuenta Corriente: "))
cuenta_corriente.depositar(deposito)

retiro = float(input("\nIngrese el monto a retirar de la Cuenta : "))
cuenta_ahorro.retirar(retiro)

transferencia = float(input("\nIngrese el monto a transferir de la Cuenta de Ahorro a la Cuenta Corriente: "))
cuenta_ahorro.transferir(transferencia, cuenta_corriente)

print("\nInformación de las cuentas:")
print(cuenta_corriente)
print(cuenta_ahorro)

sistema.guardar_datos()

dni_buscar = input("\nIngrese el DNI para buscar la cuenta en el sistema: ")
print(sistema.buscar_cliente(dni_buscar))