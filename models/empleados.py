from core.database import get_connection

class EmpleadosModel:
    @staticmethod
    def get_all():
        cnx = get_connection()
        if not cnx:
            return []
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT id, nombres, apellidos, rut, fecha_nacimiento, direccion FROM empleados")
        empleados = cursor.fetchall()
        cursor.close()
        cnx.close()
        return empleados

    @staticmethod
    def create(nombres: str, apellidos: str, rut: str, fecha_nacimiento: str, direccion: str):
        cnx = get_connection()
        if not cnx:
            return False
        cursor = cnx.cursor()
        cursor.execute(
            """
            INSERT INTO empleados (nombres, apellidos, rut, fecha_nacimiento, direccion)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (nombres, apellidos, rut, fecha_nacimiento, direccion)
        )
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
