
import mysql.connector
from mysql.connector import Error
from decouple import config



class CuentaBancaria :
   def __init__(self, titular_de_la_cuenta, numero_de_cuenta, dni, monto) :
       self.titular_de_la_cuenta = titular_de_la_cuenta
       self.numero_de_cuenta = numero_de_cuenta
       self.dni = self.validar_dni=(dni)
       self.monto = self.validar_monto=(monto)

   @property
   def titular_de_la_cuenta(self):
       return self.titular_de_la_cuenta
   
   @titular_de_la_cuenta.setter
   def titular_de_la_cuenta(self, value):
        self.titular_de_la_cuenta = value.capitalize()

   @property
   def numero_de_cuenta(self):
        return self.numero_de_cuenta()
     
   @numero_de_cuenta.setter
   def numero_de_cuenta(self, value):
        self.numero_de_cuenta = value

   @property
   def dni(self):
       return self.dni()
     
   @dni.setter
   def dni(self, value):
        self._dni = self.validar_dni(value)
     
   @property
   def monto(self):
        return self.monto()
     
   @monto.setter
   def monto(self, value):
      self._monto = self.validar_monto(value)

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

   def validar_monto(self, monto):
        try:
            monto_num = float(monto)
            if monto_num < 0: 
                raise ValueError("Saldo Insuficiente.")
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
       return f"Cuenta Bancaria: { self.numero_de_cuenta }, Titular: {self.titular_de_la_cuenta}, DNI: {self.dni}, Saldo: ${self.monto}"

class CuentaBancariaCorriente (CuentaBancaria):
     def __init__(self, titular_de_la_cuenta,  numero_de_cuenta, dni, monto):
         super().__init__(titular_de_la_cuenta, numero_de_cuenta, dni, monto) 
     
     def depositar(self, monto):
        self.monto += monto
        print("Se han depositado ${monto} en la Cuenta {self.numero_de_cuenta}. Su Nuevo saldo: ${self.monto}.")

     def retirar(self, monto):
       if monto > self.monto:
           print("Fondos Insuficientes.")
       else:
            self.monto -= monto
            print("Se han retirado ${monto} de la cuenta {self.numero_de_cuenta}. Su Nuevo saldo: ${self.monto}")

     def obtener_saldo(self):
        return self.monto 

     def transferir(self, monto, cuenta_destino):
       if monto > self.monto:
            print("Fondos Insuficientes.")
       else:
        self.retirar -= monto
        cuenta_destino.depositar += monto
       print(f"Se transfirió ${monto} de {self.numero_de_cuenta} a la cuenta {cuenta_destino}. Su Nuevo saldo es: ${self.monto}")
      
class CuentaBancariaAhorro (CuentaBancaria) :
     def __init__(self, titular_de_la_cuenta,  numero_de_cuenta, dni, monto):
      super().__init__(self, titular_de_la_cuenta, numero_de_cuenta, dni, monto) 


     def depositar(self, monto):
         self.monto += monto
         print ("Se han depositado ${monto} en la Cuenta {self.numero_de_cuenta}. Su Nuevo saldo es: ${self.monto}")


     def retirar(self, monto) :
       if monto > self.monto:  
            print("Fondos Insuficientes.")
       else:
        self.monto -= monto
        print("Se han retirado ${monto} de la cuenta {self.numero_de_cuenta}. Su Nuevo saldo es: ${self.monto}")

     def obtener_saldo(self):
        return self.monto 

     def transferir(self, monto, cuenta_destino):
       if monto > self.monto:
             print("Fondos Insuficientes.")
       else:
           self.retirar -= monto
           cuenta_destino.depositar += monto
           print(f"Se transfirió ${monto} de {self.numero_de_cuenta} a la cuenta {cuenta_destino}. Su Nuevo saldo es: ${self.monto}")

class CuentasdeBancoCH:
    def __init__(self):
        self.host = config('DB_HOST')
        self.database = config('DB_NAME')
        self.user = config('DB_USER')
        self.password= config('DB_PASSWORD')
        self.port= config('DB_PORT')

    def connect(self):
        try:
            connection = mysql.connector.connect(
             host=self.host,
             database=self.database,
             user=self.user,
             password=self.password,
             port=self.port

         )
            if connection.is_connected():
             return connection


        except Error as e:
           print(f'Error al conectar a la base de datos: {e}')
           return None  

        self.datos = self.leer_datos()

    def leer_datos(self, dni):
        try:
          connection = self.connect()
          if connection:
              with connection.cursor(dictionary=True) as cursor:
                  cursor.execute('SELECT * FORM cliente WHERE DNI = %s', (dni))
                  cliente_data = cursor.fetchone()

                  if cliente_data:
                      cursor.execute('SELECT titular_de_la_cuenta FROM CuentaBancariaCorriente WHERE dni = %s', (dni))
                      cliente = cursor.fetchone()

                      if cliente: 
                          cliente_data['Titular de la Cuenta'] = cliente['Titular de la Cuenta']
                          cliente = CuentaBancariaCorriente(**cliente_data)
                      else:
                          cursor.execute('SELECT Cliente FROM CuentaBancariaAhorro WHERE dni = %s', (dni))
                          cliente = cursor.fetchone()
                  print(f'Cliente encontrado: {cliente}')       
          else:
              print(f'No se encontro titular de la cuenta con el DNI: {dni}')

        except Error as e:
            print(f'Error al leer datos del archivo: {e}')
        else: 
            return cliente
        finally:
          if connection.is_connected():
              connection.close()

    def guardar_datos(self):
         try:
            with open(self.archivo, 'w') as file:
                mysql.dump(self.datos, file, indent=4)
         except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
         except Exception as error:
            print(f'Error inesperado: {error}')

    def crear_cliente(self, cliente):
         try:
            connection = self.connect()
            if connection:
                with connection.cursor() as cursor:                  
                    cursor.execute('SELECT DNI FROM cliente WHERE DNI = %s', (cliente.dni,))
                    if cursor.fetchone():
                        print(f'Error ya existe un cliente con DNI {cliente.dni}')
                        return
                    
                    if isinstance(cliente, CuentaBancariaCorriente):
                        query = '''''
                        INSERT INTO CLIENTES (titular, numero de cuenta, dni, monto )
                          VALUES (%s, %s, %s, %s)'''''
           
                        cursor.execute(query, (cliente.titular_de_la_cuenta, cliente.numero_de_cuenta, cliente.dni, cliente.monto))

                        query = '''
                        INSERT INTO CuentaBancariaCorriente (dni, cliente)
                        VALUES (%s, %s) '''

                        cursor.execute(query, (cliente.titular_de_la_cuenta, cliente.numero_de_cuenta, cliente.dni, cliente.monto))

                    elif isinstance(cliente, CuentaBancariaAhorro):
                        query = '''
                        INSERT INTO CLIENTES (titular, numero de cuenta, dni, monto )
                        VALUES (%s, %s, %s, %s)'''
           
                        cursor.execute(query, (cliente.titular_de_la_cuenta, cliente.numero_de_cuenta, cliente.dni, cliente.monto))

                        query = '''
                        INSERT INTO CuentaBancariaAhorro (dni, cliente)
                        VALUES (%s, %s) '''

                        cursor.execute(query, (cliente.titular_de_la_cuenta, cliente.numero_de_cuenta, cliente.dni, cliente.monto))
                    
                    connection.commit()
                    print(f'Cliente {cliente.titular_de_la_cuenta} {cliente.numero_de_cuenta} creado correctamente.')


         except Exception as error:
               print(f'Error inesperado al crear cliente: {error}')

    def buscar_cliente(self, dni):
          return self.datos.get(dni, "Cliente no encontrado") 
   