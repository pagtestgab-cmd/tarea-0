import requests

# Remoto en Render
url = "https://tarea-0-lcth.onrender.com/tarea-0"


respuesta = requests.get(url)
print(respuesta.json())