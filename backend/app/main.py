from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#Import API routers 
from app.routers import cars
from app.routers import chatbot
from app.routers import test_drivers
