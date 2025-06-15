import json

class Estudiante:
    """
    Representa a un estudiante con su ID, nombre y una lista de calificaciones.
    """
    def __init__(self, id_est, nombre):
        self.id = id_est
        self.nombre = nombre
        self.calificaciones = [] # Lista para almacenar las calificaciones
        self.MAX_CALIFICACIONES = 5 # Definir el límite máximo de calificaciones

    def agregar_calificacion(self, nota):
        """
        Agrega una calificación a la lista del estudiante si está en el rango válido (0.0 a 5.0)
        y si no se ha alcanzado el límite máximo de calificaciones.

        Args:
            nota (float): La calificación a agregar.

        Returns:
            bool: True si la calificación fue agregada, False en caso contrario (límite alcanzado o nota inválida).
        """
        # NUEVO: Verificar si ya se alcanzó el límite máximo de calificaciones
        if len(self.calificaciones) >= self.MAX_CALIFICACIONES:
            print(f"Advertencia: El estudiante {self.nombre} (ID: {self.id}) ya tiene el máximo de {self.MAX_CALIFICACIONES} calificaciones.")
            return False # No se puede agregar más calificaciones

        if 0.0 <= nota <= 5.0:
            self.calificaciones.append(nota)
            return True
        return False

    def calcular_promedio(self):
        """
        Calcula el promedio de las calificaciones del estudiante.
        """
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    def to_dict(self):
        """
        Convierte el objeto Estudiante a un diccionario para serialización JSON.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "calificaciones": self.calificaciones
        }

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Estudiante a partir de un diccionario (deserialización JSON).
        """
        estudiante = Estudiante(data["id"], data["nombre"])
        estudiante.calificaciones = data.get("calificaciones", [])
        return estudiante

    def __str__(self):
        """
        Devuelve una representación en cadena del estudiante.
        """
        return f"ID: {self.id}, Nombre: {self.nombre}, Calificaciones: {self.calificaciones}"