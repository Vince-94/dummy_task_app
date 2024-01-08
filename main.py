from typing import List

from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel


app = FastAPI(
    title="TestRestAPI",
    version=2.0
)

handler = Mangum(app)


@app.get("/")
def read_item():
    return {"message": "Hello, this is a dummy REST API!"}
