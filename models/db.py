from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db = create_engine("sqlite:///database/test.db", connect_args={"check_same_thread": False})

Base = declarative_base()
