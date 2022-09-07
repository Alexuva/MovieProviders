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