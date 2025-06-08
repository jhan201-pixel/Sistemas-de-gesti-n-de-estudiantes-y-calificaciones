import json
from Estudiante import Estudiante

def guardar_estudiantes(estudiantes, archivo="estudiantes.json"):
    data = []
    for est in estudiantes:
        data.append({
            "id": est.id,
            "nombre": est.nombre,
            "calificaciones": est.calificaciones
        })
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def cargar_estudiantes(archivo="estudiantes.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
            estudiantes = []
            for item in data:
                est = Estudiante(item["id"], item["nombre"])
                est.calificaciones = item["calificaciones"]
                estudiantes.append(est)
            return estudiantes
    except FileNotFoundError:
        return []
