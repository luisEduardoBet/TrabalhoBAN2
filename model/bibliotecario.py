class Bibliotecario:  
    def __init__(self): 
        self.__id  = -1 
        self.__cpf  = ''
        self.__nome = ''
        self.__endereco = '' 
        self.__telefone = ''

        
    def from_tupla(self, tupla): 
        self.__id =  tupla[0]
        self.__cpf  = tupla[1]
        self.__nome = tupla[2]
        self.__endereco = tupla[3]
        self.__telefone = tupla[4]

    

        return self 
    
    def __repr__(self):        
        return u"({}, {}, {}, {}, {})".format(self.__id, self.__cpf, self.__nome, self.__endereco, self.__telefone)