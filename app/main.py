from database import engine
from fastapi import FastAPI
import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Amazon Review Insight Hub")

@app.get("/")
def root():
    return {"message": "API is running"}