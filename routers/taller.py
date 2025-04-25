from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import mantenimiento as models
from schemas import mantenimiento as schemas

router = APIRouter(
    prefix="/taller",
    tags=["Módulo Taller"]
)

# Crear un nuevo servicio realizado en el taller
@router.post("/", response_model=schemas.Mantenimiento)
def crear_servicio_taller(mantenimiento: schemas.MantenimientoCreate, db: Session = Depends(get_db)):
    db_mantenimiento = models.Mantenimiento(
        vehiculo_id=mantenimiento.vehiculo_id,
        mecanico_id=mantenimiento.mecanico_id,
        servicio_solicitado_id=mantenimiento.servicio_solicitado_id,
        observaciones=mantenimiento.observaciones,
    )
    db.add(db_mantenimiento)
    db.commit()
    db.refresh(db_mantenimiento)

    for detalle in mantenimiento.detalles:
        db_detalle = models.DetalleMantenimiento(
            mantenimiento_id=db_mantenimiento.id,
            producto_id=detalle.producto_id,
            cantidad=detalle.cantidad,
            observaciones=detalle.observaciones,
        )
        db.add(db_detalle)

    db.commit()
    db.refresh(db_mantenimiento)
    return db_mantenimiento

# Listar todos los servicios realizados
@router.get("/", response_model=list[schemas.Mantenimiento])
def listar_servicios_taller(db: Session = Depends(get_db)):
    return db.query(models.Mantenimiento).all()

# Obtener un servicio específico
@router.get("/{id}", response_model=schemas.Mantenimiento)
def obtener_servicio_taller(id: int, db: Session = Depends(get_db)):
    mantenimiento = db.query(models.Mantenimiento).filter(models.Mantenimiento.id == id).first()
    if not mantenimiento:
        raise HTTPException(status_code=404, detail="Servicio de taller no encontrado")
    return mantenimiento

# Actualizar un servicio
@router.put("/{id}", response_model=schemas.Mantenimiento)
def actualizar_servicio_taller(id: int, datos: schemas.MantenimientoUpdate, db: Session = Depends(get_db)):
    mantenimiento = db.query(models.Mantenimiento).filter(models.Mantenimiento.id == id).first()
    if not mantenimiento:
        raise HTTPException(status_code=404, detail="Servicio de taller no encontrado")

    if datos.fecha_fin:
        mantenimiento.fecha_fin = datos.fecha_fin
    if datos.estado:
        mantenimiento.estado = datos.estado
    if datos.observaciones:
        mantenimiento.observaciones = datos.observaciones

    db.commit()
    db.refresh(mantenimiento)
    return mantenimiento
