from Connection import Connection
from Usuario import Usuario

class UsuarioDAO:
    def __init__(self):
        self.query = None
    
    def consulta(self, consulta) -> list:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        usuarios = []
        for i in result:
            usuarios.append(Usuario().from_tupla(i))

        return usuarios