from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from models.schemas import FolderRequest,UserCreate
from db import engine
from models.db_models import Base
import os
folders= [] 
folder_id = 1
templates=Jinja2Templates(directory="frontend")
app=FastAPI()
Base.metadata.create_all(bind=engine)
@app.get("/")
async def home():
    return FileResponse("frontend/upload.html")
@app.post("/files/upload")
async def upload(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(await file.read())
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }
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
@app.post("/folders")
def create_folder(folder: FolderRequest):
    global folder_id
    if folder.parent_id is not None:
        parent = next(
            (f for f in folders if f["id"] == folder.parent_id),
            None
        )
        if parent is None:
            return {"error": "Parent folder was not found"}
    new_folder = {
        "id":folder_id,
        "name":folder.name,
        "parent_id":folder.parent_id
    }
    folders.append(new_folder)
    folder_id+=1
