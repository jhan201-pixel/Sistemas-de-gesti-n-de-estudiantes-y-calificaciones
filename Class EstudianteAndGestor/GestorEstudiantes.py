from Estudiante import Estudiante 
from Persistencia import guardar_estudiantes, cargar_estudiantes
class GestorEstudiantes:
    """
    Clase para gestionar una lista de estudiantes.
    """
    def __init__(self):
        """
        Inicializa una lista vacía de estudiantes.
        """
        self.estudiantes = cargar_estudiantes()

    def agregar_estudiante(self, id_estudiante, nombre):
        """
        Agrega un nuevo estudiante si no existe ya con ese ID.

        Parámetros:
        id_estudiante (str): ID único del estudiante.
        nombre (str): Nombre del estudiante.
        """
        if self.buscar_estudiante(id_estudiante):
            print("⚠️ Ya existe un estudiante con ese ID.")
            return
        nuevo = Estudiante(id_estudiante, nombre)
        self.estudiantes.append(nuevo)
        guardar_estudiantes(self.estudiantes)
        print("✅ Estudiante agregado.")

    def buscar_estudiante(self, id_estudiante):
        """
        Busca un estudiante por su ID.

        Parámetros:
        id_estudiante (str): ID a buscar.

        Retorna:
        Estudiante o None.
        """
        for est in self.estudiantes:
            if est.id == id_estudiante:
                return est
        return None

    def ingresar_calificacion(self, id_estudiante, nota):
        """
        Agrega una calificación a un estudiante existente.

        Parámetros:
        id_estudiante (str): ID del estudiante.
        nota (float): Calificación a agregar.
        """
        est = self.buscar_estudiante(id_estudiante)
        if est:
            est.agregar_calificacion(nota)
            guardar_estudiantes(self.estudiantes)
        else:
            print("❌ Estudiante no encontrado.")

    def eliminar_estudiante(self, id_estudiante):
        """
        Elimina un estudiante por su ID.

        Parámetros:
        id_estudiante (str): ID del estudiante a eliminar.
        """
        est = self.buscar_estudiante(id_estudiante)
        if est:
            self.estudiantes.remove(est)
            guardar_estudiantes(self.estudiantes)
            print("🗑️ Estudiante eliminado.")
        else:
            print("❌ Estudiante no encontrado.")

    def mostrar_todos(self):
        """
        Muestra la información de todos los estudiantes.
        """
        if not self.estudiantes:
            print("📭 No hay estudiantes registrados.")
            return
        for est in self.estudiantes:
            est.mostrar_informacion()
