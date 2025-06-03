from Connection import Connection
from Reserva import Reserva

class ReservaDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        reservas = []
        for i in result:
            reservas.append(Reserva().from_tupla(i))

        return reservas