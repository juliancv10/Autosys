from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Mantenimiento(Base):
    __tablename__ = "mantenimientos"

    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"))
    mecanico_id = Column(Integer, ForeignKey("usuarios.id"))
    servicio_solicitado_id = Column(Integer, ForeignKey("servicios_solicitados.id"), nullable=True)
    fecha_inicio = Column(DateTime, default=datetime.now)
    fecha_fin = Column(DateTime, nullable=True)
    observaciones = Column(Text, nullable=True)
    estado = Column(String(50), default="En progreso")

    vehiculo = relationship("Vehiculo")
    mecanico = relationship("Usuario")
    servicio_solicitado = relationship("ServicioSolicitado")
    detalles = relationship("DetalleMantenimiento", back_populates="mantenimiento")


class DetalleMantenimiento(Base):
    __tablename__ = "detalle_mantenimiento"

    id = Column(Integer, primary_key=True, index=True)
    mantenimiento_id = Column(Integer, ForeignKey("mantenimientos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer)
    observaciones = Column(Text, nullable=True)

    mantenimiento = relationship("Mantenimiento", back_populates="detalles")
    producto = relationship("Producto")
