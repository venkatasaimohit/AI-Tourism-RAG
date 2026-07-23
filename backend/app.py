from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to AI Tourism RAG Planner"}


@app.get("/db-test")
def db_test():
    return {
        "database": "Connected Successfully"
    }
