from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#Import API routers 
from app.routers import cars
from app.routers import test_drivers
from app.routers import chatbot

#---------------------------------------
#Create FastAPI Applications
#---------------------------------------

app=FastAPI(
    title="EV car Manufacturer API",
    description="Backend API for an Electric Vehiccle Manufacturer Website",
    version="1.0.0"
)

#---------------------------------------
#CORS Configuration
#---------------------------------------

#This allows the Next.js frontend to communicate
#with the FastAPI backend duriong development

origins=[
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#------------------------------------
#Include API Routers
# -----------------------------------

#Car APIs
# Example:
# GET/api/cars
# GET/api/cars/{care_id}


app.include_router(
    cars.router,
    prefix="/api/cars",
    tags=["Rest Drivers"]
)

# Test Drive APIs
# Example:
# POST/api/test-drivers
# GET/api/test-drivers

app.include_router(
    test_drivers.router,
    prefix="/api/test-drivers",
    tags=["Test Drivers"]
)


#AI Chatbot APIs
# Example:
#POST/api/chat

app.include_router(
    chatbot.router,
    prefix="/api/chat",
    tags=["AI Chatbot"]
)

#----------------------------------
# Root Endpoint
#----------------------------------

@app.get("/")
def root():
    return{
        "message": "Welcome to the EV Car Manufacturer API",
        "status": "running",
        "version": "1.0.0"
    }


#-------------------------------------
#Health Check Endpoint
#-------------------------------------

@app.get("/health")
def helth_check():
    return{
        "status": "healthy",
        "service": "EV Car Manufacturer Backend"
    }

