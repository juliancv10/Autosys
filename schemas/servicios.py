from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Cliente
class ClienteBase(BaseModel):
    nombres: str
    apellidos: str
    identificacion: str
    telefono: Optional[str]
    correo: Optional[str]

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id: int
    class Config:
        orm_mode = True


# Vehículo
class VehiculoBase(BaseModel):
    placa: str
    marca: str
    modelo: Optional[str]
    anio: Optional[int]

class VehiculoCreate(VehiculoBase):
    cliente_id: int

class VehiculoOut(VehiculoBase):
    id: int
    cliente_id: int
    class Config:
        orm_mode = True


# Servicio Solicitado
class ServicioSolicitadoBase(BaseModel):
    descripcion: str
    fecha_solicitud: Optional[datetime] = None

class ServicioSolicitadoCreate(ServicioSolicitadoBase):
    cliente_id: int
    vehiculo_id: int
    servicio_id: int

class ServicioSolicitadoOut(ServicioSolicitadoBase):
    id: int
    cliente_id: int
    vehiculo_id: int
    servicio_id: int
    class Config:
        orm_mode = True
