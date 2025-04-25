from database import Base, engine
from models.administracion import Rol, Usuario  # importa los modelos
from models.servicios import Cliente, Vehiculo, Servicio, ServicioSolicitado
from models.inventario import Categoria, Producto, MovimientoInventario, OrdenCompra, DetalleOrdenCompra
from models.taller import Mantenimiento, DetalleMantenimiento

from fastapi import FastAPI
from database import engine, Base
from routers import servicios

from routers import inventario

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app.include_router(servicios.router)
app.include_router(inventario.router)