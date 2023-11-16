import requests
import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
dt_now = datetime.datetime.now(JST)

uri = "http://127.0.0.1:8000/create_pptx"
# uri = "https://render-test-q8db.onrender.com/create_pptx"
payload = {"presentation_title": "pptx作成テスト20231116_1648",
           "slides": [ 
                {
                    "title": "スライド作成プラグインと同様",
                    "content": "スライド作成プラグインと同様に" + dt_now.strftime('%Y/%m/%d %H:%M:%S'),
                    "note": "ノート", 
                    "keywords": [] 
                },
                {
                    "title": "pptxをAPI経由で作成する",
                    "content": "API経由でpptxを作成することができます",
                    "note": "ノート", 
                    "keywords": [] 
                },
            ]
        }

response = requests.post(uri, json=payload)
fileData = response.content

outputFolder = "C:\\Users\\itscuser\\pyproject\\fastapi_test\\"
outputFileName = "response_" + dt_now.strftime('%Y%m%d_%H%M%S') + ".pptx"
with open(outputFolder + outputFileName ,mode='wb') as f: # wb でバイト型を書き込める
  f.write(fileData)