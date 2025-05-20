from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class DetalleMantenimiento(Base):
    __tablename__ = 'detalle_mantenimiento'

    id = Column(Integer, primary_key=True, index=True)
    mantenimiento_id = Column(Integer, ForeignKey("mantenimientos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer)
    descripcion = Column(String(255))
    fecha = Column(DateTime, default=datetime.utcnow)

    mantenimiento = relationship("Mantenimiento", back_populates="detalles")
    producto = relationship("Producto")
