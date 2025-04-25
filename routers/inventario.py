from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import inventario as models
from schemas import inventario as schemas

router = APIRouter(
    prefix="/inventario",
    tags=["Inventario"]
)

# Crear un producto
@router.post("/productos/", response_model=schemas.ProductoOut)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# Obtener todos los productos
@router.get("/productos/", response_model=list[schemas.ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    productos = db.query(models.Producto).all()
    return productos

# Crear un movimiento de inventario
@router.post("/movimientos_inventario/", response_model=schemas.MovimientoInventarioOut)
def crear_movimiento_inventario(movimiento: schemas.MovimientoInventarioCreate, db: Session = Depends(get_db)):
    db_movimiento = models.MovimientoInventario(**movimiento.dict())
    db.add(db_movimiento)

    # Actualizar el stock del producto
    producto = db.query(models.Producto).filter(models.Producto.id == movimiento.producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if movimiento.tipo.lower() == "entrada":
        producto.cantidad += movimiento.cantidad
    elif movimiento.tipo.lower() == "salida":
        if producto.cantidad < movimiento.cantidad:
            raise HTTPException(status_code=400, detail="Stock insuficiente")
        producto.cantidad -= movimiento.cantidad
    else:
        raise HTTPException(status_code=400, detail="Tipo de movimiento inválido")

    db.commit()
    db.refresh(db_movimiento)
    return db_movimiento

# Registrar un movimiento adicional
@router.post("/movimientos/", response_model=schemas.MovimientoOut)
def registrar_movimiento(movimiento: schemas.MovimientoCreate, db: Session = Depends(get_db)):
    db_movimiento = models.Movimiento(**movimiento.dict())
    db.add(db_movimiento)
    db.commit()
    db.refresh(db_movimiento)
    return db_movimiento
