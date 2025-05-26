class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def asignar_rol(self, rol):
        self.rol = rol
    
    def mostrar_info_persona(self):
        return print(f"Nombre: {self.nombre}"), print(f"Apellido: {self.apellido}")
    
    def mostrar_info(self):
        self.mostrar_info_persona()
        return print(f"Rol: {self.rol}")
    
class Estudiante(Persona):
    def __init__(self, nombre, apellido, carrera): #GPH = gasto por kilometro
        super().__init__(nombre, apellido)
        self.carrera = carrera
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Asignatura: {self.carrera}")


class Profesor(Persona):
    def __init__(self, nombre, apellido, asignatura):
        super().__init__(nombre, apellido)
        self.asignatura = asignatura
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Carrera: {self.asignatura}")
        
if __name__ == "__main__":
    PA = Estudiante("Juan", "Perez", "Ingeniería Informática")
    PE = Profesor("Ezequiel", "Garcia", "Programación Avanzada")
    PA.asignar_rol("Estudiante")
    PE.asignar_rol("Profesor")
    PA.mostrar_info()
    print()
    PE.mostrar_info()
