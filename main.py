from pathlib import Path
from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/get_file/{filename:path}")
async def get_file(filename: str):
    '''任意ファイルのダウンロード'''
    current = Path()
    file_path = current / "files" / filename
    
    now = datetime.now()
    
    response = FileResponse(
                            path=file_path,
                            filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{filename}"
                            )
    return response

@app.get("/get_sample_pptx")
async def get_sample_pptx():
    '''任意ファイルのダウンロード'''
    current = Path()
    file_path = current / "files" / "test.pptx"
    
    now = datetime.now()
    
    response = FileResponse(
                            path=file_path,
                            filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{filename}"
                            )
    return response



# if __name__ == "__main__":
#     uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
