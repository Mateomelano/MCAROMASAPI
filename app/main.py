from fastapi import FastAPI
from app.routes import products
from app.db.db import init_db  # Asegúrate de que esto esté correcto

app = FastAPI()

# Inicializar la base de datos
init_db()

# Registrar las rutas
app.include_router(products.router)
