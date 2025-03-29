from app.models import Producto
from typing import List

# Base de datos simulada en memoria
productos: List[Producto] = [
    Producto(id=1, nombre="Laptop", categoria="Electrónica", marca="Dell", precio=799.99, imagen="laptop.jpg", habilitado=True, descripcion="Laptop potente para trabajo y estudio"),
    Producto(id=2, nombre="Teléfono", categoria="Electrónica", marca="Samsung", precio=599.99, imagen="telefono.jpg", habilitado=True, descripcion="Smartphone con excelente cámara"),
    Producto(id=3, nombre="Teclado", categoria="Accesorios", marca="Logitech", precio=49.99, imagen="teclado.jpg", habilitado=True, descripcion="Teclado mecánico retroiluminado")
]
