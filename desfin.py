''
import json
class CuentaBancaria :
   def __init__(self, titular_de_la_cuenta, numero_de_cuenta, dni, monto) :
     self.titular_de_la_cuenta = titular_de_la_cuenta
     self.numero_de_cuenta = numero_de_cuenta
     self.dni = self.validar_dni=(dni)
     self.monto = self.validar_monto=(monto)

     @property
     def titular_de_la_cuenta(self):
      return self.titular_de_la_cuentacapitalize()
     @property
     def numero_de_cuenta(self):
        return self.numero_de_cuenta()
     @property
     def dni(self):
       return self.dni()
     @property
     def monto(self):
        return self.monto()
     @monto.setter
     def monto(self, nuevo_monto):
      self.monto = self.validar_monto(nuevo_monto)

   def validar_dni(self, dni):
        try:
            dni_num = int(dni)
            if len(str(dni)) not in [7, 8]:
                raise ValueError("El DNI debe tener 7 u 8 dígitos.")
            if dni_num <=0:
                raise ValueError("El DNI debe ser número positivo.")
            return dni_num
        except ValueError as e:
            raise ValueError(f"El DNI es invalido: {e}")

   def validar_saldo(self, monto):
        try:
            monto_num = float(monto)
            if monto_num < 0: 
               raise ValueError("El saldo debe ser positivo.")
            return monto_num
        except ValueError as e:
            raise ValueError(f"Saldo inválido: {e}") 

   def to__dict(self):
     return {
        "Titular de la Cuenta" : self.titular_de_la_cuenta,
        "Número de Cuenta" : self.numero_de_cuenta,
        "DNI" : self.dni,
        "Saldo":  self.monto
     }

   def __str__(self):
    return f"Cuenta Bancaria: { self.numero_de_cuenta }, Titular: {self.titular_de_la_cuenta}, DNI: {self.dni}, Saldo: {self.monto}"

class CuentaBancariaCorriente (CuentaBancaria) :
     def __init__(self, titular_de_la_cuenta,  numero_de_cuenta, dni, monto):
      super().__init__(titular_de_la_cuenta, numero_de_cuenta, dni, monto) 

      self.titular_de_la_cuenta = titular_de_la_cuenta

     @property
     def numero_de_cuenta(self):
      return self.numero_de_cuenta
     
     def depositar(self, monto):
        if monto < 0:
           print("ERROR: monto no puede ser negativo")
        else:
         self.monto += monto
        print ("Se depositó {monto} en la cuenta {self.numero_de_cuenta}. Nuevo saldo es {self.monto}")


     def retirar(self, monto) :
        
       if monto < 0:
           print("ERROR: el monto no puede ser negativo")
       elif monto > self.monto:  
        print("ERROR: fondos insuficientes")
       else:
            self.monto += monto
       print("Se retiró {monto} en la cuenta {self.numero_de_cuenta}. Nuevo saldo es {self.monto}")


     def transferir(self, monto, otra_cuenta):
       if monto < 0:
           print("ERROR: el monto no puede ser negativo")
       elif monto > self.monto:
        print("ERROR: fondos insuficientes")
       if otra_cuenta not in CuentaBancaria:
        print("ERROR: Cuenta destino no existe.")
       else:
        self.monto -= monto
       CuentaBancaria[otra_cuenta].monto += monto
       print("Se transfirió {monto} en la cuenta {otra_cuenta}. Nuevo saldo es {self.monto}")


   
class CuentaBancariaAhorro (CuentaBancaria) :
     def __init__(self, titular_de_la_cuenta,  numero_de_cuenta, dni, monto):
      super().__init__(numero_de_cuenta, dni, monto) 
      self.titular_de_la_cuenta : titular_de_la_cuenta

     @property
     def numero_de_cuenta(self):
      return self.numero_de_cuenta
     
     def to_dict(self):
        data = super().to_dict()
        data["CuentaBancaria"] = self.monto
        return data

     def __str__(self):
        return f"{super().__str__()} - Cuenta Bancaria: {self.monto}"


     def depositar(self, monto):
        if monto < 0:
           print("ERROR: monto no puede ser negativo")
        else:
         self.monto += monto
        print ("Se depositó {monto} en la cuenta {self.numero_de_cuenta}. Nuevo saldo es {self.monto}")


     def retirar(self, monto) :
        
       if monto < 0:
           print("ERROR: el saldo no puede ser negativo")
       elif monto > self.monto:  
        print("ERROR: fondos insuficientes")
       else:
            self.monto += monto
       print("Se retiró {monto} en la cuenta {self.numero_de_cuenta}. Nuevo saldo es {self.monto}")


     def transferir(self, monto, otra_cuenta):
       if monto < 0:
           print("ERROR: el saldo no puede ser negativo")
       elif monto > self.monto:
        print("ERROR: fondos insuficientes")
       if otra_cuenta not in CuentaBancaria:
        print("ERROR: Cuenta destino no existe.")
       else:
        self.monto -= monto
       CuentaBancaria[otra_cuenta].monto += monto
       print("Se transfirió {monto} en la cuenta {otra_cuenta}. Nuevo saldo es {self.monto}")

class CuentasdeBancoCH:
 def __init__(self, archivo):
        self.archivo = archivo

def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                titular_de_la_cuenta = json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')
        else:
            return titular_de_la_cuenta

def guardar_datos(self, titular_de_la_cuenta):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(titular_de_la_cuenta, file, indent=4)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')

def crear_cliente(self, numero_de_cuenta, cliente):
        try:
            numero_de_cuenta = self.leer_datos()
            dni = cliente.dni
            if not str(dni) in numero_de_cuenta.keys():
                cliente[dni] = numero_de_cuenta.to_dict()
                self.guardar_numero_de_cuenta(numero_de_cuenta)
                print(f'Guardado exitoso')
            else:
                print(f'Colaborador con DNI {dni} ya existe')
        except Exception as error:
            print(f'Error inesperado al crear colaborador: {error}')

def eliminar_datos_titular(self, titular_de_la_cuenta, dni):
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

