from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your database URL (replace with actual credentials if needed)
DATABASE_URL = "postgresql://postgres:aalekh45@localhost/my_team2"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a sessionmaker bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
