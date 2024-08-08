from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int | None = None
    
app = FastAPI(title="Greeter app")

@app.get("/")
async def root():
    return {"message": "Hello, this is a fastAPI app"}

@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": "Hello, {}, this is a fastAPI app".format(name)}

@app.get("/greet-many-times")
async def greet_many_times(n: int = 4):
    message = ""
    for i in range(n):
        message += "Hello, this is a fastAPI app. "
    return {"message": message}

@app.post("/greet-a-person/")
async def greet_a_person(person: Person):
    message = "Hello, {} {}, ".format(person.first_name, person.last_name)
    if(person.age):
        message += "I know you are {} years old".format(person.age)
    else:
        message += "I do not know how old you are"
        
    return {"message": message}

@app.post("/greet-a-form/")
async def greet_a_form(first_name: Annotated[str, Form()], last_name: Annotated[str, Form()]):
    return {"message": "Hello, {} {}, you really nailed that form".format(first_name, last_name)}