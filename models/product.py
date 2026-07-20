from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    rating: float
    seller: str = "Unknown"
    source: str
    url: str
    image: str = ""
    
    value_score: float = 0.0
    recommendation_score: float = 0.0
