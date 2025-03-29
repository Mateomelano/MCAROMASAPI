from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models
from app.database import SessionLocal

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todos los productos
@router.get("/", response_model=List[schemas.Producto])
def obtener_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Producto).offset(skip).limit(limit).all()

# Agregar un producto
@router.post("/", response_model=schemas.Producto)
def agregar_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# Editar un producto
@router.put("/{id}", response_model=schemas.Producto)
def editar_producto(id: int, producto_actualizado: schemas.ProductoCreate, db: Session = Depends(get_db)):
    producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    for key, value in producto_actualizado.dict().items():
        setattr(producto, key, value)
    
    db.commit()
    db.refresh(producto)
    return producto

# Eliminar un producto
@router.delete("/{id}")
def eliminar_producto(id: int, db: Session = Depends(get_db)):
    producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    db.delete(producto)
    db.commit()
    return {"mensaje": "Producto eliminado"}
