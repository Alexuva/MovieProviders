from fastapi import FastAPI
from moviedata import Movie

app = FastAPI()

movie = Movie()

@app.get("/")
async def read_item():
    try:
        return [
            {
                "Bienvenido": "Introduce '/movie=' o '/tv=' seguido del id del producto en TmDB"
            }
        ]
    except:
        return [
            {
                "Error": "No se encuentran proveedores para esa película"
            }
        ]
@app.get("/movie={id}")
async def read_item(id):
    try:
        return movie.searchproviders(id)
    except:
        return [
            {
                "Error": "No se encuentran proveedores para esa película"
            }
        ]