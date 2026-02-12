from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_session():
    with sessionmaker as session:
        yield session

def get_db():
    db = Session()
    try:
        yield db 
    finally:
        db.close()

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)
