# from multipledispatch import dispatch

class Animal:
    #constructor con parametros
    def __init__(self, nombre:str, raza:str, edad:int, peso:float):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        
    # @dispatch(str, str, int, float)
    # def __init__(self, nombre, raza, edad, peso):
    #     self.nombre = nombre
    #     self.raza = raza
    #     self.edad = edad
    #     self.peso = peso
        
    def __init__(self, nombre=None, raza=None, edad=None, peso=None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    
    def get_nombre(self):
        return self.nombre
        
    def get_raza(self):
        return self.raza
    
    def get_edad(self):
        return self.edad   
    
    def get_peso(self):
        return self.peso  
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def set_raza(self, raza):
        self.raza = raza
        
    def set_edad(self, edad):
        self.edad = edad
        
    def set_edad(self, peso):
        self.peso = peso
                 
#Definir una instancia de tipo Animal para un objeto llamado perro
caballo = Animal("Zeus","Pura sangre",5,450)
#Definir una instancia de tipo Animal para un objeto llamado gato
leon = Animal("Boulder","Atlas",10,130)

print('-----------Caballo-----------')
print(caballo.get_nombre())
print(caballo.get_raza())
print(caballo.get_edad())
print(caballo.get_peso())

print('-----------Leon-----------')
print(leon.get_nombre())
print(leon.get_raza())
print(leon.get_edad())
print(leon.get_peso())

print('-----------Cambios del Caballo-----------')
caballo.set_raza('Caballo de Paso')
print(caballo.get_raza())

