from fastapi import FastAPI
from backend.schemas import Data
from uvicorn import run
from backend.services import runes_calculator

app = FastAPI()


@app.post("/api_runes")
async def read_item(data: Data):
    runes = runes_calculator(data.day, data.month, data.year, data.first_name, data.father_name, data.second_name)
    return runes
