from urllib import request
from urllib.request import Request

from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/test_form_data/{user_id}")
def test_form_data(request: Request, user_id: int, query_args1: str| None = None , query_args2: str| None = None):
    return templates.TemplateResponse(request,
                                      "item.html",
                                      context = {"user_id": user_id, "query_args1": query_args1, "query_args2": query_args2}
                                      )



class FormData(BaseModel):
    first_name: str
    last_name: str


@app.post("/test_form_data")
def test_form_data(form_data: FormData):
    return {"message": f"Hello World {form_data.first_name} {form_data.last_name}"}

