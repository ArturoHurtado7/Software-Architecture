from pydantic import BaseModel, Field
from typing import List

class User(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="John Doe")
    email: str = Field(..., example="")

class Location(BaseModel):
    latitude: float = Field(..., example=4.599469)
    longitude: float = Field(..., example=-74.117057)

class Stops(BaseModel):
    planned: float = Field(..., example=5)
    non_planned: float = Field(..., example=1)

class Truck(BaseModel):
    id: int = Field(..., example=5240)
    registration: str = Field(..., example="BBV545")
    location: Location = Field(..., example={"latitude": 4.599469, "longitude": -74.117057})
    speed: float = Field(..., example=44.0)
    address: str = Field(..., example="AC 72 No 12 - 22")
    stops: Stops = Field(..., example={"planned": 5, "non_planned": 1})
    camera: str = Field(..., example="https://mytruckcamlive.com/live.html?truckid=5240")

class Shipment(BaseModel):
    name: str = Field(..., example="Bannanas")
    state: bool = Field(..., example=True)
    temperature: float = Field(..., example=25.0)

class CentralSchema(BaseModel):
    truck: Truck = Field(..., example={"id": 5240, "registration": "BBV545", "location": {"latitude": 4.599469, "longitude": -74.117057}, "speed": 44.0, "address": "AC 72 No 12 - 22", "stops": {"planned": 5, "non_planned": 1}, "camera": "https://mytruckcamlive.com/live.html?truckid=5240"})
    shipment: Shipment = Field(..., example={"name": "Bannanas", "state": True, "temperature": 25.0})
    panic: bool = Field(..., example=False)
