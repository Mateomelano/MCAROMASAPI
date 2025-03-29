from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de producto
class Producto(BaseModel):
    id: int
    nombre: str
    categoria: str
    marca: str
    precio: float
    imagen: str
    habilitado: bool
    descripcion: str

# Base de datos simulada en memoria
productos: List[Producto] = [
    Producto(id=1, nombre="Laptop", categoria="Electrónica", marca="Dell", precio=799.99, imagen="laptop.jpg", habilitado=True, descripcion="Laptop potente para trabajo y estudio"),
    Producto(id=2, nombre="Teléfono", categoria="Electrónica", marca="Samsung", precio=599.99, imagen="telefono.jpg", habilitado=True, descripcion="Smartphone con excelente cámara"),
    Producto(id=3, nombre="Teclado", categoria="Accesorios", marca="Logitech", precio=49.99, imagen="teclado.jpg", habilitado=True, descripcion="Teclado mecánico retroiluminado")
]

# Obtener todos los productos
@app.get("/productos", response_model=List[Producto])
def obtener_productos():
    return productos

# Agregar un producto
@app.post("/productos", response_model=Producto)
def agregar_producto(producto: Producto):
    for p in productos:
        if p.id == producto.id:
            raise HTTPException(status_code=400, detail="ID de producto ya existe")
    productos.append(producto)
    return producto

# Editar un producto
@app.put("/productos/{id}", response_model=Producto)
def editar_producto(id: int, producto_actualizado: Producto):
    for i, p in enumerate(productos):
        if p.id == id:
            productos[i] = producto_actualizado
            return producto_actualizado
    raise HTTPException(status_code=404, detail="Producto no encontrado")

# Eliminar un producto
@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    global productos
    productos = [p for p in productos if p.id != id]
    return {"mensaje": "Producto eliminado"}
