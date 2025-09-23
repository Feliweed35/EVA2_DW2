from fastapi import APIRouter, HTTPException
from models.empleados import EmpleadosModel

router = APIRouter(prefix="/empleados", tags=["Empleados"])

@router.get("/")
def list_empleados():
    return EmpleadosModel.get_all()

@router.post("/")
def create_empleado(
    nombres: str,
    apellidos: str,
    rut: str,
    fecha_nacimiento: str,
    direccion: str
):
    # Validar obligatorios
    if not all([nombres, apellidos, rut, fecha_nacimiento, direccion]):
        raise HTTPException(status_code=400, detail="Todos los campos son obligatorios")

    success = EmpleadosModel.create(nombres, apellidos, rut, fecha_nacimiento, direccion)
    if not success:
        raise HTTPException(status_code=500, detail="Empleado no pudo ser creado")

    return {"message": "Empleado creado con éxito"}
