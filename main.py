from fastapi import Depends,FastAPI
from model import product
from fastapi.middleware.cors import CORSMiddleware
from database import session,engine
import db_models
from sqlalchemy.orm import Session
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)
db_models.Base.metadata.create_all(bind=engine)

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()
@app.get('/')
def greet():
    return "Welcome guys"

products=[
    product(id=1,name="laptop",description="dell laptop",price=45000.0,quantity=5),
    product(id=2,name="phone",description="iphone",price=90000.0,quantity=10),
    product(id=8,name="tablet",description="samsung tablet",price=30000.0,quantity=7)]

def init_db():
    db=session()
    count=db.query(db_models.product).count
    if count==0:
        for product in products:
            db.add(db_models.product(**product.model_dump()))
        db.commit()
init_db()
@app.get('/products')
def all_products(db:Session=Depends(get_db)):        
    db_products=db.query(db_models.product).all()
    #db.query()
    return db_products

@app.get('/products/{id}')
def get_product(id:int,db:Session=Depends(get_db)):
    db_product=db.query(db_models.product).filter(db_models.product.id==id).first()
    if db_product:
        return db_product
    return {"product not found"}

@app.post('/products')
def add_product(product:product,db:Session=Depends(get_db)):
    db.add(db_models.product(**product.model_dump()))
    db.commit()
    return "product added successfully"

@app.put('/products/{id}')
def update_product(id:int,product:product,db:Session=Depends(get_db)):
    db_product=db.query(db_models.product).filter(db_models.product.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()
        return "product change successfully"

    return{"product not found"}

@app.delete('/products')
def del_product(id:int,db:Session=Depends(get_db)):
    db_product=db.query(db_models.product).filter(db_models.product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return {"product not found"}
