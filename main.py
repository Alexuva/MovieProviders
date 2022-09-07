
from fastapi import FastAPI
from moviedata import Movie
from tvdata import Tv

app = FastAPI()

movie = Movie()

tv = Tv()

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

@app.get("/tv={tvid}")
async def read_item(tvid):
    try:
        return tv.searchproviders(tvid)
    except:
        return [
            {
                "Error": "No se encuentran proveedores para esa serie"
            }
        ]