def centrar_ventana(ventana,aplicacion_ancho,aplicacion_alto):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho / 2) - (aplicacion_ancho / 2))
    y = int((pantall_largo / 2) - (aplicacion_alto / 2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_alto}+{x}+{y}")