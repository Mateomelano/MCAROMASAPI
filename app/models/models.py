from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    categoria = Column(String)
    marca = Column(String)
    precio = Column(Float)
    imagen = Column(String)
    habilitado = Column(Boolean, default=True)
    descripcion = Column(String)
