class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        
    def imprimir_detalles(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio): #GPH = gasto por kilometro
        super().__init__(marca, modelo, anio)
    
    def eficiencia_combustible(self, distancia_recorrida, litros_consumidos):
        if (litros_consumidos <= 0):
            raise ValueError("Los litros deben ser mayor a cero")
        return distancia_recorrida / litros_consumidos
    
    def combustible_necesario(self, distancia, eficiencia):
        if eficiencia < 0:
            raise ValueError("La eficiencia debe ser mayor a cero")
        return distancia / eficiencia

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo, anio)
    
    def eficiencia_combustible(self, distancia_recorrida, litros_consumidos):
        if (litros_consumidos <= 0):
            raise ValueError("Los litros deben ser mayor a cero")
        return distancia_recorrida / litros_consumidos
    
    def combustible_necesario(self, distancia, eficiencia):
        if eficiencia < 0:
            raise ValueError("La eficiencia debe ser mayor a cero")
        return distancia / eficiencia              

if __name__ == "__main__":
    a = Automovil("Toyota", "Corolla", 2020)
    m = Motocicleta("Honda", "CBR500R", 2022)
    print("Detalles del automovil:")
    a.imprimir_detalles()
    eficiencia_auto = a.eficiencia_combustible(450, 30)
    print(f"Eficiencia calculada: {eficiencia_auto:.2f} km/litro")
    distancia = 300
    print(f"Combustible necesario para {distancia} km: {a.combustible_necesario(distancia, eficiencia_auto):.2f} litros\n")
    
    print("Detalles de la motocicleta:")
    m.imprimir_detalles()
    eficiencia_moto = m.eficiencia_combustible(300, 10)
    print(f"Eficiencia calculada: {eficiencia_moto:.2f} km/litro")
    print(f"Combustible necesario para {distancia} km: {m.combustible_necesario(distancia, eficiencia_moto):.2f} litros")
