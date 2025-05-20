from pydantic import BaseModel

class VehiculoBase(BaseModel):
    placa: str
    marca: str
    modelo: str
    anio: int

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoOut(VehiculoBase):
    id: int

    class Config:
        orm_mode = True
