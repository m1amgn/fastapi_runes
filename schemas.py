from pydantic import BaseModel


class Data(BaseModel):
    day: int
    month: int
    year: int
    first_name: str
    father_name: str
    second_name: str
