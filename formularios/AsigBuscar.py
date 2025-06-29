import tkinter as tk
from tkinter import messagebox, font
import ClassEstudianteAndGestor.GestorEstudiantes as GestorEstudiantes

def mostrar_info_en_frame(parent_window, estudiante):
    # Cierra cualquier frame anterior activo
    if hasattr(parent_window, 'current_form_frame') and parent_window.current_form_frame is not None:
        parent_window.current_form_frame.destroy()

    # Crea un frame centrado para mostrar la información del estudiante
    frame_info = tk.Frame(parent_window.cuerpo_principal, bg="#ffffff", bd=2, relief="ridge",
                          highlightbackground="#AA7C64", highlightthickness=1)
    frame_info.place(relx=0.5, rely=0.5, anchor='center', width=400, height=290)
    parent_window.current_form_frame = frame_info

    # Fuentes personalizadas
    fuente_info = font.Font(family="Roboto", size=13)
    fuente_titulo = font.Font(family="Roboto", size=15, weight="bold")

    # Título del panel de información
    titulo = tk.Label(frame_info, text="Estudiante Encontrado", font=fuente_titulo, bg="#ffffff", fg="#007bff")
    titulo.pack(pady=(15, 10))

    # Datos del estudiante: ID, Nombre, Calificaciones, Promedio
    datos = [
        f"ID: {estudiante.id}",
        f"Nombre: {estudiante.nombre}",
        f"Calificaciones: {estudiante.calificaciones}",
        f"Promedio: {estudiante.calcular_promedio():.2f}"
    ]

    # Muestra cada dato en una línea con padding vertical
    for linea in datos:
        etiqueta = tk.Label(frame_info, text=linea, font=fuente_info, bg="#ffffff", fg="#333", justify="left")
        etiqueta.pack(padx=10, pady=6)

    # Botón para cerrar el panel informativo
    btn_cerrar = tk.Button(frame_info, text="Cerrar", command=lambda: cerrar_frame(parent_window),
                           font=("Roboto", 12, "bold"), bg="#dc3545", fg="white",
                           activebackground="#c82333", activeforeground="white",
                           relief="flat", width=15, height=1, cursor="hand2")
    btn_cerrar.pack(pady=10)

def cerrar_frame(parent_window):
    # Cierra el frame activo y limpia la referencia
    if hasattr(parent_window, 'current_form_frame') and parent_window.current_form_frame is not None:
        parent_window.current_form_frame.destroy()
        parent_window.current_form_frame = None

def mostrar_formulario_buscar(parent_window, gestor_estudiantes):
    # Cierra el formulario actual si ya existe
    if hasattr(parent_window, 'current_form_frame') and parent_window.current_form_frame is not None:
        parent_window.current_form_frame.destroy()
        parent_window.current_form_frame = None
        return

    # Elimina widgets previos excepto el logo
    for widget in parent_window.cuerpo_principal.winfo_children():
        if hasattr(parent_window, 'label_logo') and widget != parent_window.label_logo:
            widget.destroy()
        elif not hasattr(parent_window, 'label_logo'):
            widget.destroy()

    # Crea el frame del formulario de búsqueda
    frame_formulario = tk.Frame(parent_window.cuerpo_principal, bg="#f9f9f9", bd=2, relief="groove")
    frame_formulario.place(relx=0.5, rely=0.5, anchor='center', width=500, height=250)
    parent_window.current_form_frame = frame_formulario

    # Título del formulario
    titulo = tk.Label(frame_formulario, text="Buscar Estudiante", font=("Roboto", 16, "bold"),
                      bg="#f9f9f9", fg="#333")
    titulo.pack(pady=(20, 10))

    # Frame interno para el campo de entrada
    campos_frame = tk.Frame(frame_formulario, bg="#f9f9f9")
    campos_frame.pack(pady=10)

    # Campo para ingresar el ID del estudiante
    tk.Label(campos_frame, text="ID Estudiante:", font=("Roboto", 12),
             bg="#f9f9f9", anchor="w", width=15).grid(row=0, column=0, padx=10, pady=10)

    entry_id = tk.Entry(campos_frame, font=("Roboto", 11), width=25)
    entry_id.grid(row=0, column=1, padx=10, pady=10)

    # Función que busca el estudiante y muestra la información si lo encuentra
    def buscar():
        id_est = entry_id.get().strip()
        if id_est:
            estudiante_encontrado = gestor_estudiantes.buscar_estudiante(id_est)
            if estudiante_encontrado:
                mostrar_info_en_frame(parent_window, estudiante_encontrado)
            else:
                messagebox.showwarning("No Encontrado", f"No se encontró ningún estudiante con el ID: {id_est}")
        else:
            messagebox.showwarning("Campo Vacío", "Por favor, ingresa el ID del estudiante.")

    # Botón de búsqueda
    btn_buscar = tk.Button(frame_formulario, text="Buscar", command=buscar,
                           bg="#007bff", fg="white", font=("Roboto", 12, "bold"),
                           width=20, height=1, relief="flat", cursor="hand2")
    btn_buscar.pack(pady=20)