from fastapi import FastAPI

app = FastAPI()

@app.get("/1")
def hello():
    return {"msg": "AI server running"}