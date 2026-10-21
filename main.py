from fastapi import FastAPI, UploadFile, File, Request, Depends
from fastapi.responses import FileResponse 
from fastapi.templating import Jinja2Templates
from models.schemas import UserCreate,UserLogin
from db import engine,SessionLocal,get_db
from security import password_hash, create_access_token
from models.db_models import Base,User
import os
from uuid import uuid4
from storage import upload_file
db = SessionLocal()

templates=Jinja2Templates(directory="frontend")
app=FastAPI()
Base.metadata.create_all(bind=engine)
@app.get("/")
async def home():
    return FileResponse("frontend/upload.html")

@app.get("/uploads")
def FileNames():
    file_path="uploads"
    entries=os.listdir(file_path)
    return entries
@app.get("/files")
async def list_files(request: Request):
    files= os.listdir("uploads")
    return templates.TemplateResponse(
        request=request,
        name="view.html",
        context=
        {
            "files":files
        }
    )
@app.get("/files/{filename}")
async def view_file(filename: str):
    return FileResponse(f"uploads/{filename}")
@app.delete("/files/{filename}")
async def delete_file(filename: str):
    file_path = f"uploads/{filename}"
    if not os.path.exists(file_path):
        return {"Error : File not found"}
    os.remove(file_path)                 
    return {"message": f"{filename} deleted successfully"}

@app.post("/register")
def register(user: UserCreate, db=Depends(get_db)):
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()
    if existing_user:
        return {"error": "Username already exists"}
    hashed_password = password_hash.hash(user.password)
    new_user = User(
        username=user.username,
        password_hash=hashed_password
    )
    db.add(new_user)
    db.commit()
    return {
        "message": "User registered successfully",
        "username": new_user.username
    }
@app.post("/login")
async def login(user_data: UserLogin,db=Depends(get_db)):
    user = db.query(User).filter(
        User.username == user_data.username
    ).first()
    if not user:
        return {"error":"Invalid username or passsword"}
    if not password_hash.verify(
        user_data.password,
        user.password_hash
    ):
        return {"error":"Invalid username or password"}
    token = create_access_token(user.id)
    return {
        "access_token":token,
        "token_type": "bearer"
    }
@app.post("/files/upload")
async def upload(file:UploadFile=File(...)):
    object_key=f"files/{uuid4().hex}"
    upload_file(
        file.file,
        object_key,
        file.content_type
    )
    return {
        "filename":file.filename,
        "object_key":object_key,
     
        "content_type":file.content_type,
        "message":"File Uplaoded successfully"
    }
