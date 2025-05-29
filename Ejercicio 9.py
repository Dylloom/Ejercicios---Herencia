class Tienda:
    def __init__(self, Empleados, total_ventas=0):
        self.Empleados = Empleados
        self.Productos = {}
        self.total_ventas = total_ventas
        
    def informacion_general(self):
        return (f"Empleados: {self.Empleados}, Productos: {self.Productos}, Total Ventas: {self.total_ventas}")
    
class TiendaRopa(Tienda):
    def __init__(self, Empleados, total_ventas=0):
        super().__init__(Empleados, total_ventas)
        self.tipo = "Ropa"
    
    def informacion_general(self):
        return print(f"Tienda de {self.tipo}: {super().informacion_general()}")
    
    def agregar_producto(self, producto, precio):
        self.Productos[producto] = precio
        print(f"Producto {producto} agregado con precio {precio}.")
    
    def calcular_ventas(self, ventas):
        self.total_ventas += ventas
        print(f"Ventas totales actualizadas: {self.total_ventas}, Ganancia: {self.total_ventas * 30}")

class TiendaElectronica(Tienda):
    def __init__(self, Empleados, total_ventas=0):
        super().__init__(Empleados, total_ventas)
        self.tipo = "Electronica"
    
    def informacion_general(self):
        return print(f"Tienda de {self.tipo}: {super().informacion_general()}")
    
    def agregar_producto(self, producto, precio):
        self.Productos[producto] = precio
        print(f"Producto {producto} agregado con precio {precio}.")
    
    def calcular_ventas(self, ventas):
        self.total_ventas += ventas
        print(f"Ventas totales actualizadas: {self.total_ventas}, Ganancia: {self.total_ventas * 30}")
               
if __name__ == "__main__":
    TP = TiendaRopa(["Juan", "Emilia"])
    TE = TiendaElectronica(["Ernesto", "Alexander"])
    TP.informacion_general()
    TP.agregar_producto("Camisa", 20)
    TP.calcular_ventas(100)
    TP.informacion_general()
    print()
    TE.informacion_general()
    TE.agregar_producto("Televisor", 300)
    TE.calcular_ventas(500)
    TE.informacion_general()
