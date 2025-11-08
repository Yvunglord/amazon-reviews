import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm

load_dotenv()

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
chunksize = 100_000
for chunk in tqdm(pd.read_csv("data/amazon_reviews.csv", 
                               chunksize=chunksize,
                               header=None,
                               names=['user_id', 'product_id', 'rating', 'timestamp'])):

    chunk.to_sql('reviews', engine, if_exists='append', index=False)