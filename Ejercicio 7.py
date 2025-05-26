class Instrumento:
    def __init__(self, nombre, material):
        self.nombre = nombre
        self.material = material
        
    def tipo_sonido(self):
        return f"El {self.nombre} de {self.material} produce un sonido único."
    
class Guitarra(Instrumento):
    def __init__(self, nombre, material):
        super().__init__(nombre, material)
        
    def tocar_nota(self, nota):
        return f"Tocando la nota {nota} en la guitarra {self.nombre} de {self.material}."


class Piano(Instrumento):
    def __init__(self, nombre, material):
        super().__init__(nombre, material)
        
    def tocar_nota(self, nota):
        return f"Tocando la nota {nota} en el piano {self.nombre} de {self.material}."
        
if __name__ == "__main__":
    PA = Guitarra("Gibson", "Madera")
    PE = Piano("Yamaha", "Metal")
    print(PA.tipo_sonido())
    print(PA.tocar_nota("Do"))
    print()
    print(PE.tipo_sonido())
    print(PE.tocar_nota("Re"))
