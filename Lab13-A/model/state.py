from dataclasses import dataclass
from datetime import datetime
@dataclass
class State:
    id: int
    Name: str
    Capital: str
    Lat: float
    Lng: float
    Area: float
    Population: int
    Neighbors: []

    def __str__(self):
        return self.Name

    def __hash__(self):
        return hash(self.id)