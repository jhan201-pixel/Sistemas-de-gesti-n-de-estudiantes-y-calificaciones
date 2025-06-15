import tkinter as tk
from tkinter import messagebox, font
import ClassEstudianteAndGestor.GestorEstudiantes as GestorEstudiantes

def mostrar_formulario_ingresar_calificacion(parent_window, gestor_estudiantes):
    """
    Muestra un formulario para ingresar o actualizar la calificación de un estudiante.
    """
    if hasattr(parent_window, 'current_form_frame') and parent_window.current_form_frame is not None:
        parent_window.current_form_frame.destroy()
        parent_window.current_form_frame = None
        return

    for widget in parent_window.cuerpo_principal.winfo_children():
        if hasattr(parent_window, 'label_logo') and widget != parent_window.label_logo:
            widget.destroy()
        elif not hasattr(parent_window, 'label_logo'):
            widget.destroy()

    frame_formulario = tk.Frame(parent_window.cuerpo_principal, bg="#f9f9f9", bd=2, relief="groove")
    frame_formulario.place(relx=0.5, rely=0.5, anchor='center', width=500, height=300)

    parent_window.current_form_frame = frame_formulario

    titulo = tk.Label(frame_formulario, text="Ingresar Calificación", font=("Roboto", 16, "bold"), bg="#f9f9f9", fg="#333")
    titulo.pack(pady=(20, 10))

    campos_frame = tk.Frame(frame_formulario, bg="#f9f9f9")
    campos_frame.pack(pady=10)

    tk.Label(campos_frame, text="ID Estudiante:", font=("Roboto", 12), bg="#f9f9f9", anchor="w", width=18).grid(row=0, column=0, padx=10, pady=10)
    entry_id = tk.Entry(campos_frame, font=("Roboto", 11), width=25)
    entry_id.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(campos_frame, text="Calificación (0.0 - 5.0):", font=("Roboto", 12), bg="#f9f9f9", anchor="w", width=18).grid(row=1, column=0, padx=10, pady=10)
    entry_nota = tk.Entry(campos_frame, font=("Roboto", 11), width=25)
    entry_nota.grid(row=1, column=1, padx=10, pady=10)

    def ingresar_calificacion():
        id_est = entry_id.get().strip()
        try:
            nota = float(entry_nota.get().strip())
        except ValueError:
            messagebox.showerror("Error", "La calificación debe ser un número.")
            return

        if not id_est:
            messagebox.showwarning("Campo Vacío", "Por favor, ingresa el ID del estudiante.")
            return

        estudiante = gestor_estudiantes.buscar_estudiante(id_est)
        if estudiante:
            if 0.0 <= nota <= 5.0:
                if gestor_estudiantes.ingresar_calificacion(id_est, nota):
                    messagebox.showinfo("Éxito", f"Calificación {nota} agregada a {estudiante.nombre}.")
                    entry_nota.delete(0, tk.END)
                    entry_id.delete(0, tk.END)
                else:
                    # Mensaje específico si no se pudo agregar por el límite
                    messagebox.showwarning("Límite Alcanzado", f"El estudiante {estudiante.nombre} (ID: {estudiante.id}) ya tiene el máximo de {estudiante.MAX_CALIFICACIONES} calificaciones. No se puede ingresar más.")
                    entry_nota.delete(0, tk.END) # NUEVO: Borrar la nota
                    entry_id.delete(0, tk.END)   # NUEVO: Borrar el ID
            else:
                messagebox.showerror("Error", "La calificación debe estar entre 0.0 y 5.0.")
        else:
            messagebox.showerror("No encontrado", f"No se encontró estudiante con ID: {id_est}")

    btn_ingresar = tk.Button(frame_formulario, text="Ingresar Calificación", command=ingresar_calificacion,
                             bg="#28a745", fg="white", font=("Roboto", 12, "bold"),
                             width=22, height=1, relief="flat", cursor="hand2")
    btn_ingresar.pack(pady=20)
