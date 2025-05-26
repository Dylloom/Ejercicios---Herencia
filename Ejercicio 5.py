from datetime import datetime

class Producto:
    def __init__(self, nombre, precio, fecha):
        self.nombre = nombre
        self.precio = precio
        self.fecha = fecha
        
    def imprimir_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Fecha: {self.fecha}")

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, fecha): #GPH = gasto por kilometro
        super().__init__(nombre, precio, fecha)

        
    def descuento(self):
        fecha_actual = datetime.now()
        diferencia_dias = (fecha_actual - self.fecha).days
        if diferencia_dias > 30:
            return self.precio - (self.precio * 0.1)

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, fecha):
        super().__init__(nombre, precio, fecha)
    
    def descuento(self):
        fecha_actual = datetime.now()
        diferencia_dias = (fecha_actual - self.fecha).days
        if diferencia_dias > 60:
            return self.precio - (self.precio * 0.15 )
        else:
            return 0
        
if __name__ == "__main__":
    PA = ProductoAlimenticio("Manzana", 1.5, datetime(2024, 8, 1))
    PE = ProductoElectronico("Samsung", 1500, datetime(2023, 5, 15))
    PA.imprimir_detalles()
    descuento_alimenticio = PA.descuento()
    if descuento_alimenticio:
        print(f"Descuento alimenticio: {descuento_alimenticio}")
    else:
        print("No hay descuento alimenticio disponible.")
    print()
    PE.imprimir_detalles()
    descuento_electronico = PE.descuento()
    if descuento_electronico:
        print(f"Descuento electrónico: {descuento_electronico}")
    else:
        print("No hay descuento electrónico disponible.")
