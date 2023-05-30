"""Disene un programa en Python que agregue el siguiente contenido al archivo: informacion.dat 
Hola Mundo
Este en una nueva linea en el archivo
agregando la segunda linea del archivo
finalizando la linea agregada
"""

def agregar_info_al_archivo(texto):
    try:
        with open ("informacion.dat", "a", encoding="utf-8") as file:
            file.write(texto+"\n")
    except FileNotFoundError:
        print("ERROR: ARCHIVO NO ENCONTRADO")
    except Exception as e:
        print("ERROR: ", e)
agregar_info_al_archivo("Hola Mundo")
agregar_info_al_archivo("Este es una nueva linea en el archivo")
agregar_info_al_archivo("finalizando la linea agregada")