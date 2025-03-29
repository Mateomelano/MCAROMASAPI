from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str
    categoria: str
    marca: str
    precio: float
    imagen: str
    habilitado: bool
    descripcion: str
