from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models.servicios as models
import schemas.servicios as schemas

router = APIRouter(
    prefix="/servicios",
    tags=["Servicios"]
)

# 🧱 Crear cliente
@router.post("/clientes/", response_model=schemas.ClienteOut)
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    nuevo_cliente = models.Cliente(**cliente.dict())
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente


# 🧱 Crear vehículo
@router.post("/vehiculos/", response_model=schemas.VehiculoOut)
def crear_vehiculo(vehiculo: schemas.VehiculoCreate, db: Session = Depends(get_db)):
    nuevo_vehiculo = models.Vehiculo(**vehiculo.dict())
    db.add(nuevo_vehiculo)
    db.commit()
    db.refresh(nuevo_vehiculo)
    return nuevo_vehiculo


# 🧱 Crear servicio solicitado
@router.post("/servicios-solicitados/", response_model=schemas.ServicioSolicitadoOut)
def crear_servicio(servicio: schemas.ServicioSolicitadoCreate, db: Session = Depends(get_db)):
    nuevo_servicio = models.ServicioSolicitado(**servicio.dict())
    db.add(nuevo_servicio)
    db.commit()
    db.refresh(nuevo_servicio)
    return nuevo_servicio


# ✅ Obtener todos los clientes
@router.get("/clientes/", response_model=list[schemas.ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(models.Cliente).all()


# ✅ Obtener todos los vehículos
@router.get("/vehiculos/", response_model=list[schemas.VehiculoOut])
def listar_vehiculos(db: Session = Depends(get_db)):
    return db.query(models.Vehiculo).all()


# ✅ Obtener todos los servicios solicitados
@router.get("/servicios-solicitados/", response_model=list[schemas.ServicioSolicitadoOut])
def listar_servicios(db: Session = Depends(get_db)):
    return db.query(models.ServicioSolicitado).all()
