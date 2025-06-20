## 🎓 Sistema de Gestión de Estudiantes y Calificaciones

Este proyecto, desarrollado en **Python**, es el resultado de nuestro curso de Fundamentos de Programación. Nace con el propósito de crear una **aplicación de escritorio** que simplifique la gestión de estudiantes y sus calificaciones.

Un aspecto fundamental es su **interfaz gráfica de usuario (GUI)**, desarrollada con **Tkinter**, que proporciona una experiencia más intuitiva y fácil de usar. Además, el sistema **guarda y carga los datos de forma persistente utilizando un archivo JSON**, asegurando que la información no se pierda al cerrar la aplicación. Hemos implementado **validaciones exhaustivas** para garantizar la integridad de los datos, y el sistema utiliza **ventanas emergentes** para notificar al usuario sobre el éxito de las operaciones o posibles errores. El sistema puede compilarse como un **archivo ejecutable (.exe)**, facilitando su uso en computadoras Windows sin necesidad de tener Python instalado.

-----

### 📌 Objetivo General

Nuestro objetivo fue desarrollar un programa de escritorio que permitiera:

  * **Registrar estudiantes** de manera sencilla a través de una interfaz gráfica.
  * **Gestionar sus calificaciones**, permitiendo tanto añadir como modificar notas con validaciones.
  * **Calcular y mostrar promedios** de forma automática.
  * **Consultar o eliminar estudiantes** del sistema con confirmaciones visuales.
  * Incluir una sección "Acerca de" con información del equipo de desarrollo.
  * Proveer una **experiencia de usuario mejorada** 

-----

### ⚙️ Funcionalidades del Sistema

El sistema ahora cuenta con una **interfaz gráfica amigable** que ofrece las siguientes opciones y características:

1.  **Agregar estudiante**: Permite registrar un nuevo estudiante con su ID y nombre a través de un formulario intuitivo. Incluye **validaciones para asegurar la unicidad del ID** y el formato correcto de los datos.
2.  **Ingresar o actualizar calificaciones**: Facilita la adición de nuevas notas o la modificación de las existentes para un estudiante específico. Se han implementado **validaciones para que las calificaciones estén dentro de un rango válido** y sean numéricas.
3.  **Consultar estudiantes**: Muestra todos los estudiantes registrados junto con sus promedios actuales en una tabla o lista clara.
4.  **Eliminar estudiante**: Permite eliminar un estudiante del sistema buscando por su ID, con una **ventana emergente de confirmación** antes de proceder.
5.  **Acerca de**: Muestra información sobre nuestro equipo de desarrollo en una ventana dedicada.
6.  **Salir**: Finaliza el programa, **guardando automáticamente todos los cambios** en el archivo JSON.
7.  **Notificaciones Interactivas**: Se utilizan **ventanas emergentes para informar al usuario sobre el éxito de una operación (ej. "Estudiante agregado con éxito"), errores de validación (ej. "ID ya existe") o confirmaciones (ej. "¿Está seguro de eliminar?").

-----

### 🖥️ Requisitos del Sistema

Para asegurar el óptimo funcionamiento, se recomienda cumplir con los siguientes requisitos:

  * **Sistema Operativo**: Windows, macOS o Linux.
  * **Python**: Se requiere tener instalado Python (si se va a ejecutar desde el código fuente) y Visual Studio Code. Puedes descargarlos desde sus sitios oficiales.
  * **Librerías Python**: **Tkinter** (generalmente incluida con Python estándar) y otras dependencias si las hubiera (ej. `json` para persistencia, ya integrada).
  * **Entorno de Desarrollo**: El programa fue desarrollado utilizando **Visual Studio Code** y **Python**.
  * **Memoria RAM**: Mínimo 2 GB (se recomiendan 4 GB o más para un rendimiento óptimo).
  * **Espacio en Disco**: Al menos 100 MB de espacio libre para almacenar el proyecto y sus dependencias.

-----

### 🚀 Guía de Instalación y Ejecución

Tienes dos opciones para poner en marcha el sistema:

#### Opción 1: Descargar el ejecutable (.exe)

Puedes descargar directamente la carpeta con el archivo ejecutable (.exe) desde nuestra página web, lo que te permitirá ejecutar el programa sin necesidad de instalar Python ni clonar el repositorio:

➡️ **[Descargar Sistema de Gestión de Estudiantes](https://sites.google.com/view/error404software/p%C3%A1gina-principal)**

#### Opción 2: Clonar el Repositorio (para desarrolladores)

Si deseas trabajar con el código fuente o no tienes acceso a la descarga directa, sigue estos pasos:

##### 1\. Preparación del Entorno

  * **Guía de Instalación de Python**:

    1.  Descarga el instalador desde el [sitio oficial de Python](https://www.python.org/downloads/).
    2.  Ejecuta el instalador.
    3.  Inicia la instalación, asegurándote de seleccionar la opción para **añadir Python al PATH**.
    4.  Finaliza la instalación.
    5.  Verifica la instalación abriendo una terminal y ejecutando `python --version`.

  * **Guía de Instalación de Visual Studio Code**:

    1.  Descarga el instalador desde el [sitio oficial de Visual Studio Code](https://code.visualstudio.com/download).
    2.  Ejecuta el instalador.
    3.  Acepta el acuerdo de licencia.
    4.  Selecciona la ubicación de instalación deseada.
    5.  Sigue las instrucciones para completar la instalación.

##### 2\. Clonar el Repositorio

1.  Abre Visual Studio Code.
2.  Haz clic en la parte superior "Terminal" o en los 3 puntos y luego en "Nuevo terminal".
3.  En la terminal, escribe el siguiente comando para clonar el repositorio:
    ```bash
    git clone https://github.com/jhan201-pixel/Sitemas-de-gesti-n-de-estudiante-y-calidicaciones.git
    ```
    Una vez clonado, el repositorio ya estará listo para usarse.

##### 3\. Ejecución del Programa

Una vez clonado el repositorio y con Python instalado, puedes ejecutar el programa directamente desde Visual Studio Code o desde la terminal. Navega a la carpeta del proyecto y ejecuta el archivo principal de Python.
-----

### ⚠️ Errores Comunes y Soluciones

  * **Error: El programa no corre**
      * **Solución**: Asegúrate de que Python esté instalado correctamente en tu sistema. Verifica que estés ejecutando el archivo correcto del programa.
  * **Error: El programa necesita una librería llamada pip**
      * **Solución**: Asegúrate de tener la librería instalada en Python. Puedes instalarla utilizando `pip install <nombre_de_la_libreria>`. (En este caso, Tkinter suele venir incluida con Python).

-----

### 👥 Equipo de Desarrollo

  * Jhan Carlos Gómez
  * Ronaldo Diaz
  * Álvaro Suárez
  * Luis Flórez
