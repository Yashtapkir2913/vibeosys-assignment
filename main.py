from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import models, crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vibeosys Product API")

# List products with pagination
@app.get("/product/list")
def list_products(page: int = 1, db: Session = Depends(get_db)):
    skip = (page - 1) * 10
    products = crud.get_products(db, skip=skip, limit=10)
    return products

# Get product info
@app.get("/product/{pid}/info")
def product_info(pid: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, pid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Add product
@app.post("/product/add")
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

# Update product
@app.put("/product/{pid}/update")
def update_product(pid: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    updated = crud.update_product(db, pid, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated
