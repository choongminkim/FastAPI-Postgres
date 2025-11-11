import os
from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(prefix="/image", tags=["image"])


@router.get("/{image_name}")
async def get_image(image_name: str):
    file_path = os.path.join(*[os.getcwd(), "assets", image_name])
    print(file_path)
    return FileResponse(file_path)
