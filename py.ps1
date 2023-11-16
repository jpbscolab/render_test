
$uri = "http://127.0.0.1:8000/get_pptx"
# $uri = "https://render-test-q8db.onrender.com/get_pptx"

$headers = @{}
$headers["Accept"] = "application/json;charset=utf-8"
$headers["Content-Type"] = "application/json;charset=utf-8"
# $body = '{"presentation_title": "pptx作成テスト","slides": [ {"slide_title": "pptxをAPI経由で作成する","slide_content": "API経由でpptxを作成することができます","slide_note": "ノート", "keywords": [] }]}'
# $body = '{"presentation_title": "pptx","slides": [ {"slide_title": "pptx test","slide_content": "createing pptx via API ","slide_note": "note", "keywords": [] }]}'
$slide = @{
  slide_title = "pptx"
  slide_content = "API"
  slide_note = "note"
  keywords = "","" }
$obj = @{
  presentation_title = "pptx test"
  slides = $slide, $slide
}
$jsonData = $obj | ConvertTo-Json
$sendbody = [System.Text.Encoding]::UTF8.GetBytes($jsonData)
# $body = [System.Text.Encoding]::UTF8.GetBytes('{"presentation_title": "pptx作成テスト","slides": [ {"slide_title": "pptxをAPI経由で作成する","slide_content": "API経由でpptxを作成することができます","slide_note": "ノート", "keywords": [] }]}')

Invoke-RestMethod -Uri $uri `
  -Method POST `
  -Headers $headers `
  -Body $sendbody `
  -OutFile "C:\Users\itscuser\Downloads\response.pptx"

<#
curl -X 'POST' `
  "http://127.0.0.1:8000/get_pptx" `
  -H "Accept: application/json" `
  -H "Content-Type: application/json" `
  -d "{  \"presentation_title\": \"string\",  \"slides\": [    {      \"slide_title\": \"string\",      \"slide_content\": \"string\",      \"slide_note\": \"string\",      \"keywords\": []    }  ]}"
#>
