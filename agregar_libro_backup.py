import requests

# URL de la API para agregar libros
url = "http://library.domino.local/api/v1/books"

# Token de autenticación (reemplaza con tu token real)
token = "TU_TOKEN_AQUI"

# Datos del libro a agregar
data = {
    "title": "Examen Final Programacion Redes",
    "author": "MiguelVillaEditorUaTF"  # Cambia por tu nombre completo sin espacios
}

# Encabezados, incluyendo el token para autenticación (Bearer Token)
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Enviar solicitud POST
response = requests.post(url, json=data, headers=headers)

# Mostrar código de estado y respuesta JSON
print("Código de estado:", response.status_code)
print("Respuesta JSON:", response.json())
