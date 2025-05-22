import math

class Figura:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        
    def imprimir_detalles(self):
        print(f"Figura: {self.nombre}")
        print(f"Color: {self.color}")

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__("Circulo", color)
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Radio: {self.radio}")
        print(f"Área: {self.area():.2f}")
        print(f"Perímetro: {self.perimetro():.2f}")

class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__("Rectángulo", color)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Base: {self.base}")
        print(f"Altura: {self.altura}")
        print(f"Área: {self.area():.2f}")
        print(f"Perímetro: {self.perimetro():.2f}")

# Ejemplo de uso:
if __name__ == "__main__":
    c = Circulo("Rojo", 5)
    r = Rectangulo("Azul", 4, 6)
    c.imprimir_detalles()
    print()
    r.imprimir_detalles()
