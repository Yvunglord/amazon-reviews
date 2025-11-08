import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

def load_reviews(limit=1_000_000):
    query = f"""
        SELECT user_id, product_id, rating, timestamp
        FROM reviews
        LIMIT {limit}
    """
    df = pd.read_sql(query, engine)
    return df

def analyze_reviews(df: pd.DataFrame):
    res = {}
    res["avg_rating"] = df["rating"].mean()
    res["unique_users"] = df["user_id"].nunique()
    res["unique_products"] = df["unique_products"].nunique()
    res["rating_distribution"] = df["rating"].value_counts(normalize=True).round(3).to_dict()
    res["top_products"] = (
        df.groupby("product_id")["rating"]
        .count()
        .sort_values(ascending=False)
        .head(10)
        .to_dict()
    )

    return res

if __name__ == "__main__":
    print("Загружаем данные...")
    df = load_reviews(limit=500_000)
    print("Загружено:", len(df), "строк")
    print("Анализ")
    stats = analyze_reviews(df)
    for key, val in stats.items():
        print(f"{key}: {val}")