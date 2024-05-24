from pydantic import BaseModel


class Data(BaseModel):
    birthday: int
    birthmonth: int
    birthyear: int
    firstname: str
    fathername: str
    secondname: str
