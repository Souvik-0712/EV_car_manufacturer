from typing import List

from fastapi import(
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import session

from app.database import get_db
from app.models import Car
from app.schemas import(
    CarCreate,
    CarResponse,
    CarUpdate
)

#========================================
# CREATE ROUTER 
#========================================

router=APIRouter()


#=======================================
# Get All Cars
#=======================================

@router.get(
    "/",
    response_model=List(CarResponse)
)
def get_all_cars(
    db:session=Depends(get_db)
):
    """
    Get all EV cars from the database.
    """

    cars=db.query(Car).all()

    return cars

#=========================================
# Get Single Car
#=========================================

@router.get(
    "/{car_id}",
    response_model=CarResponse
)
def get_car(
    car_id:int,
    db: session=Depends(get_db)
):
    """
    Get a single EV car using its ID.
    """

    car=(
        db.query(Car)
        .filter(Car.id==car_id)
        .first()
    )

    #If car doesn't exist
    if car is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Car Not Found"
        )
    return car


# ==================================================
# CREATE NEW CAR
# ==================================================

@router.post(
    "/",
    response_model=CarResponse,
    status_code=status.HTTP_201_CREATED
)
def create_car(
    car_data: CarCreate,
    db: session = Depends(get_db)
):
    """
    Create a new EV car.
    """

    # Create SQLAlchemy Car object
    new_car = Car(
        name=car_data.name,
        model=car_data.model,
        price=car_data.price,
        battery_capacity=car_data.battery_capacity,
        range_km=car_data.range_km,
        charging_time=car_data.charging_time,
        description=car_data.description,
        image_url=car_data.image_url
    )
    # Add car to database session
    db.add(new_car)

    # Save changes
    db.commit()

    # Refresh object to get generated ID
    db.refresh(new_car)

    return new_car

# ==================================================
# UPDATE CAR
# ==================================================

@router.put(
    "/{car_id}",
    response_model=CarResponse
)
def update_car(
    car_id: int,
    car_data: CarUpdate,
    db: session = Depends(get_db)
):
    """
    Update an existing EV car.
    """

    # Find car
    car = (
        db.query(Car)
        .filter(Car.id == car_id)
        .first()
    )

    # Check if car exists
    if car is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Car not found"
        )

    # Get only fields provided by the user
    update_data = car_data.model_dump(
        exclude_unset=True
    )

    # Update each field
    for field, value in update_data.items():
        setattr(car, field, value)

    # Save changes
    db.commit()

    # Refresh updated object
    db.refresh(car)

    return car


# ==================================================
# DELETE CAR
# ==================================================

@router.delete(
    "/{car_id}"
)
def delete_car(
    car_id: int,
    db: session = Depends(get_db)
):
    """
    Delete an EV car from the database.
    """

    # Find car
    car = (
        db.query(Car)
        .filter(Car.id == car_id)
        .first()
    )

    # Check if car exists
    if car is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Car not found"
        )

    # Delete car
    db.delete(car)

    # Save changes
    db.commit()

    return {
        "message": "Car deleted successfully",
        "car_id": car_id
    }