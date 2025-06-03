from Connection import Connection
from Exemplar import Exemplar

class ExemplarDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        exemplares = []
        for i in result:
            exemplares.append(Exemplar().from_tupla(i))

        return exemplares