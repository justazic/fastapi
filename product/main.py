from fastapi import FastAPI

app = FastAPI()

products = []
categories = []
orders = []

@app.get("/products")
async def get_products():
    return products

@app.post("/products")
async def create_product(product: dict):
    products.append(product)
    return {"message": "Product qoshildi", "product": product}


@app.get("/categories")
async def get_categories():
    return categories

@app.post("/categories")
async def create_category(category: dict):
    categories.append(category)
    return {"message": "Category yaratildi", "category": category}


@app.get("/orders")
async def get_orders():
    return orders

@app.post("/orders")
async def create_order(order: dict):
    orders.append(order)
    return {"message": " Buyurtma yaratildi", "order": order}