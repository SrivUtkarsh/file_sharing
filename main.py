from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse


app=FastAPI()
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
    