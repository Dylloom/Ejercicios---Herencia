import math

class Empleado:
    def __init__(self, nombre, salario, cargo):
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo
        
    def imprimir_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")
        print(f"Cargo: {self.cargo}")

class Gerente(Empleado):
    def __init__(self, nombre, salario, rendimiento):
        super().__init__(nombre, salario, "Gerente")
        self.rendimiento = rendimiento
    
    def aumento(self):
        if (self.rendimiento >= 8):
            aumento = self.salario * 0.10
            self.salario = self.salario + aumento
            return print(f"Nuevo salario: {self.salario}")
        else:
            return print(f"No se dio un aumento")
            
    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Rendimiento del (1 al 10): {self.rendimiento}")

class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, salario, terminado):
        super().__init__(nombre, salario, "Empleado Temporal")
        self.terminado = terminado
    
    def aumento(self):
        if self.terminado > 4:
            aumento = self.terminado - 4
            aumento = aumento/100 + 0.10 
            if aumento > 0.5:
                aumento = 0.5
            self.salario = (self.salario * aumento) + self.salario
            return print(f"Nuevo salario: {self.salario}")
        else:
            return print(f"No se dio un aumento")
                    

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Trabajos Terminados: {self.terminado}")

# Ejemplo de uso:
if __name__ == "__main__":
    g = Gerente("Gabriel", 3000000, 9)
    e = EmpleadoTemporal("Juan", 1000000, 1000)
    g.imprimir_detalles()
    g.aumento()
    print()
    e.imprimir_detalles()
    e.aumento()
