from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "weclome": "welcome to my REST API"
    }

@app.get("/home")
def getHome():
    return {
        "Message Home": "This is your home"
    }

@app.get("/test")
def test():
    return {
        "message Test": "New endpoint"
    }