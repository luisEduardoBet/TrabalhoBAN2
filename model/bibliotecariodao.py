from model.connection import Connection
from model.bibliotecario import Bibliotecario
from typing import List

class BibliotecarioDAO: 

    def consulta(self, consulta) -> List:
        con = Connection()
        cursor = con.cursor()
        cursor.execute(consulta)

        result = cursor.fetchall()

        bibliotecarios = []
        for i in result:
            bibliotecarios.append(Bibliotecario().from_tupla(i))


        con.close()

        return bibliotecarios
    

    def insercao(self, tupla) -> List: 
        
        con = Connection()
        cursor = con.cursor()
        cursor.execute(f"INSERT INTO bibliotecario (cpf, nome, endereco, telefone) VALUES ('{tupla[1]}','{tupla[2]}','{tupla[3]}','{tupla[4]}')")
        
        con.commit()


        