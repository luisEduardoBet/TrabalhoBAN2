from Connection import Connection
from Assistente import Assistente

class AssistenteDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        assistentes = []
        for i in result:
            assistentes.append(Assistente().from_tupla(i))

        return assistentes