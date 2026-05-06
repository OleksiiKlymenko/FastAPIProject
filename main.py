from idlelib import query
from unittest import result

##from urllib import request
from urllib.request import Request

from fastapi.responses import RedirectResponse
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.ext.asyncio import session
from sqlalchemy.orm import Session

from database import engine
from model import Workers

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/test_form_data/{user_id}")
def test_form_data(
    request: Request,
    user_id: int,
    query_args1: str | None = None,
    query_args2: str | None = None,
):
    return templates.TemplateResponse(
        request,
        "item.html",
        context={
            "user_id": user_id,
            "query_args1": query_args1,
            "query_args2": query_args2,
        },
    )


class FormData(BaseModel):
    first_name: str
    last_name: str


@app.post("/test_form_data")
def test_form_data(form_data: FormData):
    return {"message": f"Hello World {form_data.first_name} {form_data.last_name}"}


@app.post("/calculator")
def calculator(
    request: Request, num1: int = Form(), num2: int = Form(), option: str = Form()
):
    result = None
    if option == "+":
        result = num1 + num2
    elif option == "-":
        result = num1 - num2
    elif option == "*":
        result = num1 * num2
    elif option == "/":
        result = num1 / num2
    return templates.TemplateResponse(
        request=request,
        name="item.html",
        context={"result": result, "num1": num1, "num2": num2},
    )


@app.get("/calculator")
def calculator_get(request: Request):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"result": None}
    )


class WorkerSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    ipn: int

    class Config:
        from_attributes = True


@app.get("/workers")
async def all_workers(request: Request):
    session = Session(engine)
    query = select(Workers)
    result = []

    result = session.scalars(query).all()

    session.close()
    return templates.TemplateResponse(
        request=request, name="workers.html", context={"workers": result}
    )


class WorkerFormData(BaseModel):
    first_name: str
    last_name: str
    passport: str
    ipn: int


@app.post("/workers")
def test_form_data(
    Request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    passport: str = Form(...),
    ipn: int = Form(...),
):
    with Session(engine) as session:
        new_worker = Workers(
            first_name=first_name, last_name=last_name, passport=passport, ipn=ipn
        )
        session.add(new_worker)
        session.commit()
    return RedirectResponse(url="/workers", status_code=303)
