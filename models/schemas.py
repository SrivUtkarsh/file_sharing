from pydantic import BaseModel
class FolderRequest(BaseModel):
    name: str
    parent_id: int | None = None
    
class UserCreate(BaseModel):
    username: str
    password : str

class UserLogin(BaseModel):
    username : str
    password : str