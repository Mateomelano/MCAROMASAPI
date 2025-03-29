from fastapi import FastAPI
from app.routes import productos
from app.database import init_db

app = FastAPI()

# Inicializar la base de datos
init_db()

# Registrar rutas
app.include_router(productos.router)
