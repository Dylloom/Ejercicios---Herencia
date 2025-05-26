class Transporte:
    def __init__(self, capacidad, velocidad_max):
        self.capacidad = capacidad
        self.velocidad_max = velocidad_max
        
    def detalles(self):
        return f"Capacidad: {self.capacidad}, Velocidad Máxima: {self.velocidad_max} km/h"
    
class Avion(Transporte):
    def __init__(self, capacidad, velocidad_max, nombre):
        super().__init__(capacidad, velocidad_max)
        self.nombre = nombre

    def tiempo_viaje(self, distancia):
        return distancia / self.velocidad_max
    
    def detalles(self):
        return print(f"{super().detalles()}"), print(f"Nombre: {self.nombre}")


class Barco(Transporte):
    def __init__(self, capacidad, velocidad_max, nombre):
        super().__init__(capacidad, velocidad_max)
        self.nombre = nombre
    
    def tiempo_viaje(self, distancia):
        return distancia / self.velocidad_max
    
    def detalles(self):
        return print(super().detalles()), print(f"Nombre: {self.nombre}")
        
if __name__ == "__main__":
    PA = Avion(100, 900, "Boeing 747")
    PE = Barco(10000, 50, "Titanic")
    PA.detalles()
    PE.detalles()
    distancia = 1000
    print(f"Tiempo de viaje en avión: {PA.tiempo_viaje(distancia)} horas")
    print(f"Tiempo de viaje en barco: {PE.tiempo_viaje(distancia)} horas")
