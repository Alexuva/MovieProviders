from fastapi import FastAPI
from moviedata import Movie

app = FastAPI()

movie = Movie()

@app.get("/movie/{id}")
async def read_item(id):
    try:
        return movie.searchproviders(id)
    except:
        return [
            {
                "Error": "No se encuentran proveedores para esa película"
            }
        ]