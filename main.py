from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/funcaoteste")
async def funcaoteste(): 
    return {
        "teste": True,
        "num_aleatorio": random.randint(0, 10000)
        }