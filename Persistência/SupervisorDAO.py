from Connection import Connection
from Supervisor import Supervisor

class SupervisorDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        supervisores = []
        for i in result:
            supervisores.append(Supervisor().from_tupla(i))

        return supervisores