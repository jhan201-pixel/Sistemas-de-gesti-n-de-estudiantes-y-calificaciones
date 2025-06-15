import json
import os
from ClassEstudianteAndGestor.Estudiante import Estudiante # <--- This is the correct import

class GestorEstudiantes:
    """
    Gestiona las operaciones relacionadas con los estudiantes, como agregar, buscar,
    ingresar calificaciones, eliminar, y ahora, persistencia de datos con JSON.
    """
    def __init__(self, archivo_json='estudiantes.json'):
        self.estudiantes = {}
        self.archivo_json = archivo_json
        self._cargar_estudiantes()

    def _cargar_estudiantes(self):
        if os.path.exists(self.archivo_json):
            try:
                with open(self.archivo_json, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for est_data in data:
                        estudiante = Estudiante.from_dict(est_data)
                        self.estudiantes[estudiante.id] = estudiante
                print(f"Estudiantes cargados desde {self.archivo_json}")
            except json.JSONDecodeError:
                print(f"Error al decodificar JSON en {self.archivo_json}. El archivo puede estar corrupto.")
                self.estudiantes = {}
            except Exception as e:
                print(f"Ocurrió un error al cargar estudiantes: {e}")
        else:
            print(f"No se encontró el archivo {self.archivo_json}. Iniciando con lista de estudiantes vacía.")

    def _guardar_estudiantes(self):
        try:
            data_to_save = [est.to_dict() for est in self.estudiantes.values()]
            with open(self.archivo_json, 'w', encoding='utf-8') as f:
                json.dump(data_to_save, f, indent=4)
            print(f"Estudiantes guardados en {self.archivo_json}")
        except Exception as e:
            print(f"Ocurrió un error al guardar estudiantes: {e}")

    def agregar_estudiante(self, id_est, nombre):
        if id_est not in self.estudiantes:
            self.estudiantes[id_est] = Estudiante(id_est, nombre)
            self._guardar_estudiantes()
            return True
        return False

    def buscar_estudiante(self, id_est):
        return self.estudiantes.get(id_est)

    def ingresar_calificacion(self, id_est, nota):
        estudiante = self.buscar_estudiante(id_est)
        if estudiante:
            if estudiante.agregar_calificacion(nota):
                self._guardar_estudiantes()
                return True
        return False

    def obtener_todos_los_estudiantes(self):
        return list(self.estudiantes.values())

    def eliminar_estudiante(self, id_est):
        if id_est in self.estudiantes:
            del self.estudiantes[id_est]
            self._guardar_estudiantes()
            return True
        return False