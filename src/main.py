import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel): 
    name: str
    curso: str
    ativo: bool

@app.get("/helloworld")
def root():
    return {"message": "HelloWorld"}

@app.get("/funcaoteste")
async def funcaoteste(): 
    return {
        "teste": True,
        "num_aleatorio": random.randint(0, 30000)
    }

@app.get("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id_estudante > 0

@app.delete("estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0