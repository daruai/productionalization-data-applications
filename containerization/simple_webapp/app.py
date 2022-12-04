# Example web app using FastAPI

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def hello_name_view(name: str):
    return {"message": f"Hello {name}"}

