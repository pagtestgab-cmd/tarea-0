import requests

url = "https://tarea-0-1-161w.onrender.com"

response = requests.get(url)

print("Código de estado:", response.status_code)
print("Respuesta:", response.json())
