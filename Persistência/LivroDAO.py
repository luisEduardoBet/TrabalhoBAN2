from Connection import Connection
from Livro import Livro

class LivroDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        livros = []
        for i in result:
            livros.append(Livro().from_tupla(i))

        return livros