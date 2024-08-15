from desfin import (CuentaBancaria, CuentaBancariaCorriente, CuentaBancariaAhorro, CuentasdeBancoCH)
sistema = CuentaBancaria('cuentas_bancarias.json')

sistema.mostrar_menu(CuentaBancaria, CuentaBancariaCorriente, CuentaBancariaAhorro, CuentasdeBancoCH)
def mostrar_menu():
 print('Menu CuentaBancaria')
print('1. Cuenta Bancaria')
print('2. Cuenta Corriente')
print('3. Cuenta de Ahorro')
print('4. Salir')
print('---------------------------------')


cuenta_corriente = CuentaBancaria()
sistema.crear_cliente()
print("Crear nueva Cuenta Bancaria:")
titular_de_la_cuenta = input("Ingrese el nombre del titular: ")
numero_de_cuenta = input("Ingrese el número de cuenta: ")
dni = input("Ingrese el DNI: ")
saldo = float(input("Ingrese el saldo inicial: "))

cuenta_corriente = CuentaBancariaCorriente()
sistema.crear_cliente()
print("Crear nueva Cuenta Bancaria:")
titular_de_la_cuenta = input("Ingrese el nombre del titular: ")
numero_de_cuenta = input("Ingrese el número de cuenta: ")
dni = input("Ingrese el DNI: ")
saldo = float(input("Ingrese el saldo inicial: "))

'''
def __init__(self, archivo):
  self.archivo = archivo

def leer_datos(self):
   try:
     with open(self.archivo, 'r') as file:
       datos = (file)
   except Exception as error:
       raise Exception(f'Error al leer datos del archivo: {error}')  
   else:
      return datos
   
def actualizar_datos_titular(self,numero_de_cuenta, monto):
 try:
     datos = self.leer_datos()
     if str(monto) in datos.keys():
       datos[numero_de_cuenta]['monto'] = monto
       self.guardar_datos(datos)
       print(f'Monto actualizado para el número de cuenta: {numero_de_cuenta}')
     else:
       print(f'No se encontró titular con numero de cuenta: {numero_de_cuenta}')
 except Exception as e:
   print(f'Error al actualizar el monto: {e}')

def eliminar_datos_titular(self, titular_de_la_cuenta):
  try:
   datos = self.leer_datos()
   if str(titular_de_la_cuenta) in datos.keys():
      datos[titular_de_la_cuenta]
      self.guardar_datos(datos)
      print(f'Titular de la Cuenta {titular_de_la_cuenta} eliminado correctamente')
   else:
      print(f'No se encontró titular de la cuenta con DNI: {dni}')
  except Exception as e:
   print(f'Error al eliminar Titular:{e}')
'''

cuenta_corriente = CuentaBancariaCorriente(titular_de_la_cuenta, numero_de_cuenta, dni, saldo)
sistema.crear_cliente(titular_de_la_cuenta)

print("Crear nueva Cuenta Corriente:")
titular_de_la_cuenta = input("Ingrese el nombre del titular: ")
numero_de_cuenta = input("Ingrese el número de cuenta: ")
dni = input("Ingrese el DNI: ")
saldo = float(input("Ingrese el saldo inicial: "))

cuenta_corriente = CuentaBancariaCorriente(titular_de_la_cuenta, numero_de_cuenta, dni, saldo)
sistema.crear_cliente(titular_de_la_cuenta)

print("\nCrear nueva Cuenta de Ahorro:")
titular_de_la_cuenta = input("Ingrese el nombre del titular: ")
numero_de_cuenta = input("Ingrese el número de cuenta: ")
dni = input("Ingrese el DNI: ")
saldo = float(input("Ingrese el saldo inicial: "))

cuenta_ahorro = CuentaBancariaAhorro(titular_de_la_cuenta, numero_de_cuenta, dni, saldo)
sistema.crear_cliente(cuenta_ahorro)

deposito = float(input("\nIngrese el monto a depositar en la Cuenta Corriente: "))
cuenta_corriente.depositar(deposito)

retiro = float(input("\nIngrese el monto a retirar de la Cuenta de Ahorro: "))
cuenta_ahorro.retirar(retiro)

transferencia = float(input("\nIngrese el monto a transferir de la Cuenta de Ahorro a la Cuenta Corriente: "))
cuenta_ahorro.transferir(transferencia, cuenta_corriente)

print("\nInformación de las cuentas:")
print(cuenta_corriente)
print(cuenta_ahorro)

sistema.guardar_datos()

dni_buscar = input("\nIngrese el DNI para buscar la cuenta en el sistema: ")
print(sistema.buscar_cliente(dni_buscar))

