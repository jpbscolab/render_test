from pathlib import Path
from datetime import datetime

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import FileResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from typing import Optional

from createPptx import createSamplePptx, createPptx

app = FastAPI()

# リクエストbodyの定義
class SlideDef(BaseModel):
    slide_title: str
    slide_content: str
    slide_note: Optional[str]=None
    keywords: Optional[list[str]]=[]

class PresentationDef(BaseModel):
    presentation_title: str
    slides: list[SlideDef]

@app.exception_handler(RequestValidationError)
async def handler(request:Request, exc:RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@app.get("/")
def home():
    return {"message": "Hello World"}


# @app.get("/get_file/{filename:path}")
# async def get_file(filename: str):
#     '''任意ファイルのダウンロード'''
#     current = Path()
#     file_path = current / "files" / filename
    
#     now = datetime.now()
    
#     response = FileResponse(
#                             path=file_path,
#                             filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{filename}"
#                             )
#     return response

@app.get("/get_sample_pptx")
async def get_sample_pptx():
    '''サンプルパワーポイントファイルの作成'''
    file_name = createSamplePptx()

    '''任意ファイルのダウンロード'''
    current = Path()
    file_path = current / "files" / file_name
    
    now = datetime.now()
    
    response = FileResponse(
                            path=file_path,
                            filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{file_name}"
                            )
    return response

@app.post("/create_pptx")
async def create_pptx(presentationDef: PresentationDef):
    '''パワーポイントファイルの作成'''
    slide_titles = [slide.slide_title for slide in presentationDef.slides]
    slide_contents = [slide.slide_content for slide in presentationDef.slides]
    slide_notes = [slide.slide_note for slide in presentationDef.slides]
    keywords = [slide.keywords for slide in presentationDef.slides]
    file_name = createPptx(slide_titles, slide_contents, slide_notes, keywords)

    '''任意ファイルのダウンロード'''
    current = Path()
    file_path = current / "files" / file_name
    
    now = datetime.now()
    
    response = FileResponse(
                            path=file_path,
                            filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{file_name}"
                            )
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
