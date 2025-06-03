from Connection import Connection
from Bibliotecario import Bibliotecario

class BibliotecarioDAO:
    def __init___(self):  
        self.query = None

    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        bibliotecarios = []
        for i in result:
            bibliotecarios.append(Bibliotecario().from_tupla(i))

        return bibliotecarios