from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "This is my first Controller in my life. I'm so proud of myself."}