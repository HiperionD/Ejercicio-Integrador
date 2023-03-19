class Persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre (self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad (self):
        return self.__edad
    
    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    @property
    def dni (self):
        return self.__dni
    
    @dni.setter
    def dni(self, valor):
        self.__dni = valor


    def mostrar(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"dni: {self.dni}")

    def Es_mayor_de_edad(self):
        return self.edad >= 18
    

p1 = Persona ("Luciano", 31, 37299299)

p1.mostrar()

if p1.Es_mayor_de_edad():
    print("La persona es mayor de edad")

else:
    print("La persona es menor de edad")

#ejercicio 7#
class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular (self):
        return self.__titular
    
    @titular.setter
    def titular(self, valor):
        self.__titular = valor

    @property
    def cantidad (self):
        return self.__cantidad
    

    def mostrar(self):
        print(f"titular: {self.titular}")
        print(f"cantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        self.__cantidad -= cantidad
        
c1 = Cuenta ("luciano", 25)

c1.ingresar(25)

c1.retirar(100)

c1.mostrar()

#ejercicio 8 #

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion = 0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion (self):
        return self.__bonificacion
    
    @bonificacion.setter
    def titular(self, valor):
        self.__bonificacion = valor

    def es_titular_valido(self):
        return self.titular.Es_mayor_de_edad() and self.titular.edad < 25
    
    def retirar(self, cantidad):
        return super().retirar(cantidad)
    

    
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print(f"Bonificación: {self.bonificacion}%")
        


cj1 = CuentaJoven("roberto", 25, 20)

cj1.mostrar()

