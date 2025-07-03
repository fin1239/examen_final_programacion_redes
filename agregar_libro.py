import requests

url = "http://library.domino.local/api/v1/books"
token = "TU_TOKEN_AQUI"

data = {
    "title": "Examen Final Programacion Redes",
    "author": "MiguelVillaEditorUaTF"
}

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)

print("Código de estado:", response.status_code)
print("Respuesta JSON:", response.json())
