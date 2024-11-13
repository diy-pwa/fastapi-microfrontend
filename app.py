from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/src", StaticFiles(directory="src"), name="src")

@app.get("/")
async def index():
   return {
      "message": "Hello World",
      "code":11
      }