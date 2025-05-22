class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def emitir_sonido(self):
        return print(f"Este animal emite sonido")
        
    def imprimir_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Tipo: {self.__class__.__name__}")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    
    def emitir_sonido(self):
        return print("¡Guau, guau!")
               
    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Raza: {self.raza}")

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    
    def emitir_sonido(self):
        return print("¡Miau!")                

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Color: {self.color}")

if __name__ == "__main__":
    p = Perro("Zeus", 3, "Border Collie")
    g = Gato("Máximo Décimo Meridio", 1, "Naranja")
    p.imprimir_detalles()
    p.emitir_sonido()
    print()
    g.imprimir_detalles()
    g.emitir_sonido()
