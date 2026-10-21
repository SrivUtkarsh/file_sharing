from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.db_models import Base
db_url = "sqlite:///./file_sharing.db"
engine = create_engine(
    db_url,
    connect_args={"check_same_thread":False}
)
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind = engine
)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()