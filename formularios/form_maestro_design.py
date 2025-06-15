import tkinter as tk # Importa la librería Tkinter para crear interfaces gráficas
from tkinter import font, messagebox, ttk # Importa módulos específicos de Tkinter:
                                          # - font: para manejar fuentes personalizadas.
                                          # - messagebox: para mostrar cuadros de diálogo (alertas, información).
                                          # - ttk: para widgets con estilo más moderno (aunque en este código no se usa directamente ttk.Entry, se importa por si acaso).

# Importa configuraciones de colores y utilidades desde otros archivos del proyecto
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana # Módulo con funciones de utilidad para la ventana (centrado, etc.)
import util.util_imagenes as util_img     # Módulo con funciones de utilidad para cargar y procesar imágenes
from PIL import Image, ImageTk            # Módulos de Pillow para manejo de imágenes:
                                          # - Image: para abrir y manipular imágenes.
                                          # - ImageTk: para convertir imágenes de Pillow a un formato que Tkinter pueda usar.
import os
# Importa las clases relacionadas con la gestión de estudiantes
import ClassEstudianteAndGestor.GestorEstudiantes as GestorEstudiantes # Clase para manejar la lógica de negocio de los estudiantes
from ClassEstudianteAndGestor.Estudiante import Estudiante         # Clase que representa a un estudiante individual
from .AsigBuscar import mostrar_formulario_buscar
from formularios.AsigIngresar import mostrar_formulario_ingresar_calificacion # Importa la clase que maneja el ingreso de calificaciones
from formularios.AsigConsultar import mostrar_formulario_consultar
from formularios.AsigEliminar import mostrar_formulario_eliminar # Importa la clase que maneja la eliminación de estudiantes
 # Importa la función para mostrar información de un estudiante en un frame
# Importa la función para mostrar información de un estudiante en un frame
# Define la clase principal de la aplicación, que hereda de tk.Tk (la ventana raíz de Tkinter)
class FormularioMaestroDesign(tk.Tk):
    # Constructor de la clase, se ejecuta al crear una instancia de FormularioMaestroDesign
    def __init__(self):
        super().__init__() # Llama al constructor de la clase padre (tk.Tk) para inicializar la ventana principal
        
        # --- Carga y preparación de imágenes ---
        # Carga la imagen del logo desde el archivo y la almacena en self.logo_original (objeto PIL Image)
        self.logo_original = Image.open("./imagenes/logo.png")
        
        # Define un tamaño inicial por defecto para el logo.
        # Aunque el logo se redimensionará dinámicamente, es bueno tener un tamaño inicial.
        initial_logo_size = (200, 200) 
        # Convierte la imagen original redimensionada a un formato compatible con Tkinter (PhotoImage)
        # Image.LANCZOS es un filtro de alta calidad para redimensionamiento.
        self.logo = ImageTk.PhotoImage(self.logo_original.resize(initial_logo_size, Image.LANCZOS))
        
        # Carga la imagen de perfil usando una función de utilidad y la redimensiona a (220, 220)
        self.perfil = util_img.leer_imagen("./imagenes/perfil.png", (220, 220))
        
        # Crea una instancia del gestor de estudiantes, que manejará las operaciones de los estudiantes
        self.gestor = GestorEstudiantes.GestorEstudiantes()
        self.acerca_logo = None 
        # Variable para mantener la referencia al formulario de registro actual.
        # Se inicializa en None; si hay un formulario abierto, apuntará a ese frame.
        self.current_form_frame = None
        ico_path = "./imagenes/logo.ico"
        print(f"DEBUG: Intentando cargar {ico_path}")
        print(f"DEBUG: Existe el archivo '{ico_path}'? {os.path.exists(ico_path)}")
        print(f"DEBUG: Directorio actual: {os.getcwd()}")
        acerca_original_logo = Image.open(ico_path)
        logo_size = (240, 240) 
        self.acerca_logo = ImageTk.PhotoImage(acerca_original_logo.resize(logo_size, Image.LANCZOS))
    
        # --- Configuración inicial de la interfaz ---
        self.config_window()             # Configura propiedades de la ventana principal (título, icono, tamaño)
        self.paneles()                   # Crea los paneles principales (barra superior, menú lateral, cuerpo principal)
        self.controles_barra_superior()  # Añade los widgets a la barra superior
        self.controles_menu_lateral()    # Añade los widgets al menú lateral
        self.controles_cuerpo()          # Añade los widgets al cuerpo principal (inicialmente el logo)

    # Configura las propiedades básicas de la ventana principal
    def config_window(self):
        self.title('Sistema de Gestión de Estudiantes y Calificaciones') # Establece el título de la ventana
        self.iconbitmap("./imagenes/logo.ico")                           # Establece el icono de la ventana
        w, h = 1024, 700                                                # Define el ancho y alto deseado de la ventana
        util_ventana.centrar_ventana(self, w, h)                        # Centra la ventana en la pantalla utilizando una función de utilidad
        
    # Crea los tres paneles principales de la interfaz: barra superior, menú lateral y cuerpo principal
    def paneles(self):
        # Frame para la barra superior
        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=50) # Color de fondo y altura definidos en config.py
        self.barra_superior.pack(side=tk.TOP, fill='both') # Empaqueta el frame en la parte superior, llenando horizontalmente
    
        # Frame para el menú lateral
        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=190) # Color de fondo y ancho definidos
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) # Empaqueta el frame a la izquierda, llenando verticalmente

        # Frame para el cuerpo principal, donde se mostrará el contenido dinámico
        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL) # Color de fondo principal definido
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True) # Empaqueta el frame a la derecha, llenando todo el espacio restante

    # Configura y añade los controles (widgets) a la barra superior
    def controles_barra_superior(self):
        # Define una fuente personalizada para iconos (FontAwesome)
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta para el título de la aplicación en la barra superior
        self.labelTitulo = tk.Label(self.barra_superior, text="Gestión De Calificaciones")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 12, "bold" ), bg=COLOR_BARRA_SUPERIOR, pady=10, width=26) # Configuración de estilo
        self.labelTitulo.pack(side=tk.LEFT) # Empaqueta a la izquierda

        # Botón para alternar la visibilidad del menú lateral (icono de menú)
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                         command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT) # Empaqueta a la izquierda

        # Etiqueta para mostrar la URL del repositorio de GitHub (información de contacto/proyecto)
        self.labelTitulo = tk.Label(
            self.barra_superior, text="📧 https://github.com/jhan201-pixel/Sistemas-de-gesti-n-de-estudiantes-y-calificaciones.git")
        self.labelTitulo.config(fg="#ffffff", font=(
            "Segoe UI", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=77) # Configuración de estilo
        self.labelTitulo.pack(side=tk.RIGHT) # Empaqueta a la derecha

    # Configura y añade los controles (botones) al menú lateral
    def controles_menu_lateral(self):
        ancho_menu =29 # Ancho de los botones del menú
        alto_menu = 2  # Alto de los botones del menú
        font_awesome = font.Font(family='FontAwesome', size=11) # Fuente para los iconos de los botones

        # Etiqueta para mostrar la imagen de perfil en el menú lateral
        self.labelperfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL) # Imagen y color de fondo
        self.labelperfil.pack(side=tk.TOP, pady=35) # Empaqueta en la parte superior con padding

        # Creación de los botones del menú lateral
        # Se asocia self.mostrar_formulario_agregar al comando del botón "Agregar estudiante"
        self.buttonAgregar = tk.Button(self.menu_lateral,command=self.mostrar_formulario_agregar)
        self.buttonBuscar = tk.Button(self.menu_lateral,command=lambda: mostrar_formulario_buscar(self, self.gestor))
        self.buttonIngresar = tk.Button(self.menu_lateral,command=lambda: mostrar_formulario_ingresar_calificacion(self, self.gestor))
        self.buttonConsultar = tk.Button(self.menu_lateral,command=lambda: mostrar_formulario_consultar(self, self.gestor))
        self.buttonEliminar = tk.Button(self.menu_lateral,command=lambda: mostrar_formulario_eliminar(self, self.gestor))
        self.buttonAcerca = tk.Button(self.menu_lateral, command=self.mostrar_acerca_de)

        # Lista de tuplas con la información para cada botón: (texto, icono, objeto botón)
        buttons_info = [
            ("Agregar estudiante", "\uf234", self.buttonAgregar),
            ("Buscar estudiante", "\uf002", self.buttonBuscar),
            ("Ingresar calificaciones", "\uf044", self.buttonIngresar),
            ("Consultar estudiantes", "\uf0c0", self.buttonConsultar),
            ("Eliminar estudiante", "\uf235", self.buttonEliminar),
            ("Acerca de", "\uf129", self.buttonAcerca)
        ]
        
        # Itera sobre la lista y configura cada botón usando la función auxiliar configurar_boton_menu
        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button,text,icon,font_awesome,ancho_menu,alto_menu)
        
    # Configura y añade el logo de fondo al cuerpo principal
    def controles_cuerpo(self):
        # El label_logo debe ser un tk.Label para que la lógica de limpiar widgets (winfo_children)
        # lo detecte y la función mostrar_formulario_agregar lo respete (no lo destruya).
        self.label_logo = tk.Label(self.cuerpo_principal, image=self.logo,
                             bg=COLOR_CUERPO_PRINCIPAL) # Asigna la imagen y el color de fondo principal
        # place permite posicionar el widget de forma relativa al padre, cubriendo todo el espacio
        self.label_logo.place(x=0, y=0, relwidth=1, relheight=1)

        # Asocia el evento de redimensionamiento de la ventana a la función redimensionar_logo
        self.bind("<Configure>", self.redimensionar_logo)
    
    # Redimensiona el logo de fondo cuando la ventana cambia de tamaño
    def redimensionar_logo(self, event=None):
        # Verifica si self.logo_original existe para evitar errores si la imagen no se cargó
        if hasattr(self, "logo_original"):
            ancho = self.cuerpo_principal.winfo_width()  # Obtiene el ancho actual del cuerpo principal
            alto = self.cuerpo_principal.winfo_height() # Obtiene el alto actual del cuerpo principal
            # Solo redimensiona si el ancho y alto son válidos (no cero)
            if ancho > 0 and alto > 0:
                # Redimensiona la imagen original usando Image.LANCZOS para mejor calidad
                imagen_redimensionada = self.logo_original.resize((ancho, alto), Image.LANCZOS)
                # Crea un nuevo PhotoImage con la imagen redimensionada
                self.logo = ImageTk.PhotoImage(imagen_redimensionada)
                # Actualiza la imagen del label_logo
                self.label_logo.config(image=self.logo)
            
    # Función auxiliar para configurar los botones del menú lateral de forma consistente
    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        # Configura las propiedades del botón
        button.config(text=f"{icon}   {text}", anchor = "w", font=font_awesome, # Texto con icono y alineación a la izquierda
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu) # Sin borde, colores y tamaño
        button.pack(side=tk.TOP, padx=15, pady=5) # Empaqueta en la parte superior con padding
        self.bind_hover_events(button) # Asocia eventos de hover al botón

    # Asocia los eventos de "mouseover" y "mouseout" a un botón para cambiar su apariencia
    def bind_hover_events(self, button):
        # Cuando el ratón entra en el botón, llama a on_enter
        button.bind("<Enter>",lambda event: self.on_enter(event,button))
        # Cuando el ratón sale del botón, llama a on_leave
        button.bind("<Leave>", lambda event: self.on_leave(event, button))
    
    # Función que se ejecuta cuando el ratón entra en un botón (hover)
    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white') # Cambia el fondo y el color del texto
    
    # Función que se ejecuta cuando el ratón sale de un botón
    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white') # Restaura el fondo y el color del texto

    # Alterna la visibilidad del panel del menú lateral
    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped(): # Si el menú lateral es visible (está empaquetado)
            self.menu_lateral.pack_forget()    # Lo "desempaqueta" para ocultarlo
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y') # Lo "reempaqueta" para hacerlo visible

    # Muestra el formulario para agregar un estudiante
    def mostrar_formulario_agregar(self):
        """
        Gestiona la visualización del formulario para agregar un nuevo estudiante.
        Si el formulario ya está abierto, lo cierra. Si no, lo crea y lo muestra.
        Incluye la lógica para mostrar errores si el ID ya está registrado.
        """
        # --- Lógica para cerrar/abrir el formulario ---
        # Si ya hay un formulario de registro abierto, lo destruye (lo cierra)
        if self.current_form_frame is not None:
            self.current_form_frame.destroy()
            self.current_form_frame = None # Resetea la referencia a None
            return # Sale de la función, permitiendo que el botón actúe como un "toggle"

        # Limpia otros widgets del cuerpo principal (excepto el logo de fondo)
        # Esto evita que se superpongan formularios o widgets antiguos
        for widget in self.cuerpo_principal.winfo_children():
            if widget != self.label_logo: # Evita destruir el logo si es un widget persistente
                widget.destroy()

        # --- Creación del nuevo formulario de registro ---
        frame_formulario = tk.Frame(self.cuerpo_principal, bg="#f9f9f9", bd=2, relief="groove")
        # Posiciona el frame del formulario en el centro
        frame_formulario.place(relx=0.5, rely=0.5, anchor='center', width=500, height=300)
        self.current_form_frame = frame_formulario # Guarda la referencia al nuevo frame

        # Título del formulario
        titulo = tk.Label(frame_formulario, text="Registro de Estudiante", 
                          font=("Roboto", 16, "bold"), bg="#f9f9f9", fg="#333")
        titulo.pack(pady=(20, 10))

        # Frame para agrupar los campos de entrada
        campos_frame = tk.Frame(frame_formulario, bg="#f9f9f9")
        campos_frame.pack(pady=10)

        # Etiqueta y campo de entrada para el ID del estudiante
        tk.Label(campos_frame, text="ID Estudiante:", font=("Roboto", 12), 
                 bg="#f9f9f9", anchor="w", width=15).grid(row=0, column=0, padx=10, pady=10)
        entry_id = tk.Entry(campos_frame, font=("Roboto", 12), width=25)
        entry_id.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y campo de entrada para el Nombre del estudiante
        tk.Label(campos_frame, text="Nombre:", font=("Roboto", 12), 
                 bg="#f9f9f9", anchor="w", width=15).grid(row=1, column=0, padx=10, pady=10)
        entry_nombre = tk.Entry(campos_frame, font=("Roboto", 12), width=25)
        entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        # --- Función para guardar los datos del estudiante ---
        def guardar():
            id_est = entry_id.get().strip()
            nombre = entry_nombre.get().strip()
            
            # Valida que ambos campos no estén vacíos
            if id_est and nombre:
                # Intenta agregar el estudiante usando tu GestorEstudiantes
                # El método `agregar_estudiante` retorna True si se agregó exitosamente,
                # y False si el ID ya existía.
                if self.gestor.agregar_estudiante(id_est, nombre):
                    messagebox.showinfo("Éxito", "Estudiante registrado correctamente.")
                    entry_id.delete(0, tk.END) # Limpia el campo de ID
                    entry_nombre.delete(0, tk.END) # Limpia el campo de Nombre
                    
                    # Cierra el formulario después de un registro exitoso
                    if self.current_form_frame is not None:
                        self.current_form_frame.destroy()
                        self.current_form_frame = None 
                else:
                    # Muestra un mensaje de error si el ID ya está registrado
                    messagebox.showerror("Error de Registro", 
                                         f"¡Error! El ID '{id_est}' ya está registrado. Por favor, use otro ID.")
            else:
                # Advertencia si los campos están vacíos
                messagebox.showwarning("Campos Vacíos", "Debes llenar ambos campos: ID y Nombre.")
                
        # Botón para guardar los datos del estudiante
        btn_guardar = tk.Button(frame_formulario, text="Guardar", command=guardar,
                                 bg="#4CAF50", fg="white", font=("Roboto", 12, "bold"),
                                 width=20, height=1, relief="flat", cursor="hand2")
        btn_guardar.pack(pady=20)

    def mostrar_acerca_de(self):
        # Siempre limpia el cuerpo principal de cualquier formulario anterior.
        # Esto incluye el formulario de agregar si estaba visible.
        if self.current_form_frame is not None:
            self.current_form_frame.destroy()
            self.current_form_frame = None
        
        # Destruye todos los widgets en cuerpo_principal excepto el logo de fondo persistente
        for widget in self.cuerpo_principal.winfo_children():
            if widget != self.label_logo:
                widget.destroy()

        # Crea el nuevo frame para el contenido "Acerca de"
        acerca_frame = tk.Frame(self.cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
        # Usa place para superponerlo sobre el logo de fondo, cubriendo todo el espacio.
        acerca_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.current_form_frame = acerca_frame # Establece este como el frame activo actual

        # Título
        title_label = tk.Label(acerca_frame, text="Acerca de Nosotros", 
                               font=("Roboto", 22, "bold"), bg=COLOR_CUERPO_PRINCIPAL, fg="#333")
        title_label.pack(pady=(30, 5))

        # Imagen del Logo
        if self.acerca_logo:
            logo_label = tk.Label(acerca_frame, image=self.acerca_logo, bg=COLOR_CUERPO_PRINCIPAL)
            logo_label.pack(pady=2)
            # ¡Importante! Mantener una referencia a la imagen para evitar que sea eliminada por el recolector de basura.
            # Ya tienes self.acerca_logo como referencia de instancia, así que esto es más una precaución
            # si en algún momento se recreara la imagen localmente.
            logo_label.image = self.acerca_logo 
        else:
            tk.Label(acerca_frame, text="[Logo no disponible]", font=("Roboto", 12, "italic"),
                     bg=COLOR_CUERPO_PRINCIPAL, fg="#999").pack(pady=10)

        # Frase "Si funciona no lo toques"
        phrase_label = tk.Label(acerca_frame, text="Si funciona, No lo toques", 
                                font=("Roboto", 12,"bold", "italic"), bg=COLOR_CUERPO_PRINCIPAL, fg="#777")
        phrase_label.pack(pady=(0, 0)) # Ajusta el padding según sea necesario

        # Nombres de los desarrolladores
        developers_frame = tk.Frame(acerca_frame, bg=COLOR_CUERPO_PRINCIPAL)
        developers_frame.pack(pady=20)

        developers_title = tk.Label(developers_frame, text="Desarrollado por:", 
                                     font=("Roboto", 16, "bold"), bg=COLOR_CUERPO_PRINCIPAL, fg="#555")
        developers_title.pack(pady=(20, 10))

        developer_names = ["Jhan Carlos Gomez", "Luis Flores", "Ronaldo Díaz", "Andres Suarez"]
        for name in developer_names:
            tk.Label(developers_frame, text=name, 
                     font=("Roboto", 14), bg=COLOR_CUERPO_PRINCIPAL, fg="#666").pack(pady=5)
        
        # Descripción/Versión opcional
        version_label = tk.Label(acerca_frame, text="Sistema de Gestión de Estudiantes y Calificaciones v1.0",
                                 font=("Roboto", 10, "italic"), bg=COLOR_CUERPO_PRINCIPAL, fg="#888")
        version_label.pack(pady=(10, 0))