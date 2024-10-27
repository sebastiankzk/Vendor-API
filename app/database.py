import os 
from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

# Read environment variables for database credentials
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Database URL
# connectionString = getenv('DB_CONNECTION_STRING')
connectionString: str = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Check if connectionString is None
if connectionString is None:
    raise ValueError("DB_CONNECTION_STRING environment variable not set.")

# SQLAlchemy Engine
try:
    engine = create_engine(connectionString, connect_args={"charset": "utf8mb4"})
    # Optionally, test the connection
    with engine.connect() as conn:
        print("Connected to the database successfully.")
except Exception as e:
    raise ConnectionError(f"Failed to connect to the database: {e}")

# Session Local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base
Base: DeclarativeMeta = declarative_base()
