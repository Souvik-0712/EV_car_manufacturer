from sqlalchemy import(
    Column,
    Integer,
    String,
    Float,
    Text,
    Date,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


#==========================================
# CAR MODEL
#==========================================

class Car(Base):
    """
    Database model for storing EV car information.
    """
    __tablename__="cars"

    #=======================================
    # Promary Key
    #=======================================

    id=Column(
        Integer,
        primary_key=True,
        index=True
    )

    #========================================
    # Basic Car Information 
    #========================================

    name=Column(
        String(100),
        nullable=False
    )

    model=Column(
        String(100),
        nullable=False
    )

    #=======================================
    # Car Price
    #=======================================


    price=Column(
        Float,
        nullable=False
    )


    #=====================================
    # Bettery Information
    #=====================================

    bettery_capacity=Column(
        Float,
        nullable=False
    )

    #=======================================
    # Driving Range
    #=======================================

    range_km=Column(
        Integer,
        nullable=False
    )


    #=======================================
    # Charging Time
    #=======================================


    charging_time=Column(
        Float,
        nullable=False
    )


    #========================================
    # Car Description 
    #========================================

    description=Column(
        Text,
        nullable=True
    )


    #=======================================
    # Car Image URL
    #=======================================


    image_url=Column(
        String(500),
        nullable=True
    )


    #==========================================
    # Relationship with Testdrive
    #==========================================

    test_drivers=relationship(
        "TestDrive",
        back_populates="car"
    )



#==========================================
# Test Drive Model
#==========================================

class TestDrive(Base):
    """
    Database model for storing customer test-drive
    booking information.
    """

    __tablename__="test_drivers"

    #===================================
    # Primary Key
    #===================================

    id=Column(
        Integer,
        primary_key=True,
        index=True
    )

    #====================================
    # Customer Information
    #====================================

    customer_name=Column(
        String(100),
        nullable=False
    )

    email=Column(
        String(20),
        nullable=False
    )

    phone=Column(
        String(20),
        nullable=False
    )


    #=========================================
    # Car ID
    #=========================================

    car_id=Column(
        Integer,
        ForeignKey("cars.id"),
        nullable=False
    )

    #========================================
    # Preferred Test Drive Date
    #========================================

    preferred_date=Column(
        Date,
        nullable=False
    )

    #========================================
    # Booking Creation Date
    #========================================

    created_at=Column(
        DateTime,
        default=datetime.vtcnow
    )

    #=======================================
    # Relationship with car
    #=======================================

    car=relationship(
        "Car",
        back_populates="test_drives"
    )
