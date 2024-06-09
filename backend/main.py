from fastapi import FastAPI
from schemas import Data
from uvicorn import run
from services import runes_calculator
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ['http://localhost:8080']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.post("/api_runes")
async def read_item(data: Data):
    runes = runes_calculator(data.birthday, data.birthmonth, data.birthyear,
                             data.firstname, data.fathername, data.secondname)
    return runes
