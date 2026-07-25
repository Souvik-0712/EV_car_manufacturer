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

class CarResponse(CarBase):
    """
    Schema returned to the frontend when retrieving
    car information.
    """

    id: int

    model_config = ConfigDict(
        from_attributes=True
    )


# ==================================================
# TEST DRIVE SCHEMAS
# ==================================================


class TestDriveBase(BaseModel):
    """
    Common fields for test-drive booking.
    """

    customer_name: str
    email: str
    phone: str
    car_id: int
    preferred_date: date

class TestDriveCreate(TestDriveBase):
    """
    Schema used when creating a test-drive booking.
    """

    pass


class TestDriveResponse(TestDriveBase):
    """
    Schema returned after creating or retrieving
    a test-drive booking.
    """

    id: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )