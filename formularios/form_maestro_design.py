import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from PIL import Image, ImageTk


class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.logo_original = Image.open("./imagenes/logo.png")  # Usa PIL directamente
        self.logo = ImageTk.PhotoImage(self.logo_original)
        self.perfil = util_img.leer_imagen("./imagenes/perfil.png", (220, 220))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    def config_window(self):
        self.title('Sistema de Gestión de Estudiantes y Calificaciones')
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 1024, 700
        util_ventana.centrar_ventana(self, w, h)
        

    def paneles(self):
        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')
    
        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=190)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="Gestión De Calificaciones")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 12, "bold" ), bg=COLOR_BARRA_SUPERIOR, pady=10, width=26)
        self.labelTitulo.pack(side=tk.LEFT)

        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                        command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.labelTitulo = tk.Label(
            self.barra_superior, text="📧 https://github.com/jhan201-pixel/Sistemas-de-gesti-n-de-estudiantes-y-calificaciones.git")
        self.labelTitulo.config(fg="#ffffff", font=(
            "Segoe UI", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=77)
        self.labelTitulo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu =29
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=11)

        self.labelperfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelperfil.pack(side=tk.TOP, pady=35)

        self.buttonAgregar = tk.Button(self.menu_lateral)
        self.buttonBuscar = tk.Button(self.menu_lateral)
        self.buttonIngresar = tk.Button(self.menu_lateral)
        self.buttonConsultar = tk.Button(self.menu_lateral)
        self.buttonEliminar = tk.Button(self.menu_lateral)
        self.buttonAcerca = tk.Button(self.menu_lateral)

        buttons_info = [
        ("Agregar estudiante", "\uf234", self.buttonAgregar),
        ("Buscar estudiante", "\uf002", self.buttonBuscar),
        ("Ingresar o actualizar calificaciones", "\uf044", self.buttonIngresar),
        ("Consultar estudiantes", "\uf0c0", self.buttonConsultar),
        ("Eliminar estudiante", "\uf235", self.buttonEliminar),
        ("Acerca de", "\uf129", self.buttonAcerca)
        ]
        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button,text,icon,font_awesome,ancho_menu,alto_menu)
        
    
    def controles_cuerpo(self):
        self.label_logo = tk.Label(self.cuerpo_principal, image=self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        self.label_logo.place(x=0, y=0, relwidth=1, relheight=1)

        self.bind("<Configure>", self.redimensionar_logo)
    
    def redimensionar_logo(self, event=None):
        if hasattr(self, "logo_original"):
            ancho = self.cuerpo_principal.winfo_width()
            alto = self.cuerpo_principal.winfo_height()
            if ancho > 0 and alto > 0:
                imagen_redimensionada = self.logo_original.resize((ancho, alto), Image.ANTIALIAS)
                self.logo = ImageTk.PhotoImage(imagen_redimensionada)
                self.label_logo.config(image=self.logo)
            

    
    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f"{icon}   {text}", anchor = "w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP, padx=15, pady=5)
        self.bind_hover_events(button)
    
    def bind_hover_events(self, button):
        button.bind("<Enter>",lambda event: self.on_enter(event,button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))
    
    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')
    
    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

