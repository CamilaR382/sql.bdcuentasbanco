import os 
import platform 
from desafiosql import (CuentaBancaria, CuentaBancariaCorriente, CuentaBancariaAhorro, CuentasdeBancoCH)

def limpiar_pantalla():
    if platform.system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu():
    print("========== Menú de Cuentas de Banco ==========")
    print('1. Crear Cuenta')
    print('2. Cuenta Bancaria Corriente')
    print('3. Cuenta de Ahorro')
    print('4. Depositar Dinero')
    print('5. Retirar Dinero')
    print('6. Ver Saldo')
    print('7. Transferir Dinero')
    print('8. Salir')
    print('======================================================')


def crear_cuenta(titular_de_la_cuenta, dni):
 try:
    titular_de_la_cuenta = input("Ingrese el nombre del titular: ")
    numero_de_cuenta = input("Ingrese el número de cuenta: ")
    dni = int(input("Ingrese el DNI: "))
    monto = float(input("Ingrese el saldo inicial: "))  
    if crear_cuenta == '1':
            titular_de_la_cuenta = input('Ingrese Apellido y Nombre del titular: ')
            numero_de_cuenta = CuentaBancaria(titular_de_la_cuenta, numero_de_cuenta, dni, monto)
            dni= int(input('Ingrese el DNI: '))
    else:
     print('Elija una opcion de la (4-8): ')
     
 except Exception as e:
  print('Error: {e}')

def cuenta_bancaria_corriente(titular_de_la_cuenta, dni):
 try:
    titular_de_la_cuenta = input("Ingrese el nombre del titular: ")
    numero_de_cuenta = input("Ingrese el número de cuenta: ")
    dni = int(input("Ingrese el DNI: "))
    monto = float(input("Ingrese el saldo inicial: "))  
    if crear_cuenta == '2':
            titular_de_la_cuenta = input('Ingrese Apellido y Nombre del titular: ')
            numero_de_cuenta = CuentaBancariaCorriente(titular_de_la_cuenta, numero_de_cuenta, dni, monto)
            dni= int(input('Ingrese el DNI: '))
    else:
     print('Elija una opcion de la (4-8): ')
     return
    mostrar_menu()
    input('Presione enter para continuar...')
 except Exception as e:
  print('Error: {e}')

def cuenta_ahorro(titular_de_la_cuenta, dni):
 try:
    titular_de_la_cuenta = input("Ingrese el nombre del titular: ")
    numero_de_cuenta = input("Ingrese el número de cuenta: ")
    dni = int(input("Ingrese el DNI: "))
    monto = float(input("Ingrese el saldo inicial: "))  
 
    if crear_cuenta == '3':
            titular_de_la_cuenta = input('Ingrese Apellido y Nombre del titular: ')
            numero_de_cuenta = CuentaBancariaAhorro(titular_de_la_cuenta, numero_de_cuenta, dni, monto)
            dni= int(input('Ingrese el DNI: '))
    else:
     print('Elija una opcion de la (4-8): ')
     return
    mostrar_menu()
    input('Presione enter para continuar...')
 except Exception as e:
  print('Error: {e}')


 print('=========================================')
 input('Presione enter...')

def depositar_dinero():
    dni = int(input("Ingrese DNI: "))
    monto = float(input("Ingrese Saldo a Depositar: "))
    monto.depositar(dni, monto)
    input('Presione enter')

def retirar_dinero():
    dni = int(input("Ingrese DNI: "))
    monto = float(input("Ingrese Saldo a Depositar: "))
    monto.retirar(dni, monto)
    input('Presione enter para continuar...')

def obtener_saldo(monto):
    dni = int(input('Ingrese el DNI del titular de la cuenta: {dni}. '))
    monto.obtener_monto(dni, monto)
    input('Presione enter para continuar...')
    
def transferir_saldo(monto, cuenta_origen, cuenta_destino):
    dni = int(input('Ingrese el DNI del titular de la cuenta: {dni}. '))
    monto.tranferir_monto(dni, cuenta_origen)
    numero_de_cuenta = input('Ingrese Numero de Cuenta Destino:  ')
    monto.tranferir_monto(numero_de_cuenta, cuenta_destino)
    input('Presione enter para continuar..')

mostrar_menu()
opcion = input('Seleccione una opcion: ')

def main():
  if __name__ == "__main__":
    cuenta = CuentasdeBancoCH()

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')
 
        if opcion == '1':
         crear_cuenta(titular_de_la_cuenta, dni)
         titular_de_la_cuenta = input('Introduce Titular de la Cuenta: ')
         cuenta [dni] = dni
         print('Cuenta creada para {dni} .') 
    
        elif opcion == '2':
         cuenta_bancaria_corriente(titular_de_la_cuenta, dni)
         titular_de_la_cuenta = titular_de_la_cuenta.get(dni)
         dni = int(input('Introduce DNI del titular: '))
        if dni:
          print(f'Saldo de {dni}: ${dni.obtener_monto}.')

        elif opcion == '3':
         cuenta_ahorro(titular_de_la_cuenta, dni)
         titular_de_la_cuenta = titular_de_la_cuenta.get(dni)
         dni = int(input('Introduce DNI del titular: '))
        if dni:
          print(f'Saldo de {dni}: ${dni.obtener_monto}.')

        elif opcion == '4':
         depositar_dinero()
         titular_de_la_cuenta = titular_de_la_cuenta.get(dni)
         dni = input('Introduce DNI del titular: ')
         monto = float(input('Introduce la cantidad a depositar: '))
        if dni:
          dni.depositar(monto)

        elif opcion == '5':
         retirar_dinero()
         titular_de_la_cuenta = titular_de_la_cuenta.get(dni)
         dni = input('Introduce DNI del titular: ')
         monto = float(input('Introduce la cantidad a retirar: '))
        if dni:
          dni.retirar(monto)

        elif opcion == '6':
         obtener_saldo()
         titular_de_la_cuenta = titular_de_la_cuenta.get(dni)
         dni = input('Introduce DNI del titular: ')
        if dni:
          print(f'Saldo de {dni}: ${dni.obtener_monto}.')

        elif opcion == '7':
         transferir_saldo()
         titular_de_la_cuenta = titular_de_la_cuenta.get(dni)
         numero_de_cuenta_origen = input('Introduce DNI del titular: ')
         numero_de_cuenta_destino = input('Introduce DNI: ')
         monto = float(input('Introduce la cantidad a transferir: '))
      
         cuenta_origen = cuenta.get(numero_de_cuenta_origen)
         cuenta_destino = cuenta.get(numero_de_cuenta_destino)

        if cuenta_origen and cuenta_destino:
          cuenta_origen.tranferir(monto, cuenta_destino)
          
          print('Una de las cuentas no se encuentra.')

        elif opcion == '8':
          print('Saliendo del programa.')
        else:
           print('Opción no válida. Intente de nuevo.')
  if __name__ == "__main__":
   main()

