from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/helloworld")
def root():
    return {"message":"HelloWorld"}

@app.get("/funcaoteste")
async def funcaoteste(): 
    return {
        "teste": True,
        "num_aleatorio": random.randint(0, 10000)
        }