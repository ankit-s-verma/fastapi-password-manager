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

@app.get("/")
def home(request : Request):
    return templates.TemplateResponse(request, "index.html")

@app.get("/add")
def add_page(request : Request):
    return templates.TemplateResponse(request, "add.html", {"message" : "Saved Successfully"})

@app.get("/list")
def list_page(request: Request):

    data = credential.get_credentials()
    return templates.TemplateResponse(request, "list.html", {"data": data})

@app.get("/generate-password")
def generate_password():
    return {"password" : password.generate_password()}

@app.get("/credentials")
def get_credentials():
    return credential.get_credentials()

@app.post("/save")
def save_credentials(
    request : Request,
    website: str = Form(...),
    username : str = Form(...),
    password : str = Form(...)
    ):

    try:
        credential.save_credentials(website, username, password)
        return templates.TemplateResponse(request, "add.html")
    except ValueError as e:
        return templates.TemplateResponse(request, "add.html", {"error": str(e)})

@app.put('/update/{website}/{username}')
def update_credentials(website : str,username : str,password : str):
    try:
        credential.update_credentials(website, username, password)
        return {'message' : 'Updated Successfully'}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete('/delete/{website}/{username}')
def delete_credentials(website : str,username : str):
    try:
        credential.delete_credentials(website, username)
        return {'message' : 'Deleted Successfully'}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@app.get("/search")
def search(request: Request, website: str):
    results = credential.search_credentials(website)
    return templates.TemplateResponse(request, "list.html", {"data": results})