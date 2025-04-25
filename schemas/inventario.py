from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema para Producto
class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    cantidad: int
    precio_unitario: float
    categoria_id: int

class ProductoCreate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    id: int

    class Config:
        orm_mode = True

# Schema para MovimientoInventario
class MovimientoInventarioBase(BaseModel):
    tipo: str  # entrada o salida
    cantidad: int
    fecha: Optional[datetime] = None
    producto_id: int

class MovimientoInventarioCreate(MovimientoInventarioBase):
    pass

class MovimientoInventarioOut(MovimientoInventarioBase):
    id: int

    class Config:
        orm_mode = True

# Schema para Movimiento
class MovimientoBase(BaseModel):
    producto_id: int
    tipo_movimiento: str
    cantidad: int
    fecha: Optional[datetime] = None
    descripcion: Optional[str] = None

class MovimientoCreate(MovimientoBase):
    pass

class MovimientoOut(MovimientoBase):
    id: int

    class Config:
        orm_mode = True
