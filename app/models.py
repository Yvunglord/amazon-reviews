from sqlalchemy import Column, String, Float, BigInteger
from app.database import Base

class Review(Base) :
    __tablename__ = "reviews"

    user_id = Column(String, primary_key=True)
    product_id = Column(String, primary_key=True)
    rating = Column(Float)
    timestamp = Column(BigInteger)