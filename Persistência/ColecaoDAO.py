from Connection import Connection
from Colecao import Colecao

class ColecaoDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        colecoes = []
        for i in result:
            colecoes.append(Colecao().from_tupla(i))

        return colecoes