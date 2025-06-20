import json
import os
from ClassEstudianteAndGestor.Estudiante import Estudiante  # Importa la clase Estudiante correctamente

class GestorEstudiantes:
    """
    Gestiona operaciones sobre estudiantes:
    agregar, buscar, ingresar calificaciones, eliminar y guardar/cargar desde archivo JSON.
    """

    def __init__(self, archivo_json='estudiantes.json'):
        self.estudiantes = {}  # Diccionario para almacenar estudiantes por ID
        self.archivo_json = archivo_json  # Ruta del archivo JSON
        self._cargar_estudiantes()  # Carga datos existentes al iniciar

    def _cargar_estudiantes(self):
        """
        Carga estudiantes desde un archivo JSON, si existe.
        Maneja errores de archivo corrupto o ausente.
        """
        if os.path.exists(self.archivo_json):
            try:
                with open(self.archivo_json, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for est_data in data:
                        estudiante = Estudiante.from_dict(est_data)  # Crea instancia desde dict
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
        """
        Guarda todos los estudiantes actuales en el archivo JSON.
        Usa el método `to_dict()` de cada estudiante para serializarlo.
        """
        try:
            data_to_save = [est.to_dict() for est in self.estudiantes.values()]
            with open(self.archivo_json, 'w', encoding='utf-8') as f:
                json.dump(data_to_save, f, indent=4)
            print(f"Estudiantes guardados en {self.archivo_json}")
        except Exception as e:
            print(f"Ocurrió un error al guardar estudiantes: {e}")

    def agregar_estudiante(self, id_est, nombre):
        """
        Agrega un nuevo estudiante si el ID no está repetido.
        """
        if id_est not in self.estudiantes:
            self.estudiantes[id_est] = Estudiante(id_est, nombre)
            self._guardar_estudiantes()  # Guarda cambios
            return True
        return False

    def buscar_estudiante(self, id_est):
        """
        Busca y retorna el estudiante con el ID dado. Retorna None si no existe.
        """
        return self.estudiantes.get(id_est)

    def ingresar_calificacion(self, id_est, nota):
        """
        Agrega una calificación a un estudiante y guarda los cambios si es válido.
        """
        estudiante = self.buscar_estudiante(id_est)
        if estudiante:
            if estudiante.agregar_calificacion(nota):  # Valida la nota internamente
                self._guardar_estudiantes()
                return True
        return False

    def obtener_todos_los_estudiantes(self):
        """
        Devuelve la lista completa de estudiantes.
        """
        return list(self.estudiantes.values())

    def eliminar_estudiante(self, id_est):
        """
        Elimina un estudiante del diccionario y actualiza el archivo JSON.
        """
        if id_est in self.estudiantes:
            del self.estudiantes[id_est]
            self._guardar_estudiantes()
            return True
        return False
