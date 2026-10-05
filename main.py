from fastapi import FastAPI
from api import user, product, category, review

app = FastAPI()

app.include_router(product.router, prefix="/api/v1/products", tags=["products"])