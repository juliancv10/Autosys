from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.vehiculo import Vehiculo
from schemas.vehiculo import VehiculoCreate, VehiculoOut

router = APIRouter(prefix="/vehiculos", tags=["vehiculos"])

@router.post("/", response_model=VehiculoOut)
def crear_vehiculo(vehiculo: VehiculoCreate, db: Session = Depends(get_db)):
    db_vehiculo = Vehiculo(**vehiculo.dict())
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

@router.get("/", response_model=list[VehiculoOut])
def listar_vehiculos(db: Session = Depends(get_db)):
    return db.query(Vehiculo).all()

@router.get("/{vehiculo_id}", response_model=VehiculoOut)
def obtener_vehiculo(vehiculo_id: int, db: Session = Depends(get_db)):
    vehiculo = db.query(Vehiculo).get(vehiculo_id)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehiculo
