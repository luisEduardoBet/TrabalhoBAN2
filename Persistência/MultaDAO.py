from Connection import Connection
from Multa import Multa

class MultaDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        multas = []
        for i in result:
            multas.append(Multa().from_tupla(i))

        return multas