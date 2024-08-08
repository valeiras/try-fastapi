from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Worldly creatures"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/lookup")
async def lookup_item(q, limit: int= 5):
    return {"q": q, "limit": limit}