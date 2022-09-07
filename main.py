
from fastapi import FastAPI
from moviedata import Movie

app = FastAPI()

movie = Movie()

@app.get("/")
async def bienvenido():
    return [
            {
                "Bienvenido": "Introduce '/movie=' o '/tv=' seguido del id del producto en TmDB"
            }
        ]
@app.get("/movie={movieid}")
async def read_item(movieid):
    try:
        return movie.searchproviders(movieid)
    except:
        return [
            {
                "Error": "No se encuentran proveedores para esa película"
            }
        ]