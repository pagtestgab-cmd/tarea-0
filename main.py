from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"respuesta": "Primer tarea realizada"}

@app.get("/tarea-0")
def tarea_0():
    return {"respuesta": "Primer tarea realizada"}