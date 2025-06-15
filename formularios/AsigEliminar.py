# formularios/AsigEliminar.py

import tkinter as tk
from tkinter import messagebox, font
import ClassEstudianteAndGestor.GestorEstudiantes as GestorEstudiantes

def mostrar_formulario_eliminar(parent_window, gestor_estudiantes):
    """
    Muestra el formulario para eliminar un estudiante.
    Actúa como un 'toggle': si ya está abierto, lo cierra; si está cerrado, lo abre.
    """
    # Lógica para eliminar cualquier frame de formulario existente y actuar como toggle
    if hasattr(parent_window, 'current_form_frame') and parent_window.current_form_frame is not None:
        # Si el formulario actual es el mismo que intentamos abrir, lo cerramos
        # y reseteamos la referencia, luego salimos.
        if parent_window.current_form_frame.winfo_exists(): # Asegura que el widget aún existe
            parent_window.current_form_frame.destroy()
            parent_window.current_form_frame = None
            return # Si ya estaba abierto, lo cerramos y salimos, no creamos uno nuevo.

    # Limpia otros widgets (excepto el logo de fondo) del cuerpo principal
    # Esto asegura que no queden widgets de formularios anteriores si se cambió entre funciones
    for widget in parent_window.cuerpo_principal.winfo_children():
        if hasattr(parent_window, 'label_logo') and widget != parent_window.label_logo:
            widget.destroy()
        elif not hasattr(parent_window, 'label_logo'):
            # Si label_logo aún no está definido, destruye todos los widgets
            widget.destroy()

    # Crea el frame del formulario de eliminación
    frame_eliminar = tk.Frame(parent_window.cuerpo_principal, bg="#f9f9f9", bd=2, relief="groove")
    frame_eliminar.place(relx=0.5, rely=0.5, anchor='center', width=500, height=250)
    parent_window.current_form_frame = frame_eliminar # Guarda la referencia al nuevo frame

    # Título del formulario
    titulo = tk.Label(frame_eliminar, text="Eliminar Estudiante", font=("Roboto", 16, "bold"),
                      bg="#f9f9f9", fg="#333")
    titulo.pack(pady=(20, 10))

    # Frame para los campos de entrada
    campos_frame = tk.Frame(frame_eliminar, bg="#f9f9f9")
    campos_frame.pack(pady=10)

    # Etiqueta y campo de entrada para el ID del estudiante
    tk.Label(campos_frame, text="ID Estudiante:", font=("Roboto", 12),
             bg="#f9f9f9", anchor="w", width=15).grid(row=0, column=0, padx=10, pady=10)
    
    entry_id = tk.Entry(campos_frame, font=("Roboto", 11), width=25)
    entry_id.grid(row=0, column=1, padx=10, pady=10)
    entry_id.focus_set()

    # Función interna para manejar la lógica de eliminación
    def eliminar():
        id_est = entry_id.get().strip()
        if id_est:
            if messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que quieres eliminar al estudiante con ID: {id_est}?"):
                if gestor_estudiantes.eliminar_estudiante(id_est):
                    messagebox.showinfo("Éxito", f"Estudiante con ID: {id_est} eliminado correctamente.")
                    
                    # CERRAR EL FORMULARIO DESPUÉS DE LA ELIMINACIÓN EXITOSA
                    if parent_window.current_form_frame is not None:
                        parent_window.current_form_frame.destroy()
                        parent_window.current_form_frame = None # Importante: resetear la referencia
                        
                else:
                    messagebox.showwarning("Error", f"No se pudo eliminar al estudiante con ID: {id_est}. Puede que no exista.")
            else:
                messagebox.showinfo("Cancelado", "Operación de eliminación cancelada.")
        else:
            messagebox.showwarning("Campo Vacío", "Por favor, ingresa el ID del estudiante a eliminar.")

    # Botón para eliminar
    btn_eliminar = tk.Button(frame_eliminar, text="Eliminar", command=eliminar,
                             bg="#dc3545", fg="white", font=("Roboto", 12, "bold"),
                             width=20, height=1, relief="flat", cursor="hand2")
    btn_eliminar.pack(pady=20)