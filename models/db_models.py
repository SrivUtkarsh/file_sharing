from sqlalchemy import Column, Integer, String , ForeignKey, BigInteger, DateTime, func
from sqlalchemy.orm import declarative_base,relationship, 
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True , index= True)
    username = Column(String, unique=True, index = True)
    password_hash= Column(String) # password is hashed because if someone logs in we store the output after putting password through the hash function so bruteforcing/guessing becomes impossible
    files=relationship("FileMetaData",back_populates="owner",cascade="all,delete-orphan")
class FileMetaData(Base):
    __tablename__ ="Files"
    id=Column(Integer,primary_key=True,index=True)
    filename=Column(String,nullable=False)
    object_key=Column(String,unique=True,nullable=False,index=True)
    owner_id=Column(Integer,ForeignKey("users.id"),nullable=False,index=True)
    file_size=Column(BigInteger,nullable=False)
    content_type=Column(String,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    owner=relationship("User",back_populates="files")