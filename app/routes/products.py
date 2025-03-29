from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Producto
from app.db import productos

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

# Obtener todos los productos
@router.get("/", response_model=List[Producto])
def obtener_productos():
    return productos

# Agregar un producto
@router.post("/", response_model=Producto)
def agregar_producto(producto: Producto):
    for p in productos:
        if p.id == producto.id:
            raise HTTPException(status_code=400, detail="ID de producto ya existe")
    productos.append(producto)
    return producto

# Editar un producto
@router.put("/{id}", response_model=Producto)
def editar_producto(id: int, producto_actualizado: Producto):
    for i, p in enumerate(productos):
        if p.id == id:
            productos[i] = producto_actualizado
            return producto_actualizado
    raise HTTPException(status_code=404, detail="Producto no encontrado")

# Eliminar un producto
@router.delete("/{id}")
def eliminar_producto(id: int):
    global productos
    productos = [p for p in productos if p.id != id]
    return {"mensaje": "Producto eliminado"}
