import tkinter as tk
from tkinter import ttk
import ClassEstudianteAndGestor.GestorEstudiantes as GestorEstudiantes

def mostrar_formulario_consultar(parent_window, gestor_estudiantes):
    if hasattr(parent_window, 'current_form_frame') and parent_window.current_form_frame is not None:
        parent_window.current_form_frame.destroy()
        parent_window.current_form_frame = None
        return

    for widget in parent_window.cuerpo_principal.winfo_children():
        if hasattr(parent_window, 'label_logo') and widget != parent_window.label_logo:
            widget.destroy()
        elif not hasattr(parent_window, 'label_logo'):
            widget.destroy()

    frame_formulario = tk.Frame(parent_window.cuerpo_principal, bg="#f9f9f9")
    frame_formulario.place(relx=0.5, rely=0.5, anchor='center', width=750, height=550)

    parent_window.current_form_frame = frame_formulario

    titulo = tk.Label(frame_formulario, text="Consultar Estudiantes", font=("Roboto", 16, "bold"),
                      bg="#f9f9f9", fg="#333")
    titulo.pack(pady=(20, 10))

    tree_frame = tk.Frame(frame_formulario, bg="#ffffff", bd=1, relief="solid")
    tree_frame.pack(padx=20, pady=10, fill='both', expand=True)

    columnas = ("ID", "Nombre", "Calificaciones", "Promedio")
    tree = ttk.Treeview(tree_frame, columns=columnas, show="headings", selectmode="none")

    # Encabezados centrados
    tree.heading("ID", text="ID Estudiante", anchor=tk.CENTER)
    tree.heading("Nombre", text="Nombre", anchor=tk.CENTER)
    tree.heading("Calificaciones", text="Calificaciones", anchor=tk.CENTER)
    tree.heading("Promedio", text="Promedio", anchor=tk.CENTER)

    # Columnas con alineación coherente
    tree.column("ID", width=100, anchor=tk.CENTER)
    tree.column("Nombre", width=180, anchor=tk.CENTER)
    tree.column("Calificaciones", width=290, anchor=tk.CENTER)
    tree.column("Promedio", width=100, anchor=tk.CENTER)

    # Centramos visualmente el Treeview
    tree.pack(anchor='center', fill='both', expand=True)

    # Estilo
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background="#E8E8E8",
                    foreground="#333333",
                    rowheight=30,
                    fieldbackground="#E8E8E8",
                    bordercolor="#D3D3D3",
                    borderwidth=1)

    style.map('Treeview',
              background=[('selected', '#E8E8E8'), ('focus', '#E8E8E8')],
              foreground=[('selected', '#333333'), ('focus', '#333333')])

    style.configure("Treeview.Heading",
                    font=("Roboto", 11, "bold"),
                    background="#2e649b",
                    foreground="white",
                    relief="flat",
                    padding=(5, 5))

    style.map("Treeview.Heading",
              background=[('active', '#2e649b'), ('pressed', '#2e649b')],
              foreground=[('active', 'white'), ('pressed', 'white')])

    estudiantes = gestor_estudiantes.obtener_todos_los_estudiantes()

    if estudiantes:
        for estudiante in estudiantes:
            if estudiante.calificaciones:
                formatted_grades = [f"{cal:.2f}" for cal in estudiante.calificaciones]
                calificaciones_str = f"[{', '.join(formatted_grades)}]"
            else:
                calificaciones_str = "N/A"

            tree.insert("", tk.END, values=(
                estudiante.id,
                estudiante.nombre,
                calificaciones_str,
                f"{estudiante.calcular_promedio():.2f}"
            ))
    else:
        tk.Label(tree_frame, text="No hay estudiantes registrados para mostrar.",
                 font=("Roboto", 12), bg="#ffffff", fg="#666").pack(pady=20)

    btn_cerrar = tk.Button(frame_formulario, text="Cerrar",
                           command=lambda: parent_window.current_form_frame.destroy() if parent_window.current_form_frame else None,
                           bg="#dc3545", fg="white", font=("Roboto", 12, "bold"),
                           width=20, height=1, relief="flat", cursor="hand2")
    btn_cerrar.pack(pady=(5, 15))
