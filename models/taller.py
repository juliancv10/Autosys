from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Mantenimiento(Base):
    __tablename__ = "mantenimientos"

    id = Column(Integer, primary_key=True, index=True)
    fecha_inicio = Column(DateTime, default=datetime.utcnow)
    fecha_fin = Column(DateTime, nullable=True)
    estado = Column(Text, default="en_proceso")  # en_proceso, finalizado

    servicio_solicitado_id = Column(Integer, ForeignKey("servicios_solicitados.id"))
    servicio_solicitado = relationship("ServicioSolicitado")

    detalles = relationship("DetalleMantenimiento", back_populates="mantenimiento")


class DetalleMantenimiento(Base):
    __tablename__ = "detalle_mantenimiento"

    id = Column(Integer, primary_key=True, index=True)
    descripcion_trabajo = Column(Text, nullable=False)
    repuestos_usados = Column(Text)
    observaciones = Column(Text)

    mantenimiento_id = Column(Integer, ForeignKey("mantenimientos.id"))
    mantenimiento = relationship("Mantenimiento", back_populates="detalles")
