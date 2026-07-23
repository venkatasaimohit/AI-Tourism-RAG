from pydantic import BaseModel



class TripCreate(BaseModel):

    destination:str

    budget:int

    duration:int