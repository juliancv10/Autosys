from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    identificacion = Column(String(30), unique=True, nullable=False)
    telefono = Column(String(20))
    correo = Column(String(100))

    vehiculos = relationship("Vehiculo", back_populates="cliente")
    servicios_solicitados = relationship("ServicioSolicitado", back_populates="cliente")


class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(10), unique=True, nullable=False)
    marca = Column(String(50))
    modelo = Column(String(50))
    anio = Column(String(50))

    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    cliente = relationship("Cliente", back_populates="vehiculos")

    servicios_solicitados = relationship("ServicioSolicitado", back_populates="vehiculo")


class Servicio(Base):
    __tablename__ = "servicios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    precio_estimado = Column(Integer)

    servicios_solicitados = relationship("ServicioSolicitado", back_populates="servicio")


class ServicioSolicitado(Base):
    __tablename__ = "servicios_solicitados"

    id = Column(Integer, primary_key=True, index=True)
    fecha_solicitud = Column(DateTime, default=datetime.utcnow)
    estado = Column(String(30), default="pendiente")  # pendiente, en_proceso, finalizado
    descripcion = Column(Text)
    
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"))
    servicio_id = Column(Integer, ForeignKey("servicios.id"))

    cliente = relationship("Cliente", back_populates="servicios_solicitados")
    vehiculo = relationship("Vehiculo", back_populates="servicios_solicitados")
    servicio = relationship("Servicio", back_populates="servicios_solicitados")
