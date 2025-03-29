from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    categoria: str
    marca: str
    precio: float
    imagen: str
    habilitado: bool
    descripcion: str

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int

    class Config:
        orm_mode = True
