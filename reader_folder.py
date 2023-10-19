# Analisar carpeta y subcarpetas apartir de una carpeta raiz

import os

# Carpeta raiz
root_folder = r'C:\Users\kayam\Documents\projects_iOS\mr-bumper'

# Lista de carpetas
folders = []

# Lista de archivos
files = []


# Funcion para analizar carpetas y subcarpetas
def read_folder(folder):
    # Lista de carpetas
    folders = []
    # Lista de archivos
    files = []
    # Recorrer carpeta
    for file in os.listdir(folder):
        # Ruta completa
        path = os.path.join(folder, file)
        # Si es una carpeta
        if os.path.isdir(path):
            # Agregar a la lista de carpetas
            folders.append(path)
        # Si es un archivo
        else:
            # Agregar a la lista de archivos
            files.append(path)
    # Retornar listas
    return folders, files


# Funcion para imprimir carpetas y subcarpetas
def print_folders(folder, level=0):
    # Analizar carpeta
    folders, files = read_folder(folder)
    # Imprimir carpeta
    print(' ' * level * 4, os.path.basename(folder))
    # Recorrer carpetas
    for folder in folders:
        # Imprimir carpetas
        print_folders(folder, level + 1)
    # Recorrer archivos
    for file in files:
        # Imprimir archivos
        print(' ' * (level + 1) * 4, os.path.basename(file))


# Imprimir carpetas y subcarpetas
print_folders(root_folder)

# Imprimir carpetas y subcarpetas
folders, files = read_folder(root_folder)

# Imprimir carpetas
print(folders)

# Imprimir archivos
print(files)

