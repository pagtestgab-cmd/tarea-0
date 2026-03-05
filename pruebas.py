import requests

url = "https://tarea-0_py0u.onrender.com/tarea-0"

response = requests.get(url)

print("Código de estado:", response.status_code)
print("Respuesta:", response.json())
