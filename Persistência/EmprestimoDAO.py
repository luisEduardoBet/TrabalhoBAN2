from Connection import Connection
from Emprestimo import Emprestimo

class EmprestimoDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        emprestimos = []
        for i in result:
            emprestimos.append(Emprestimo().from_tupla(i))

        return emprestimos