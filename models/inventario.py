from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    productos = relationship("Producto", back_populates="categoria")


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    cantidad = Column(Integer, default=0)
    precio_unitario = Column(Float)

    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categoria = relationship("Categoria", back_populates="productos")

    movimientos = relationship("MovimientoInventario", back_populates="producto")
    detalles_orden = relationship("DetalleOrdenCompra", back_populates="producto")


class MovimientoInventario(Base):
    __tablename__ = "movimientos_inventario"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(20))  # entrada o salida
    cantidad = Column(Integer, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)

    producto_id = Column(Integer, ForeignKey("productos.id"))
    producto = relationship("Producto", back_populates="movimientos")


class OrdenCompra(Base):
    __tablename__ = "ordenes_compra"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    tipo = Column(String(20))  # materiales o servicios
    estado = Column(String(30), default="pendiente")  # pendiente, aprobada, completada

    detalles = relationship("DetalleOrdenCompra", back_populates="orden")


class DetalleOrdenCompra(Base):
    __tablename__ = "detalle_orden_compra"

    id = Column(Integer, primary_key=True, index=True)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float)

    producto_id = Column(Integer, ForeignKey("productos.id"))
    orden_id = Column(Integer, ForeignKey("ordenes_compra.id"))

    producto = relationship("Producto", back_populates="detalles_orden")
    orden = relationship("OrdenCompra", back_populates="detalles")
