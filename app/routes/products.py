from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.db.db import SessionLocal, get_db
from app.models import models
from app.schemas import schemas

router = APIRouter()

# Obtener todos los productos
@router.get("/productos", response_model=List[schemas.Producto])
def obtener_productos(db: Session = Depends(get_db)):
    productos = db.query(models.Producto).all()
    return productos
