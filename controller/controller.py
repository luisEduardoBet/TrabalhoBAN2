from model.bibliotecario import Bibliotecario 
from model.bibliotecariodao import BibliotecarioDAO

class Controller: 

    @staticmethod
    def negocioTeste(dados):
        dao = BibliotecarioDAO()
        
        dao.insercao(dados)
    
        
        