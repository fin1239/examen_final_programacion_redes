import json

# Abrir y leer el archivo JSON
with open("usuarios.json", "r") as archivo:
    datos = json.load(archivo)

# Extraer y mostrar los nombres
for usuario in datos:
    print(usuario["nombre"])
