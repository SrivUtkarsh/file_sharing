from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True , index= True)
    username = Column(String, unique=True, index = True)
    password_hash= Column(String) # password is hashed because if someone logs in we store the output after putting password through the hash function so bruteforcing/guessing becomes impossible
    
    