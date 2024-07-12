from fastapi import APIRouter,UploadFile
from pathlib import Path
from fastapi.responses import FileResponse
import os


image_router = APIRouter(prefix='/images')

@image_router.get("/{image_name}")
async def get_image(image_name:str):
    path = os.getcwd()+"/images/"+image_name
    image_path = Path(path)
    if not image_path.is_file():
        return {"message": "File not found in server"}
    return FileResponse(image_path)

