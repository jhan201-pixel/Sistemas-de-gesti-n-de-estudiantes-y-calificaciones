class Estudiante:
    """
    Clase estudiante con ID, nombre y lista de calificaciones.
    """

    def __init__(self, id_estudiante, nombre):
        """
        Inicializa un nuevo estudiante.
        
        Parámetros:
        id_estudiante (str): Identificador único del estudiante.
        nombre (str): Nombre completo del estudiante.
        """
        self.id = id_estudiante
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, nota):
        """
        Agrega una calificación a la lista del estudiante, si está en el rango 0.0 a 5.0.
        
        Parámetros:
        nota (float): Calificación a agregar.
        """
        if 0.0 <= nota <= 5.0:
            self.calificaciones.append(nota)
        else:
            print("❌ Error: La calificación debe estar entre 0.0 y 5.0")

    def calcular_promedio(self):
        """
        Calcula y retorna el promedio de calificaciones del estudiante.
        
        Retorna:
        float: Promedio de calificaciones, o 0.0 si no hay notas.
        """
        if len(self.calificaciones) == 0:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    def mostrar_informacion(self):
        """
        Muestra la información básica del estudiante y su promedio.
        """
        print(f"📄 ID: {self.id}")
        print(f"👤 Nombre: {self.nombre}")
        print(f"📚 Calificaciones: {self.calificaciones}")
        print(f"📈 Promedio: {self.calcular_promedio():.2f}")
