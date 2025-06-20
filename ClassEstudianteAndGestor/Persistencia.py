import json
from .Estudiante import Estudiante

def guardar_estudiantes(estudiantes, archivo="estudiantes.json"):
    """
    Guarda una lista de objetos Estudiante en un archivo JSON.
    
    Args:
        estudiantes (list): Lista de instancias de Estudiante.
        archivo (str): Nombre del archivo donde se guardarán los datos.
    """
    data = []
    for est in estudiantes:
        # Convierte cada estudiante en un diccionario
        data.append({
            "id": est.id,
            "nombre": est.nombre,
            "calificaciones": est.calificaciones
        })
    # Guarda la lista de diccionarios como JSON en el archivo especificado
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)  # indent=4 hace el archivo más legible

def cargar_estudiantes(archivo="estudiantes.json"):
    """
    Carga los estudiantes desde un archivo JSON y devuelve una lista de objetos Estudiante.
    
    Args:
        archivo (str): Nombre del archivo desde donde se cargarán los datos.
    
    Returns:
        list: Lista de instancias de Estudiante.
    """
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)  # Carga la lista de diccionarios
            estudiantes = []
            for item in data:
                # Crea una instancia de Estudiante con los datos cargados
                est = Estudiante(item["id"], item["nombre"])
                est.calificaciones = item["calificaciones"]
                estudiantes.append(est)
            return estudiantes
    except FileNotFoundError:
        # Si no existe el archivo, devuelve una lista vacía
        return []
