from fastapi import FastAPI
from schemas import Data
from uvicorn import run

app = FastAPI()


@app.post("/api_runes")
async def read_item(data: Data):
    return {
        'day': data.day,
        'month': data.month,
        'year': data.year,
        'first_name': data.first_name,
        'father_name': data.father_name,
        'second_name': data.second_name
    }
