from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class DetalleMantenimiento(Base):
    __tablename__ = "detalle_mantenimiento"

    id = Column(Integer, primary_key=True, index=True)
    mantenimiento_id = Column(Integer, ForeignKey("mantenimientos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer, nullable=False)

    mantenimiento = relationship("Mantenimiento", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles")


class DetalleMantenimientoBase(BaseModel):
    producto_id: int
    cantidad: int
    descripcion: str

class DetalleMantenimientoCreate(DetalleMantenimientoBase):
    pass

class DetalleMantenimientoResponse(DetalleMantenimientoBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
