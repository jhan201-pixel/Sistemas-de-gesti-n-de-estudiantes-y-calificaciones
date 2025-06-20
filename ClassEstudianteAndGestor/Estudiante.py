import json

class Estudiante:
    """
    Representa a un estudiante con su ID, nombre y una lista de calificaciones.
    """

    def __init__(self, id_est, nombre):
        self.id = id_est
        self.nombre = nombre
        self.calificaciones = []  # Lista para almacenar las calificaciones del estudiante
        self.MAX_CALIFICACIONES = 5  # Límite máximo de calificaciones permitidas por estudiante

    def agregar_calificacion(self, nota):
        """
        Agrega una calificación al estudiante si:
        - No ha superado el máximo de calificaciones
        - La nota está en el rango válido de 0.0 a 5.0

        Args:
            nota (float): La calificación a agregar.

        Returns:
            bool: True si la calificación se agregó correctamente, False si no.
        """
        if len(self.calificaciones) >= self.MAX_CALIFICACIONES:
            print(f"Advertencia: El estudiante {self.nombre} (ID: {self.id}) ya tiene el máximo de {self.MAX_CALIFICACIONES} calificaciones.")
            return False  # Límite alcanzado, no se permite agregar más

        if 0.0 <= nota <= 5.0:
            self.calificaciones.append(nota)
            return True
        return False  # Nota fuera de rango

    def calcular_promedio(self):
        """
        Calcula el promedio de las calificaciones del estudiante.

        Returns:
            float: El promedio o 0.0 si no hay calificaciones.
        """
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    def to_dict(self):
        """
        Convierte la instancia del estudiante a un diccionario, útil para guardar en JSON.

        Returns:
            dict: Representación serializable del estudiante.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "calificaciones": self.calificaciones
        }

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Estudiante a partir de un diccionario (al cargar desde JSON).

        Args:
            data (dict): Diccionario con claves 'id', 'nombre' y 'calificaciones'.

        Returns:
            Estudiante: Objeto estudiante creado desde los datos.
        """
        estudiante = Estudiante(data["id"], data["nombre"])
        estudiante.calificaciones = data.get("calificaciones", [])
        return estudiante

    def __str__(self):
        """
        Devuelve una representación en texto del estudiante.

        Returns:
            str: Cadena legible con ID, nombre y calificaciones.
        """
        return f"ID: {self.id}, Nombre: {self.nombre}, Calificaciones: {self.calificaciones}"
