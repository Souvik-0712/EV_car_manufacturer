import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv


# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()


# --------------------------------------------------
# Database URL
# --------------------------------------------------

DATABASE_URL = os.getenv("DATABASE_URL")


# --------------------------------------------------
# Check if DATABASE_URL exists
# --------------------------------------------------

if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is not set. "
        "Please add DATABASE_URL to your .env file."
    )


# --------------------------------------------------
# Create Database Engine
# --------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


# --------------------------------------------------
# Create Database Session
# --------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# --------------------------------------------------
# Create Base Class
# --------------------------------------------------

Base = declarative_base()


# --------------------------------------------------
# Database Dependency
# --------------------------------------------------

def get_db():
    """
    Creates a database session for each API request.

    The session is automatically closed
    after the request is completed.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()