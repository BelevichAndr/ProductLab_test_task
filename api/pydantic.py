from pydantic import BaseModel


class ProductData(BaseModel):
    article: int
    article_title: str
    brand: str
