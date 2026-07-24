from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#Import API routers 
from app.routers import cars
from app.routers import chatbot
from app.routers import test_drivers


#====================================
# Create Fast API Application
#====================================

app=FastAPI(
    title="EV Car Manufacturer App",
    description="Backend API for an Electric Vehicle Manufacturer Website",
    version="1.0.0"
)

#====================================
#CORS Config
#====================================

#This allows the Next.js frontend to communicate 
#with the FastAPI backend during development

origins=[
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


#=======================================
# Include API Routers
#=======================================

# Car APIs
# Example:
# GET /api/cars
# GET /api/cars/{car_id}

app.include_router(
    cars.router,
    prefix="/api/cars",
    tags=["Cars"]
)

# Test Drive APIs
# Example:
# POST /api/test-drives
# GET /api/test-drives

app.include_router(
    test_drivers.router,
    prefix="/api/test-drivers",
    tags=["Test Drivers"]
)


# AI Chatbot APIs
# Example:
# POST /api/chat

app.include_router(
    chatbot.router,
    prefix="/api/chat",
    tags=["AI Chatbot"]
)


#====================================
# Root Endpoint
#====================================


@app.get("/")
def root():
    return{
        "message": "Welcome to the EV Car Manufacturer API",
        "status": "running",
        "version": "1.0.0"
    }

#=====================================
# Healthcheck Endpoint
#=====================================
@app.get("/")
def root():
    return{
        "status": "healthy",
        "service": "EV Car Manufacturer Backend" 
    }

