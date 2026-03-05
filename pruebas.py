import requests

url = "https://Clase_2_tarea-py0u.onrender.com/tarea-0"

response = requests.get(url)

print("Código de estado:", response.status_code)
print("Respuesta:", response.json())
