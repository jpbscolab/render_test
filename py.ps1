$uri = "http://127.0.0.1:8000/get_pptx"
$headers = @{}
$headers["Accept"] = "application/json"
$headers["Content-Type"] = "application/json"
$body = [System.Text.Encoding]::UTF8.GetBytes('{"presentation_title": "string","slides": [ {"slide_title": "string","slide_content": "string","slide_note": "string", "keywords": [] }]}')

Invoke-RestMethod -Uri $uri `
  -Method POST `
  -Headers $headers `
  -Body $body `
  -OutFile "C:\Users\itscuser\Downloads\response.pptx"



<#
curl -X 'POST' `
  "http://127.0.0.1:8000/get_pptx" `
  -H "Accept: application/json" `
  -H "Content-Type: application/json" `
  -d "{  \"presentation_title\": \"string\",  \"slides\": [    {      \"slide_title\": \"string\",      \"slide_content\": \"string\",      \"slide_note\": \"string\",      \"keywords\": []    }  ]}"
#>
