from pydantic import BaseModel,ConfigDict
from datetime import date,datetime
from typing import Optional


#=================================================
# CAR Schemes
#=================================================


class CarBase(BaseModel):
    """
    Common fields shared by Car schemas.
    """ 
    name: str
    model: str
    price: float
    bettery_capacity: float
    range_km: int
    charging_time: float
    description: Optional[str]=None
    image_url: Optional[str]=None

class CarCreate(CarBase):
    """
    Schema used when creating a new EV car.
    """

    pass 


class CarUpdate(BaseModel):
    """
    Schema used when updating an existing EV car.

    All fields are optional so that we can update
    only the fields we need.
    """

    name: Optional[str]=None
    model: Optional[str]=None
    price: Optional[str]=None
    battery_capacity: Optional[float] = None
    range_km: Optional[int] = None
    charging_time: Optional[float] = None
    description: Optional[str] = None
    image_url: Optional[str] = None