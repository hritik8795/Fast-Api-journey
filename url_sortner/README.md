creted a virtual env for the specific version because i use here two versions of hte python

step:1- python3 -m venv venv
step:2-source venv/bin/activate
step3:pip install -r requirements.txt
step4:uvicorn app.main:app --reload


land on the page 8000
http://127.0.0.1:8000/docs

just pass the argument to the post ui 

{
  "original_url": "https://google.com"
}


get out put as this 

{
  "original_url": "https://google.com",
  "short_code": "abc123",
  "short_url": "http://localhost:8000/abc123"
}


now go for test just do it 

http://127.0.0.1:8000/short_code 
