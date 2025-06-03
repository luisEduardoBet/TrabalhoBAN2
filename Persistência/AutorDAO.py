from Connection import Connection
from Autor import Autor

class AutorDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        autores = []
        for i in result:
            autores.append(Autor().from_tupla(i))

        return autores