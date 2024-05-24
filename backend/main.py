from fastapi import FastAPI
from schemas import Data
from uvicorn import run
from services import runes_calculator
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


# @app.get("/api_runes")
# async def get_response():
#     return 'Response'


@app.post("/api_runes")
async def read_item(data: Data):
    print(data)
    runes = runes_calculator(data.birthday, data.birthmonth, data.birthyear,
                             data.firstname, data.fathername, data.secondname)
    return runes
