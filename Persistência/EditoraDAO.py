from Connection import Connection
from Editora import Editora

class EditoraDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        editoras = []
        for i in result:
            editoras.append(Editora().from_tupla(i))

        return editoras