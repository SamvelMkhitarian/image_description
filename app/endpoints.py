import io
from datetime import datetime

from app.database import AsyncSessionLocal
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from app.generate_caption import generate_caption
from app.models import CaptionHistory
from PIL import Image
from sqlalchemy.future import select

router = APIRouter()


@router.post("/caption")
async def caption_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400, detail="Неподдерживаемый формат файла")
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
    except Exception:
        raise HTTPException(
            status_code=400, detail="Ошибка обработки изображения")

    caption = await generate_caption(image)
    print(f"Generated caption: {caption}")

    # Сохраняем результат в БД
    async with AsyncSessionLocal() as session:
        record = CaptionHistory(
            caption=caption, timestamp=datetime.now())
        session.add(record)
        await session.commit()

    return JSONResponse(content={"caption": caption})


@router.get("/history")
async def get_history():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(CaptionHistory))
        history = result.scalars().all()
        return [
            {"id": record.id, "caption": record.caption,
                "timestamp": record.timestamp.isoformat()}
            for record in history
        ]
