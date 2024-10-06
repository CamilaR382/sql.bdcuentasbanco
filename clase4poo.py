
#crear una clase de colaborador tenemos una clase y definimos los atributos con self
'''''
class Colaborador: 
    def __init__(self, dni, nombre, apellido, edad, salario):
        self.dni = dni 
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad
        self.salario = salario
        #devuelve los atributos como diccionario
    def to__dict(self):
     return {
        "dni" : self.dni,
        "nombre" : self.nombre,
        "apellido": self.apellido,
        "edad" : self.edad,
        "salario" : self.salario
    }
## _ _ doble guion bajo es un atributo privado _ uno solo es publico
def __str__(self):
    return f"{self.nombre} {self.apellido}"
##
@salario.setter
def salario(self, nuevo_salario):
 self.__salario = self.validar_salario(nuevo_salario)

def validar_salario(self, salario):
   try:
      salario_num = float(salario)
      if salario_num <0:
       raise ValueError("El salario debe ser un numero positivo")
      return salario_num
   except ValueError:
      raise ValueError("El salario debe ser un numero valido")

def validar_dni(self, dni):
       try :
      dni_num = int(dni)
      
# nueva clase subclase

class ColaboradorTiempoCompleto(Colaborador):
   def __init__(self, dni, nombre, apellido, edad, salario, departamento):
      super().__init__(dni, nombre, apellido, edad, salario):
      self.__departamento = departamento
   @property
   def departamento(self):#
      return self.__departamento
   
   def to_dict(self):
      data = super().to_dict()
      data["dapartamento"] = self.departamento
      return data 
   def __str__(self):
     return f"{super().__str__()} - Departamento: {self.departamento}"

#una clase base dos clases q depend de la base y una cuarta q gestiona
#persistir los datos en archivo JSON
#import json
#dump datos que quiero guardar y en donde creo un atributo propio de json
'''
'''
Desafío 1: Sistema de Gestión de Colaborador

Objetivo: Desarrollar un sistema para gestionar colaboradores de una empresa.

Requisitos:
    • Crear una clase base Colaborador con atributos como nombre, apellido, edad, salario, etc.
    • Definir clases derivadas para diferentes tipos de empleados (por ejemplo, ColaboradorTiempoCompleto, ColaboradorTiempoParcial) con atributos y métodos específicos.
    • Implementar operaciones CRUD para gestionar los empleados.
    • Manejar errores con bloques try-except para validar entradas y gestionar excepciones (por ejemplo, salario negativo, longitud dni, etc).
    • Persistir los datos en archivo JSON.
'''
''