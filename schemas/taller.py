from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class DetalleMantenimientoBase(BaseModel):
    producto_id: int
    cantidad: int
    observaciones: Optional[str] = None

class DetalleMantenimientoCreate(DetalleMantenimientoBase):
    pass

class DetalleMantenimiento(DetalleMantenimientoBase):
    id: int

    class Config:
        orm_mode = True


class MantenimientoBase(BaseModel):
    vehiculo_id: int
    mecanico_id: int
    servicio_solicitado_id: Optional[int] = None
    observaciones: Optional[str] = None

class MantenimientoCreate(MantenimientoBase):
    detalles: List[DetalleMantenimientoCreate]

class MantenimientoUpdate(BaseModel):
    fecha_fin: Optional[datetime]
    estado: Optional[str]
    observaciones: Optional[str]

class Mantenimiento(MantenimientoBase):
    id: int
    fecha_inicio: datetime
    fecha_fin: Optional[datetime]
    estado: str
    detalles: List[DetalleMantenimiento] = []

    class Config:
        orm_mode = True
