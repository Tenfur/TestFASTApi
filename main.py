from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 


app = FastAPI()

products = []

# Product model
class Product(BaseModel):
    id: str
    title: Optional[str]
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: datetime

@app.get("/")
def read_root():
    return {
        "weclome": "welcome to my REST API"
    }

@app.get("/products")
def getProducts():
    return products

@app.get("/products/{productId}")
def getProductById(productId):
    for product in products:
        if product["id"] == productId:
            return product
    raise HTTPException(status_code=404, detail ="Post Not Found")

@app.post("/products")
def createProduct(product: Product):
    product.id = str(uuid4())
    products.append(product.model_dump())


@app.delete("/products/{productId}")
def deleteProduct(productId: str):
    for index, product in enumerate(products):
        if product["id"] == productId:
            products.pop(index)
            return {
                "message": "Post has been deleted correctly!"
            }
    raise HTTPException(status_code=404, detail="Post Not Found")


@app.put("/posts/{productId}")
def updateProduct(productId: str, updatePost: Product):
    pass