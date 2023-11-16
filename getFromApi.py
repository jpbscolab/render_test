import requests

uri = "http://127.0.0.1:8000/get_pptx"
# uri = "https://render-test-q8db.onrender.com/get_pptx"
payload = {"presentation_title": "pptx作成テスト",
           "slides": [ 
                {
                   "slide_title": "スライド作成プラグインと同様",
                    "slide_content": "スライド作成プラグインと同様に",
                    "slide_note": "ノート", 
                    "keywords": [] 
                },
                {
                   "slide_title": "pptxをAPI経由で作成する",
                    "slide_content": "API経由でpptxを作成することができます",
                    "slide_note": "ノート", 
                    "keywords": [] 
                },
            ]
        }

response = requests.post(uri, json=payload)
fileData = response.content

outputFolder = "C:\\Users\\itscuser\\pyproject\\fastapi_test\\"
outputFileName = "response.pptx"
with open(outputFolder + outputFileName ,mode='wb') as f: # wb でバイト型を書き込める
  f.write(fileData)