from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from  database import Base

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(20), unique=True, nullable=False)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    propietario = Column(String(100), nullable=True)  # opcional

    mantenimientos = relationship("Mantenimiento", back_populates="vehiculo")
