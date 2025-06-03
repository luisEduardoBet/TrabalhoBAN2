from Connection import Connection
from Escrito import Escrito

class EscritoDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        escritores = []
        for i in result:
            escritores.append(Escrito().from_tupla(i))

        return escritores