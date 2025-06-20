import tkinter as tk  # Librería principal para interfaces gráficas
from tkinter import font, messagebox, ttk

from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana  # Utilidad para centrar ventana
import util.util_imagenes as util_img     # Utilidad para cargar imágenes
from PIL import Image, ImageTk            # Manejo de imágenes con compatibilidad para Tkinter
import os
import sys  # Para compatibilidad con PyInstaller

import ClassEstudianteAndGestor.GestorEstudiantes as GestorEstudiantes
from ClassEstudianteAndGestor.Estudiante import Estudiante
from formularios.AsigBuscar import mostrar_formulario_buscar
from formularios.AsigIngresar import mostrar_formulario_ingresar_calificacion
from formularios.AsigConsultar import mostrar_formulario_consultar
from formularios.AsigEliminar import mostrar_formulario_eliminar

# Ruta absoluta de recursos (útil cuando se empaqueta con PyInstaller)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Carpeta temporal de PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Ventana principal de la aplicación
class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()

        # Carga de imágenes (logo y perfil)
        self.logo_original = Image.open(resource_path("./imagenes/logo.png"))
        self.logo = ImageTk.PhotoImage(self.logo_original.resize((200, 200), Image.LANCZOS))
        self.perfil = util_img.leer_imagen(resource_path("./imagenes/perfil.png"), (220, 220))

        self.gestor = GestorEstudiantes.GestorEstudiantes()
        self.acerca_logo = None
        self.current_form_frame = None

        # Cargar logo para "Acerca de"
        ico_path = resource_path("./imagenes/logo.ico")
        acerca_original_logo = Image.open(ico_path)
        self.acerca_logo = ImageTk.PhotoImage(acerca_original_logo.resize((240, 240), Image.LANCZOS))

        # Inicializar interfaz
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    # Configura propiedades generales de la ventana
    def config_window(self):
        self.title('Sistema de Gestión de Estudiantes y Calificaciones')
        self.iconbitmap(resource_path("./imagenes/logo.ico"))
        util_ventana.centrar_ventana(self, 1024, 700)

    # Crea los paneles principales: barra superior, menú lateral y cuerpo
    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=190)
        self.menu_lateral.pack(side=tk.LEFT, fill='both')

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    # Widgets de la barra superior
    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="Gestión De Calificaciones")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 12, "bold"), bg=COLOR_BARRA_SUPERIOR, pady=10, width=26)
        self.labelTitulo.pack(side=tk.LEFT)

        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.labelTitulo = tk.Label(self.barra_superior,
            text="📧 https://github.com/jhan201-pixel/Sistemas-de-gesti-n-de-estudiantes-y-calificaciones.git")
        self.labelTitulo.config(fg="#ffffff", font=("Segoe UI", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=77)
        self.labelTitulo.pack(side=tk.RIGHT)

    # Botones del menú lateral
    def controles_menu_lateral(self):
        ancho_menu = 29
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=11)

        self.labelperfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelperfil.pack(side=tk.TOP, pady=35)

        # Botones y comandos asociados
        self.buttonAgregar = tk.Button(self.menu_lateral, command=self.mostrar_formulario_agregar)
        self.buttonBuscar = tk.Button(self.menu_lateral, command=lambda: mostrar_formulario_buscar(self, self.gestor))
        self.buttonIngresar = tk.Button(self.menu_lateral, command=lambda: mostrar_formulario_ingresar_calificacion(self, self.gestor))
        self.buttonConsultar = tk.Button(self.menu_lateral, command=lambda: mostrar_formulario_consultar(self, self.gestor))
        self.buttonEliminar = tk.Button(self.menu_lateral, command=lambda: mostrar_formulario_eliminar(self, self.gestor))
        self.buttonAcerca = tk.Button(self.menu_lateral, command=self.mostrar_acerca_de)

        # Configuración común de los botones
        buttons_info = [
            ("Agregar estudiante", "\uf234", self.buttonAgregar),
            ("Buscar estudiante", "\uf002", self.buttonBuscar),
            ("Ingresar calificaciones", "\uf044", self.buttonIngresar),
            ("Consultar estudiantes", "\uf0c0", self.buttonConsultar),
            ("Eliminar estudiante", "\uf235", self.buttonEliminar),
            ("Acerca de", "\uf129", self.buttonAcerca)
        ]

        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)

    # Logo en el cuerpo principal
    def controles_cuerpo(self):
        self.label_logo = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.label_logo.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.redimensionar_logo)

    # Redimensiona el logo al cambiar el tamaño de la ventana
    def redimensionar_logo(self, event=None):
        if hasattr(self, "logo_original"):
            ancho = self.cuerpo_principal.winfo_width()
            alto = self.cuerpo_principal.winfo_height()
            if ancho > 0 and alto > 0:
                imagen_redimensionada = self.logo_original.resize((ancho, alto), Image.LANCZOS)
                self.logo = ImageTk.PhotoImage(imagen_redimensionada)
                self.label_logo.config(image=self.logo)

    # Configuración general de botones del menú
    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f"{icon}   {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP, padx=15, pady=5)
        self.bind_hover_events(button)

    # Efecto hover en botones
    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    # Ocultar/mostrar menú lateral
    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    # Formulario para agregar estudiante
    def mostrar_formulario_agregar(self):
        if self.current_form_frame is not None:
            self.current_form_frame.destroy()
            self.current_form_frame = None
            return

        for widget in self.cuerpo_principal.winfo_children():
            if widget != self.label_logo:
                widget.destroy()

        frame_formulario = tk.Frame(self.cuerpo_principal, bg="#f9f9f9", bd=2, relief="groove")
        frame_formulario.place(relx=0.5, rely=0.5, anchor='center', width=500, height=300)
        self.current_form_frame = frame_formulario

        titulo = tk.Label(frame_formulario, text="Registro de Estudiante",
                          font=("Roboto", 16, "bold"), bg="#f9f9f9", fg="#333")
        titulo.pack(pady=(20, 10))

        campos_frame = tk.Frame(frame_formulario, bg="#f9f9f9")
        campos_frame.pack(pady=10)

        tk.Label(campos_frame, text="ID Estudiante:", font=("Roboto", 12),
                 bg="#f9f9f9", anchor="w", width=15).grid(row=0, column=0, padx=10, pady=10)
        entry_id = tk.Entry(campos_frame, font=("Roboto", 12), width=25)
        entry_id.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(campos_frame, text="Nombre:", font=("Roboto", 12),
                 bg="#f9f9f9", anchor="w", width=15).grid(row=1, column=0, padx=10, pady=10)
        entry_nombre = tk.Entry(campos_frame, font=("Roboto", 12), width=25)
        entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        def guardar():
            id_est = entry_id.get().strip()
            nombre = entry_nombre.get().strip()
            if id_est and nombre:
                if self.gestor.agregar_estudiante(id_est, nombre):
                    messagebox.showinfo("Éxito", "Estudiante registrado correctamente.")
                    entry_id.delete(0, tk.END)
                    entry_nombre.delete(0, tk.END)
                    if self.current_form_frame is not None:
                        self.current_form_frame.destroy()
                        self.current_form_frame = None
                else:
                    messagebox.showerror("Error de Registro", f"El ID '{id_est}' ya está registrado.")
            else:
                messagebox.showwarning("Campos Vacíos", "Debes llenar ambos campos.")

        btn_guardar = tk.Button(frame_formulario, text="Guardar", command=guardar,
                                bg="#4CAF50", fg="white", font=("Roboto", 12, "bold"),
                                width=20, height=1, relief="flat", cursor="hand2")
        btn_guardar.pack(pady=20)

    # Vista "Acerca de"
    def mostrar_acerca_de(self):
        if self.current_form_frame is not None:
            self.current_form_frame.destroy()
            self.current_form_frame = None

        for widget in self.cuerpo_principal.winfo_children():
            if widget != self.label_logo:
                widget.destroy()

        acerca_frame = tk.Frame(self.cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
        acerca_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.current_form_frame = acerca_frame

        title_label = tk.Label(acerca_frame, text="Acerca de Nosotros",
                               font=("Roboto", 22, "bold"), bg=COLOR_CUERPO_PRINCIPAL, fg="#333")
        title_label.pack(pady=(30, 5))
        if self.acerca_logo:
            logo_label = tk.Label(acerca_frame, image=self.acerca_logo, bg=COLOR_CUERPO_PRINCIPAL)
            logo_label.pack(pady=2)
            logo_label.image = self.acerca_logo
        else:
            tk.Label(acerca_frame, text="[Logo no disponible]", font=("Roboto", 12, "italic"),
                     bg=COLOR_CUERPO_PRINCIPAL, fg="#999").pack(pady=10)

        phrase_label = tk.Label(acerca_frame, text="Si funciona, No lo toques",
                                font=("Roboto", 12, "bold", "italic"), bg=COLOR_CUERPO_PRINCIPAL, fg="#777")
        phrase_label.pack()
        developers_frame = tk.Frame(acerca_frame, bg=COLOR_CUERPO_PRINCIPAL)
        developers_frame.pack(pady=20)

        developers_title = tk.Label(developers_frame, text="Desarrollado por:",
                                    font=("Roboto", 16, "bold"), bg=COLOR_CUERPO_PRINCIPAL, fg="#555")
        developers_title.pack(pady=(20, 10))

        developer_names = ["Jhan Carlos Gomez", "Luis Flores", "Ronaldo Díaz", "Andres Suarez"]
        for name in developer_names:
            tk.Label(developers_frame, text=name,
                     font=("Roboto", 14), bg=COLOR_CUERPO_PRINCIPAL, fg="#666").pack(pady=5)

        version_label = tk.Label(acerca_frame, text="Sistema de Gestión de Estudiantes y Calificaciones v1.0",
                                 font=("Roboto", 10, "italic"), bg=COLOR_CUERPO_PRINCIPAL, fg="#888")
        version_label.pack(pady=(10, 0))
