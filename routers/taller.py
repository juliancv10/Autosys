from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.mantenimiento import Mantenimiento
from models.detalle_mantenimiento import DetalleMantenimiento
from models.producto import Producto
from schemas.detalle_mantenimiento import DetalleMantenimientoCreate, DetalleMantenimientoResponse

router = APIRouter(prefix="/taller", tags=["Taller"])

# Agregar detalle al mantenimiento
@router.post("/mantenimientos/{mantenimiento_id}/detalle", response_model=DetalleMantenimientoResponse)
def agregar_detalle_mantenimiento(mantenimiento_id: int, detalle: DetalleMantenimientoCreate, db: Session = Depends(get_db)):
    mantenimiento = db.query(Mantenimiento).filter(Mantenimiento.id == mantenimiento_id).first()
    if not mantenimiento:
        raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")

    producto = db.query(Producto).filter(Producto.id == detalle.producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if producto.stock < detalle.cantidad:
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    # Crear detalle
    nuevo_detalle = DetalleMantenimiento(
        mantenimiento_id=mantenimiento_id,
        producto_id=detalle.producto_id,
        cantidad=detalle.cantidad,
        descripcion=detalle.descripcion
    )

    # Descontar del stock
    producto.stock -= detalle.cantidad

    db.add(nuevo_detalle)
    db.commit()
    db.refresh(nuevo_detalle)

    return nuevo_detalle
