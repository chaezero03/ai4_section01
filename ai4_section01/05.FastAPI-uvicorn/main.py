from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/sports")
def sports():
    return {"sports": ["Soccer", "Basketball", "Tennis", "Baseball"]}
