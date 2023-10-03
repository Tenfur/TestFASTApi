from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "weclome": "welcome to my REST API"
    }