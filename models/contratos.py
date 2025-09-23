from core.database import get_connection

class ContratosModel:
    @staticmethod
    def create(
        empleado_id: int,
        empresa_id: int,
        tipo: str,
        fecha_inicio: str,
        sueldo_base: int,
        afp_id: int,
        salud_id: int,
        afc_id: int = None,
        fecha_termino: str = None
    ):
        cnx = get_connection()
        if not cnx:
            return False
        cursor = cnx.cursor()
        cursor.execute(
            """
            INSERT INTO contratos 
            (empleado_id, empresa_id, tipo, fecha_inicio, fecha_termino, sueldo_base, afp_id, salud_id, afc_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (empleado_id, empresa_id, tipo, fecha_inicio, fecha_termino, sueldo_base, afp_id, salud_id, afc_id)
        )
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
