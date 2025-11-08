from app.database import engine
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.analytics import load_reviews, analyze_reviews
import app.models as models

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Amazon Review Insight Hub")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/analytics/summary")
def analytics_summary(limit: int = Query(100_000, ge=1000, le=1_000_000)):
    df = load_reviews(limit)
    res = analyze_reviews(df)
    return res