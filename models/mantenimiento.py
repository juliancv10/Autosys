from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Mantenimiento(Base):
    __tablename__ = 'mantenimientos'

    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"))
    fecha = Column(DateTime, default=datetime.utcnow)
    estado = Column(String(50))

    detalles = relationship("DetalleMantenimiento", back_populates="mantenimiento", cascade="all, delete-orphan")
    vehiculo = relationship("Vehiculo", back_populates="mantenimientos")
