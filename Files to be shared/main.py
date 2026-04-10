from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from services import credential, password
from storage.db import create_table
import os

app = FastAPI()

create_table()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

templates = Jinja2Templates(directory='templates')

# @app.get("/")
# def home():
#     return {"status": "working"}

@app.get("/")
def home(request : Request):
    # return templates.TemplateResponse("index.html", {"request" : request})
    return templates.TemplateResponse(request, "index.html")
    # return {"status": "working"}

@app.get("/add")
def add_page(request : Request):
    return templates.TemplateResponse(request, "add.html")

@app.get("/list")
def list_page(request: Request):

    data = credential.get_credentials()

    print("DEBUG TYPE:", type(data))
    print("DEBUG DATA:", data)
    return templates.TemplateResponse(request, "list.html", {"data": data})

# @app.get("/")
# def home():
#     return {"status": "working"}

@app.get("/generate-password")
def generate_password():
    return {"password" : password.generate_password()}

@app.get("/credentials")
def get_credentials():
    return credential.get_credentials()

@app.post("/save")
def save_credentials(
    website: str = Form(...),
    username : str = Form(...),
    password : str = Form(...)
    ):

    try:
        credential.save_credentials(website, username, password)
        return {'message' : 'Saved Successfully'}
    except ValueError as e:
        return {"error" : str(e)}

    # try:
    #     credential.save_credentials(website, username, password)
    #     return RedirectResponse(url="/list", status_code=303)
    # except ValueError as e:
    #     return RedirectResponse(url="/add", status_code=303)


@app.put('/update/{website}/{username}')
def update_credentials(website : str, username : str, password : str):
    try:
        credential.update_credentials(website, username, password)
        return {'message' : 'Updated Successfully'}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete('/delete/{website}/{username}')
def delete_credentials(website : str, username : str):
    try:
        credential.delete_credentials(website, username)
        return {'message' : 'Deleted Successfully'}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))