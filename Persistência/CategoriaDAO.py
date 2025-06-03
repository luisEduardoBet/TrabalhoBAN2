from Connection import Connection
from Categoria import Categoria

class CategoriaDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        categorias = []
        for i in result:
            categorias.append(Categoria().from_tupla(i))

        return categorias