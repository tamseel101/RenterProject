from pydantic import BaseModel
from enum import Enum

class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

class HousingType(Enum):
    CONDO = 1
    RENT = 2
    SUBLET = 3
    ACCOMODATION: 4

class Location(BaseModel):
    longitude: float = 0.0
    latitude: float = 0.0
    line1: str = ""
    postal: str | None
    city: str = ""
    province: str = ""
    line2: str | None

class Property(BaseModel):
    type: HousingType
    cost_low: int # Daily for Accomodation, Monthly for rent/sublet, overall for Condo
    cost_high: int
    location: Location
    bedrooms: int
    bathrooms: int
    sqft: int | None
    accessible: bool | None
    roommates: bool | None
    coed: bool | None
    images: list[str] | None
    gender_restricted: Gender | None = None
